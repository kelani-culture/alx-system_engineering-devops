#install flask

file {'/usr/bin/pip2':
  ensure => present,
}
package {'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
