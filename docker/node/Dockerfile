FROM ubuntu:24.04

ARG NODE_VERSION
ARG NVM_VERSION

RUN apt-get update  \
    && apt-get install -y \
       net-tools \
       curl \
       iputils-ping \
       git \
       netcat-traditional \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/*

# nvm environment variables
ENV NVM_DIR /usr/local/nvm
RUN mkdir $NVM_DIR

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/${NVM_VERSION}/install.sh | bash

ENV NODE_PATH $NVM_DIR/${NODE_VERSION}/lib/node_modules
ENV PATH $NVM_DIR/versions/node/${NODE_VERSION}/bin:$PATH

RUN echo "source $NVM_DIR/nvm.sh && \
    nvm install ${NODE_VERSION} && \
    nvm alias default ${NODE_VERSION} && \
    nvm use default" | bash