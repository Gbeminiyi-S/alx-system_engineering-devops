# 0x0C. Web server
An introductory project on:

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

## Requirements
- Files are to be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- Bash script files must be executable
- Bash script must pass `Shellcheck` (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- Can’t use systemctl for restarting a process

## File Descriptions
### Mandatory
[0-transfer_file](./0-transfer_file) - a Bash script that transfers a file from our client to a server
- Requirements:
  - Accepts 4 parameters
    - The path to the file to be transferred
    - The IP of the server we want to transfer the file to
    - The username `scp` connects with
    - The path to the SSH private key that scp uses
- Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- `scp` must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using `scp`
```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```
