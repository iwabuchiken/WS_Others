=begin

file from: C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\10_1\10_1.rb
at: 2017/05/05 12:06:18

pushd C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\11_1
10_1.rb

=end
require 'shellwords'
require 'fileutils'

require "C:/WORKS_2/WS/WS_Others/utils/utils.20161228_123529.rb"

def execute

  #ref http://stackoverflow.com/questions/2232/calling-shell-commands-from-ruby answered Aug 5 '08 at 14:42
  
  time_label = get_time_label()
  
  ### new directory
  dname = "data.#{time_label}.txt"
  res = File.exist?(dname)
  
  if res == false
  
    #ref http://stackoverflow.com/questions/19280341/create-directory-if-it-doesnt-exist-with-ruby answered Oct 9 '13 at 19:08
    FileUtils.mkdir_p dname
  
  end#if res == false
  
  
  #ref http://blog.cototoco.net/work/201405/ruby-%E9%85%8D%E5%88%97/ "多次元配列を初期化する"
#  aryof_nmax = Array.new(10){|i| (i + 1) * 100}
#  aryof_nmax = Array.new(20){|i| (i + 1) * 100}
#  aryof_nmax = Array.new((300-100) / 10 + 1){|i| (i + 10) * 10}
#  aryof_nmax = Array.new((500-50)/5+1){|i| (i+10) * 5}
  aryof_nmax = Array.new((800-100)/100+1){|i| (i) * 100 + 100}
  
  variable_name = "step"
    
  aryof_nmax.each {|x|

    command = "example-2.exe #{x.to_s} > #{dname}\\data.#{time_label}.#{variable_name}-#{x.to_s}.txt"  #=> 
#    command = "example-2.exe #{x.to_s} > #{dname}\\data.#{time_label}.nmax-#{x.to_s}.txt"  #=> 
#    command = "example-2.exe #{x.to_s} > data.#{time_label}.nmax-#{x.to_s}.txt"  #=> 
      
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] command => #{command}"
    
    system(command)
    
  }
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] shell ---> done"
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done"
  
end#execute

execute
