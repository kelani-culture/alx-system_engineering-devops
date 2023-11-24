#lill a precess called killmenow
exec { 'killme_now':
command: 'pkill killmenow',
refreshonly: True,
onlyif: 'grep killmenow'
}
