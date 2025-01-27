#!/bin/sh

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# exits if any of your variables is not set
set -o nounset

docker compose -f docker-compose/docker-compose.base.yml \
               -f docker-compose/docker-compose.dev.yml \
               --env-file envs/.env.dev up -d