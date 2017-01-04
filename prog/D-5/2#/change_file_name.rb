=begin

file:         change_file_name.rb
created at:   2016/12/28 12:34:28

<Usage>
C:\WORKS_2\WS\WS_Others\prog\D-5\2#\change_file_name.rb

pushd C:\WORKS_2\WS\WS_Others\prog\D-5\2#
change_file_name.rb

=end

require 'pathname'
require 'fileutils'


#ref http://stackoverflow.com/questions/837123/adding-a-directory-to-load-path-ruby
libdir = File.expand_path(File.dirname(__FILE__))
$LOAD_PATH.unshift(libdir) unless $LOAD_PATH.include?(libdir)

puts "add path => done"

require 'utils.20161228_123529'

################################
#	
#	vars
#
################################
# path to the folder
DPATH = "C:/WORKS_2/WS/WS_Processing/projects/3#/sketch_3_1_20161229_124619/images"



def change_file_names
  
  ################################
  #	
  #	get: list
  #
  ################################
  dpath = DPATH
#  dpath = "C:/WORKS_2/WS/WS_Processing/1#/sketch_1_3_20161227_141618/movie_frame.20161228_122543"
  
  result = get_dir_list(dpath, "files", sort = true)
  
  # sort ==> reverse
  result.reverse!
  
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
    
    fname_src = pname.basename
    
    #debug
    puts "src file => #{fname_src}"
    
    tokens = fname_src.to_s.split("\.")
    
    p tokens  #=> ["frame", "20161227_160931", "0006", "tif"]
    
    p tokens[2].to_i  #=> 6
    
    num_new = (tokens[2].to_i - (result.size + 1)).abs

    p num_new
    
    num_new_final = num_new + result.size
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] num_new_final => #{num_new_final}"
    
    fname_dst = sprintf("%s.%s.%04d.%s", tokens[0], tokens[1], num_new_final, tokens[3])

    FileUtils.cp(File.join(dpath, fname_src), File.join(dpath, fname_dst))
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] file copied => dst = #{fname_dst}"
    
  end#result.each do |name|
  
end#change_file_names

def exec

  change_file_names
    
end

exec
