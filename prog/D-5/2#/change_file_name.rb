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
  
  # sort ==> reverse
  #ref http://stackoverflow.com/questions/22639201/sorting-an-array-in-reverse-order answered Mar 25 '14 at 15:35
  result.reverse!
#  result.sort_reverse!
  
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
    
    num_new_final = num_new + result.size
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] num_new_final => #{num_new_final}"
    
    
    #ref https://docs.ruby-lang.org/ja/latest/doc/print_format.html
#    fname_dst = num_new_final
    fname_dst = sprintf("%s.%s.%04d.%s", tokens[0], tokens[1], num_new_final, tokens[3])
    
#    p sprintf("%s.%s.%04d.%s", tokens[0], tokens[1], fname_dst, tokens[3])
#    p sprintf("%s.%s.%04d.%s", tokens[0], tokens[1], num_new_final, tokens[3])
#    p sprintf("%s.%s.%04d.%s", tokens[0], tokens[1], num_new, tokens[3])
    
    # copy file
    #ref join http://stackoverflow.com/questions/597488/how-to-do-a-safe-join-pathname-in-ruby
    #ref copy http://stackoverflow.com/questions/9519645/copying-a-file-from-one-directory-to-another-with-ruby
    FileUtils.cp(File.join(dpath, fname_src), File.join(dpath, fname_dst))
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] file copied => dst = #{fname_dst}"
    
    ################################
    #	
    #	stopper
    #
    ################################
#    count += 1
#    
#    if count > 5
##    if count > 10
#      
#      break
#      
#    end
    
  end#result.each do |name|
  
end#change_file_names

def exec

  change_file_names
    
end

exec
