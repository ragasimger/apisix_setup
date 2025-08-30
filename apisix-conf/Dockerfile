FROM apache/apisix:3.13.0-debian

USER root

RUN apt-get update && \
apt-get install -y gettext && \
rm -rf /var/lib/apt/lists/*

COPY config.yaml.template /usr/local/apisix/conf/config.yaml.template


COPY entrypoint_wrapper.sh /docker-entrypoint-custom.sh
RUN chmod +x /docker-entrypoint-custom.sh


# Do not use entrypoint.sh as there is collision or something and server did not start
# /docker-entrypoint.sh did not work either

# So going with entrypoint_wrapper and docker-entrypoint-custom.sh
ENTRYPOINT ["/docker-entrypoint-custom.sh"]
CMD ["docker-start"]