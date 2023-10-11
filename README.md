[![Gitter](https://img.shields.io/gitter/room/usnistgov-OSCAL/Lobby)](https://gitter.im/usnistgov-OSCAL/Lobby) ![Process Content](https://github.com/usnistgov/oscal-content/workflows/Process%20Content/badge.svg?branch=main)

# OSCAL Examples

This directory contains numerous OSCAL examples in XML, JSON, and YAML formats based on [the latest OSCAL stable release](github.com/usnistgov/OSCAL/releases/latest).

These files are maintained by a Continuous Integration and Continuous Deployment (CI/CD) process that automatically converts source content into the alternate formats found in the many subdirectories of this repository. As a result, these example files should not be modified. Instead, the source of the file should be edited in the [src](src) subdirectories.

The structure and contents of the examples directory are as follows:

- [examples](examples): This directory contains sample OSCAL content organized by OSCAL model.
- [nist.gov/SP800-53/rev4](nist.gov/SP800-53/rev4): This directory contains OSCAL examples of the catalog, and low, moderate, and high baselines defined by NIST Special Publication (SP) [800-53 Revision 4](https://csrc.nist.gov/publications/detail/sp/800-53/rev-4/final).
- [nist.gov/SP800-53/rev5](nist.gov/SP800-53/rev5): This directory contains OSCAL examples of the catalog, and low, moderate, and high baselines defined by NIST Special Publication (SP) [800-53 Revision 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) and [SP 800-53B](https://csrc.nist.gov/publications/detail/sp/800-53b/final) respectively.
- [src](src): This directory contains the source files for all the OSCAL examples located in this repository.
- [build](build): This directory includes [instructions](./build/README.md) and tools to build OSCAL dependencies, generate, convert, and check example content in this repository for release.
