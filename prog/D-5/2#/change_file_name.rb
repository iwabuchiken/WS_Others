=begin

file:         change_file_name.rb
created at:   2016/12/28 12:34:28

<Usage>
C:\WORKS_2\WS\WS_Others\prog\D-5\2#\change_file_name.rb

pushd C:\WORKS_2\WS\WS_Others\prog\D-5\2#
change_file_name.rb

=end

require 'pathname'


#ref http://stackoverflow.com/questions/837123/adding-a-directory-to-load-path-ruby
libdir = File.expand_path(File.dirname(__FILE__))
$LOAD_PATH.unshift(libdir) unless $LOAD_PATH.include?(libdir)

#$LOAD_PATH.each do |elem|
#  puts elem
#end

puts "add path => done"

#require 'utils.rb'
#require 'utils'
require 'utils.20161228_123529'

def change_file_names
  
  ################################
  #	
  #	get: list
  #
  ################################
  dpath = "C:/WORKS_2/WS/WS_Processing/1#/sketch_1_3_20161227_141618/movie_frame.20161228_122543"
#  dpath = "C:\\WORKS_2\\WS\\WS_Processing\\1#\\sketch_1_3_20161227_141618\\movie_frame.20161228_122543"
  
  result = get_dir_list(dpath, "files", sort = true)
  
#  p result
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] files => #{result.size.to_s}"
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] dpath => #{dpath}"

  # validate
  if result.size < 1
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] no items in the directory"
    
    return
    
  end  
  
  ################################
  #	
  #	new name, new file
  #
  ################################
  count = 0
  
  result.each do |name|
    
    pname = Pathname.new(name)
    
    
    
#    pname = Pathname.new(name)
    
    fname_src = pname.basename
#    fname_src = Pathname.extname(name)
#    fname_src = File.basename file, ext
#    fname_src = File.basename file, extn
    
    #debug
    puts "src file => #{fname_src}"
    
#    #debug
#    p fname_src
#    p fname_src.to_s
    
#    p fname_src.methods.sort
    
    
    # split
#    tokens = fname_src.split()
#    tokens = fname_src.split("r")
#    tokens = fname_src.split("\\.")
#    tokens = fname_src.split("\.")
    tokens = fname_src.to_s.split("\.")
    
    p tokens  #=> ["frame", "20161227_160931", "0006", "tif"]
    
    p tokens[2].to_i  #=> 6
    
    #ref https://ruby-doc.org/core-1.9.3/Numeric.html
    num_new = (tokens[2].to_i - (result.size + 1)).abs
#    num_new = (tokens[2].to_i - result.size).abs
#    num_new = (tokens[2].to_i - 501).abs
    
    p num_new
    
    
    count += 1
    
    if count > 5
#    if count > 10
      
      break
      
    end
    
  end
  

#  puts "[#{__LINE__}] files => #{result.size.to_s}"
#  puts "[#{__LINE__}] dpath => #{dpath}"
  
#  print "[#{__LINE__}] yes"
  
end#change_file_names

def exec

  change_file_names
    
end

exec
