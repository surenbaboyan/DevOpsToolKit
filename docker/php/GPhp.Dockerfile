ARG PHP_VERSION

FROM itechcastle/php:${PHP_VERSION}
ARG PHP_VERSION

RUN apt-get update && apt-get install --no-install-recommends -y \
    supervisor

RUN mkdir -p /var/www/g/current
WORKDIR /var/www/g/current

COPY conf.d/xdebug.ini /etc/php/${PHP_VERSION}/fpm/conf.d/20-xdebug.ini
COPY conf.d/php.ini /etc/php/${PHP_VERSION}/fpm/php.ini

CMD ["/usr/bin/supervisord"]