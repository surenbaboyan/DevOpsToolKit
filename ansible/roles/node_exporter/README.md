## Install Node Exporter
- For installing the Node Exporter, first set the variables in the `common_settings/vars` Node Exporter section.
- Run the following command to install and configure Node Exporter for the first time:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="install,configure"
  ```
- Answer the questions:
  - Type all names or groups of servers to install Node Exporter. (The server and group names should be separated by commas)
  - When Node Exporter is proposed during the installation, type "yes".
## Update Node Exporter
- For updating the Node Exporter, first set the new version for the `NODE_EXPORTER_VERSION` variable in the `common_settings/vars` Node Exporter section.
- Run the following command to update Node Exporter:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="update"
  ```
- Answer the questions:
  - Type all names or groups of servers to update Node Exporter. (The server and group names should be separated by commas)
  - When Node Exporter is proposed during the installation, type "yes".
## Add or remove new collector
- To add a new collector or remove it, in the `common_settings/vars` node_exporter_enabled_collectors section, add a new service or remove the current one.
- Run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="service_file"
  ```
- Answer the questions:
  - Type all names or groups of servers to update or remove collectors. (The server and group names should be separated by commas)
  - When Node Exporter is proposed during the installation, type "yes".
## Uninstall Node Exporter 
- For uninstalling Node Exporter, run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="remove"
  ```
- Answer the questions:
  - Type all names or groups of servers to remove Node Exporter. (The server and group names should be separated by commas)
  - When Node Exporter is proposed during the installation, type "yes".