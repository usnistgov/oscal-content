SHELL:=/usr/bin/env bash

.PHONY: help
# Run "make" or "make help" to get a list of user targets
# Adapted from https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?##.*$$' $(MAKEFILE_LIST) | awk 'BEGIN { \
	 FS = ":.*?## "; \
	 printf "\033[1m%-30s\033[0m %s\n", "TARGET", "DESCRIPTION" \
	} \
	{ printf "\033[32m%-30s\033[0m %s\n", $$1, $$2 }'

.PHONY: all
all: artifacts checks ## Run all steps for content preparation

.PHONY: artifacts
artifacts: copy-readmes copy-xml-content resolve-xml-profiles convert-min-json-content reformat-json-content convert-yaml-content ## Generate all artifacts

.PHONY: checks
checks: validate-xml-content validate-json-content validate-yaml-content validate-xml-by-cli ## Check all content with schema and other validation methods

.PHONY: clean
clean: clean-core-artifacts clean-readmes clean-json-content clean-xml-content clean-yaml-content ## Clean all generated content

#
# Dependencies
#





CURL_INSTALL_OPTS:=--silent --location

# Used to automatically install certain executables
JQ_INSTALL_BIN:=jq-linux-amd64
JQ_INSTALL_VERSION:=jq-1.7
JQ_INSTALL_URL:=https://github.com/jqlang/jq/releases/download/$(JQ_INSTALL_VERSION)/$(JQ_INSTALL_BIN)
JQ_INSTALL_PATH:=./jq
JQ_PATH:=$(shell which jq || echo $(JQ_INSTALL_PATH))
JQ_INSTALL_COMMAND=curl $(CURL_INSTALL_OPTS) -o $(JQ_INSTALL_PATH) $(JQ_INSTALL_URL) && chmod +x $(JQ_INSTALL_PATH)

# Adjust JQ_INSTALL_BIN as appropriate, e.x. `make JQ_INSTALL_BIN=./jq_darwin_arm64`
$(JQ_INSTALL_PATH):
	@$(JQ_INSTALL_COMMAND)

YQ_INSTALL_BIN:=yq_linux_amd64
YQ_INSTALL_VERSION:=v4.35.2
YQ_INSTALL_URL:=https://github.com/mikefarah/yq/releases/download/$(YQ_INSTALL_VERSION)/$(YQ_INSTALL_BIN)
YQ_INSTALL_PATH:=./yq
YQ_PATH:=$(shell which yq || echo $(YQ_INSTALL_PATH))
YQ_INSTALL_COMMAND:=curl $(CURL_INSTALL_OPTS) -o $(YQ_INSTALL_PATH) $(YQ_INSTALL_URL) && chmod +x $(YQ_INSTALL_PATH)

$(YQ_INSTALL_PATH):
	@$(YQ_INSTALL_COMMAND)

XMLLINT_PATH=$(shell which xmllint || { echo "Use operating system to install XMLLINT_INSTALL_COMMAND"; exit 1; })

$(XMLLINT_PATH):
	@$(XMLLINT_INSTALL_COMMAND)

OSCAL_CORE_DIR:=oscal/build

NPM_PKGS_DIR:=node_modules

$(NPM_PKGS_DIR):
	$(MAKE) -C $(OSCAL_CORE_DIR) dependencies

OSCAL_CLI_VERSION=`curl -s https://api.github.com/repos/usnistgov/oscal-cli/releases/latest | jq -r '.name[1:]'`
OSCAL_CLI_BIN:=oscal-cli
OSCAL_CLI_INSTALL_URL:=https://repo1.maven.org/maven2/gov/nist/secauto/oscal/tools/oscal-cli/cli-core/$(OSCAL_CLI_VERSION)/cli-core-$(OSCAL_CLI_VERSION)-oscal-cli.zip
OSCAL_CLI_INSTALL_PATH := $(shell which oscal-cli 2>/dev/null)
ifeq ($(OSCAL_CLI_INSTALL_PATH),)
OSCAL_CLI_INSTALL_PATH := ./oscal-cli/
$(OSCAL_CLI_INSTALL_PATH):	
	@echo "Downloading OSCAL CLI version $(OSCAL_CLI_VERSION)..."; \
	mkdir -p $(OSCAL_CLI_INSTALL_PATH); \
	curl $(CURL_INSTALL_OPTS) -o $(OSCAL_CLI_INSTALL_PATH)/oscal-cli.zip $(OSCAL_CLI_INSTALL_URL); \
	unzip -o $(OSCAL_CLI_INSTALL_PATH)/oscal-cli.zip -d $(OSCAL_CLI_INSTALL_PATH); \
	chmod +x $(OSCAL_CLI_INSTALL_PATH)/bin/$(OSCAL_CLI_BIN)
else
OSCAL_CLI_INSTALL_PATH := $(shell dirname $$(dirname $$(which oscal-cli)))
endif


.PHONY: dependencies
dependencies: $(JQ_PATH) $(XMLLINT_PATH) $(YQ_PATH) $(NPM_PKGS_DIR) $(OSCAL_CLI_INSTALL_PATH) ## Install needed jq and yq binaries, and download needed downstream dependencies

