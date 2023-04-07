# 0x0F. Load balancer
An introductory project on:

- Load balancing algorithm
- How to configure a load balancer

## Requirements
- Files are to be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- Bash script must pass `Shellcheck` (version 0.3.7) without any error

## File Descriptions
### Mandatory
[0-custom_http_response_header](./0-custom_http_response_header) - Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
- The name of the custom HTTP header must be `X-Served-By`
- The value of the custom HTTP header must be the hostname of the server Nginx is running on
```
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
```

[1-install_load_balancer](./1-install_load_balancer) - Install and configure HAproxy on your `lb-01` server
- Configure HAproxy so that it send traffic to web-01 and web-02
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`
- Configures a new Ubuntu machine to respect above requirements
```
sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes

sylvain@ubuntu$
```

[2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp) - using puppet, automate the task of creating a custom HTTP header response
- The name of the custom HTTP header must be `X-Served-By`
- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Configures a new Ubuntu machine to respect above requirements
