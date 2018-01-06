=begin

file:         C:\WORKS_2\WS\WS_Others\proj_home-appliances-engineer\15_2\main.rb
created at:   2017/02/23 16:51:49

<Usage>
C:\WORKS_2\WS\WS_Others\proj_home-appliances-engineer\15_2\main.rb

pushd C:\WORKS_2\WS\WS_Others\proj_home-appliances-engineer\15_2
main.rb

=end

require 'pathname'
require 'fileutils'


#ref http://stackoverflow.com/questions/837123/adding-a-directory-to-load-path-ruby
libdir = File.expand_path(File.dirname(__FILE__))
$LOAD_PATH.unshift(libdir) unless $LOAD_PATH.include?(libdir)

require 'utils.20170223_165359'

=begin

20170223_170658

process_data

    data: http://kankimaru.com/pdf/kankimaru/netukoukankouritu.pdf

<usage>
pushd C:\WORKS_2\WS\WS_Others\proj_home-appliances-engineer\15_2
main.rb

<what the function does>
  1. read data from: data.txt
  2. re-order all the entries
  3. output to: data.XXXX.txt
  4. then --> replace " " with tab char
  5. copy the text to spreadsheet
  6. analyze what you want to

<where to use>
  in: 家電製品エンジニア資格 / 15#2 / 20170223_160835

=end
def process_data
  
  f = File.new("data.txt")
  
  ary = Array.new()
  ary2 = Array.new()
  
  f.each_line do |line|
    
#    p line.split(" ")
#    puts line.split(" ")
    
    # puts first 4 numbers
    ary << line.split(" ")[0..3]
    ary2 << line.split(" ")[4..7]
    
  end
  
  f.close
  
  #debug
#  p ary
  ################################
  #	
  #	new file
  #
  ################################
  join_char = "\t"
  
  ################################
  #	
  #	first 4 numbers
  #
  ################################
  
  fname_new = "data." + get_time_label("serial") + ".txt"
    
  #ref http://qiita.com/mogulla3/items/fbc2a46478872bebbc47
  f2 = File.new(fname_new, "w")
  
  f2.write("ＯＡ側#{join_char}ＳＡ側#{join_char}ＲＡ側#{join_char}交換率");
  f2.write("\n")
  
  # write data
  ary.each do |elem|
    
    f2.write(elem.join(join_char))
#    f2.write(elem.join(" "))
      
    f2.write("\n")
    
  end
  
  f2.close
  
  ################################
  # 
  # 2nd 4 numbers
  #
  ################################
  f2 = File.new(fname_new, "a")
  
  # write data
  ary2.each do |elem|
    
    f2.write(elem.join(join_char))
      
    f2.write("\n")
    
  end
  
  f2.close
  
  #message
  ################################
  #	
  #	message
  #
  ################################
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] file closed"
  
  
end

def exec
  
  process_data
  
end


exec
