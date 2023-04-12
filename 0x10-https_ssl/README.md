# 0x10. HTTPS SSL
An introductory project on:
- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means

## Requirements
- The first line of Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts is a comment explaining what is the script doing

## File Descriptions
### Mandatory
[0-world_wide_web](./0-world_wide_web) - Configures domain zone so that the subdomain `www` points to the load-balancer `IP (lb-01)`
Requirements:
- Add the subdomain `www` to your domain, point it to your `lb-01 IP`
- Add the subdomain `lb-01` to your domain, point it to your `lb-01 IP`
- Add the subdomain `web-01` to your domain, point it to your `web-01 IP`
- Add the subdomain `web-02` to your domain, point it to your `web-02 IP`
- The Bash script must accept 2 arguments:
  - domain:
    - type: string
    - what: domain name to audit
    - mandatory: yes
  - subdomain:
    - type: string
    - what: specific subdomain to audit
    - mandatory: no
- Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
- When only the parameter `domain` is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order
- When passing `domain` and `subdomain` parameters, display information for the specified subdomain
- Must use:
    - `awk`
    - at least one Bash function
```
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```

[1-haproxy_ssl_termination](./1-haproxy_ssl_termination) - Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www.`
Requirements:
- HAproxy must be listening on port TCP 443
- HAproxy must be accepting SSL traffic
- HAproxy must serve encrypted traffic that will return the `/` of your web server
- When querying the root of your domain name, the page returned must contain `Holberton School`
- The file [1-haproxy_ssl_termination](./1-haproxy_ssl_termination) must be your HAproxy configuration file
```
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```
### Advanced
[100-redirect_http_to_https](./100-redirect_http_to_https) -  Configure HAproxy to automatically redirect HTTP traffic to HTTPS
Requirements:
- This should be transparent to the user
- HAproxy should return a `301`
- HAproxy should redirect HTTP traffic to HTTPS
- The file [100-redirect_http_to_https](./100-redirect_http_to_https) must be your HAproxy configuration file
```
sylvain@ubuntu$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$
```
