<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns="http://csrc.nist.gov/ns/oscal/1.0"
                xmlns:uuid="java:java.util.UUID"
                xpath-default-namespace="http://csrc.nist.gov/ns/oscal/1.0"
                exclude-result-prefixes="#all"
                version="3.0">


   <xsl:output indent="yes"/>
   
   <xsl:mode on-no-match="shallow-copy"/>
   
   <xsl:mode name="copy" on-no-match="shallow-copy"/>

   <xsl:param name="schema-location" as="xs:string" select="''"/>
   
   <xsl:variable select="uuid:randomUUID()" name="new-document-uuid"/>
   
   <xsl:template match="/comment()"/>
   
   <xsl:template match="/*">
      <xsl:copy copy-namespaces="no">
         <xsl:apply-templates select="@* except @id"/>
         <xsl:attribute name="uuid" select="$new-document-uuid"/>
         <xsl:if test="$schema-location => boolean()">
            <xsl:attribute name="xsi:schemaLocation" namespace="http://www.w3.org/2001/XMLSchema-instance" select="$schema-location"/>
         </xsl:if>
         <xsl:apply-templates/>
      </xsl:copy>
   </xsl:template>

   <xsl:template match="@xsi:schemaLocation"/>
   
   <xsl:template match="oscal-version">
      <oscal-version>1.0.0</oscal-version>
   </xsl:template>
   
   <xsl:template match="metadata/version[count(tokenize(.,'\.')) > 2]">
      <xsl:copy>
         <xsl:iterate select="tokenize(., '\.')">
            <xsl:choose>
               <xsl:when test="position() eq last()">
                  <xsl:value-of select="(.[. castable as xs:integer] ! xs:integer(.) + 1, .)[1]"/>
               </xsl:when>
               <xsl:otherwise>
                  <xsl:value-of select="."/>
                  <xsl:text>.</xsl:text>
               </xsl:otherwise>
            </xsl:choose>
         </xsl:iterate>
      </xsl:copy>     
   </xsl:template>
   
   <xsl:template match="last-modified" expand-text="true">
      <last-modified>{ current-dateTime() }</last-modified>
   </xsl:template>
      
   <!--Surgical mods rectifying errors in source-->
   
   <xsl:template match="part[@id='ca-1_obj.a.1.a-2']/p">
      <p>the  <insert type="param" id-ref="ca-01_odp.03"/> assessment, authorization, and monitoring policy addresses scope;</p>
   </xsl:template>
   
   <xsl:template match="part[@id='ca-1_obj.a.1.a-3']/p">
      <p>the <insert type="param" id-ref="ca-01_odp.03"/> assessment, authorization, and monitoring policy addresses roles;</p>
   </xsl:template>
   
   <xsl:template match="control[@id='ia-8.3']/p">
      <title>Use of FICAM-approved Products</title>
   </xsl:template>
   
   <xsl:template priority="5" match="param[@id='pe-06.02_odp.03']/guideline/p">
      <p>automated mechanisms used to recognize classes or types of intrusions and initiate response actions (defined in <a href="#pe-06.02_odp.02">PE-06(02)_ODP</a>) are defined;</p>
   </xsl:template>
   
   <xsl:key name="param-by-odp-key" match="param" use="prop[@name='label'][@class='sp800-53a']/@value"/>
   
   <!--ODPs inside guidelines have not yet been recognized -->
   <!--Hitherto this content had no markup so string crunching is safe -->
   <xsl:template match="guideline/p">
      <xsl:variable name="home" select="/"/>
      <xsl:copy>
         <xsl:apply-templates select="@*"/>
         <xsl:analyze-string select="string(.)" regex="&lt;(.+?)>">
            <xsl:matching-substring>
               <xsl:variable name="odp-key" select="regex-group(1) ! tokenize(., '\s+')[1]"/>
               <xsl:variable name="param-target" select="key('param-by-odp-key', $odp-key, $home)"/>
               <xsl:choose>
                  <xsl:when test="empty($param-target)">
                     <xsl:message expand-text="true">Oops, parameter not targeted... { $odp-key
                        }</xsl:message>
                     <xsl:value-of select="regex-group(0)"/>
                  </xsl:when>
                  <xsl:otherwise>
                     <insert type="param" id-ref="{$param-target/@id}"/>
                  </xsl:otherwise>
               </xsl:choose>
               
            </xsl:matching-substring>
            <xsl:non-matching-substring>
               <xsl:sequence select="."/>
            </xsl:non-matching-substring>
         </xsl:analyze-string>
      </xsl:copy>
   </xsl:template>

</xsl:stylesheet>
