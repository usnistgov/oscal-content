<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="#all"
    xpath-default-namespace="http://csrc.nist.gov/ns/oscal/1.0"
    xmlns="http://csrc.nist.gov/ns/oscal/1.0"
    xmlns:o="http://csrc.nist.gov/ns/oscal/1.0"
    version="3.0">
    
    
    <xsl:output indent="false"/>
    
    <!--<xsl:param name="indent" select="2"/>-->
    
    <!--<xsl:variable name="indent-ws" select="(1 to xs:integer($indent)) ! ' '"/>-->
    
    <!-- <xsl:import href="https://raw.githubusercontent.com/usnistgov/oscal-tools/main/xslt/generate/generate-oscal.xsl"/>-->
    
    <!--<xsl:strip-space elements="catalog metadata param control group back-matter prop link part mapping target-resource map usage constraint guideline select remarks description test revisions revision role location party responsible-party address external-id resource citation rlink base64 relationship source target ul ol table tr"/>-->
    
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="comment() | processing-instruction()"/>
    
    <xsl:template priority="101"
        match="/*/metadata/last-modified/text()">
        <xsl:text expand-text="true">{ current-dateTime() }</xsl:text>
    </xsl:template>
    
    <xsl:template match="/*">
        <xsl:text>&#xA;</xsl:text>
        <xsl:next-match/>
    </xsl:template>
    
    <xsl:template match="/*/@uuid" xmlns:uuid="java:java.util.UUID">
        <xsl:attribute name="uuid" expand-text="true">{ uuid:randomUUID() }</xsl:attribute>
    </xsl:template>
    
    <xsl:template match="metadata/version">
        <version>5.2.3</version>
    </xsl:template>
    
    <!-- returns labels that are not followed by other labels designated as the SP800-53A scheme
         (with padding zeros) - in this data set this gives a single label, an sp800-53a
         when available or the only label when not -->
    <xsl:function name="o:label" as="xs:string?">
        <xsl:param name="n" as="element()"/>
        <xsl:value-of>
            <!-- if an sp800-53 classed label is available, return it
             if not, pad a decimal value with zeros to two places so '1' returns '01.' -->
            <xsl:variable name="label53a"
                select="$n/child::prop[@name = 'label'][@class = 'sp800-53a'][1]"/>
            <xsl:sequence select="$label53a/string(@value)"/>
            <!-- padding digits here -->
            <xsl:if test="empty($label53a)">
                <xsl:analyze-string select="$n/child::prop[@name = 'label'][1]/@value" regex="[0-9]+">
                    <xsl:matching-substring>
                        <xsl:value-of select="format-number(number(.), '01')"/>
                    </xsl:matching-substring>
                    <xsl:non-matching-substring>
                        <xsl:value-of select="."/>
                    </xsl:non-matching-substring>
                </xsl:analyze-string>
            </xsl:if>
        </xsl:value-of>
            
    </xsl:function>
    
    <xsl:function name="o:long-label" as="xs:string">
        <xsl:param name="p" as="element()"/>
        <!--for an 'item' part with a truncated label i.e. '(a)', returns the long label AC-02(a) -->
        <xsl:variable name="ancestry" select="$p/ancestor-or-self::* except $p/ancestor::control[1]/ancestor::*"/>
        <xsl:sequence select="string-join($ancestry/o:label(.),'') => replace('\p{P}','')"/>
    </xsl:function>
    
    <xsl:key name="item-by-label" match="part[@name=('statement','item')]" use="o:long-label(.)"/>
    
    <!-- strips away bracketed substrings
          so 'AC-01(a)[2](2)[2]' returns 'AC-01a2' -->
          
    <xsl:function name="o:reduce-label" as="xs:string">
        <xsl:param name="p" as="element()"/>
        <xsl:variable name="l" select="o:label($p)"/>
        <xsl:text expand-text="true">{ replace($l,'\[[0-9]+?\]','')  => replace('\p{P}','') }</xsl:text>
    </xsl:function>
    
    <!--<xsl:template match="part[@name=('statement','item')]">
       <xsl:next-match/>     
       
        <xsl:message expand-text="true">Seeing { @name } { @id } being tagged as '{ o:long-label(.) }'</xsl:message>
    </xsl:template>-->
    
    
<!-- 
     on assessment-objective #AC-01a.01(a)
        the reduced label is 'AC-01a.01(a)' linking to '' (0)
    
    -->
    <!-- Each part[@name='assessment-objective'] has a single label -->
    <xsl:template match="part[@name='assessment-objective']/link"/>

    <xsl:template match="part[@name='assessment-objective']/text()[not(matches(.,'\S'))]">
        <xsl:if test="empty(following-sibling::*[1]/self::link)">
            <xsl:next-match/>
        </xsl:if>
    </xsl:template>
    

    <xsl:template match="part[@name='assessment-objective']">
        <xsl:copy>
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates/>
            

            <xsl:variable name="part-key" select="o:reduce-label(.)"/>
            <xsl:variable name="statement-item" select="key('item-by-label',$part-key)"/>
            
            <xsl:text>  </xsl:text>
            <link rel="depends-on" href="#{ $statement-item/@id }"></link>
            
            <xsl:if test="empty($statement-item)">
                <xsl:message expand-text="true">No link made for part '{ o:label(.) }'</xsl:message>
            </xsl:if>
            <xsl:copy-of select="text()[last()]"></xsl:copy-of>
        </xsl:copy>
        
        
    </xsl:template>
    
    
</xsl:stylesheet>