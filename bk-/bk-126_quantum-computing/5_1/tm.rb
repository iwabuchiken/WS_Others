=begin

pushd C:\WORKS_2\WS\WS_Others\bk-\bk-126_quantum-computing\5_1
tm.rb


tm ---> Turing machine
at: 2017/05/08 18:20:17

=end

=begin

["0", "1", "0", "0", "0+", "1", "1", "0", "1"]
===> "+" symbol ---> value edited according to the command

=end

def get_str_current_aux(str_current, loc_Head, aryof_index_changed)
  
  #ref map index http://d.hatena.ne.jp/idesaku/20100403/1270321741
  str_current_aux = str_current.map.with_index {|elem, i|
    
    if i == loc_Head
      
#      puts "[#{File.basename(__FILE__)}:#{__LINE__}] i == head ---> i = #{i.to_s}"
      
      elem = elem + "*"
      
    else  elem
    end
    
  }

  return str_current_aux
  
end

def aux_add_head_mark(str_Target, loc_Head)
  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] starting => add head mark"
  
  
  return str_Target.map.with_index {|elem, i|
  #  tmp = str_current.map!.with_index {|elem, i|
      
      if i == loc_Head
        
        puts "[#{File.basename(__FILE__)}:#{__LINE__}] i == head ---> i = #{i.to_s}"
        
        elem = elem + "*"
        
      else
        
        elem
        
      end
      
    }
  
end#aux_add_head_mark(str_Target, loc_Head)

def aux_add_changed(str_Target, aryof_index_changed)

  tmp = str_Target.map.with_index {|elem, i|
#  return str_Target.map.with_index {|elem, i|
  #  tmp = str_current.map!.with_index {|elem, i|
      
      if aryof_index_changed[i] > 0
#      if i == loc_Head
        
        puts "[#{File.basename(__FILE__)}:#{__LINE__}] "\
            "aryof_index_changed[i] > 0 ==> #{aryof_index_changed[i].to_s}"
        
        puts "[#{File.basename(__FILE__)}:#{__LINE__}] elem => '#{elem}'"
        
#        elem + "+"
        
#        puts "[#{File.basename(__FILE__)}:#{__LINE__}] i == head ---> i = #{i.to_s}"
        aryof_index_changed[i].times do
          
          puts "[#{File.basename(__FILE__)}:#{__LINE__}] update elem..."
          
          elem = elem + "+"
#          elem + "+"
#          elem.to_s
#          elem
#          elem = "a"
#          elem += "a"
#          elem += "+"
          
        end
        
        elem
        
#        elem = elem + "*"
        
      else
        
        elem
        
      end
      
  }
  
  ##### report
  print "[#{File.basename(__FILE__)}:#{__LINE__}] target => "
  p str_Target
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] index changed => "
  p tmp
  
  return tmp
  
end#aux_add_head_mark(str_Target, aryof_index_changed)

def exec_1_step(str_Target, aryof_index_changed, loc_Head, cmd)

  print "[#{File.basename(__FILE__)}:#{__LINE__}] cmd => "
  p cmd
  
  str_current_aux = aux_add_head_mark(str_Target, loc_Head)
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] str_Target =>"
  
  p str_Target
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] str_current_aux =>"
  
  p str_current_aux
  
  puts
  
  #########################
  ##### 
  #####     q0 --> q1
  ##### 
  #########################
  puts "========== q0 ---> q1 =========="
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] command 1st (cmd[0]) => "
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] command 1st =>"
  
  p cmd    #=> 
#  p cmd[0]    #=> '[1, 0, "L"]'

  ##### report: head location
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] head is at => #{loc_Head}"

  ##### read state value
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] state value => #{str_Target[loc_Head]}"
  
  ##### read: command
  command_current = str_Target[loc_Head].to_i == 1 ? cmd[0] : cmd[1]
#  command_current = str_Target[loc_Head].to_i == 1 ? cmd[0][0] : cmd[0][1]
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] command is => "
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] command is =>"
  
  p command_current

#  ##### execute: 1/0
  str_Target[loc_Head] = command_current[1].to_s
##  str_current[loc_head] = command_current[1].to_s + "+"
#  
#  
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] str_Target changed => "
  p str_Target
  
  ##### update : aryof_index_changed
  if command_current[0] == command_current[1]
  
    
  
  else#if (command_current[0] == command_current[1])
  
    aryof_index_changed[loc_Head] += 1
  
  end#if (command_current[0] == command_current[1])
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] aryof_index_changed is now => "
  
  p aryof_index_changed
  
