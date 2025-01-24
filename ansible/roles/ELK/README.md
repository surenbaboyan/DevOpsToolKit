## Elasticsearch and Kibana Installation and Configuration Role
This role is intended for installing and configuring Elasticsearch and Kibana. After installation, ensure that you save your passwords (both certificates and Elasticsearch). They will be needed for future installations of Logstash, Kibana, and when adding new nodes to the cluster.

**Note**: Leave the ELK groups in the hosts file unchanged. Instances need to be added to the appropriate groups.

- The elk-master-init-node group is the main master node where certificates are generated. This node initializes the Elasticsearch cluster for the first time and sets a password for the cluster.

### Variables Configuration
- Place all the variables in the common_settings/vars/main.yml file associated with ELK.
- Ensure that the roles are set in the hosts file for each node.
- Locate the ELK SERVICE ROLE and set values for the variables in the common_settings/vars/main.yml file.

### Running the Ansible Playbook
To install and configure Elasticsearch and Kibana, follow these steps:
- Run the Ansible playbook using the following command:
  ```sh
  ansible-playbook play_logging_systems.yml --tags="install,configure"
  ```
- Specify the ELK group.
- When prompted during the installation, type "yes".

**Note**: Install Elasticsearch and Kibana together.

### Adding a New Node to an Existing Cluster
#### To Install a New Node:
- Set the current Elasticsearch version in the common_settings/vars/main.yml file.
- Run the playbook with the install tag:
  ```sh
  ansible-playbook play_logging_systems.yml --tags="install"
  ```
- Specify the node instance.
- When prompted during the installation, type "yes".

#### To Configure a New Node:
- Run the playbook with the re_configure tag:
  ```sh
  ansible-playbook play_logging_systems.yml --tags="re_configure"
  ```
- Specify the node instance and elk-master-init-node.
- When prompted during the installation, type "yes".

#### Resetting Cluster Password
To reset the cluster's password, follow these steps:
- Run the playbook with the reset_password tag:
  ```sh
  ansible-playbook play_logging_systems.yml --tags="reset_password"
  ```
- Specify the elk-master-init-node group.
- When prompted during the process, type "yes".

#### Updating Node Roles
- In the hosts file, set the role variable for each node, e.g., roles="master,data,...".
- Run the playbook with the conf_file tag:
  ``` sh
  ansible-playbook play_logging_systems.yml --tags="conf_file"
  ```
- Specify the node instances.
- When prompted during the installation, type "yes".