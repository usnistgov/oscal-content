![Process Content](https://github.com/usnistgov/oscal-content/workflows/Process%20Content%20Artifacts/badge.svg)

# OSCAL Examples Source

This directory contains the source files for all the OSCAL examples located in this repository.

**Automated:** The source for a given file is in one of the supported XML, JSON, or YAML formats. The Continuous Integration and Continuous Deployment (CI/CD) scripting automatically converts these content sources into the alternate formats. As a result, the example files, who's directories are located in the root directory of this repository, should not be modified. Instead, the source of the file should be edited here.

The structure and contents of the examples directory are as follows:

 * [nist.gov/SP800-53/rev4](nist.gov/SP800-53/rev4): This directory contains OSCAL examples of the catalog, and low, moderate, and high baselines defined by NIST Special Publication (SP) 800-53 Revision 4.
 * [nist.gov/SP800-53/rev5](nist.gov/SP800-53/rev5): This directory contains OSCAL examples of the catalog, and low, moderate, and high baselines defined by NIST Special Publication (SP) 800-53B Revision 5 and SP 800-53B Revision 5 respectively.
 * [fedramp.gov](fedramp.gov): This directory contains OSCAL examples of the low, moderate, and high baselines defined by FedRAMP (the Federal Risk and Authorization Management Program).
 * [components](components): This directory contains sample OSCAL component files.
 * [mini-testing](mini-testing): This directory contains sample files that can be used for unit testing in support of regressions of OSCAL.
 
