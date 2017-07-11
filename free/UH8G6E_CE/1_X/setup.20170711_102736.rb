=begin

ref : C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\setup.rb
setup.rb

pushd C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\

pushd C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\1_X
setup.20170711_102736.rb 1_11 1_12

setup.rb 1_10 1_11
setup.rb 1_9 1_10
setup.rb 1_8 1_9
setup.rb 1_7 1_8

C:\WORKS_2\WS\WS_Others\free\UH8G6E_CE\setup.rb

=end

#ref https://stackoverflow.com/questions/19391133/how-can-i-recursively-copy-the-directory-contents-and-exclude-the-source-directo 'answered Oct 15 '13 at 21:47'
require 'fileutils'

def show_Usage
  #ref ヒアドキュメント　http://qiita.com/mogulla3/items/3e114e9c4697f0dea84c
  msg =<<-MSG
  <Usage>
      setup.rb <original folder name> <new folder name>
  <e.g.>
      setup.rb 1_7 1_8
MSG

  puts msg
  
end#show_Usage

################################
#	
#	def exec
#   @return
#     -1    args not proper
#     -2    source directory --> not exist
#
################################
def exec

  ################################
  #	
  #	validate: args
  #
  ################################
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] ARGV =>"
  
#  p ARGV
  
  lenOf_ARGV = ARGV.length
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] lenOf_ARGV => #{lenOf_ARGV}"

  if lenOf_ARGV != 2
  
    show_Usage
  
    return -1
    
  end#if lenOf_ARGV != 2
    
  ################################
  #	
  #	validate : folder exists
  #
  ################################
  dpath_Src = ARGV[0]
  dpath_Dst = ARGV[1]
  
  res = File.exists?(dpath_Src)
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] res => #{res} (#{dpath_Src})"
  
  if res == false
  
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] dir => doesn't exist : '#{dpath_Src}'"
    
    return -2
  
  else
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] folder => exists (#{dpath_Src})"
    
  end#if res == false

  ################################
  #	
  #	validate : format
  #
  ################################
  regex = Regexp.compile(/\d+_\d+/)
#  regex = Regexp.compile("\d+_\d+")
  
  if regex =~ ARGV[0]
  
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] match : #{ARGV[0]}"
    
  else 

    puts "[#{File.basename(__FILE__)}:#{__LINE__}] format not proper => #{ARGV[0]}"
    
    return -3  
  
  end#if regex =~ ARGV[0]
  
  if regex =~ ARGV[1]
  
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] match : #{ARGV[1]}"
    
  else 

    puts "[#{File.basename(__FILE__)}:#{__LINE__}] format not proper => #{ARGV[1]}"
    
    return -3  
  
  end#if regex =~ ARGV[0]
  
  
  ################################
  #	
  #	dir : copy
  #
  ################################
  res = FileUtils.cp_r dpath_Src, dpath_Dst
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] copy dir => #{res}"
  
  ################################################################
  #	
  #	change names
  #
  ################################################################
  ################################
  #	
  #	storage_XXX
  #
  ################################
  dpath_Storage = "#{dpath_Dst}/storage_#{dpath_Src}"
  
  res = File.exists?(dpath_Storage)
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] storage exists? => #{res} (#{dpath_Storage})"
  
  if res == false
  
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] storage dir ==> not exist : #{dpath_Storage}"

#    return -3
  
  else
    
    # change name
  #  File.rename \
    FileUtils.mv \
          "#{dpath_Dst}/storage_#{dpath_Src}", \
            "#{dpath_Dst}/storage_#{dpath_Dst}"
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] \
            name change => done : from 'storage_#{dpath_Src}' to 'storage_#{dpath_Dst}'"
    
  end#if res == false
  
#  # change name
##  File.rename \
#  FileUtils.mv \
#        "#{dpath_Dst}/storage_#{dpath_Src}", \
#          "#{dpath_Dst}/storage_#{dpath_Dst}"
#  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] \
#          name change => done : from 'storage_#{dpath_Src}' to 'storage_#{dpath_Dst}'"
  
  ################################
  #	
  #	main.(XXX).php
  #
  ################################
  version_Label_Src = dpath_Src.split("_").join(".")
  version_Label_Dst = dpath_Dst.split("_").join(".")
  
  fpath_Src = "#{dpath_Dst}/main.(#{version_Label_Src}~).php"
  fpath_Dst = "#{dpath_Dst}/main.(#{version_Label_Dst}~).php"
  
  FileUtils.mv fpath_Src, fpath_Dst

  puts "[#{File.basename(__FILE__)}:#{__LINE__}] \
        name change => done : from '#{fpath_Src}' to '#{fpath_Dst}'"

  ################################
  #	
  #	js/main.(XXX~).js
  #
  ################################
  version_Label_Src = dpath_Src.split("_").join(".")
  version_Label_Dst = dpath_Dst.split("_").join(".")
  
  fpath_Src = "#{dpath_Dst}/js/main.(#{version_Label_Src}~).js"
  fpath_Dst = "#{dpath_Dst}/js/main.(#{version_Label_Dst}~).js"
  
  FileUtils.mv fpath_Src, fpath_Dst

  puts "[#{File.basename(__FILE__)}:#{__LINE__}] \
        name change => done : from '#{fpath_Src}' to '#{fpath_Dst}'"

  ################################
  #	
  #	css/main.(XXX~).css
  #
  ################################
  version_Label_Src = dpath_Src.split("_").join(".")
  version_Label_Dst = dpath_Dst.split("_").join(".")
  
  fpath_Src = "#{dpath_Dst}/css/main.(#{version_Label_Src}~).css"
  fpath_Dst = "#{dpath_Dst}/css/main.(#{version_Label_Dst}~).css"
  
  FileUtils.mv fpath_Src, fpath_Dst

  puts "[#{File.basename(__FILE__)}:#{__LINE__}] \
        name change => done : from '#{fpath_Src}' to '#{fpath_Dst}'"

  ################################
  #	
  #	report
  #
  ################################
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] exec => done"

end

exec
