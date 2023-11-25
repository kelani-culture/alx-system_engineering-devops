#install flask
file { '/usr/bin/pip3':
  ensure => present,
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package {'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
