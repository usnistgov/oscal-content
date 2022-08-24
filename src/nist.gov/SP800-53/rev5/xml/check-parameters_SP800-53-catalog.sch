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
    
    
    <xsl:function name="o:is-oscal" as="xs:boolean">
        <xsl:param name="who" as="element()"/>
        <xsl:sequence select="$who/(empty(@ns) or @ns='http://csrc.nist.gov/ns/oscal')"/>
    </xsl:function>

    <!--Any parameter insertion must point to a parameter either in its control hierarchy (a child of an ancestor control)
    or a child of a control referenced by the containing control or enhancement
    with <link rel="required" href="#[param parent ID]"/> -->
    <!--see  /control[@id='sc-42.2'] for an example -->
    

    <sch:let name="show-info" value="false()"/>
    
    <sch:pattern>
        <sch:rule context="o:insert[@type='param']">
            <sch:let name="my-param" value="key('parameter-by-id',@id-ref)"/>
            <sch:let name="dependencies" value="ancestor::o:control[1]/o:link[@rel='required']/key('link-targets',@href)"/>
            <sch:let name="sits-outside" value="exists($my-param/parent::* except ancestor::o:control)"/>
            <sch:report test="exists($my-param/parent::* intersect $dependencies)" role="info">Reference is made to parameter <sch:value-of select="@id-ref"/> outside the control context of the insertion, control <sch:value-of select="ancestor::o:control[1]/@id"/> (the dependency is marked).</sch:report>
            <sch:assert test="empty($my-param/parent::* except (ancestor::o:control[1] union $dependencies))" role="warning">Reference is made to parameter <sch:value-of select="@id-ref"/> outside the control context of the insertion, and no dependency is marked (use &lt;link rel="required" href="<sch:value-of select="$my-param/../@id"/>"/> on control <sch:value-of select="ancestor::o:control[1]/@id"/>).</sch:assert>
            <!--<sch:assert test="empty($my-param/parent::* except (ancestor::o:control union $dependencies))" role="error">Reference is made to a parameter <sch:value-of select="@id-ref"/> outside the hierarchy of the insertion, and no dependency is marked (use &lt;link rel="required" href="<sch:value-of select="$my-param/../@id"/>"/> on control <sch:value-of select="ancestor::o:control[1]/@id"/>).</sch:assert>-->
        </sch:rule>
    </sch:pattern>

</sch:schema>