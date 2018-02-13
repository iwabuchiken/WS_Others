

def get_Time_Current(type = "serial", mill = false)

  #ref millseconds https://stackoverflow.com/questions/1414951/how-do-i-get-elapsed-time-in-milliseconds-in-ruby answered Oct 22 '13 at 20:01
  #ref https://www.tutorialspoint.com/ruby/ruby_date_time.htm
  if type == "serial"
    
    n = Time.now
    
    mill = ((n.to_f - n.to_i) * 1000).to_i
    
    if mill == true
    
      label = Time.now.strftime("%Y%m%d_%H%M%S") + mill.to_s
    
    else#if (mill == true)
    
      label = Time.now.strftime("%Y%m%d_%H%M%S")
    
    end#if (mill == true)
    
  else#if (type == "serial")
  
    if mill == true
      
      label = Time.now.strftime("%d/%m/%Y %H:%M:%S") + mill.to_s
    
    else#if (mill == true)
    
      label = Time.now.strftime("%d/%m/%Y %H:%M:%S")
    
    end#if (mill == true)
    
  
  end#if (type == "serial")
  
#  label = Time.now.strftime("%d/%m/%Y %H:%M")
  
  return label
  
end