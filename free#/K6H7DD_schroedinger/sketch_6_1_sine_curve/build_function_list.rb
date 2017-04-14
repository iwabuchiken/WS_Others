#!C:\WORKS_2\Programs\Ruby23-x64\bin\ruby.exe

=begin

pushd C:\WORKS_2\WS\WS_Others\free#\K6H7DD_schroedinger\sketch_6_1_sine_curve\
build_function_list.rb


=end

require 'C:/WORKS_2/WS/WS_Others/prog/D-5/2#/utils.20161228_123529.rb'

def show_usage

  msg = <<"message"
  
<Usage>

  build_function_list.rb [FILE_NAME] 
  
message
  
  puts msg

  
end#show_usage

################################
# 
# @param lines
#   lines = File.readlines 
#
# @return
#   []
################################
def get_signature_list__variables_and_constants

  # array for list
  ary = Array.new
  
  #  regex = /^ *(static|void) (.+?)/
  #  regex = /^ *(static) (.+?) (.+?) .*( = )(.+?) *;/
    regex = /^ *(static|void|String) (.+?);/
  
  #  regex = /^ *(static)/
  #  regex = /^ *static/
    
#    puts "regex => #{regex}"
    
    lines.each_with_index { |elem, i|
  
      #ref http://stackoverflow.com/questions/9303984/ruby-regexp-group-matching-assign-variables-on-1-line asked Feb 16 '12 at 0:50
  #    res = elem.scan(regex)
  #    
  #    p res
        
  ##    if elem.start_with?("static")
      if elem =~ regex
  #    if elem =~ /^ *static/
        
        res = elem.scan(regex)
        
  #      p res
  #      p elem.scan(regex)
        
        puts "line:#{i.to_s} => '#{elem}'"
        
        ary << res[0]
  #      ary << [res[0],res[1]]
        
      end#if elem.start_with?("static")
      
    }#lines.each_with_index { |elem, i|

    ################################
    # 
    # return
    #
    ################################
    return ary
  

end#get_signature_list__variables_and_constants

################################
#	
#	@param lines
#   lines = File.readlines 
#	@param sorting
#   1   => ascending 
#   0   => no sorting
#   -1  => descending 
#
# @return
#   []
################################
def get_signature_list__methods(lines, sorting)

  # array for list
  ary = Array.new
  
  regex = /^ *(static|void|String) (.+?) *{/
    
#  puts "regex => #{regex}"
  
  lines.each_with_index { |elem, i|

    if elem =~ regex
      
      res = elem.scan(regex)
      
#      puts "line:#{i.to_s} => '#{elem}'"
      
      ary << res[0]
#      ary << [res[0],res[1]]
      
    end#if elem.start_with?("static")
    
  }#lines.each_with_index { |elem, i|

  ################################
  #	
  #	order
  #
  ################################
  ary_final = Array.new
  
  ary.each_with_index {|elem, i|
    
    line = elem[0]
    
#    puts "[#{File.basename(__FILE__)}:#{__LINE__}] line => #{line}"
    
    # judge
    if line.start_with?("static")
      
      new_ary = elem[1].split(" ")
      
      ary_final << [elem, new_ary[1]]
      
    else
      
      ary_final << [elem, elem[1]]
#      ary_final << [elem, line]
      
    end
    
  }#ary.each_with_index {|elem, i|
  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] ary_final =>"
#  
#  ary_final.each {|elem|
#   
#    p elem 
##    puts elem 
#    
#  }

  ################################
  #	
  #	sorting
  #
  ################################
#  puts
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] lines original =>"
#  puts
  
#  ary_final.each {|elem|
#   
#    p elem 
#    
#  }
  
  
#  #debug
#  puts
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] sorting..."
#  puts
  
  #ref http://stackoverflow.com/questions/13824444/comparing-two-strings-in-ruby answered Dec 11 '12 at 16:45
  ary_final_sorted = ary_final.sort { |x, y| x[1].casecmp y[1] }
#  ary_final_sorted = ary_final.sort { |x, y| x[1] > y[1] }
#  ary_final_sorted = ary_final.sort_by { |k| k["value"] }

#  ary_final_sorted.each {|elem|
#   
#    p elem 
#  #    puts elem 
#    
#  }
  
  ################################
  #	
  #	re-build lines
  #
  ################################
  lines_rebuilt = Array.new
  
  ary_final_sorted.each {|elem|
   
    lines_rebuilt << elem[0].join(" ") 
    
  }
    
#  puts
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] lines rebuilt =>"
#  puts
#  
#  
#  lines_rebuilt.each {|elem|
#   
#    p elem 
#  #    puts elem 
#    
#  }

  
#  puts sorted
    
#  p ary_final
  
  ################################
  #	
  #	return
  #
  ################################
  return lines_rebuilt
#  return ary
    
end#get_signature_list__methods

################################
#	
#	@param ary
#   [
#     "methods" => ["void calcWave()", "void draw()", ...],
#     "vars_constants" => [...],
#   ]
#
################################
def write_to_file(ary, fname_src)
  
  fname_dst = "list_of_signatures.#{fname_src}.#{get_time_label(type = "serial")}.txt"
