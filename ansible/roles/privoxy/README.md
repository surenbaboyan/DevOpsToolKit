- Find the "**PRIVOXY SERVICE ROLE**" and set values for the variables in **common_settings**--->**vars**--->**main.yml** file.  
- Run the **play_apps.yml** ansible playbook file using the command:
   - **ansible-playbook play_apps.yml --tags=select_tags_separated_by_comma**
   - To install Privoxy, use the **install,configure** tags.
   - To update the config file, use the **configure** tag. 
   - To delete Privoxy, use the **remove** tag.
- When prompted during the installation of privoxy, type "yes".
- Verify the installation and configuration by checking Privoxy's status.