#  ##### update : 
#  aux_add_head_mark(str_current, aryof_index_changed)
  
  ##### report: str_current
  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] str_current is now =>"
  
  ### update : loc_Head
  puts
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] Evaluating the direction command"
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] Evaluating the direction command..."
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] command_current => "
  p command_current     #=> '[1, 0, "L"]'
  
  if command_current[2] == "L"

    print "[#{File.basename(__FILE__)}:#{__LINE__}] command is => "
    
    puts " => 'L'"
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] Moving the head toward => Left"
      
    loc_Head -= 1
    
    ## validate
    if loc_Head < 0
    
      puts "[#{File.basename(__FILE__)}:#{__LINE__}] loc_Head => less than zero : #{loc_Head.to_s}"
      
      exit -1
    
    end#if loc_Head > str_current.length - 1
    
  elsif command_current[2] == "R"

    puts " => 'R'"
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] Moving the head toward => Right"
    
    loc_Head += 1
    
    ## validate
    if loc_Head > str_Target.length - 1
    
      puts "[#{File.basename(__FILE__)}:#{__LINE__}] loc_Head => out of limit : #{(str_Target.length - 1).to_s}"
      
      exit -1
    
    end#if loc_Head > str_current.length - 1
    
  elsif command_current[2] == "x"

    print "[#{File.basename(__FILE__)}:#{__LINE__}] command is => "
    
    puts " => 'x'"
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] Moving the head toward => No movement"
    
#    loc_Head += 1
    
#    ## validate
#    if loc_Head > str_Target.length - 1
#    
#      puts "[#{File.basename(__FILE__)}:#{__LINE__}] loc_Head => out of limit : #{(str_Target.length - 1).to_s}"
#      
#      exit -1
#    
#    end#if loc_Head > str_current.length - 1
    
  else#if (command_current[2] == )
  
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] Unknown direction command => '#{command_current[2]}'"

    exit -1
      
  end#if (command_current[2] == )
  
  
  ##### report: str_current_aux
  str_current_aux = aux_add_head_mark(str_Target, loc_Head)
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] head ---> processed: "
  p str_current_aux
  
  str_current_aux = aux_add_changed(str_current_aux, aryof_index_changed)
  print "[#{File.basename(__FILE__)}:#{__LINE__}] index ---> processed: "
  p str_current_aux
  
  
#  p aux_add_head_mark(str_current, loc_Head)
#  p str_current
  
  
      
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done"
  
  ################################
  #	
  #	return
  #
  ################################
  return str_Target, aryof_index_changed, loc_Head

  
end#exec_1_step(str_Target, aryof_index_changed, loc_Head)
  
	def exec_V2

  ##### command set
  cmd = [
    
        # command : 1
        [[1, 0, "L"],  [0, 0, "L"]],
        # command : 2
        [[1, 0, "L"],  [0, 1, "x"]]
    ]
  
  ##### initial loc of head
  loc_Head_initial = 4
    
  ##### setup : loc of head
  loc_Head = loc_Head_initial
  
  ##### initial : str_Current
  str = "010011101"
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] str => '#{str}'"
  
  
  str_Current = str.split("");
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] str_Current => "
  p str_Current

  ##### initial : aryOf_Index_Changed
  aryOf_Index_Changed = Array.new(str_Current.length, 0)
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] aryOf_Index_Changed created => "
  
  p aryOf_Index_Changed

  
  ################################
  #	
  #	q0 ---> q1
  #
  ################################
  
#  exec_1_step(str_current, aryof_index_changed, loc_Head, cmd[0])
  str_Current, aryOf_Index_Changed, loc_Head = \
    exec_1_step(str_Current, aryOf_Index_Changed, loc_Head, cmd[0])
    
  ################################
  #	
  #	report
  #
  ################################
  print "[#{File.basename(__FILE__)}:#{__LINE__}] aryOf_Index_Changed is now ===> "
  
  p aryOf_Index_Changed
      
  print "[#{File.basename(__FILE__)}:#{__LINE__}] loc_Head is now ===> "
  
  p loc_Head

  ################################
  # 
  # q1 ---> q2
  #
  ################################
#  exec_1_step(str_current, aryof_index_changed, loc_Head, cmd[0])
  str_Current, aryOf_Index_Changed, loc_Head = \
    exec_1_step(str_Current, aryOf_Index_Changed, loc_Head, cmd[1])
    
  ################################
  # 
  # report
  #
  ################################
  print "[#{File.basename(__FILE__)}:#{__LINE__}] aryOf_Index_Changed is now ===> "
  
  p aryOf_Index_Changed
      
  print "[#{File.basename(__FILE__)}:#{__LINE__}] loc_Head is now ===> "
  
  p loc_Head
  
    