# By default we install xmllint with operating system package manager, so
# to be sensible, we will not uninstall or delete it even with the package
# manager and reduce the amount of friction.
.PHONY: clean-dependencies
clean-dependencies: ## Clean binary dependencies for repo
	rm -f $(JQ_INSTALL_PATH) $(YQ_INSTALL_PATH)

#
# OSCAL Core
#

.PHONY: build-core-artifacts
build-core-artifacts: ## Build core OSCAL artifacts to convert content examples
	$(MAKE) -C $(OSCAL_CORE_DIR) artifacts

.PHONY: clean-core-artifacts
clean-core-artifacts: ## Clean core OSCAL artifacts to convert content examples
	@echo Cleaning OSCAL core artifacts
	$(MAKE) -C $(OSCAL_CORE_DIR) clean

# The directory all content is sourced from
SRC_DIR:=../src
# The directory all content is written to (hint: override this to ..?)
GEN_CONTENT_DIR:=generated

#
# Readmes
#

SRC_READMES:=$(shell find $(SRC_DIR) -iname 'README.md')
GEN_READMES:=$(patsubst $(SRC_DIR)/%,$(GEN_CONTENT_DIR)/%,$(SRC_READMES))

.PHONY: copy-readmes
copy-readmes: $(GEN_READMES) ## Copy README files to release location

# $(@D): The directory part of the file name of the target, with the
# trailing slash removed.
# https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html
$(GEN_CONTENT_DIR)/%.md: $(SRC_DIR)/%.md
	@mkdir -p $(@D)
	cp $(SRC_DIR)/$*.md $(GEN_CONTENT_DIR)/$*.md

.PHONY: clean-readmes
clean-readmes: ## Clean generated README files
	@echo Cleaning README content
	rm -f $(GEN_READMES)

#
# XML Content
#

# The source xml content to use for all generated files
SRC_FILES:=$(shell find $(SRC_DIR) -name '*.xml')
GEN_XML_COPIED:=$(patsubst $(SRC_DIR)/%,$(GEN_CONTENT_DIR)/%,$(SRC_FILES))
SRC_XML_PROFILES:=$(shell find $(SRC_DIR) -name '*profile.xml')
GEN_XML_RESOLVED_CATALOGS:=$(subst _profile.xml,-resolved-profile_catalog.xml,$(patsubst $(SRC_DIR)/%,$(GEN_CONTENT_DIR)/%,$(SRC_XML_PROFILES)))

# All XML content generated by this configuration
GEN_XML_FILES:=$(GEN_XML_COPIED) $(GEN_XML_RESOLVED_CATALOGS)

.PHONY: copy-xml-content
copy-xml-content: $(GEN_XML_COPIED) ## Copy OSCAL XML files to release location

$(GEN_CONTENT_DIR)/%.xml: $(SRC_DIR)/%.xml
	@mkdir -p $(@D)
	cp $(SRC_DIR)/$*.xml $(GEN_CONTENT_DIR)/$*.xml

.PHONY: resolve-xml-profiles
resolve-xml-profiles: $(GEN_XML_RESOLVED_CATALOGS) ## Resolve OSCAL XML profiles for custom catalogs

PROFILE_RESOLVER_RUNNER:=oscal/src/utils/resolver-pipeline/oscal-profile-resolve.sh
PROFILE_RESOLVER_ARGS:="uuid-method='random-xslt'"

# Do not save a backup of the in-place edited file
SED_FLAGS:=-i

ifeq ($(shell uname -s),Darwin)
	SED_FLAGS:=-i ''
endif

$(GEN_CONTENT_DIR)/%-resolved-profile_catalog.xml: $(SRC_DIR)/%_profile.xml $(GEN_XML_COPIED)
	@mkdir -p $(@D)
	$(PROFILE_RESOLVER_RUNNER) $(GEN_CONTENT_DIR)/$*_profile.xml $(GEN_CONTENT_DIR)/$*-resolved-profile_catalog.xml $(PROFILE_RESOLVER_ARGS)
	sed $(SED_FLAGS) -e 's|file:.*$(shell basename $*_profile.xml)|$(shell basename $*_profile.xml)|g' $(GEN_CONTENT_DIR)/$*-resolved-profile_catalog.xml

OSCAL_COMPLETE_XML_SCHEMA:=$(OSCAL_CORE_DIR)/generated/oscal_complete_schema.xsd

.PHONY: validate-xml-content
validate-xml-content: $(GEN_XML_FILES) ## Validate XML files
	$(MAKE) -C $(OSCAL_CORE_DIR) $(subst $(OSCAL_CORE_DIR)/,,$(OSCAL_COMPLETE_XML_SCHEMA))
	$(XMLLINT_PATH) --schema $(OSCAL_COMPLETE_XML_SCHEMA) --noout $(GEN_XML_FILES)


