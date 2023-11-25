#install flask
package { 'flaskk':
name     => 'flask',
ensure   => '2.1.0',
provider => 'pip',
}
