#!/bin/bash

source common.env

set -ex

# To run services as app user: Store UID/GID and use it in docker-compose.yml:
USERMAP_UID="$(id -u)"
export USERMAP_UID

USERMAP_GID="$(id -g)"
export USERMAP_GID

# Compose v2 is always accessible as docker compose!
# But Debian bullseye contains v1
exec docker-compose "$@"
