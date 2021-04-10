![Process Content](https://github.com/usnistgov/oscal-content/workflows/Process%20Content%20Artifacts/badge.svg)

# OSCAL Content Sources

This directory contains the source files for all the OSCAL content located in this repository.

**Automated:** The source for a given file is in one of the supported XML, JSON, or YAML formats. The Continuous Integration and Continuous Deployment (CI/CD) scripting automatically converts these content sources into the alternate formats. As a result, the example files, who's directories are located in the root directory of this repository, should not be modified. Instead, the source of the file should be edited here.

The contents of this directory are as follows:

- [config](config): This configuration file identifies which content files the CI/CD process needs to convert into alternate formats.
- [examples](examples): This directory contains sample OSCAL content organized by OSCAL model.
- [fedramp.gov](fedramp.gov): This directory contains OSCAL the low, moderate, and high baselines defined by the [Federal Risk and Authorization Management Program](https://www.fedramp.gov/) (FedRAMP).
- [nist.gov/SP800-53/rev4](nist.gov/SP800-53/rev4): This directory contains OSCAL examples of the catalog, and low, moderate, and high baselines defined by NIST Special Publication (SP) [800-53 Revision 4](https://csrc.nist.gov/publications/detail/sp/800-53/rev-4/final).
- [nist.gov/SP800-53/rev5](nist.gov/SP800-53/rev5): This directory contains OSCAL examples of the catalog, and low, moderate, and high baselines defined by NIST Special Publication (SP) [800-53 Revision 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final[) and [SP 800-53B](https://csrc.nist.gov/publications/detail/sp/800-53b/final) respectively.
  - [nist.gov/SP800-53/rev5/draft](nist.gov/SP800-53/rev5/draft): Earlier releases of draft content for the Final Public Draft (FPD) version of the Revision 5 catalog and baselines. These drafts, are now superseded by the final versions above, and are provided for reference only.
