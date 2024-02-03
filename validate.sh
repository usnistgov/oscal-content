#!/bin/bash
oscal-cli catalog validate ./src/examples/catalog/xml/basic-catalog.xml
oscal-cli ssp validate ./src/examples/ssp/xml/oscal_leveraged-example_ssp.xml
oscal-cli ssp validate ./src/examples/ssp/xml/oscal_leveraging-example_ssp.xml
oscal-cli ssp validate ./src/examples/ssp/xml/ssp-example.xml
oscal-cli ap validate ./src/examples/ap/xml/ifa_assessment-plan-example.xml
oscal-cli ar validate ./src/examples/ar/xml/ifa_assessment-results-example.xml
oscal-cli ssp validate ./src/examples/ssp/xml/ifa_ssp-example.xml
oscal-cli component-definition validate ./src/examples/component-definition/xml/example-component-definition.xml
oscal-cli poam validate ./src/examples/poam/xml/ifa_plan-of-action-and-milestones.xml
