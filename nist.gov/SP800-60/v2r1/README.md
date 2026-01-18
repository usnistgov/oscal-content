# NIST SP 800-60 Information Types in OSCAL Format

This directory contains NIST Special Publication 800-60 Volume II Revision 1 information types digitalized in OSCAL formats.

## Overview

NIST SP 800-60 provides guidance for mapping types of information and information systems to security categories. Volume II contains the complete list of information types used for FIPS 199 security categorization of federal information and information systems.

This OSCAL catalog enables automated tools to:
- Present standardized information type selections in System Security Plans (SSPs)
- Calculate system security impact levels based on processed information types
- Support FIPS 199 security categorization requirements
- Enable consistent information type definitions across organizations

## Files

- **`json/NIST_SP800-60_information_types.json`**: OSCAL JSON format (171 information types)
- **`xml/NIST_SP800-60_information_types.xml`**: OSCAL XML format (generated from JSON)
- **`yaml/NIST_SP800-60_information_types.yaml`**: OSCAL YAML format (generated from JSON)

## Content Summary

### Information Types Included

**Management and Support (C.x.x.x) - 77 types**
Business management and support services common to most government agencies:

| Category | Description | Count |
|----------|-------------|-------|
| C.2.1.x | Controls and Oversight | 3 |
| C.2.2.x | Regulatory Development | 1 |
| C.2.3.x | Planning and Budgeting | 7 |
| C.2.4.x | Internal Risk Management and Mitigation | 4 |
| C.2.5.x | Revenue Collection | 2 |
| C.2.6.x | Public Affairs | 3 |
| C.2.7.x | Legislative Relations | 1 |
| C.2.8.x | General Government | 17 |
| C.3.1.x | Administrative Management | 5 |
| C.3.2.x | Financial Management | 15 |
| C.3.3.x | Human Resource Management | 8 |
| C.3.4.x | Supply Chain Management | 7 |
| C.3.5.x | Information and Technology Management | 4 |

**Mission-Based (D.x.x) - 94 types**
Agency-specific mission delivery information types:

| Category | Description | Count |
|----------|-------------|-------|
| D.1 | Defense and National Security | 1 |
| D.2.x | Homeland Security | 6 |
| D.3 | Intelligence Operations | 1 |
| D.4.x | Disaster Management | 4 |
| D.5.x | International Affairs and Commerce | 9 |
| D.6.x | Natural Resources | 10 |
| D.7.x | Energy | 2 |
| D.8.x | Environmental Management | 3 |
| D.9.x | Economic Development | 3 |
| D.10.x | Community and Social Services | 7 |
| D.11.x | Transportation | 10 |
| D.12.x | Education | 3 |
| D.13.x | Workforce Management | 2 |
| D.14.x | Health | 3 |
| D.15.x | Income Security | 4 |
| D.16.x | Law Enforcement | 7 |
| D.17.x | Litigation and Judicial Activities | 3 |
| D.18.x | Federal Correctional Activities | 2 |
| D.19.x | Research, Development, and Innovation | 4 |
| D.20.x | Knowledge Creation and Management | 2 |
| D.21.x | Regulatory Compliance and Enforcement | 2 |
| D.22.x | Public Goods Creation and Management | 1 |
| D.23.x | Federal Financial Assistance | 3 |
| D.24.x | Credit and Insurance | 2 |
| D.25.x | Transfers to State/Local Governments | 4 |
| D.26.x | Direct Services for Citizens | 2 |

**Total: 171 information types**

## Data Structure

Each information type includes:

```json
{
  "uuid": "unique-identifier",
  "title": "Information Type Name",
  "description": "Information type description with source context",
  "categorizations": [
    {
      "system": "https://doi.org/10.6028/NIST.SP.800-60v2r1",
      "information-type-ids": ["C.x.x.x or D.x.x"]
    }
  ],
  "confidentiality-impact": {
    "base": "fips-199-low|moderate|high",
    "selected": "fips-199-low|moderate|high"
  },
  "integrity-impact": {
    "base": "fips-199-low|moderate|high",
    "selected": "fips-199-low|moderate|high"
  },
  "availability-impact": {
    "base": "fips-199-low|moderate|high",
    "selected": "fips-199-low|moderate|high"
  }
}
```

