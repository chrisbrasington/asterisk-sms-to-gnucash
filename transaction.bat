#!/usr/bin/ruby
#note: 1 - be sure to 'chmod +x' this file
#      2 - place in /sbin/
#      3 - rename 'transaction.bat' to 'transaction'

command = 'PATH_TO/text-messaging-to-gnucash/parser.py '

command += "'" + ARGV[0] + "'"

value = %x[#{command}]
puts value
