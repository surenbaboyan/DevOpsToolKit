## Install  PHP-FPM Exporter
- For installing the PHP-FPM Exporter, first set the variables in the `common_settings/vars` PHP-FPM Exporter section.
- Run the following command to install and configure PHP-FPM Exporter for the first time:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="install,configure"
  ```
- Answer the questions:
  - Type all names or groups of servers to install PHP-FPM Exporter. (The server and group names should be separated by commas)
  - When PHP-FPM Exporter is proposed during the installation, type "yes".
## Update PHP-FPM Exporter
- For updating the PHP-FPM Exporter, first set the new version for the PHP-FPM_EXPORTER_VERSION variable in the `common_settings/vars` PHP-FPM Exporter section.
- Run the following command to update PHP-FPM Exporter:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="update"
  ```
- Answer the questions:
  - Type all names or groups of servers to update PHP-FPM Exporter. (The server and group names should be separated by commas)
  - When PHP-FPM Exporter is proposed during the installation, type "yes".
## Uninstall PHP-FPM Exporter
- For uninstalling PHP-FPM Exporter, run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="remove"
  ```
- Answer the questions:
  - Type all names or groups of servers to remove PHP-FPM Exporter. (The server and group names should be separated by commas)
  - When PHP-FPM Exporter is proposed during the installation, type "yes".