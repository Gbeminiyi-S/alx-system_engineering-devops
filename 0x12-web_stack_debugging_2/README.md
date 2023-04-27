# 0x12. Web stack debugging #2
An introductory project on:
- web stack debugging

# Requirements
- Files are to be executed on Ubuntu 20.04 LTS - The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- Bash script must pass `Shellcheck` (version 0.3.7) without any error

# File Descriptions
## Mandatory
[0-iamsomeoneelse](./0-iamsomeoneelse) - runs the `whoami` command under the user passed as an argument
```
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```
[1-run_nginx_as_nginx](./1-run_nginx_as_nginx) - a Bash script that configures the container the docker container so that Nginx is running as the `nginx` user.

Requirements:

- `nginx` must be running as `nginx` user
- `nginx` must be listening on all active IPs on port `8080`
- Cannot use `apt-get remove`

After debugging:
```
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```
[100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less) - Using task [#1](./1-run_nginx_as_nginx) solution, make the fix short and sweet.

Requirements:

- Bash script must be 7 lines long or less
- There must be a new line at the end of the file
- Cannot use `;`
- Cannot use `&&`
- Cannot use `wget`
