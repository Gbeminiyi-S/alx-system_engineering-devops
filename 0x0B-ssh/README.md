# 0x0B. SSH
## Requirements
- All files will be interpreted on Ubuntu 20.04 LTS
- All Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing

## File Description
[0-use_a_private_key](./0-use_a_private_key) -  a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`
- Requirements:
  - Only use `ssh` single-character flags
  - Cannot use `-l`
  - Do not need to handle the case of a private key protected by a passphrase
```
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$ 
```

[1-create_ssh_key_pair](./1-create_ssh_key_pair) - a Bash script that creates an RSA key pair
- Requirements:
  - Name of the created private key must be `school`
  - Number of bits in the created key to be created 4096
  - The created key must be protected by the passphrase `betty`
```
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$ 
```

[2-ssh_config](./2-ssh_config) - Client configuration file to enable connectiont to a server without typing a password
- Requirements:
  - SSH client configuration must be configured to use the private key `~/.ssh/school`
  - SSH client configuration must be configured to refuse to authenticate using a password

```
vagrant@ubuntu-focal:~$ ssh -v ubuntu@34.202.157.83
OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug1: /etc/ssh/ssh_config line 55: Applying options for 34.202.157.83
debug1: Connecting to 34.202.157.83 [34.202.157.83] port 22.
debug1: Connection established.
debug1: identity file /home/vagrant/.ssh/id_rsa type 0
debug1: identity file /home/vagrant/.ssh/id_rsa-cert type -1
debug1: identity file /home/vagrant/.ssh/id_ecdsa type -1
debug1: identity file /home/vagrant/.ssh/id_ecdsa-cert type -1
debug1: identity file /home/vagrant/.ssh/id_ecdsa_sk type -1
debug1: identity file /home/vagrant/.ssh/id_ecdsa_sk-cert type -1
debug1: identity file /home/vagrant/.ssh/id_ed25519 type -1
debug1: identity file /home/vagrant/.ssh/id_ed25519-cert type -1
debug1: identity file /home/vagrant/.ssh/id_ed25519_sk type -1
debug1: identity file /home/vagrant/.ssh/id_ed25519_sk-cert type -1
debug1: identity file /home/vagrant/.ssh/id_xmss type -1
debug1: identity file /home/vagrant/.ssh/id_xmss-cert type -1
debug1: identity file /home/vagrant/.ssh/id_dsa type -1
debug1: identity file /home/vagrant/.ssh/id_dsa-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
debug1: Remote protocol version 2.0, remote software version OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
debug1: compat_banner: match: OpenSSH_8.2p1 Ubuntu-4ubuntu0.5 pat OpenSSH* compat 0x04000000
debug1: Authenticating to 34.202.157.83:22 as 'ubuntu'
debug1: load_hostkeys: fopen /home/vagrant/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ssh-ed25519
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: SSH2_MSG_KEX_ECDH_REPLY received
debug1: Server host key: ssh-ed25519 SHA256:/QANg0QDP5U0OifXCcZWZMAreZwpUbZZ6ePoWCQitE0
debug1: load_hostkeys: fopen /home/vagrant/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: Host '34.202.157.83' is known and matches the ED25519 host key.
debug1: Found key in /home/vagrant/.ssh/known_hosts:2
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: Will attempt key: /home/vagrant/.ssh/id_rsa RSA SHA256:EfCrAT6YbFvUsMPpcpjksdlbK9FkTTHxop/QpOJWIhA
debug1: Will attempt key: /home/vagrant/.ssh/id_ecdsa
debug1: Will attempt key: /home/vagrant/.ssh/id_ecdsa_sk
debug1: Will attempt key: /home/vagrant/.ssh/id_ed25519
debug1: Will attempt key: /home/vagrant/.ssh/id_ed25519_sk
debug1: Will attempt key: /home/vagrant/.ssh/id_xmss
debug1: Will attempt key: /home/vagrant/.ssh/id_dsa
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,sk-ssh-ed25519@openssh.com,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering public key: /home/vagrant/.ssh/id_rsa RSA SHA256:EfCrAT6YbFvUsMPpcpjksdlbK9FkTTHxop/QpOJWIhA
debug1: Server accepts key: /home/vagrant/.ssh/id_rsa RSA SHA256:EfCrAT6YbFvUsMPpcpjksdlbK9FkTTHxop/QpOJWIhA
Authenticated to 34.202.157.83 ([34.202.157.83]:22) using "publickey".
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: filesystem
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: client_input_hostkeys: searching /home/vagrant/.ssh/known_hosts for 34.202.157.83 / (none)
debug1: client_input_hostkeys: searching /home/vagrant/.ssh/known_hosts2 for 34.202.157.83 / (none)
debug1: client_input_hostkeys: hostkeys file /home/vagrant/.ssh/known_hosts2 does not exist
debug1: Remote: /home/ubuntu/.ssh/authorized_keys:2: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug1: Remote: /home/ubuntu/.ssh/authorized_keys:2: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug1: Sending environment.
debug1: channel 0: setting env LANG = "C.UTF-8"
debug1: client_global_hostkeys_private_confirm: server used untrusted RSA signature algorithm ssh-rsa for key 0, disregarding
debug1: update_known_hosts: known hosts file /home/vagrant/.ssh/known_hosts2 does not exist
```

[100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp) - Client configuration file (w/ Puppet) to make changes to our configuration file in order to connect to a server without typing a password.
- Requirements
 - SSH client configuration must be configured to use the private key `~/.ssh/school`
 - SSH client configuration must be configured to refuse to authenticate using a password
```
vagrant@ubuntu:~$ sudo puppet apply 100-puppet_ssh_config.pp
Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds
Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created
Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created
Notice: Finished catalog run in 0.03 seconds
vagrant@ubuntu:~$
```
