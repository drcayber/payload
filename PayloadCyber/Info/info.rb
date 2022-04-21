trap("SIGINT") { throw :ctrl_c }

 catch :ctrl_c do
 begin

require 'colorize'

def DataFormat()
    system('sleep 1')
    system('clear')
    puts ''
    puts '['.red+' LocalHost : '.yellow+']'.red+' localhost means the internal environment of your network'+' ;'.red
    puts ''
    puts '                for example all people connected to your'+' WiFi '.red
    puts ''
    puts'                are considered members of the local environment'.yellow                
    puts ''
    puts ''
    puts ''
    puts ''
    puts '['.red+' NgrokHost : '.green+']'.red+' Ngrok service is a free hosting service'+' ;'.red
    puts ''
    puts '                Which can be operated'+' Port Forwarding '.red
    puts ''
    puts'                Used to transfer data'.yellow                
    puts ''
    puts 'SLEEP 6'.blue
    system('sleep 6')
    # system('cd ..')
    system('cd .. && python3 payloads.py')
end
DataFormat()

rescue Exception
    puts "Not printed"
 end
 end