### Field Descriptions

- **`uuid`**: Unique identifier for the information type (RFC 4122 format)
- **`title`**: Official name from NIST SP 800-60 Volume II
- **`description`**: Contextual description noting source and category
- **`categorizations`**: Reference to authoritative source document
  - **`system`**: DOI link to NIST SP 800-60 Volume II Revision 1
  - **`information-type-ids`**: Original classification code(s)
- **`confidentiality-impact`**: FIPS 199 confidentiality impact level
  - **`base`**: Recommended impact level from SP 800-60
  - **`selected`**: Impact level selected for specific system (defaults to base)
- **`integrity-impact`**: FIPS 199 integrity impact level
- **`availability-impact`**: FIPS 199 availability impact level

## Source Material

- **Publication**: NIST Special Publication 800-60 Volume II Revision 1
- **Title**: Guide for Mapping Types of Information and Information Systems to Security Categories: Appendices to Volume I
- **Publication Date**: August 2008
- **DOI**: https://doi.org/10.6028/NIST.SP.800-60v2r1
- **Authors**: Stine, Kevin, Kissel, Rich, Barker, William C., Lee, Jim, Fahlsing, Anne
- **Authority**: Federal Information Processing Standards (FIPS) 199

### Related Publications

- **[NIST SP 800-60 Volume I](https://doi.org/10.6028/NIST.SP.800-60v1r1)**: Guide for Mapping Types of Information and Information Systems to Security Categories
- **[FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)**: Standards for Security Categorization of Federal Information and Information Systems
- **[NIST SP 800-53](https://doi.org/10.6028/NIST.SP.800-53r5)**: Security and Privacy Controls for Information Systems and Organizations

## Generation Process

The OSCAL format was created through the following process:

1. **Source Extraction**: Information types extracted from official NIST SP 800-60 Volume II publication
2. **Data Validation**: Verified all 171 types present with correct impact levels
3. **OSCAL Structuring**: Formatted data according to OSCAL 1.1.2 specification
4. **UUID Generation**: Assigned unique identifiers to each information type
5. **Compliance Verification**: Validated against OSCAL schema and conventions

### Generation Tools

- Python 3 script for parsing and structuring
- UUID generation (RFC 4122)
- JSON formatting and validation
- Cross-reference checking with official publication

## Usage in OSCAL SSPs

### Including Information Types

Information types from this catalog can be referenced in System Security Plans:

```json
{
  "system-security-plan": {
    "system-characteristics": {
      "information-types": [
        {
          "uuid": "119affd7-1792-4dd4-8ca7-5457a847bc4a",
          "title": "Corrective Action",
          "categorizations": [
            {
              "system": "https://doi.org/10.6028/NIST.SP.800-60v2r1",
              "information-type-ids": ["C.2.1.1"]
            }
          ],
          "confidentiality-impact": {
            "base": "fips-199-low",
            "selected": "fips-199-low"
          },
          "integrity-impact": {
            "base": "fips-199-low",
            "selected": "fips-199-low"
          },
          "availability-impact": {
            "base": "fips-199-low",
            "selected": "fips-199-low"
          }
        }
      ]
    }
  }
}
```

### Security Categorization

System security impact level is determined by the highest impact level across all information types processed:

```json
{
  "security-impact-level": {
    "security-objective-confidentiality": "fips-199-moderate",
    "security-objective-integrity": "fips-199-high",
    "security-objective-availability": "fips-199-low"
  }
}
```

**System categorization**: `SC system = {(confidentiality, moderate), (integrity, high), (availability, low)}`

Per FIPS 199, this system would be categorized as **HIGH** (highest impact level present).

### Control Baseline Selection

System categorization determines the applicable SP 800-53 control baseline:

- **LOW system**: NIST SP 800-53 Rev 5 LOW baseline
- **MODERATE system**: NIST SP 800-53 Rev 5 MODERATE baseline  
- **HIGH system**: NIST SP 800-53 Rev 5 HIGH baseline

## Implementation Guidelines

### For Tool Developers

**1. Information Type Selection Interface**
```typescript
// Load information types catalog
const catalog = await loadOscalCatalog('NIST_SP800-60_information_types.json');

// Filter by category
const managementTypes = catalog.informationTypes.filter(
  type => type.categorizations[0].informationTypeIds[0].startsWith('C.')
);

const missionTypes = catalog.informationTypes.filter(
  type => type.categorizations[0].informationTypeIds[0].startsWith('D.')
);

// Display in UI with search/filter capabilities
```

**2. Impact Level Calculation**
```typescript
function calculateSystemImpact(selectedTypes) {
  const impacts = {
    confidentiality: 'fips-199-low',
    integrity: 'fips-199-low',
    availability: 'fips-199-low'
  };
  
  const levels = { 'fips-199-low': 1, 'fips-199-moderate': 2, 'fips-199-high': 3 };
  
  selectedTypes.forEach(type => {
    // Take highest impact level for each CIA triad component
    if (levels[type.confidentialityImpact.selected] > levels[impacts.confidentiality]) {
      impacts.confidentiality = type.confidentialityImpact.selected;
    }
    // Repeat for integrity and availability...
  });
  
  return impacts;
}
```

**3. Baseline Selection**
```typescript
function selectControlBaseline(systemImpact) {
  const highestLevel = Math.max(
    levels[systemImpact.confidentiality],
    levels[systemImpact.integrity],
    levels[systemImpact.availability]
  );
  
  if (highestLevel === 3) return 'HIGH';
  if (highestLevel === 2) return 'MODERATE';
  return 'LOW';
}
```

### For SSP Authors

1. **Identify Information Types**: Determine which information types your system processes
2. **Select from Catalog**: Choose applicable types from the 171 available
3. **Review Impact Levels**: Validate that base impact levels are appropriate for your system
4. **Adjust if Necessary**: Modify `selected` values if system-specific factors warrant different levels
5. **Calculate System Impact**: Determine overall system categorization
6. **Select Control Baseline**: Apply appropriate SP 800-53 baseline based on categorization

## Validation

This catalog has been validated for:

- ✅ **Completeness**: All 171 information types from NIST SP 800-60 V2R1 included
- ✅ **Accuracy**: Impact levels match official publication
- ✅ **OSCAL Compliance**: Structure conforms to OSCAL 1.1.2 specification
- ✅ **UUID Format**: All UUIDs are RFC 4122 compliant
- ✅ **Impact Format**: Uses proper `fips-199-{level}` convention
- ✅ **Metadata**: Complete publication and version information included
- ✅ **Categorizations**: DOI reference to authoritative source present

## Limitations and Considerations

1. **Publication Date**: SP 800-60 V2R1 was published in August 2008. While information types remain relevant, organizations should consider evolving technology contexts.

2. **Base vs. Selected**: The `base` impact levels are recommendations. Organizations must evaluate their specific circumstances and may adjust `selected` values accordingly.

3. **Provisional Authorization**: Some information types may have impact levels dependent on whether data is provisional or final. Review guidance in SP 800-60 Volume I.

4. **Aggregate Systems**: Systems processing multiple information types inherit the highest impact level across all types per FIPS 199.

5. **Special Circumstances**: Certain information types (especially D.1, D.3) may require tailored impact determinations based on classification levels and national security considerations.

## License and Attribution

This OSCAL catalog is derived from NIST Special Publication 800-60 Volume II Revision 1, which is a work of the U.S. Government and is not subject to copyright protection in the United States (17 U.S.C. § 105).

This OSCAL representation is released under CC0 1.0 Universal (public domain dedication).

**Citation**:
```
Stine, K., Kissel, R., Barker, W. C., Lee, J., & Fahlsing, A. (2008). 
NIST Special Publication 800-60 Volume II Revision 1: Guide for Mapping 
Types of Information and Information Systems to Security Categories: 
Appendices to Volume I. National Institute of Standards and Technology. 
https://doi.org/10.6028/NIST.SP.800-60v2r1
```

## Contact and Contributions

For questions, issues, or contributions related to this OSCAL content:

- **NIST OSCAL Project**: https://pages.nist.gov/OSCAL/
- **GitHub Repository**: https://github.com/usnistgov/oscal-content
- **Mailing List**: oscal-dev@nist.gov

## Version History

- **1.0** (January 2026): Initial OSCAL digitalization of NIST SP 800-60 V2R1 information types
  - 171 information types included
  - OSCAL 1.1.2 format
  - JSON source with XML and YAML conversions
