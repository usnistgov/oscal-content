<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2"
    xmlns:sqf="http://www.schematron-quickfix.com/validator/process"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:o="http://csrc.nist.gov/ns/oscal/1.0">
    
    <sch:ns prefix="o" uri="http://csrc.nist.gov/ns/oscal/1.0"/>
    
    <xsl:key name="by-id" match="*[(@id|@uuid)]"     use="@id|@uuid"/>
    <xsl:key name="parameter-by-id" match="o:param"  use="@id"/>
    <xsl:key name="link-targets"    match="*[@id]"   use="'#' || @id"/>
    <xsl:key name="link-targets"    match="*[@uuid]" use="'#' || @uuid"/>
    
    <xsl:key name="insert-by-param-id" match="o:insert[@type='param']" use="@id-ref"/>
    
<!-- This Schematron checks several basic features of SP800-53, or a similarly encoded document,
     for conformance with expectations. Specifically, it tests:
     
     - @id values are unique in the document
     - Use of @name is consistent with OSCAL, avoiding clashes with named elements in OSCAL
     - Expected (named) parts and properties are given in controls and subcontrols
     - Parts and properties are not given redundantly; when expected, they are singletons
       (the only child of their parent node with the @name value)
     - Cross-references (internal links) resolve when given
     
     More complex checking of 
     
    
    -->
    
    <sch:pattern id="ids">
        <sch:rule context="o:part[@name='assessment-objects']">
            <sch:assert test="empty(@id)">no @id is expected on assessment-objects parts</sch:assert>
        </sch:rule>
        <sch:rule context="o:part | o:control">
            <sch:assert test="empty(@id) or matches(@id,'\S')">@id must have a value</sch:assert>
            <sch:assert test="exists(@id)"><sch:name/> is expected to have an @id</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <!-- Checking presence and form of link hrefs -->
    <sch:pattern id="links">
        <sch:rule context="o:rlink">
            <sch:report test="starts-with(@href,'#')">Shouldn't see an internal link on an rlink</sch:report>
            <sch:assert test="starts-with(@href,'#') or matches(@href,'\w')">@href='<sch:value-of select="@href"/>' doesn't make (much of) a link.</sch:assert>
            <sch:report test="@href = preceding-sibling::o:rlink/@href"><sch:name/> has the same @href as neighbor</sch:report>
        </sch:rule>
        <sch:rule context="o:link | o:a">
            <sch:let name="href" value="@href[matches(.,'\S')]"/>
            <sch:let name="is-anchor" value="exists(self::o:a)"/>
            <sch:assert role="warning" test="exists($href)"><sch:value-of select="local-name() || 'nchor'[$is-anchor]"/> missing @href</sch:assert>
            <sch:assert test="empty($href) or ($href castable as xs:anyURI)">An @href must be a URI</sch:assert>
            <sch:report test="$href='#'" role="warning">Link points to the document.</sch:report>
            <sch:assert test="empty($href[starts-with(.,'#')]) or (@href='#') or exists(key('link-targets',$href))">Internal link is broken.</sch:assert>
            <sch:assert test="exists(ancestor::o:back-matter|self::o:a) or starts-with(@href,'#')" role="warning">External link unexpected outside document back matter.</sch:assert>
            <sch:assert test="not(contains(@href,'@')) or starts-with(@href,'mailto:')">@href appears to be an email, but has no 'mailto:'</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <!-- Some tokens should be prohibited for use as @name flags. -->
    
    <sch:let name="interdicted" value="'control','group','part','prop','param','title'"/>
    
    <sch:let name="known-part-names" value="('overview','statement', 'item', 'guidance', 'assessment-objective', 'assessment-method', 'assessment-objects')"/>
    
    <sch:let name="rmf-property-names" value="('implementation-level','contributes-to-assurance')"/>
    
    <sch:let name="known-property-names" value="('keywords', 'label', 'sort-id', 'method', 'status', 'aggregates', 'alt-identifier', 'alt-label',$rmf-property-names)"/>
    
    <sch:pattern id="general">
        <sch:rule context="*[matches(@name,'\S')]">
            <sch:report test="@name = $interdicted">@name '<sch:value-of select="@name"/>' is not permitted</sch:report>
        </sch:rule>
        <sch:rule context="comment()">
            <sch:assert test="empty(parent::*)">Comments should not appear except at top level.</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    
    <sch:pattern id="cross-referencing-constraints">
        <sch:rule context="o:insert">
            <sch:assert test="exists(key('parameter-by-id',@id-ref))"><sch:name/> does not point to a parameter.</sch:assert>
            <sch:let name="param-id" value="@id-ref"/>
            <sch:assert role="warning" test="empty(ancestor::o:select) or (count(ancestor::o:select/key('insert-by-param-id',$param-id,.)) eq 1)"><sch:name/> calls the same parameter as its neighbor: is this right?</sch:assert> </sch:rule>
        
        
        <sch:rule context="o:param">
            <sch:assert test="empty(@depends-on)">deprecated @depends-on should not appear</sch:assert>
            <!--<sch:let name="orphans" value="tokenize(@depends-on,'\s+')[not(.=current()/key('insert-by-param-id',@id,root())/ancestor::o:param/@id)]"/>
            <sch:assert test="empty(@depends-on) or empty($orphans)">@depends-on points to a parameter that does not reference this one (<sch:value-of select="string-join($orphans,', ')"/>).</sch:assert>
            <sch:assert test="exists(@depends-on) or empty(key('insert-by-param-id',@id)/ancestor::o:param)">Parameter <sch:value-of select="@id"/> has an unmarked dependency on parameter(s) <sch:value-of select="string-join(key('insert-by-param-id',@id)/ancestor::o:param/@id,', ')"/></sch:assert>-->
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern id="uniqueness-constraints">
        <sch:rule context="*[exists(@id|@uuid)]">
            <sch:assert test="empty(key('by-id',(@id|@uuid)) except .)">ID on element is not unique.</sch:assert>
        </sch:rule>
    </sch:pattern>
    
