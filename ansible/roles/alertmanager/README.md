# Alertmanager

- For installing Alertmanager, first set variables in the `common_settings/vars` alertmanager section.
- In the hosts file, add the Alertmanager server host if there are none.
- Run the following command to install and configure Alertmanager for the first time:

```sh
ansible-playbook play_monitoring_systems.yml --tags="install,configure"
```
- Answer the questions:
  - Type the Alertmanager server name. (You can find it in the hosts file)
  - When Alertmanager is proposed during the installation, type "yes".
## Update the version of Alertmanager
- For updating Alertmanager, first set the new version for the ALERTMANAGER_VERSION variable in the `common_settings/vars` alertmanager section.
- Run the following command to update Alertmanager:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="update"
  ```
- Answer the questions:
  - Type the Alertmanager server name. (You can find it in the hosts file)
  - When Alertmanager is proposed during the installation, type "yes".
## Update the configuration file of Alertmanager
- To update the Alertmanager configuration file, make your changes in the templates/alertmanager.yml.j2 file.
- If you want to add a new service and must send it to a new Slack channel, you will add a new route and receiver:
  - In the routes section, add a new receiver:
    ```yaml
    - receiver: '' # Receiver name 
      group_by: [...] # List of labels to group by
      group_wait: 20s # Wait time before grouping alerts
      group_interval: 40s # Interval to wait before sending a new notification for an instance of an alert group
      repeat_interval: 4h # Interval to repeat sending alerts that are still active
      match:
        alerttype: ... # Define your specific alert matching criteria here. The same value in prometheus rule files <<alerttype>>
    ```
  - In the receivers section, add a new receiver:
    ```yaml
    - name: '' # Notification receiver name
      slack_configs:
      - channel: '' # Name of Slack channel
        api_url: '' # API URL for your Slack channel webhook
        send_resolved: true # Determines whether to send notifications when alerts are resolved (true to send notifications, false to omit).
        icon_url: https://avatars3.githubusercontent.com/u/3380462 # URL for the icon (optional)
        title: '{% raw %}{{ template "slack.title" . }}{% endraw %}' # Template for the title of the Slack message. It uses the slack.title template to format the title based on alert data.
        color: '{{ template "slack.color" . }}' # Template for the color of the Slack message. It uses the slack.color template to define the color based on alert severity.
        fallback: '{{ template "slack.desktop.notification" . }}' # Fallback notification (using template)
        text: '{{ template "slack.text" . }}{% endraw %}' # Template for the main content of the Slack message. It uses the slack.text template to format the message based on alert details.
    ```
  - Run the following command:
    ```sh
    ansible-playbook play_monitoring_systems.yml --tags="conf_file"
    ```
- Answer the questions:
  - Type the Alertmanager server name. (You can find it in the hosts file)
  - When Alertmanager is proposed during the installation, type "yes".

## Update the template file of Alertmanager
- To update the Alertmanager template file, make your changes in the files/slack-templates.tmpl file.
- Run the following command:
  ```sh
  ansible-playbook play_monitoring_systems.yml --tags="tmpl_file"
  ```
- Answer the questions:
  - Type the Alertmanager server name. (You can find it in the hosts file)
  - When Alertmanager is proposed during the installation, type "yes".

## Uninstall Alertmanager
For uninstalling Alertmanager, run the following command:
```sh
ansible-playbook play_monitoring_systems.yml --tags="remove"
```
- Answer the questions:
  - Type the Alertmanager server name. (You can find it in the hosts file)
  - When Alertmanager is proposed during the uninstallation, type "yes".