#  fname_dst = "list_of_signatures.#{get_time_label(type = "serial")}.txt"
  
  f = File.open(fname_dst, 'w')
  
  ################################
  #	
  #	header
  #
  ################################
  f.write("source file:\t#{fname_src}")
  f.write("\n")
  
  f.write("generated at:\t#{get_time_label(type = "display")}")
  f.write("\n")
  f.write("\n")
  
  ################################
  #	
  #	signatures
  #
  ################################
  ary.each {|name, signatures|
   
    f.write("### #{name} (#{signatures.length}) ###################")
    
    f.write("\n")
    
    signatures.each {|sig|
     
      f.write(sig)
      f.write("\n")
       
    }
     
    # separating line
    f.write("\n")
    
  }#ary.each {|name, signatures|
  
#  ary.each {|line|
#   
#    f.write(line)
#    
#    f.write("\n")
#     
#  }
  
  f.close
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] file write => done"
  
  
end#write_to_file(ary)

def get_lines_from_file(fname_src)

  #debug
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] file name => '#{fname_src}'"
  
  # validate: nil
  if fname_src == nil
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] file name is nil => '#{fname_src}'"
    
    return nil, -1
    
  end
  
#  puts "file name => #{fname_src}"
  
  result = File.exist?(fname_src)
  
  if result != true
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] file doesn't exist => '#{fname_src}'"
    
#    puts "file doesn't exist => #{fname_src}"
    
    return "", -1
    
  else
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] file exists => #{fname_src}"
    
#    puts "file exists => #{fname_src}"
    
  end

  ################################
  # 
  # file io
  #
  ################################
  f = File.open(fname_src, 'r')
  
#  puts f.read
  lines = f.readlines

  ################################
  #	
  #	return
  #
  ################################
  return lines, 0
  
end#get_lines_from_file(fname_src)

def _exec_execute(fname_src)

  lines, result = get_lines_from_file(fname_src)

  #validate
  if result == -1
    
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] quitting..."
    
    return
    
  end

  ################################
  # 
  # vars
  #
  ################################
  #ref http://ref.xaio.jp/ruby/classes/array/new
  ary_final = Array.new
#  ary = Array.new
  
  ################################
  # 
  # match: pattern 1
  #
  ################################
  ary_methods = get_signature_list__methods(lines, 1)

#  puts
#  p ary_methods

  # put to the final array
  ary_final << ["methods", ary_methods]
  
  ################################
  # 
  # write file
  #
  ################################
  write_to_file(ary_final, fname_src)
  
end#_exec_execute

def exec

#  puts "yes"
#  print "yes"
  
  ################################
  #	
  #	validate: file name input
  #
  ################################
  aryof_fnames = Array.new
  
  if ARGV.length < 1
  
    # list of files ending with ".pde"
    p File.dirname(__FILE__)
    
    #ref http://stackoverflow.com/questions/32125318/ruby-dir-glob-alternative-with-regexp answered Aug 20 '15 at 18:18
    filelist = Dir.glob("#{File.dirname(__FILE__)}/*").grep(/\.pde$/)
#    dirlist = Dir.glob("#{File.dirname(__FILE__)}/*").grep(/.pde$/)
#    dirlist = Dir.glob(File.dirname(__FILE__)).grep(/.pde$/)
#    dirlist = Dir.glob('/usr/lib/*').grep(/\/lib[A-Z]+\.so$/)
    
#    p filelist
    
    filelist.each {|e|
     
      aryof_fnames << File.basename(e)
#      aryof_fnames << e
      
#      p File.basename(e)
#      p e
       
    }
    
#    show_usage
#    
#    
#    
#    return
  
  else
    
    fname_src = ARGV[0]
    
#    aryof_fnames = Array.new
    
    aryof_fnames << fname_src
    
  end

  #debug
  aryof_fnames.each {|e|
   
    p e 
    
  }
  
  ################################
  #	
  #	validate: file exists
  #
  ################################
#  fname_src = ARGV[0]
#  
#  aryof_fnames = Array.new
#  
#  aryof_fnames << fname_src
  
  # execute
  aryof_fnames.each {|name|
    
    _exec_execute(name)
#    _exec_execute(fname_src)
    
  }
#  _exec_execute(fname_src)
  
#  lines, result = get_lines_from_file(fname_src)
#
#  #validate
#  if result == -1
#    
#    
#    puts "[#{File.basename(__FILE__)}:#{__LINE__}] quitting..."
#    
#    return
#    
#  end
#
#  ################################
#  #	
#  #	vars
#  #
#  ################################
#  #ref http://ref.xaio.jp/ruby/classes/array/new
#  ary_final = Array.new
##  ary = Array.new
#  
#  ################################
#  #	
#  #	match: pattern 1
#  #
#  ################################
#  ary_methods = get_signature_list__methods(lines, 1)
#
##  puts
##  p ary_methods
#
#  # put to the final array
#  ary_final << ["methods", ary_methods]
#  
#  ################################
#  #	
#  #	write file
#  #
#  ################################
#  write_to_file(ary_final, fname_src)
#    
end#exec


exec
