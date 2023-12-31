SHELL := /bin/bash

help: ## List all commands
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9 -_]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

###################################################################################################

setup-venv:  ## install huey monitor package
	python3 -m venv .venv
	.venv/bin/pip install -U pip
	.venv/bin/pip install -U pip-tools

update: setup-venv ## Update the requirements with pip-compile
	.venv/bin/pip-compile --output-file=conf/requirements.txt --strip-extras requirements.in

###################################################################################################

list-ynh-add-config:  ## List "ynh_add_config" statements from all ./conf/* files
	python dev-scripts/list-ynh-add-config.py

local-test:  ## Created a "local test" file structure
	python dev-scripts/local-test.py

###################################################################################################

.PHONY: help setup-venv update

