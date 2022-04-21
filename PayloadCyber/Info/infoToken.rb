trap("SIGINT") { throw :ctrl_c }

 catch :ctrl_c do
 begin
require 'colorize'
system('clear')                                                                                  
def DataFormat()
    puts'''
    ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████ ███▄    █ 
    ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀ ██ ▀█   █ 
    ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███  ▓██  ▀█ ██▒
    ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄▓██▒  ▐▌██▒
      ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒██░   ▓██░
      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒ 
        ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░
      ░      ░ ░ ░ ▒  ░ ░░ ░    ░     ░   ░ ░ 
                 ░ ░  ░  ░      ░  ░        ░ 
                                                  '''.red
    system('sleep 1')
    puts '['.red+'!'.yellow+']'.red+' In Ngrok, the token is actually used to confirm your account'.white+','.yellow
    puts ''
    system('sleep 1')
    puts '['.red+';'.yellow+'] '.red+'and after registering on the '.white+'Ngrok'.red+' site'.white+' .'.red
    sleep(1)
    puts ''
    puts '['.red+';'.yellow+']'.red+' you can receive the token and set it with our tips'.white+' .'.yellow    
    puts ''
    system('sleep 3')
    system('cd .. && python3 Ngrok.py')
end
DataFormat()

rescue Exception
  puts "Not printed"
end
end
