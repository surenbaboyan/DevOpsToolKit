## Install Nginx Exporter
- This exporter consists of two parts: Nginx Exporter and Nginxlog Exporter.
- For installing the Nginx Exporter/Nginxlog Exporter, first set the variables in the `common_settings/vars` Nginx Exporter section.
- Run the following command to install Nginx Exporter/Nginxlog Exporter for the first time:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="install_nginx_exporter,install_nginxlog_exporter"
  ```
- Answer the questions:
  - Type all names or groups of servers to install Nginx Exporter/Nginxlog Exporter. (The server and group names should be separated by commas)
  - When Nginx Exporter is proposed during the installation, type "yes".
- `Note`: To install both together, run:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="install,configure"
  ```
## Update Nginx Exporter/Nginxlog Exporter
- For updating the Nginx Exporter/Nginxlog Exporter, first set the new version for the `NGINX_EXPORTER_VERSION/NGINXLOG_EXPORTER_VERSION` variable in the common_settings/vars` Nginx Exporter section.
- Run the following command to update Nginx Exporter/Nginxlog Exporter:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="update_nginx_exporter,update_nginxlog_exporter"
  ```
- Answer the questions:
  - Type all names or groups of servers to update Nginx Exporter/Nginxlog Exporter. (The server and group names should be separated by commas)
  - When Nginx Exporter is proposed during the installation, type "yes".

- To update the Nginxlog Exporter configuration file, update the Nginxlog Exporter variables in the `common_settings/vars` Nginx Exporter section.
- Run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="configure"
  ```
- Answer the questions:
  - Type all names or groups of servers to update Nginxlog Exporter configuration. (The server and group names should be separated by commas)
  - When Nginx Exporter is proposed during the installation, type "yes".
## Uninstall Nginx Exporter/Nginxlog Exporter 
- For uninstalling Nginx Exporter/Nginxlog Exporter, run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="remove_nginx_exporter,remove_nginxlog_exporter"
  ```
- Answer the questions:
  - Type all names or groups of servers to remove Nginx Exporter/Nginxlog Exporter. (The server and group names should be separated by commas)
  - When Nginx Exporter is proposed during the installation, type "yes".