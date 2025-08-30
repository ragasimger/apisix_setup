#!/bin/sh
set -e

envsubst < /usr/local/apisix/conf/config.yaml.template > /usr/local/apisix/conf/config.yaml

exec /docker-entrypoint.sh docker-start
# exec /docker-entrypoint.sh "$@"