#!/bin/bash

set -ex

python dev-scripts/local-test.py

cd local_test/home_yunohost_app

exec make "$@"
