## Summary
This README provides detailed steps for:
  - Installing and configuring Prometheus.
  - Updating the configuration and alert rules.
  - Adding new jobs, targets, and instances.
  - Removing Prometheus.

## Prerequisites
- Ensure Prometheus server details in hosts file:
  - Add Prometheus server values in the hosts file under the appropriate group.

- Set Values in `common_settings/vars/main.yml`:
  - Find the PROMETHEUS SERVICE ROLE and set the necessary variables.

## Installation and Configuration
To install and configure Prometheus, use the following command:
```sh
  ansible-playbook play_monitoring_systems.yml --tags=install,configure
```
- During installation, find the name of the Prometheus server from the hosts file and confirm when prompted.

## Updating Prometheus Configuration
- Update Prometheus Configuration File:
  - Make changes to templates/prometheus.yml.j2.
  - Run the following command to update the configuration:  
  ```sh
    ansible-playbook play_monitoring_systems.yml --tags="conf_file"
  ```
- Update Prometheus Alert Rules:
  - Modify alert rules in `common_settings/vars/main.yml` following the provided template:
  - To update Prometheus alert rules, make the appropriate changes to the `common_settings/vars/main.yml` file (find an example in previous alert rules).
Description:

    ```yaml
    - alert: "Name of alert"
      expr: "Condition - Use exporter metric names"
      for: "The time - How many minutes or seconds later should this alert be sent after it becomes relevant"
      labels:
        severity: "Alert level, critical or warning"
        alerttype: "Service name - for sending to the exact slack channel. Find alertmanager configuration file"
      annotations: 
        instance: '{% raw %}{{ $labels.instance }}{% endraw %}' # Leave unchanged
        summary: "### Add message title for Slack###" # Use {% raw %}...{% endraw %} for variables
        description: "### Add alert description ###" # Use {% raw %}...{% endraw %} for variables  
    ```

  - Run the following command to update the alert rules:
    ```sh
    ansible-playbook play_monitoring_systems.yml --tags="rule_file"
    ```
  - Find the name of the Prometheus server from hosts file.
When Prometheus is proposed during the installation, type "yes".

## Adding Jobs and Targets
- Add a new job (exporter):
  - In the PROMETHEUS SCOPE CONFIG section of `common_settings/vars/main.yml`, add the new job.
  - In the PROMETHEUS TARGETS section, add the corresponding targets.
  - Update the hosts file if a new instance is added.
  - Run the following command:
  ```sh
    ansible-playbook play_monitoring_systems.yml --tags="conf_file,targets"
     ```
- Add a new instance:
  - In the targets section of `common_settings/vars/main.yml`, add parameters for the new instance and update the hosts file.
  - Run the following command:
    ```sh
    ansible-playbook play_monitoring_systems.yml --tags="targets"
    ```
  
  ## Removing Prometheus
  - To remove Prometheus, use the remove tag:
    ```sh
    ansible-playbook play_monitoring_systems.yml --tags="remove"
    ```
  - When Prometheus is proposed during the installation, type "yes".