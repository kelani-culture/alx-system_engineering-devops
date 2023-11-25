#lill a precess called killmenow
exec { '/usr/bin/pkill':
command => '/usr/bin/pkill -f killmenow',
onlyif  => '/usr/bin/pgrep -f killmenow',
}
