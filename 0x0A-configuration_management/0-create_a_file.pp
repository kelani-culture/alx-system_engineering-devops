
# a  puppet file that create a content and write to its
file { '/tmp/school':
  ensure  => present,
  mode    => '0744'.
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
