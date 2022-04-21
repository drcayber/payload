trap("SIGINT") { throw :ctrl_c }

 catch :ctrl_c do
 begin

require 'colorize'

system('clear')

puts '''
 ███████████                       ████                         █████
░░███░░░░░███                     ░░███                        ░░███
 ░███    ░███  ██████   █████ ████ ░███   ██████   ██████    ███████
 ░██████████  ░░░░░███ ░░███ ░███  ░███  ███░░███ ░░░░░███  ███░░███
 ░███░░░░░░    ███████  ░███ ░███  ░███ ░███ ░███  ███████ ░███ ░███
 ░███         ███░░███  ░███ ░███  ░███ ░███ ░███ ███░░███ ░███ ░███
 █████       ░░████████ ░░███████  █████░░██████ ░░████████░░████████
░░░░░         ░░░░░░░░   ░░░░░███ ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░
                         ███ ░███
                        ░░██████
                         ░░░░░░
'''.yellow

def DataFormat()
    system('sleep 1')
    puts '['.red+'!'.yellow+']'.red+' This project uses the metasplit framework '.white+','.yellow
    puts ''
    system('sleep 1')
    puts '['.red+'☦'.yellow+'] '.red+'build eavesdropping piles and '.white+'Ngrok'.red+' to connect between global ips'.white+' .'.red
    puts ''
    system('sleep 1')
    puts '['.red+'☠'.yellow+'] '.red+'Our team intends to '.white+'upgrade'.red+' it in case of feedback from this '.white+' project'.red+' ...'.blue
    puts ''
    system('sleep 1')
    puts '['.red+'✇'.yellow+'] '.red+'Thanks DrCyber'.green
    puts ''
    system('sleep 1')
    system('python3 payloads.py')
end
DataFormat()
rescue Exception
    puts "Not printed"
 end
 end