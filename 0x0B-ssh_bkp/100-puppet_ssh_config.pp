#!/usr/bin/env bash
# using Puppet to make changes to our configuration file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
