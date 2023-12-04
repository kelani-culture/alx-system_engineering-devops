# update packages
exec { 'update':
  command => 'sudo apt-get -y update',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# install nginx
package {'nginx':
 ensure => installed,
}

# write to file
file {'/var/www/html/index.nginx-debian.html':
 ensure  => present,
 content => 'Hello World!',
 mode    => 0644,
}


file { '/etc/nginx/sites-available/default':
  ensure       => present,
  content      => "server {\n\tlisten 80 default_server;\n\tserver_name _;\n\troot /var/www/html;\n\tlocation = /redirect_me{\n\t\treturn 301 https://regex101.com/;\n\t}\n}",
  validate_cmd => 'sudo /usr/sbin/nginx -t',
}


service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}
