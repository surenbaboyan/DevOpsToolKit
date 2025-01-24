## Install  Elasticsearch Exporter
- For installing the Elasticsearch Exporter, first set the variables in the `common_settings/vars` Elasticsearch Exporter section.
- Run the following command to install and Elasticsearch Exporter for the first time:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="install"
  ```
- Answer the questions:
  - Type all names or groups of servers to install Elasticsearch Exporter. (The server and group names should be separated by commas)
  - When Elasticsearch Exporter is proposed during the installation, type "yes".
## Update Elasticsearch Exporter
- For updating the Elasticsearch Exporter, first set the new version for the ELASTICSEARCH_EXPORTER_VERSION variable in the `common_settings/vars` Elasticsearch Exporter section.
- Run the following command to update Elasticsearch Exporter:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="update"
  ```
- Answer the questions:
  - Type all names or groups of servers to update Elasticsearch Exporter. (The server and group names should be separated by commas)
  - When Elasticsearch Exporter is proposed during the installation, type "yes".
## Update Elasticsearch Exporter service file
- For updating the Elasticsearch Exporter service file, first set the variables in the `common_settings/vars` Elasticsearch Exporter section. Then make your changes on elasticsearch_exporter.service.j2 file. 
- Run the following command to update Elasticsearch Exporter:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="service_file"
  ```
- Answer the questions:
  - Type all names or groups of servers to update Elasticsearch Exporter. (The server and group names should be separated by commas)
  - When Elasticsearch Exporter is proposed during the installation, type "yes".
## Uninstall PHP-FPM Exporter
- For uninstalling Elasticsearch Exporter, run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="remove"
  ```
- Answer the questions:
  - Type all names or groups of servers to remove PHP-FPM Exporter. (The server and group names should be separated by commas)
  - When PHP-FPM Exporter is proposed during the installation, type "yes".
