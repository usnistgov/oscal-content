#!/bin/bash
oscal-cli catalog validate ./src/examples/catalog/xml/basic-catalog.xml
oscal-cli ssp validate ./src/examples/ssp/xml/oscal_leveraged-example_ssp.xml
oscal-cli ssp validate ./src/examples/ssp/xml/oscal_leveraging-example_ssp.xml
oscal-cli ssp validate ./src/examples/ssp/xml/ssp-example.xml
oscal-cli ap validate ./src/examples/ap/xml/assessment-plan-example-1.xml
oscal-cli ar validate ./src/examples/ar/xml/assessment-results-example-1.xml
oscal-cli ssp validate ./src/examples/ssp/xml/workshop-ssp-example.xml
oscal-cli component-definition validate ./src/examples/component-definition/xml/example-component-definition.xml
oscal-cli poam validate ./src/examples/poam/xml/plan-of-action-and-milestones.xml
