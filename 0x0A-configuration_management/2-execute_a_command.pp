#lill a precess called killmenow
exec { 'killmenow_process':
command      => '/usr/bin/pkill -f killmenow',
refreshonly  => True,
onlyif       => '/usr/bin/pgrep -f killmenow'
}
