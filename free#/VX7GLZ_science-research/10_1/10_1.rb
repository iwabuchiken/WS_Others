require 'shellwords'

require "C:/WORKS_2/WS/WS_Others/utils/utils.20161228_123529.rb"

def execute

  #ref http://stackoverflow.com/questions/2232/calling-shell-commands-from-ruby answered Aug 5 '08 at 14:42
#  res = `dir`
#  res = `example-2.exe`  #=> works
#  res = `example-2.exe 2000`
#  res = `example-2.exe 2000 > data.1.txt` #=> not working
  
  time_label = get_time_label()
  
  #ref http://stackoverflow.com/questions/33976467/how-to-substitute-variable-in-backtick-command-in-ruby answered Nov 29 '15 at 6:28
  args = ["example-2.exe", "2000", ">", "data.2.txt"]
#  args = ["example-2.exe", "2000", ">", "data.#{time_label}.txt"]
  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] args --> '#{args.shelljoin}'"
  
#  command = "example-2.exe"    #=> works
#  command = "example-2.exe 1000"  #=> works
  aryof_nmax = [1000, 900, 800, 700]
  
  aryof_nmax.each {|x|

    command = "example-2.exe 1000 > data.#{time_label}.nmax-#{x.to_s}.txt"  #=> 
      
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] command => #{command}"
    
    system(command)
    
  }
#  command = "example-2.exe 1000 > data.#{time_label}.txt"  #=> 
#    
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] command => #{command}"
  
  
#  system(command)
#  system("example-2.exe")
#  system("#{args.shelljoin}")
#  res = `#{args.shelljoin}`
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] shell ---> done"
  
  
#  p res.split("\n")
#  
#  if res == nil
#  
#    puts "[#{File.basename(__FILE__)}:#{__LINE__}] result --> nil"
#    
#    return
#  
#  end#if res == nil
#  
#  #### show result
#  res.split("\n").each {|x|
#    
#    puts x
#    
#  }
  
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done"
  
end#execute

execute