#
# Validate XML with oscal-cli
#
.PHONY: validate-xml-by-cli
validate-xml-by-cli: $(OSCAL_CLI_INSTALL_PATH) ## Validate XML files by directory using OSCAL CLI Tool
	@echo "Validating XML files by directory using OSCAL CLI Tool"
	@$(OSCAL_CLI_INSTALL_PATH)/bin/$(OSCAL_CLI_BIN) --version
	@echo "latest oscal-cli version is $(OSCAL_CLI_VERSION)"
	@echo "Validating OSCAL content with $(OSCAL_CLI_INSTALL_PATH)/bin/oscal-cli version $(OSCAL_CLI_VERSION)"
	@find $(SRC_DIR)/examples -mindepth 1 -maxdepth 1 -type d | while read example_dir; do \
		example_type=$$(basename "$$example_dir"); \
		echo "Processing example type: $$example_type"; \
		find "$$example_dir" -name '*.xml' | while read xml_file; do \
			echo "Validating $$xml_file with OSCAL CLI as $$example_type"; \
			$(OSCAL_CLI_INSTALL_PATH)/bin/oscal-cli "$$example_type" validate "$$xml_file"; \
		done \
	done

.PHONY: clean-xml-content
clean-xml-content: ## Clean generated XML content
	@echo Cleaning XML content
	rm -f $(GEN_XML_FILES)

#
# JSON Content
#

GEN_JSON_FILES:=$(subst xml,json,$(GEN_XML_FILES))
GEN_MIN_JSON_FILES:=$(subst .json,-min.json,$(GEN_JSON_FILES))

.PHONY: convert-min-json-content
convert-min-json-content: $(GEN_MIN_JSON_FILES) ## Convert examples from OSCAL XML to JSON

XSLT_RUNNER:=$(OSCAL_CORE_DIR)/xslt-runner.sh
XML_JSON_CONVERTER_XSLT:=$(OSCAL_CORE_DIR)/generated/oscal_complete_xml-to-json-converter.xsl

$(GEN_CONTENT_DIR)/%-min.json: $(GEN_XML_FILES)
	$(MAKE) -C $(OSCAL_CORE_DIR) $(subst $(OSCAL_CORE_DIR)/,,$(XML_JSON_CONVERTER_XSLT))
	@mkdir -p $(@D)
	$(XSLT_RUNNER) $(XML_JSON_CONVERTER_XSLT) $(GEN_CONTENT_DIR)/$(subst json,xml,$*).xml $(GEN_CONTENT_DIR)/$*-min.json

.PHONY: reformat-json-content
reformat-json-content: $(GEN_JSON_FILES) ## Format minified JSON to pretty-printed JSON

$(GEN_CONTENT_DIR)/%.json: $(GEN_CONTENT_DIR)/%-min.json $(YQ_PATH)
	$(JQ_PATH) . $(GEN_CONTENT_DIR)/$*-min.json > $(GEN_CONTENT_DIR)/$*.json

OSCAL_COMPLETE_JSON_SCHEMA:=$(OSCAL_CORE_DIR)/generated/oscal_complete_schema.json

.PHONY: validate-json-content
validate-json-content: $(GEN_JSON_FILES) $(NPM_PKGS_DIR) ## Validate JSON files
	$(MAKE) -C $(OSCAL_CORE_DIR) $(subst $(OSCAL_CORE_DIR)/,,$(OSCAL_COMPLETE_JSON_SCHEMA))
	npx --prefix $(OSCAL_CORE_DIR) ajv validate -s $(OSCAL_COMPLETE_JSON_SCHEMA) -c ajv-formats $(foreach file,$(GEN_JSON_FILES),-d $(file))

.PHONY: clean-json-content
clean-json-content: ## Clean generated JSON content
	@echo Cleaning JSON content
	rm -f $(GEN_JSON_FILES)
	rm -f $(GEN_MIN_JSON_FILES)

#
# YAML
#

GEN_YAML_FILES:=$(subst xml,yaml,$(GEN_XML_FILES))

.PHONY: convert-yaml-content
convert-yaml-content: $(GEN_YAML_FILES) ## Convert examples from OSCAL JSON to YAML

$(GEN_CONTENT_DIR)/%.yaml: $(GEN_MIN_JSON_FILES) $(GEN_JSON_FILES) $(YQ_PATH)
	@mkdir -p $(@D)
	cat $(GEN_CONTENT_DIR)/$(subst yaml,json,$*).json | $(YQ_PATH) e -P - > $(GEN_CONTENT_DIR)/$(subst json,yaml,$*).yaml

.PHONY: validate-yaml-content
validate-yaml-content: $(GEN_YAML_FILES) $(NPM_PKGS_DIR) ## Validate YAML files
	$(MAKE) -C $(OSCAL_CORE_DIR) $(subst $(OSCAL_CORE_DIR)/,,$(OSCAL_COMPLETE_JSON_SCHEMA))
	npx --prefix $(OSCAL_CORE_DIR) ajv validate -s $(OSCAL_COMPLETE_JSON_SCHEMA) -c ajv-formats $(foreach file,$(GEN_YAML_FILES),-d $(file))

.PHONY: clean-yaml-content
clean-yaml-content: ## Clean generated YAML content
	@echo Cleaning YAML content
	rm -f $(GEN_YAML_FILES)
