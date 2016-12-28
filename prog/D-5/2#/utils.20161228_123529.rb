################################
# @param
#   serial    20161221_141900
#
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
  
end#get_time_label(type = "serial")


################################
# @param
#   dpath    C:\WORKS_2\WS\WS_Processing\1#\sketch_1_3_20161227_141618\movie_frame.20161228_122543
#   type
#       files
#       dirs
#       all   => files + dirs
#   sort
#       true  => sorted alphabetically, A-Z
#       false  => not sorted
#
################################
#def get dir_list(dpath)
#def get dir_list(dpath, type, sort)
def get_dir_list(dpath, type = "files", sort = true)
  
  # set path
  Dir.chdir(dpath)
  
  if type == "files"
    
    #debug
    puts "type => 'files'"
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] dpath => #{dpath}"
    
    #debug
#    p Dir.glob('*')
    
      result = Dir.glob('*').select {|f| File.file? f}
#      files = Dir.glob('*').select {|f| File.file? f}
        
      if sort == true
        
        return result.sort
        
      else
        
        return result
        
      end#if sort == true
        
  elsif type == "dirs"
    
    result = Dir.glob('*').select {|f| File.directory? f}

    if sort == true
      
      return result.sort
      
    else
      
      return result
      
    end#if sort == true

  elsif type == "all"
    
      result = Dir.glob('*')

    if sort == true
      
      return result.sort
      
    else
      
      return result
      
    end#if sort == true
    
  else

    result = Dir.glob('*')

    if sort == true
      
      return result.sort
      
    else
      
      return result
      
    end#if sort == true

  end#if type == "files"
  
end#get dir_list(dpath, type = "files", sort = true)
