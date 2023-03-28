#Set up Nginx
class nginx {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }
}

#Set up firewall
class firewall {
  Firewall {
    dport => '80',
    proto => 'tcp',
    action => 'accept',
  }
}

#Define the redirect

nginx::vhost { 'redirect_me':
  port => '80',
  ssl => false,
  www_root => '/var/www/redirect_me',
  rewrite_to => 'http://www.example.com',
  rewrite_rule => '^/redirect_me/(.*)$ /$1 redirect;',
}

#Set up hello world page

file { '/var/www/redirect_me/index.html':
  ensure => present,
  content => "Hello World!",
  require => Package['nginx'],
}
