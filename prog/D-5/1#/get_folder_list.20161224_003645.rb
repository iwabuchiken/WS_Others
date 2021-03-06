require 'pathname'


=begin

file:         get_folder_list.rb
created at:   20161223_212926

<Usage>
C:\WORKS_2\WS\WS_Others\prog\D-5\1#\get_folder_list.rb

pushd C:\WORKS_2\WS\WS_Others\prog\D-5\1#
get_folder_list.rb

=end

################################
#	
#	vars (global)
#
################################
VERSION = "1.0"
FILE_PATH = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-5\\1#\\get_folder_list.rb"


################################
#   get_folder_list
# @param
#
################################
def get_folder_list

  ################################
  #	
  #	prep: list
  #
  ################################
  #ref __FILE__ http://stackoverflow.com/questions/37101151/what-does-file-program-name-mean-in-ruby
  path = Pathname.new(__FILE__)
#  path = Pathname.new('.')
  
  #ref https://ruby-doc.org/stdlib-2.1.0/libdoc/pathname/rdoc/Pathname.html
  p "path.dirname => #{path.dirname}"
  
  dpath = path.dirname
#  dpath = "c:/works_2"
  
  #ref http://stackoverflow.com/questions/1899072/getting-a-list-of-folders-in-a-directory
  Dir.chdir(dpath)
#  Dir.chdir("c:/works_2")
#  Dir.chdir(path.dirname)
#  Dir.chdir('/destination_directory')
#  list = Dir.glob('*').select
#  list = Dir.glob('*').select {|f| File.directory? f}
  files = Dir.glob('*').select {|f| File.file? f}
  dirs = Dir.glob('*').select {|f| File.directory? f}
  
  puts
  puts "[#{__LINE__}] directory => #{dpath}" 

  puts
  puts "[#{__LINE__}] folders ...."
  p dirs
  
  puts
  puts "[#{__LINE__}] files ...."
  p files.sort
#  p files
  
#  p files.methods.sort
  
#  p __FILE__
  
#  target_directory = 
#  
#  Dir.chdir('/destination_directory')
##  Dir.chdir('/destination_directory')
#  
#  list = Dir.glob('*').select {|f| File.directory? f}
#    
#  p list
  
  ################################
  #	
  #	file: write data
  #
  ################################
  time_label = get_time_label("serial")
  
  fname = "directory_list.#{time_label}.txt"
  
  f = File.new(fname, "w")
  
  # header
  f.write("program file path = #{FILE_PATH}")
  f.write("\n")
  f.write("version = #{VERSION}")
  f.write("\n")
  
  f.write("list file created at = #{time_label}")
  f.write("\n")
  
  f.write("dir path = #{dpath}")
  f.write("\n")
  f.write("dirs = #{dirs.size}")
  f.write("\n")
  f.write("files = #{files.size}")
  f.write("\n")
  f.write("\n")
  
  # data: dirs
  f.write "<directories> #{dirs.size}"
  f.write "\n"
  
  dirs.each do |elem|
    
    f.write(elem)
    f.write("\n")
    
  end
  
  f.write("\n")
  f.write("\n")
  
  # data: files
  f.write "<files> #{files.size}"
  f.write "\n"

  files.each do |elem|
    
    f.write(elem)
    f.write("\n")
    
  end
  
  f.close
  
  puts "[#{__LINE__}] file written => #{fname}"
  
end#get_folder_list

################################
# @param
#   serial    20161221_141900
# @orig: C:\WORKS_2\WS\WS_Others\res.245\115\r.245-115.5#1.elec-conductivity.rb 
#
################################
def get_time_label(type = "serial")
  
  if type == "serial"
    
    #ref http://stackoverflow.com/questions/7415982/how-do-i-get-the-current-date-time-in-dd-mm-yyyy-hhmm-format
    return Time.now.strftime("%Y%m%d_%H%M%S")
    
  elsif type == "display"
    
    #ref http://stackoverflow.com/questions/7415982/how-do-i-get-the-current-date-time-in-dd-mm-yyyy-hhmm-format
    return Time.now.strftime("%Y/%m/%d  %H:%M:%S")
    
  else
    
    return Time.now.strftime("%Y%m%d_%H%M%S")
    
  end
  
end

def exec

  get_folder_list
    
end#exec

exec
