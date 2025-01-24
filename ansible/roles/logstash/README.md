- In the hosts file under [logstash] group set the logstash server

### ATTENTION !!!
- If the logstash server and elk-master-init-node the same, set only logstash.
- If the logstash server and elk-master-init-node difference, set logstash and elk-master-init-node.

- Find the "**LOGSTASH SERVICE ROLE**" and set values for the variables in the **common_settings**--->**vars**--->**main.yml** file.
- Run the Ansible playbook file (play_apps.yml) using the command:
    - **ansible-playbook play_logging_systems.yml --tags=elect_tags_separated_by_comma**
    - To install Logstash, use the **install,configure** tags.
      - **configure** tag configures certificate, pipeline and starts the service
      - To update the pipeline file, use the **logstash_pipeline_config** tag.
- When logstash is proposed during the installation, type "yes".

# Logstash Installation and Configuration

### Hosts File Configuration
In the hosts file, under the **[logstash]** group, set the Logstash server.

### Attention
- If the Logstash server and elk-master-init-node are the same, set only logstash.
- If the Logstash server and elk-master-init-node are different, set both logstash and elk-master-init-node.

### Variables Configuration
Find the LOGSTASH SERVICE ROLE and set values for the variables in the **common_settings -> vars -> main.yml** file.

### Running the Ansible Playbook
- Run the Ansible playbook file (play_apps.yml) using the command:


- **ansible-playbook play_logging_systems.yml --tags=select_tags_separated_by_comma**
- To install Logstash, use the **install**, **configure** tags.
- The **configure** tag configures the certificate, pipeline, and starts the service.
- To update the pipeline file, use the logstash_pipeline_config tag.
When prompted for Logstash during the installation, type "**yes**".

