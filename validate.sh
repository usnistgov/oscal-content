#!/bin/bash
oscal-cli catalog validate ./src/examples/catalog/xml/basic-catalog.xml
oscal-cli component-definition validate ./src/examples/component-definition/xml/example-component-definition.xml
oscal-cli ssp validate ./src/examples/ssp/xml/oscal_leveraged-example_ssp.xml
oscal-cli ssp validate ./src/examples/ssp/xml/oscal_leveraging-example_ssp.xml
oscal-cli ssp validate ./src/examples/ssp/xml/ssp-example.xml
