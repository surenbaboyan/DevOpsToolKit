FROM ubuntu:24.04

ENV DEBIAN_FRONTEND noninteractive
ARG PHP_VERSION

RUN apt update  \
    && apt install -y --no-install-recommends \
       apt-utils \
       openssl \
       net-tools \
       curl \
       iputils-ping \
       nano \
       ssh \
       git \
       zip \
       unzip \
       software-properties-common \
    && LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y \
    && apt-get update && apt-get install -yq --no-install-recommends \
       php${PHP_VERSION} \
       php${PHP_VERSION}-curl \
       php${PHP_VERSION}-fpm \
       php${PHP_VERSION}-bcmath \
       php${PHP_VERSION}-dom \
       php${PHP_VERSION}-gd \
       php${PHP_VERSION}-mysql \
       php${PHP_VERSION}-mbstring \
       php${PHP_VERSION}-mongodb \
       php${PHP_VERSION}-redis \
       php${PHP_VERSION}-soap \
       php${PHP_VERSION}-ssh2 \
       php${PHP_VERSION}-xdebug \
    && apt-get autoremove --purge -y \
       software-properties-common \
       gnupg2 \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* \
    && sed -i  \
       -e "s/;daemonize\s*=\s*yes/daemonize = no/g"  \
       /etc/php/${PHP_VERSION}/fpm/php-fpm.conf \
    && sed -i \
       -e "/^listen =.*/a listen = 0.0.0.0:9000" \
       /etc/php/${PHP_VERSION}/fpm/pool.d/www.conf \
    && /bin/echo -e "#!/bin/sh\nexec '/usr/sbin/php-fpm${PHP_VERSION}'" > /php-fpm \
        && chmod +x /php-fpm

#Install composer
COPY --from=composer /usr/bin/composer /usr/bin/composer

#RUN mkdir /run/php
RUN mkdir /var/www

EXPOSE 9000

CMD ["/php-fpm"]