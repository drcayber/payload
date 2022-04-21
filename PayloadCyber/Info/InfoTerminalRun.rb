trap("SIGINT") { throw :ctrl_c }

 catch :ctrl_c do
 begin

require 'colorize'
# Cut
def InfoHost()
    system('clear')
    puts '''
  8888888           .d888              8888888          
    888            d88P"                 888            
    888            888                   888            
    888   88888b.  888888 .d88b.         888   88888b.  
    888   888 "88b 888   d88""88b        888   888 "88b 
    888   888  888 888   888  888        888   888  888 
    888   888  888 888   Y88..88P        888   888 d88P 
  8888888 888  888 888    "Y88P"       8888888 88888P"  
                                               888      
                                               888      
                                               888      
    '''
    puts ''
    puts '['.red+'HOST'.yellow+']'.red+' pay attention '.white+'!'.colorize(:red)
    puts ''
    puts '['.red+' After connecting to Ngrok '.colorize(:white)
    puts ''
    puts 'Open a new terminal, go to the tool path and run the tool again'.colorize(:red)+' Then'.colorize(:yellow)
    puts ''
    puts 'In the new terminal, go to the'.white+' Get ip Host Ngrok'.colorize(:yellow)+' section'.white
    puts ''
    puts 'And put the link there and after you find the ip'.white+' ,'.colorize(:yellow)
    puts ''
    puts 'Tap '.white+'control + C '.red+' at the same time'.white+' ,'.yellow
    puts ''
    puts 'This tool takes you to the'.white+' import path of the IP'.red+' And'.yellow
    puts''
    puts 'Put the IP in that location'.white+' ]'.red
end
def InfoPort()
  puts ''
  puts '  @@@ @@@  @@@ @@@@@@@@  @@@@@@       @@@@@@@   @@@@@@  @@@@@@@  @@@@@@@
  @@! @@!@!@@@ @@!      @@!  @@@      @@!  @@@ @@!  @@@ @@!  @@@   @@!  
  !!@ @!@@!!@! @!!!:!   @!@  !@!      @!@@!@!  @!@  !@! @!@!!@!    @!!  
  !!: !!:  !!! !!:      !!:  !!!      !!:      !!:  !!! !!: :!!    !!:  
  :   ::    :   :        : :. :        :        : :. :   :   : :    :   
                                                                        '
  puts '['.red+'PORT'.yellow+']'.red
  puts ''
  puts '[ '.red+'In the port section'.white+','.yellow 
  puts ''
  puts 'use the port that'.white+' Ngrok '.red+'gives you next to the'.white+' tcp link'.yellow
  puts ''
  puts 'And in '.white+'https'.yellow+' from the port on which you ran '.white+'Ngrok'.red
  puts ''
  puts 'Use and give '.white+'port receiver'.yellow+' in the script'.white+' ]'.red
  puts ''
end

InfoHost()
system('sleep 5')
system('clear')
InfoPort()
system('sleep 4')
system('cd .. && python3 CreatorNgrok.py')

rescue Exception
  puts "Not printed"
end
end