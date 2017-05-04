require "C:/WORKS_2/WS/WS_Others/utils/utils.20161228_123529.rb"

def execute

  exec_path = "C:/WORKS_2/Programs/gnuplot_4.6.7/bin/pgnuplot.exe"
  
#  plot_command = "plot sin(x)"
#  plot_command = "load \"C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/10_1/test.plt\"\n";
  plot_command = "load \"C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/10_1/example-2.plt\"\n";
  
  p io = IO.popen(exec_path, "r+")  # => #<IO:fd 4>
#  p io = IO.popen("cat", "r+")  # => #<IO:fd 4>
  
#  io.puts "abc = 2345"
  
  io.puts "input_file = \"data.20170504_133655.nmax-800.txt\""
  
  io.puts plot_command
#  io.puts "foo"
  
  io.puts "set term wxt; set output"
  
  input = gets
  
  io.close_write
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] gets => '#{input}'"
  
  
#  p IO.popen(exec_path, "r+") {|io|
##  p IO.popen("cat", "r+") {|io|
#    
#    io.puts "plot(x)"
##    io.puts "foo"
#    
#    io.close_write
#    
##    io.gets
#    
#    input = gets
#    
#  }
#  # => "foo\n"
  
  
  puts "yes"
  
end

def execute_2

  exec_path = "C:/WORKS_2/Programs/gnuplot_4.6.7/bin/pgnuplot.exe"
  
  plot_command = "load \"C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/10_1/example-2.plt\"\n";
  
  p io = IO.popen(exec_path, "r+")  # => #<IO:fd 4>

  aryof_fnames = [

    "data.20170504_133655.nmax-1000.txt",    
    "data.20170504_133655.nmax-900.txt" ,   
    "data.20170504_133655.nmax-800.txt" ,   
    "data.20170504_133655.nmax-700.txt"
    
  ]

  aryof_fnames.each {|fname|

    io.puts "input_file = \"#{fname}\""
    
    io.puts plot_command
    
    io.puts "set term wxt; set output"
    
  }
    
#    io.puts "input_file = \"data.20170504_133655.nmax-800.txt\""
#    
#    io.puts plot_command
#  #  io.puts "foo"
#    
#    io.puts "set term wxt; set output"
  
  input = gets
  
  io.close_write
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] gets => '#{input}'"
  
  
#  p IO.popen(exec_path, "r+") {|io|
##  p IO.popen("cat", "r+") {|io|
#    
#    io.puts "plot(x)"
##    io.puts "foo"
#    
#    io.close_write
#    
##    io.gets
#    
#    input = gets
#    
#  }
#  # => "foo\n"
  
  
  puts "yes"
  
end#execute_2

#execute
execute_2