<!-- Ensure all the values of @name given are known.  -->
    <sch:pattern id="occurrences">
        <sch:rule context="o:part[exists(@name)]">
            <sch:assert test="@name=$known-part-names">@name '<sch:value-of select="@name"/>' on part is not recognized: we expect <sch:value-of select="o:or-sequence($known-part-names)"/></sch:assert>
        </sch:rule>
        <sch:rule context="o:prop[exists(@name)]">
            <sch:assert test="@name=$known-property-names">@name on property is not recognized: we expect <sch:value-of select="o:or-sequence($known-property-names)"/></sch:assert>
            <sch:assert test="not(@name=$rmf-property-names) or @ns='http://csrc.nist.gov/ns/rmf'">Namespace @ns='http://csrc.nist.gov/ns/rmf' is expected on RMF property name '<sch:value-of select="@name"/>'.</sch:assert>
        </sch:rule>
        
    </sch:pattern>
    
    <!-- Controls and their parts may require properties or subparts designated for particular contents. -->
    <sch:pattern id="required-items">
        <sch:rule context="o:control">
            <sch:let name="withdrawn" value="o:prop[@name='status']/@value = 'withdrawn'"/>
           <sch:assert test="count(o:prop[@class='sp800-53']/@name='alt-identifier') eq 1">control must have a child 'prop' with @name='alt-identifier' and @class='sp800-53' (<sch:value-of select="@id"/>)</sch:assert>
           <sch:assert test="count(o:prop[@class='sp800-53a']/@name='alt-identifier') eq 1">control must have a child 'prop' with @name='alt-identifier' and @class="sp800-53a' (<sch:value-of select="@id"/>)</sch:assert>
           <sch:assert test="empty(o:prop[@name='label'])">'label' props are not now being used (<sch:value-of select="@id"/>)</sch:assert>
           <sch:assert test="o:prop/@name='sort-id'">control must have a child 'prop' with @name='sort-id'</sch:assert>
            <sch:assert test="o:part/@name='statement' or $withdrawn">control must have a child 'part' with @name='statement'</sch:assert>
            <!--<sch:assert test="o:part/@name='objective' or $withdrawn">control with name='SP800-53' must have a child 'part' with @name='objective'</sch:assert>-->
        </sch:rule>
        <sch:rule context="o:part[@name='item']">
            <sch:assert test="o:prop/@name='label'">part with name='item' must have a child prop with @name='label'</sch:assert>            <sch:assert test="exists(../o:part[@name='item'][2])" role="warning">Solitary item.</sch:assert>
        </sch:rule>
        <sch:rule context="o:part[@name='assessment-method']">
            <sch:assert test="o:prop/@name='method'">part with name='assessment-method' must have a child prop with @name='method'</sch:assert>
            <sch:assert test="o:part/@name='assessment-objects'">part with name='assessment-method' must have a child part with @name='assessment-objects'</sch:assert>
        </sch:rule>
        <sch:rule context="o:link">
            <sch:assert test="matches(@rel,'\S')"><sch:name/> should have @rel given</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <!-- Many properties exhibit regularities; we need to detect if they are violated. -->
    <!-- Note that these validations will not work on catalogs that do not have, for example, consistent
         continuous numbering of controls and their constituent parts (control, prop, part elements).
         So for example, a catalog produced by resolving a profile, which contains gaps, will show
         those gaps in validation against this Schematron. -->
    <sch:pattern id="appearances">
        <!-- o:control/o:control is a control enhancement -->
        <!-- pre-empting rules for 53A labels       -->
        <sch:rule context="o:control/o:prop[@name = 'label'][@class='sp800-53a']"/>
        
        <sch:rule context="o:control/o:control/o:prop[@name = 'alt-identifier'][@class='sp800-53']">
            <sch:let name="label-regex" value="'^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)\-\d\d?\(\d\d?\)$'"/>
            <!--<sch:assert test="o:singleton(.)">prop with name='label'
                must be a singleton: no other properties named 'label' may appear in the same
                context</sch:assert>-->
            <sch:assert test="matches(@value, $label-regex)">prop with name='label' must match regular expression <sch:value-of select="$label-regex"/></sch:assert>
            <sch:let name="parent-label" value="../../o:prop[@name = 'alt-identifier'][@class='sp800-53']"/>
            <xsl:variable name="formatted-no">
                <xsl:number count="o:control" format="(01)"/>
            </xsl:variable>
            <sch:assert test="@value = (($parent-label/@value) || $formatted-no)">Control enhancement
                label is inconsistent: we expect <sch:value-of select="$parent-label/@value || $formatted-no"/> here</sch:assert>
        </sch:rule>

        <sch:rule context="o:control/o:prop[@name = 'label']">
            <sch:let name="label-regex" value="'^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)[\d\.\-]*$'"/>
            <!--<sch:assert test="o:singleton(.)">prop with name='label'
                must be a singleton: no other properties named 'label' may appear in the same
                context</sch:assert>-->
            <sch:assert test="matches(@value, $label-regex)">prop with name='label' must match regular expression <sch:value-of select="$label-regex"/></sch:assert>
            <sch:assert test="substring(@value,1,2) = upper-case(../../@id)">Control label does not match its family, '<sch:value-of select="upper-case(../../@id)"/></sch:assert>
            <xsl:variable name="formatted-no">
                <xsl:number count="o:control"/>
            </xsl:variable>
            <sch:assert test="replace(@value,'\D','') = $formatted-no">Control label appears to be out of sequence</sch:assert>
        </sch:rule>
        <sch:rule context="o:part[@name = 'statement']">
            <sch:assert test="o:singleton(.)">part with name='statement'
                must be a singleton: no other parts named 'statement' may appear in the same
                context</sch:assert>
        </sch:rule>
        <sch:rule context="o:part[@name = 'item']/o:prop[@name = 'label']">
            <sch:assert test="o:singleton(.)">prop with name='label'
                must be a singleton: no other properties named 'label' may appear in the same
                context</sch:assert>
            <sch:assert test="ends-with(../@id, replace(., '[\.\(\)\[\]]', ''))">Label
                    '<sch:value-of select="."/>' does not match with parent id '<sch:value-of
                    select="../@id"/>'</sch:assert>
        </sch:rule>
        <sch:rule context="o:prop[@name = 'label']">
            <sch:assert test="o:singleton(.)">prop with name='label'
                must be a singleton: no other properties named 'label' may appear in the same
                context</sch:assert>
            <sch:let name="parent-label"
                value="../ancestor::*[o:prop/@name = 'label'][1]/o:prop[@name = 'label']"/>
            <sch:assert test="not(count($parent-label) = 1) or starts-with(., $parent-label)">Label is expected to start with
                inherited label '<sch:value-of select="$parent-label"/>'</sch:assert>
        </sch:rule>
        <sch:rule context="o:prop[@name = 'sort-id']">
            <sch:assert test="o:singleton(.)">prop with name='sort-id'
                must be a singleton: no other properties named 'sort-id' may appear in the same
                context</sch:assert>
        </sch:rule>
        <sch:rule context="o:part[@name = 'assessment-method']/o:prop[@name = 'method']">
            <sch:assert test="o:singleton(.)">prop with name='method'
                must be a singleton: no other properties named 'method' may appear in the same
                context</sch:assert>
            <sch:assert test="@value = ('EXAMINE', 'INTERVIEW', 'TEST')">prop name='method' here must
                have a value 'EXAMINE', 'INTERVIEW', or 'TEST'</sch:assert>
        </sch:rule>
        <sch:rule context="o:prop[@name = 'status']">
            <sch:assert test="o:singleton(.)">prop with name='status'
                must be a singleton: no other properties named 'status' may appear in the same
                context</sch:assert>
            <sch:assert test="exists(parent::o:control)">'status' property should not appear except on controls</sch:assert>
            <sch:assert test="@value = ('withdrawn')">prop name='status' here must have a value
                'withdrawn'</sch:assert>
        </sch:rule>
        <sch:rule context="o:prop[@name = 'method']">
            <sch:assert test="o:singleton(.)">prop with name='method' must be a singleton: no other
                properties named 'method' may appear in the same context</sch:assert>
        </sch:rule>
        <sch:rule context="o:prop[@name = 'keywords']">
            <sch:assert test="exists(parent::o:metadata)">prop with name='keywords' is not expected outside metadata</sch:assert>
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern id="element-content-conversions">
        <sch:rule context="o:p|o:li">
            <sch:report test="matches(.,'^\s*\d')"><sch:name/> starts with a numeral</sch:report>
        </sch:rule>
        <sch:rule context="o:b | o:i | o:u | o:a | o:code | o:q">
            <sch:assert test="matches(.,'\S')"><sch:name/> appears without content</sch:assert>
        </sch:rule>
        <sch:rule context="o:title">
            <sch:report test="matches(.,'\p{Ps}\p{Ll}')">Title contains an open bracket followed by lower case</sch:report>
            <sch:report test="matches(.,'(&#x8212;\S|\S&#x8212;)')">Title contains an em dash without whitespace </sch:report>
            <!--<sch:report test="matches(.,'(/\S|\S/)')">Title contains a slash without whitespace</sch:report>-->
        </sch:rule>
    </sch:pattern>
    
    <sch:pattern id="text-conversions">
        <sch:rule context="*[exists(text()[matches(.,'\S')])]">
            <sch:report test="matches(string(.),'\[Assign')">Check text for dropped paramater ("[Assign")</sch:report>
        </sch:rule>
        
        
    </sch:pattern>

    
    <!-- Returns 'true' for elements without siblings with the same @name value -->
    <xsl:function name="o:singleton" as="xs:boolean">
        <xsl:param name="who" as="element()"/>
        <xsl:variable name="competitors" select="$who/parent::*/(* except $who)[@name = $who/@name]"/>
        <xsl:sequence select="empty($competitors)"/>
    </xsl:function>
    
    <xsl:function name="o:or-sequence" as="xs:string?">
        <xsl:param name="seq" as="item()*"/>
        <xsl:value-of>
            <xsl:for-each select="$seq ! ('''' || . || '''')">
                <xsl:if test="position() ne 1">
                    <xsl:choose>
                        <xsl:when test="(position() eq 2 and last() eq 2)"> or </xsl:when>
                        <xsl:when test="position() = last()">, or </xsl:when>
                        <xsl:otherwise>, </xsl:otherwise>
                    </xsl:choose>
                </xsl:if>
                <xsl:value-of select="."/>
            </xsl:for-each>
        </xsl:value-of>
    </xsl:function>
    

</sch:schema>