# NIST Special Publication (SP) 800-53: Controls and SP 800-53A Rev 5 Assessment Procedures in OSCAL format

Data sources here are published into the appropriate target directory: so /src/nist.gov/SP800-53/rev5/xml/ files, for example, are published into the /nist.gov/SP800-53/rev5 directory, *in all supported formats* (XML, JSON, YAML), along with derived files or resources such as static resolved profiles (serialized as valid OSCAL catalogs).

For use, those copies should be considered to be the preferred reference versions.

In addition to XML source files for those public resources, this directory also contains utilities convenient for maintenance and error-checking.

- `validate-labels_SP800-53-catalog.sch`
  Labels in a full catalog should be structured, sorted and aligned, as confirmed by this Schematron

- `validate-names-etc_SP800-53-catalog.sch`
  Miscellaneous sanity checks over catalogs
  
- `check-parameters_SP800-53-catalog.sch`
  Checks parameter references to ensure parameters are available either in the ancestry of the reference point, or a control declared as required (as a dependency)

- `validate-profiles_SP800-53B-baselines.sch`
  Validates links given in profiles to confirm they resolve successfully in referenced control sets (works on `catalog` not on  `profile` inputs)

An XSLT utility, `oscal-restamp.xsl` can be applied to generate a copy of an OSCAL file with timestamp refreshed and a new UUID assigned (at the top level).
