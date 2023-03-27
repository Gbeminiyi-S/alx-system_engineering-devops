# Client configuration file (w/ Puppet)

file { '/etc/ssh/ssh_config':
  ensure => 'present',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  content => '
    Host myserver
        HostName 34.202.157.83
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ',
}

