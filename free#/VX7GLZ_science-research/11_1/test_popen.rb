=begin

pushd C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\11_1
test_popen.rb

C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/11_1

=end

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
  
  dir_root = "C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research"
  
  dir_specific = "data.20170505_142139.txt"
  
  dir_session = "11_1"
  
  dir_target = "#{dir_root}/#{dir_session}/#{dir_specific}"
#  dir_target = "C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/11_1"
  
  dir_plt = "#{dir_root}/#{dir_session}"
  
  plt_target = "example-2.plt"
  
  plot_command = "load \"#{dir_plt}/#{plt_target}\"\n";
#  plot_command = "load \"#{dir_target}/#{plt_target}\"\n";
#  plot_command = "load \"C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/10_1/example-2.plt\"\n";
  
  #ref https://docs.ruby-lang.org/ja/latest/method/IO/s/popen.html
  p io = IO.popen(exec_path, "r+")  # => #<IO:fd 4>

  #test
  #ref pwd https://www.google.co.jp/search?q=ruby+directory+list&oq=ruby+directory+list&aqs=chrome..69i64j5l2j0l3.5690j0j9&sourceid=chrome&ie=UTF-8#q=ruby+pwd
#  dir_tmp = Dir.pwd
  
#  dir_target = "C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/11_1"
#  dir_target = "C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/10_1"
  
#  Dir.chdir("C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/10_1")
  
  aryof_fnames = get_dir_list(dir_target)
  
  #ref start_with? http://ref.xaio.jp/ruby/classes/string/start_with
  #ref select http://ref.xaio.jp/ruby/classes/array/select
  aryof_fnames = aryof_fnames.select {|item| item.start_with?("data") and item.end_with?("txt")}
  
  ##### validate
  if aryof_fnames == nil or aryof_fnames.size < 1
  
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] aryof_fnames == nill or aryof_fnames.size < 1"
  
    return  
  
  end#if aryof_fnames == nill or aryof_fnames.size < 1
  
  aryof_fnames.each {|fname|

    io.puts "input_file = \"#{dir_target}/#{fname}\""
#    io.puts "input_file = \"#{fname}\""
        #    dir_target = "#{dir_root}/#{dir_session}/#{dir_specific}"

    # namax value
    #ref match http://ref.xaio.jp/ruby/classes/string/match
    m = fname.match(/nmax-(\d+)/)
    
    if m != nil
    
      io.puts "nmax = #{m[1]}"
    
    else#if ()
    
      io.puts "nmax = -1"
    
    end#if ()
    
    io.puts plot_command
    
    io.puts "set term wxt; set output"
   
  }
    
  input = gets
  
  io.close_write
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] gets => '#{input}'"
  
  puts "yes"
  
end#execute_2

def show_usage
  
  msg =<<EOF
<Usage>

test_popen.rb "data.20170505_133410.nmax-300.txt" 300  
  
EOF

  puts msg

end

def execute_1_file(fname_src, nmax)

  puts "[#{File.basename(__FILE__)}:#{__LINE__}] data source => '#{fname_src}'"
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] nmax => #{nmax}"
  
  
  exec_path = "C:/WORKS_2/Programs/gnuplot_4.6.7/bin/pgnuplot.exe"
  
  dir_target = "C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/11_1"
  
  plt_target = "example-2.plt"
  
  plot_command = "load \"#{dir_target}/#{plt_target}\"\n";
  
  #ref https://docs.ruby-lang.org/ja/latest/method/IO/s/popen.html
  p io = IO.popen(exec_path, "r+")  # => #<IO:fd 4>

  io.puts "input_file = \"#{fname_src}\""

  io.puts "nmax = #{nmax}"
  
  io.puts plot_command
    
  io.puts "set term wxt; set output"
   
  input = gets
  
  io.close_write
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] gets => '#{input}'"
  
  puts "yes"
  
end#execute_1_file(fname_src, fname_dst)

##p ARGV
#      #test_popen.rb abc => ["abc"]
#puts "[#{File.basename(__FILE__)}:#{__LINE__}] ARGC =>"
#
#p ARGV == nil ? "ARGV => nil" : ARGV.length

#execute
if ARGV.size == 0

  execute_2

elsif ARGV.size == 1#if (ARGC = 0)

  puts "[#{File.basename(__FILE__)}:#{__LINE__}] ARGV.size => 1"
  
  p ARGV
  
  show_usage
  
#  return

elsif ARGV.size == 2#if (ARGC = 0)

  ### validate : file name
  fpath = "C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/11_1/#{ARGV[0]}"
  
  #ref exist https://docs.ruby-lang.org/ja/search/query:File.exist%3F/#entry-0
  res = File.exist?(fpath)
  
  if res == false
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] file doesn't exist => '#{fpath}'"
    
    show_usage

    exit    
    
  end
  
  ### validate : numeric
  #ref http://qiita.com/yutackall/items/76c931d4029665a7192c
  res = ARGV[1].to_i.integer?

  if res == false
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] arg is not an integer => '#{ARGV[1]}'"
    
    show_usage
    
    exit
#    return
    
  end
    
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] executing..."
  
  execute_1_file(ARGV[0], ARGV[1].to_i)

else
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] unknown argument => "
  p ARGV

  p ARGV.size
  
  show_usage
  
#  return
  
end#if (ARGC = 0)
#execute_2

##execute_1_file("data.20170505_122426.nmax-300.txt", 300)

