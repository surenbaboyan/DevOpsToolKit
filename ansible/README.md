### Prerequisites:
 - Required software (Ansible version must be at least **2.13.12**, Python).
 - Access credentials (SSH keys, passwords).
 - Target hosts or inventory setup.
 - Before starting the dante role, make sure that the **passlib** library is installed 
   - **pip install passlib**
### Common Settings
- The **main.yml** file (located in **roles**--->**common_settings**--->**vars**) contains all the variables for the roles.
### Hosts
- The Ansible hosts file contains a list of all the hosts that Ansible can manage.
- Hosts can be grouped together into logical groups, which makes it easier to manage them.
- For example, you might have a group for all of your production servers, and another group for all of your development servers.
- Add the following information in the hosts file:
   - **ansible_host**=IP_address
   - **ansible_port**=port_of_server
   - **ansible_user**=username
   - **private_key_file**=path_to_ssh_private_key
### Run Ansible Playbook
- Depending on your requirements, replace TAG_NAME with install, update, or another appropriate tag. 
- Only with play_apps can you add the run_pre_task tag for additional tasks such as application installation.
  - **ansible-playbook {{ansible-playbook.yml}}** file --tags="TAG_NAME"
### Create new role
 - cd to roles folder and run
 - **ansible-galaxy init {{role name}}**