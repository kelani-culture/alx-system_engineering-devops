# configure ssh file using puppet

file_line { ' passwd auth':
ensure => present,
line   => ' PasswordAuthentication no',
path   => '/etc/ssh/ssh_config',
}

file_line { 'IdentityFile':
ensure => present,
line   => '   IdentityFile ~/.ssh/school',
path   => '/etc/ssh/ssh_config',
}
