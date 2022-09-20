<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    xpath-default-namespace="http://csrc.nist.gov/ns/oscal/1.0"
    xmlns="http://csrc.nist.gov/ns/oscal/1.0"
    version="3.0">
    
    <!-- The imported stylesheet makes adjustments to metadata and assigns an updated UUID -->
    <xsl:output indent="false"/>
    
    <xsl:param name="indent" select="2"/>
    
    <xsl:variable name="indent-ws" select="(1 to xs:integer($indent)) ! ' '"/>
    
    <!-- <xsl:import href="https://raw.githubusercontent.com/usnistgov/oscal-tools/main/xslt/generate/generate-oscal.xsl"/>-->
    
    <xsl:strip-space elements="catalog metadata param control group back-matter prop link part mapping target-resource map usage constraint guideline select remarks description test revisions revision role location party responsible-party address external-id resource citation rlink base64 relationship source target ul ol table tr"/>
    
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="comment() | processing-instruction()"/>
    
    <xsl:template priority="101"
        match="/*/metadata/last-modified/text()">
        <xsl:text expand-text="true">{ current-dateTime() }</xsl:text>
    </xsl:template>
    
    <xsl:template match="/*/@uuid" xmlns:uuid="java:java.util.UUID">
        <xsl:attribute name="uuid" expand-text="true">{ uuid:randomUUID() }</xsl:attribute>
    </xsl:template>
        
        <!-- Keeping whitespace but removing it from value, where it is significant (and we don't want it added) -->
        <xsl:strip-space elements="value"/>
        
        <xsl:mode on-no-match="shallow-copy"/>
        
        <xsl:output indent="no"/>
        
        <xsl:template match="/*">
            <xsl:text>&#xA;</xsl:text>
            <xsl:copy>
                <xsl:apply-templates select="@*"/>
                <xsl:apply-templates/>
            </xsl:copy>
        </xsl:template>
        
        <!-- Whitespace spiffup depends on knowing up front which elements have element-only content
             vs text or mixed content. An XSLT such as xsd-ws-assess.xsl can do this.
            
-->  
        
        <xsl:template
            match="catalog/* | metadata/* | param/* | control/* | group/* | back-matter/* | prop/* | link/* | part/* | mapping/* | target-resource/* | map/* | usage/* | constraint/* | guideline/* | select/* | remarks/* | description/* | test/* | revisions/* | revision/* | role/* | location/* | party/* | responsible-party/* | address/* | external-id/* | resource/* | citation/* | rlink/* | base64/* | relationship/* | source/* | target/* | ul/* | ol/* | table/* | tr/*">
            <!-- indent -->
            <xsl:variable name="me" select="."/>
            <!--LF before start tag if no one has closed before us (giving an LF) -->
            <xsl:text expand-text="true">{ (: conditional LF :) '&#xA;'[$me/preceding-sibling::* => empty()] }</xsl:text>
            <xsl:text expand-text="true">{ (: indent :) (ancestor::* ! $indent-ws) => string-join('') }</xsl:text>
            
            <xsl:copy>
                <xsl:copy-of select="@*"/>
                <xsl:apply-templates/>
                <!-- indent for end tag *only* for element-only, not their children -->
                <xsl:apply-templates select="." mode="end-tag-ws"/>
            </xsl:copy>
            <!--LF after end tag-->
            <xsl:text>&#xA;</xsl:text>
        </xsl:template>
        
        <!-- will match any element not element-only -->
        <xsl:template match="*" mode="end-tag-ws"/>
        
        <!--this time matching element-only, but not their children -->
        <xsl:template match="catalog | metadata | param | control | group | back-matter | prop | link | part | mapping | target-resource | map | usage | constraint | guideline | select | remarks | description | test | revisions | revision | role | location | party | responsible-party | address | external-id | resource | citation | rlink | base64 | relationship | source | target | ul | ol | table | tr" mode="end-tag-ws">
            <xsl:if test="exists(*)">
            <xsl:text expand-text="true">{ (ancestor::* ! $indent-ws) => string-join('') }</xsl:text>
            </xsl:if>
        </xsl:template>
        
        <xsl:template match="text()">
            <xsl:sequence select="replace(.,'\s+',' ')"/>
        </xsl:template>
    
    <xsl:template match="title/descendant::text()[1] |
                            label/descendant::text()[1] |
                            value/descendant::text()[1] |
                            expression/descendant::text()[1] |
                            choice/descendant::text()[1] |
                            published/descendant::text()[1] |
                            version/descendant::text()[1] |
                            oscal-version/descendant::text()[1] |
                            document-id/descendant::text()[1] |
                            email-address/descendant::text()[1] |
                            telephone-number/descendant::text()[1] |
                            url/descendant::text()[1] |
                            name/descendant::text()[1] |
                            short-name/descendant::text()[1] |
                            location-uuid/descendant::text()[1] |
                            member-of-organization/descendant::text()[1] |
                            text/descendant::text()[1] |
                            hash/descendant::text()[1] |
                            party-uuid/descendant::text()[1] |
                            addr-line/descendant::text()[1] |
                            city/descendant::text()[1] |
                            state/descendant::text()[1] |
                            postal-code/descendant::text()[1] |
                            country/descendant::text()[1] |
                            h1/descendant::text()[1] |
                            h2/descendant::text()[1] |
                            h3/descendant::text()[1] |
                            h4/descendant::text()[1] |
                            h5/descendant::text()[1] |
                            h6/descendant::text()[1] |
                            p/descendant::text()[1] |
                            pre/descendant::text()[1] |
                            li/descendant::text()[1] |
                            td/descendant::text()[1] |
                            th/descendant::text()[1]">
        <xsl:if test="matches(.,'\S')">
            <xsl:next-match/>
        </xsl:if>
    </xsl:template>
    
</xsl:stylesheet>