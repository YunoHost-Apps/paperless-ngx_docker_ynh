SHELL := /bin/bash

help: ## List all commands
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9 -_]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

###################################################################################################

build: ## Update/Build docker services
	./compose.sh pull
	./compose.sh build --pull

up: build ## Start docker containers
	./compose.sh up -d
	$(MAKE) logs

down: ## Stop all containers
	./compose.sh down

restart: down up ## Restart by call "down" and "up"

###################################################################################################

ps: ## List containers
	./compose.sh ps

logs: ## Display and follow docker logs
	./compose.sh logs --tail=500 --follow

###################################################################################################

shell-app: ## go into a interactive bash shell in App container
	./compose.sh exec app /bin/bash

run-shell-app: ## Build and start the App container and go into shell
	./compose.sh build --pull app
	./compose.sh run --entrypoint '/bin/bash' app

shell-postgres: ## go into a interactive bash shell in App container
	./compose.sh exec postgres /bin/bash

###################################################################################################

systemd-status:  ## Status of the app SystemD services
	systemctl status __APP__

systemd-restart:  ## Status of the app SystemD services
	systemctl restart __APP__

###################################################################################################

.PHONY: help build up down restart ps logs shell-app run-shell-app shell-postgres systemd-status systemd-restart

