# kill a process called killmenow

exec { 'kill_killmenow_process':
command => 'pkill -f killmenow',
path    => ['/usr/bin', '/bin'],
onlyif  => 'pgrep -f killmenow',
}
