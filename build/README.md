# Developer Guide for oscal-content

This directory contains infrastructure used to generate OSCAL document instances and perform checks upon them.

## Prerequisites

The build tools in this directory require a Unix environment that meets those outlined [in the OSCAL submodule's build instructions in its `build/README.md` file](./oscal) for the relevant tag or commit. For a quick reference, here is the [current version of this guidance](https://github.com/usnistgov/OSCAL/tree/develop/build/README.md) on the latest version of the `develop` branch.

## Building

### Overview

All oscal-content build targets are defined in a [`Makefile`](./Makefile).

To summarize the build targets, run `make help`.

To generate all artifacts and run all checks, simply run `make all`.

If you want to run `make` commands outside of this directory, for example from [the top-level directory of this repository](..) cloned onto a developer workstation, use the `-C` argument, such as `make -C ./build all`.

By default, the destination for all generated content is in the [`generated`](./generated) sub-directory. To generate content "inline" like the GitHub Actions CI/CD automation, you want to change the `GEN_CONTENT_DIR` relative to location of the `Makefile`. Either executing `make -C build all GEN_CONTENT_DIR=..` from the top-level directory or executing `make all GEN_CONTENT_DIR=..` from this directory are correct. Either will generate source content in [`src/nist.gov`](../src/nist.gov) and [`examples`](../src/examples) into [`nist.gov`](../nist.gov) and [`examples`](../examples), respectively.

### Build OSCAL Tools and Install Dependencies

You can use the `make all` to build the necessary schemas and content converters in addition to other steps, or use specific targets to build and install accordingly.

```sh
make build
make dependencies
```

### Artifact Generation

You can use the `make artifacts` to generate all artifacts in addition to other steps, or you can use specific target(s) to generate a specific artifact.

```sh
make copy-readmes
make copy-xml-content
make resolve-xml-profiles
make convert-min-json-content
make reformat-json-content
make convert-yaml-content
```

### Checks

You can use the `make checks` to validate generated artifacts in addition to other steps, or you can use specific target(s) to generate a specific artifact.

```sh
make validate-xml-content
make validate-json-content
make validate-yaml-content
```

### Cleaning Dependencies and Artifacts

You can use the `make clean` to clean all artifacts generated from `make all` or other [artifact generation targets](#artifact-generation). You can als also use any of the targets below to clean specific generated artifacts, while choosing to preserve others.

```sh
make clean-build
make clean-dependencies
make clean-readmes
make clean-json-content
make clean-xml-content
make clean-yaml-content
```
