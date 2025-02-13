ARG NODE_VERSION

FROM itechcastle/node:${NODE_VERSION}

RUN apt-get update \
    && npm install -g pm2 cross-env \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/www/p/current

WORKDIR /var/www/p/current

COPY script.sh /

RUN chmod +x /script.sh

CMD ["bash", "-c", "/script.sh"]