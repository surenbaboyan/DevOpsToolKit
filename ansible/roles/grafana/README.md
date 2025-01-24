## Install Grafana

- For installing Grafana, first set the variables in the `common_settings/vars` Grafana section.
- In the hosts file, add the Grafana server host if there are none.
- Run the following command to install and configure Grafana for the first time:
```sh
    ansible-playbook play_monitoring_systems.yml --tags="install,configure"
```
- Answer the questions:
  - Type the Grafana server name. (You can find it in the hosts file)
  - When Grafana is proposed during the installation, type "yes".
## Update Grafana
- For updating Grafana, first set the new version for the GRAFANA_VERSION variable in the `common_settings/vars` Grafana section.
- Run the following command to update Grafana:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="update"
  ```
- Answer the questions:
  - Type the Grafana server name. (You can find it in the hosts file)
  - When Grafana is proposed during the installation, type "yes".
## Update configuration file
- To update the Grafana configuration file, make your changes in the templates/grafana.ini.yml.j2 file and/or in the `common_settings/vars` Grafana section.
- Run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="conf_file"
  ```
- Answer the questions:
  - Type the Grafana server name. (You can find it in the hosts file)
  - When Grafana is proposed during the installation, type "yes".
## Update Grafana's current data source or add a new one
- To update Grafana's current data source or add a new one, make the appropriate changes or add new data source settings in the `common_settings/vars` `GRAFANA_DATASOURCES` section.
- Run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="datasources"
  ```
- Answer the questions:
  - Type the Grafana server name. (You can find it in the hosts file)
  - When Grafana is proposed during the installation, type "yes".
## Add Dashboard in Grafana
- There are two options for adding a dashboard in Grafana: remote and local.
  - For remote addition, from the official Grafana site, find the appropriate dashboard and add its settings in the `common_settings/vars` `GRAFANA_DASHBOARDS` section.
  - Run the following command:
    ```sh
    ansible-playbook play_monitoring_systems.yml --tags="dashboard_from_remote_src"
    ```
  - Answer the questions:
    - Type the Grafana server name. (You can find it in the hosts file)
    - When Grafana is proposed during the installation, type "yes".  
  - For local addition, create your own dashboard in Grafana, then download this dashboard's JSON file into the `files/dashboards` directory.
  - Run the following command:
    ```sh
      ansible-playbook play_monitoring_systems.yml --tags="dashboard_from_local_src"
    ```
  - Answer the questions:
    - Type the Grafana server name. (You can find it in the hosts file)
    - When Grafana is proposed during the installation, type "yes".

- To add both remote and local dashboards together, run the following command:
  ```sh
    ansible-playbook play_monitoring_systems.yml --tags="dashboards"
    ```
- Answer the questions:
  - Type the Grafana server name. (You can find it in the hosts file)
  - When Grafana is proposed during the installation, type "yes".

## Uninstall Grafana
- For uninstalling Grafana, run the following command:
  ```sh
    ansible-playbook play_monitoring_systems.yml --tags="remove"
  ```
- Answer the questions:
  - Type the Grafana server name. (You can find it in the hosts file)
  - When Grafana is proposed during the installation, type "yes".