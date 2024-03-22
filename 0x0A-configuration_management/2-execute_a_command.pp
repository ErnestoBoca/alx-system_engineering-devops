# kills a process

exec { 'pkill killmenow':
  path    => '/bin/'
  command => 'pkill killmenow',
}
