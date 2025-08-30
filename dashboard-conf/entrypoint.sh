#!/bin/sh
set -e

envsubst < /usr/local/apisix-dashboard/conf/conf.yaml.template > /usr/local/apisix-dashboard/conf/conf.yaml

exec /usr/local/apisix-dashboard/manager-api