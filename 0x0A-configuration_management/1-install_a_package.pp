#install flask
package { 'flask':
name     => 'flask',
ensure   => '2.1.0',
provider => 'pip',
}
