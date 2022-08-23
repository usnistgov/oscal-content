<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    xpath-default-namespace="http://csrc.nist.gov/ns/oscal/1.0"
    version="3.0">
    
    <!-- The imported stylesheet makes adjustments to metadata and assigns an updated UUID -->
    <xsl:output indent="false"/>
    <xsl:import href="../../../../../../oscal-tools/xslt/generate/generate-oscal.xsl"/>
    <!-- <xsl:import href="https://raw.githubusercontent.com/usnistgov/oscal-tools/main/xslt/generate/generate-oscal.xsl"/>-->
    
    <xsl:template match="catalog">
        <xsl:text>&#xA;</xsl:text>
        <xsl:apply-imports/>
    </xsl:template>
    
</xsl:stylesheet>