end#exec_V2

def exec

  ##### command set
  cmd = [
    
        # command : 1
        [[1, 0, "L"],  [0, 0, "L"]],
        # command : 2
        [[1, 0, "L"],  [0, 1, "x"]]
    ]
  
  ##### initial loc of head
  loc_Head_initial = 4
    
  ##### setup : loc of head
  loc_Head = loc_Head_initial
  
  ##### initial : str_current
  str = "010011101"
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] str => '#{str}'"
  
  
  str_current = str.split("");
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] str_current => "
  p str_current

  ##### initial : aryof_index_changed
  aryof_index_changed = Array.new(str_current.length, 0)
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] aryof_index_changed => "
  
  p aryof_index_changed
    
  ##### str ---> add head mark
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] callling ---> aux_add_head_mark"
  
  
  str_current_aux = aux_add_head_mark(str_current, loc_Head)
#  str_current_aux = str_current.map.with_index {|elem, i|
##  tmp = str_current.map!.with_index {|elem, i|
#    
#    if i == loc_head
#      
#      puts "[#{File.basename(__FILE__)}:#{__LINE__}] i == head ---> i = #{i.to_s}"
#      
#      elem = elem + "*"
#      
#    else
#      
#      elem
#      
#    end
#    
#  }
  
  
#  str_current.each_with_index {|elem, i|
#   
#    if i == loc_head
#    
#      elem = elem + "*"
#    
#    end#if i == loc_head
#     
#  }
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] str_current =>"
  
  p str_current
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] str_current_aux =>"
  
  p str_current_aux
  
  puts
  
  #########################
  ##### 
  #####     q0 --> q1
  ##### 
  #########################
  puts "========== q0 ---> q1 =========="
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] command 1st => "
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] command 1st =>"
  
  p cmd[0]

  ##### report: head location
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] head is at => #{loc_Head}"

  ##### read state value
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] state value => #{str_current[loc_Head]}"
  
  ##### read: command
  command_current = str_current[loc_Head].to_i == 1 ? cmd[0][0] : cmd[0][1]
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] command is => "
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] command is =>"
  
  p command_current

#  ##### execute: 1/0
  str_current[loc_Head] = command_current[1].to_s
##  str_current[loc_head] = command_current[1].to_s + "+"
#  
#  
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] str_current changed => "
  p str_current
  
  ##### update : aryof_index_changed
  if command_current[0] == command_current[1]
  
    
  
  else#if (command_current[0] == command_current[1])
  
    aryof_index_changed[loc_Head] += 1
  
  end#if (command_current[0] == command_current[1])
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] aryof_index_changed is now => "
  
  p aryof_index_changed
  
#  ##### update : 
#  aux_add_head_mark(str_current, aryof_index_changed)
  
  ##### report: str_current
  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] str_current is now =>"
  
  ### update : loc_Head
  puts
  print "[#{File.basename(__FILE__)}:#{__LINE__}] Evaluating the direction command"
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] Evaluating the direction command..."
  
  if command_current[2] == "L"

    puts " => 'L'"
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] Moving the head toward => Left"
      
    loc_Head -= 1
    
    ## validate
    if loc_Head < 0
    
      puts "[#{File.basename(__FILE__)}:#{__LINE__}] loc_Head => less than zero : #{loc_Head.to_s}"
      
      exit -1
    
    end#if loc_Head > str_current.length - 1
    
  elsif command_current[2] == "R"

    puts " => 'R'"
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] Moving the head toward => Right"
    
    loc_Head += 1
    
    ## validate
    if loc_Head > str_current.length - 1
    
      puts "[#{File.basename(__FILE__)}:#{__LINE__}] loc_Head => out of limit : #{(str_current.length - 1).to_s}"
      
      exit -1
    
    end#if loc_Head > str_current.length - 1
    
  else#if (command_current[2] == )
  
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] Unknown direction command => '#{command_current[2]}'"

    exit -1
      
  end#if (command_current[2] == )
  
  
  ##### report: str_current_aux
  str_current_aux = aux_add_head_mark(str_current, loc_Head)
  
  print "[#{File.basename(__FILE__)}:#{__LINE__}] head ---> processed: "
  p str_current_aux
  
  str_current_aux = aux_add_changed(str_current_aux, aryof_index_changed)
  print "[#{File.basename(__FILE__)}:#{__LINE__}] index ---> processed: "
  p str_current_aux
  
  
#  p aux_add_head_mark(str_current, loc_Head)
#  p str_current
  
  
      
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done"
  
    
end

#exec
exec_V2

