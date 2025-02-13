### Create base php image
- docker build -t php:{{PHP_VERSION}} --build-arg="PHP_VERSION={{PHP_VERSION}}" .

### Create base node image
- docker build -t node:{{NODE_VERSION}} --build-arg="NODE_VERSION={{vNODE_VERSION}}" --build-arg="NVM_VERSION={{vNVM_VERSION}}" .

### Create base mariadb image
- docker build -t mariadb:{{MARIADB_VERSION}} --build-arg="MARIADB_VERSION={{MARIADB_VERSION}}" .

### Push php base image to DockerHub Repository
- docker tag php:{{TAG_PHP_VERSION}} itechcastle/php:{{PHP_VERSION}}
- docker push itechcastle/php:{{PHP_VERSION}}

### Push node base image to DockerHub Repository
- docker tag node:{{TAG_NODE_VERSION}} itechcastle/node:{{NODE_VERSION}}
- docker push itechcastle/node:{{NODE_VERSION}}

### Push mariadb base image to DockerHub Repository
- docker tag mariadb:{{TAG_MARIADB_VERSION}} itechcastle/mariadb:{{MARIADB_VERSION}}
- docker push itechcastle/mariadb:{{MARIADB_VERSION}}

### Create php image for project 
- cd ```PHP/{{PROJECT_NAME}}``` directory and run commands
- ```docker build -t {{PROJECT_NAME}}-php -f {{DOCKERFILE_NAME}} --build-arg="PHP_VERSION={{PHP_VERSION}}" .```
- ```docker tag {{PROJECT_NAME}}-php itechcastle/{{PROJECT_NAME}}-php```
- ```docker push itechcastle/{{PROJECT_NAME}}-php```

### Create node image for project
- cd ```NODE/{{PROJECT_NAME}}``` directory and run commands
- ```docker build -t {{PROJECT_NAME}}-node -f {{DOCKERFILE_NAME}} --build-arg="NODE_VERSION={{NODE_VERSION}}" .```
- ```docker tag {{PROJECT_NAME}}-node itechcastle/{{PROJECT_NAME}}-node```
- ```docker push itechcastle/{{PROJECT_NAME}}-node```

### Create mariadb image for project using official mariadb image
- cd ```mariadb/{{PROJECT_NAME}}``` directory and run commands
- ```docker build -t {{PROJECT_NAME}}-mariadb -f {{DOCKERFILE_NAME}} --build-arg="MARIADB_VERSION={{MARIADB_VERSION}}" .```
- ```docker tag {{PROJECT_NAME}}-mariadb itechcastle/{{PROJECT_NAME}}-mariadb```
- ```docker push itechcastle/{{PROJECT_NAME}}-mariadb```