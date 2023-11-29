#install nginx and configure server
exec { 'update':
  command => 'sudo apt-get -y update',
  path    => '/usr/bin:/usr/sbin:/bin',
}

package {'nginx':
  ensure => installed,
  provider => 'apt',
}

service {'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}

file {'/etc/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure       => present,
  content      => "server {\n\tlisten 80 default_server;\n\tserver_name _;\n\troot /var/www/html;\n\tlocation = /redirect_me{\n\t\treturn 301 https://regex101.com/;\n\t}\n}",
  validate_cmd => 'sudo /usr/sbin/nginx -t',
  require      => [Service['nginx']],
}
