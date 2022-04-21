trap("SIGINT") { throw :ctrl_c }

 catch :ctrl_c do
 begin
    

require 'colorize'

system('clear')

def DataFormat()
    puts'''
    d8b           .d888         
    Y8P          d88P"          
                 888            
    888 88888b.  888888 .d88b.  
    888 888 "88b 888   d88""88b 
    888 888  888 888   888  888 
    888 888  888 888   Y88..88P 
    888 888  888 888    "Y88P"  
    '''.red
    system('sleep 1')
    puts '['.red+'!'.yellow+']'.red+' If option 1 is not your choice (Token section only) '.white+','.yellow
    puts ''
    system('sleep 1')
    puts '['.red+'☦'.yellow+'] '.red+'copy and paste it from the '.white+'Ngrok'.red+' site'.white+' .'.red
    puts ''
    system('sleep 3')
    system('cd .. && python3 Ngrok.py')
end
DataFormat()

rescue Exception
    puts "Not printed"
 end
 end