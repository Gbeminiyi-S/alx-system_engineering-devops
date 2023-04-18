# 0x0E. Web stack debugging #1
An introductory project on:
- web stack debugging
# Requirements
- Files are to be executed on Ubuntu 20.04 LTS - The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- Bash script must pass `Shellcheck` (version 0.3.7) without any error
- Not allowed to use `wget`

# File Descriptions
## Mandatory
[0-nginx_likes_port_80](./0-nginx_likes_port_80) - Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port `80`
- Requirements:
  - Nginx must be running, and listening on port `80` of all the server’s active IPv4 IPs
  - The Bash script configures a server to the above requirements
```
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
```

[1-debugging_made_short](./1-debugging_made_short) - Using what you did for task #0, make the fix short and sweet
- Requirements
   - Bash script must be 5 lines long or less
  - There must be a new line at the end of the file
  - Respect usual Bash script requirements
  - Cannot use `;`
  - Cannot use `&&`
  - Cannot use `wget`
  - Cannot execute your previous answer file (Do not include the name of the previous script in this one)
  - `service` (init) must say that `nginx` is not running ← for real
```
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
root@966c5664b21f:/# service nginx status
 * nginx is not running
root@966c5664b21f:/# 
```
