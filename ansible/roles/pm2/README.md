- Find the "**PM2 SERVICE ROLE**" and set values for the variables in the **common_settings**--->**vars**--->**main.yml** file.
- Run the **play_apps.yml** Ansible playbook file using the command:
  - **ansible-playbook play_apps.yml --tags=select_tag**
  - To install PM2, use the **install** tag.
  - To delete PM2, use the **remove** tag.
- When PM2 is proposed during the installation, type "yes".