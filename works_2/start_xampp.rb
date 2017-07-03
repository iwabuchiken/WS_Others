=begin

pushd C:\WORKS_2\WS\WS_Others\works_2\start_xampp.rb
C:\WORKS_2\WS\WS_Others\works_2\start_xampp.rb

=end

def exec
  
  #ref https://stackoverflow.com/questions/2232/calling-shell-commands-from-ruby
  res = %x(tasklist|sort)
#  res = %x(dir)
  
#  puts res
  
  if res.include?("xampp-control.exe")
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] xampp ---> running"
#    puts "[#{File.basename(__FILE__)}:#{__LINE__}] yes"
    
  else
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] no"
    
    res = %x(start C:\\WORKS_2\\Programs\\xampp\\xampp-control.exe)
    
  end
  
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done"
  
  
end


exec