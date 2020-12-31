<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2"
    xmlns:sqf="http://www.schematron-quickfix.com/validator/process"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:o="http://csrc.nist.gov/ns/oscal/1.0">
    
    <sch:ns prefix="o"     uri="http://csrc.nist.gov/ns/oscal/1.0"/>
    <sch:ns prefix="oscal" uri="http://csrc.nist.gov/ns/oscal/1.0"/>
    
    <!-- This Schematron checks the representation of labels in SP800-53
           - labels given on controls and their parts correspond to their @id values
           - labels are formatted correctly and represent the order of the document
             by incrementing regularly -->
         
    <xsl:key name="control-by-id" match="o:control" use="@id"/>
    
    <sch:pattern>
      <sch:rule context="o:call">
          <sch:let name="imported-catalog" value="ancestor::o:import/document(@href)/o:catalog"/>
          <sch:let name="control-id"       value="@control-id"/>
          
          <!--<sch:report test="true()">
              <xsl:text expand-text="true">Seeing { count( $imported-catalog/key('control-by-id',$control-id) ) } in { count($imported-catalog ) }</xsl:text>
          </sch:report>-->
          <sch:report test="$imported-catalog/key('control-by-id',$control-id)/o:prop[@name='status']='withdrawn'">
              <xsl:text expand-text="true">Profile calls control { @control-id }, which has a property[@name='status']='withdrawn'.</xsl:text>
          </sch:report>
          
      </sch:rule> 
    </sch:pattern>
    
</sch:schema>