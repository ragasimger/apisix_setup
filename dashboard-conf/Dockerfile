FROM apache/apisix-dashboard:3.0.1-alpine

USER root

# envsubst is available with gettext
RUN apk add --no-cache gettext

COPY config.yaml.template /usr/local/apisix-dashboard/conf/conf.yaml.template
COPY entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]