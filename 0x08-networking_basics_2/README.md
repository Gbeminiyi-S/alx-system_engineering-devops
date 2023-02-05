# 0x08. Networking basics #1
An introductory project on:
- What is localhost
- What is 0.0.0.0
- What is the hosts file
- Netcat examples

# Requirements
- files are interpreted on Ubuntu 20.04 LTS
- Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error
- The first line of all the Bash scripts should be exactly `#!/usr/bin/env bash`

# File Descriptions
## Mandatory
[0-change_your_home_IP](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x08-networking_basics_2/0-change_your_home_IP) - a Bash script that configures an Ubuntu server with the below requirements:
- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`

[1-show_attached_IPs](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x08-networking_basics_2/1-show_attached_IPs) - a Bash script that displays all active IPv4 IPs on the machine it’s executed on

## Advanced
[100-port_listening_on_localhost](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x08-networking_basics_2/100-port_listening_on_localhost) - a Bash script that listens on port `98` on `localhost`
