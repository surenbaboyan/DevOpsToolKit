ARG NODE_VERSION

FROM itechcastle/node:${NODE_VERSION}

RUN apt-get update \
    && apt-get update  \
    && apt install supervisor -y  \
    && npm install -g laravel-echo-server  \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/www/g/current

WORKDIR /var/www/g/current/echo-server

CMD ["/usr/bin/supervisord"]