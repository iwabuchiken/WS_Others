require 'kconv'

=begin

file:         r.245-115.5#1.elec-conductivity.rb
created at:   2016/12/21 15:50:47

<Usage>
C:\WORKS_2\WS\WS_Others\res.245\r.245-115.5#1.elec-conductivity.rb

pushd C:\WORKS_2\WS\WS_Others\res.245
r.245-115.5#1.elec-conductivity.rb

=end

###############################
   prep data for => def: gen_elec_conductivity
#
# How to prepare the data file
#
# 1. copy/paste from web page to ---> sakura file
#   1) from:  https://en.wikipedia.org/wiki/Electrical_resistivity_and_conductivity#Resistivity_and_conductivity_of_various_materials
#   2) to:    sakura file
# 2. replace
#  1) tab    ==> ','
#  2) '×'    ==> 'x'
#  3) '−'    ==> '-'
# 3. copy/paste from sakurafile to  --> eclipse "dat" file
#   1) from:  sakura file
#   2) to:    r.245-115.5#1.elec-conductivity.dat
# 4. run this program: C:\WORKS_2\WS\WS_Others\res.245\r.245-115.5#1.elec-conductivity.rb
#
###############################

###############################
#   prep data for => def: gen_elec_conductivity_periodical
#
# How to prepare the data file
#
# 1. copy/paste from web page to ---> sakura file
#   1) from:  https://ja.wikipedia.org/wiki/%E9%9B%BB%E6%B0%97%E4%BC%9D%E5%B0%8E%E7%8E%87
#   2) to:    sakura file
#
# 2. replace
#  1) tab    ==> '\r\n'
#
# 3. copy/paste
#   1) from:  sakurafile
#   2) to:    eclipse "dat" file: 'r.245-115.5#1.elec-conductivity.periodical.dat'
#4. run this program: C:\WORKS_2\WS\WS_Others\res.245\r.245-115.5#1.elec-conductivity.rb period
#

###############################




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
  
end

def gen_elec_conductivity

  fname = "r.245-115.5#1.elec-conductivity.dat"
  
#  f = File.new(fname, "a+:sjis")
#  f = File.new(fname, "a+")
  f = File.new(fname, "r")
  
#  puts "f.readlines.class.name ==> "
#  puts f.readlines.class.name
  
#  f.readlines.each do |line|
#  f.readlines.each_with_index do |i, line|
#  f.readlines.each_with_index do |line, i|
  
  ary = Array.new
  
  #ref http://udemy.benesse.co.jp/development/ruby-each-with-index.html
  f.readlines.each.with_index(5) do |line, i|
    
#    puts "#{line}"
    puts "(#{i}) #{line}"
    
#    tokens = line.encode("Shift_JIS").split(" ")
    tokens = line.split(",")
#    tokens = line.split(" ")
    
    t2s = tokens[1].split("x")
    
    t3s = t2s[1].split("-")
    
    #debug
    p t2s[0].to_f
    
#    val = t3s[1].to_f == 7 ? t2s[0].to_f.round(3) * 10 : t2s[0].to_f.round(3)
#    val = t3s[1].to_f == 7 ? t2s[0].to_f * 10 : t2s[0].to_f
    val = t3s[1].to_f == 7 ? t2s[0].to_f * 10.0 : t2s[0].to_f
    
#    ary << [tokens[0], val.round(3), t3s[0].to_f**(t3s[1].to_f*(-1))]
#    ary << [tokens[0], val, t3s[0].to_f**(t3s[1].to_f*(-1))]
#    ary << [tokens[0], val, t3s[0].to_f**(t3s[1].to_f*(-1))]  #=> 14.29999999999
#    ary << [tokens[0], val.round(3), t3s[0].to_f**(t3s[1].to_f*(-1))] #=> 14.3
    
    #ref http://stackoverflow.com/questions/2054217/rounding-float-in-ruby
    ary << [tokens[0], val.round(3)] #=> 14.3
#    ary << [tokens[0], val.round(7), t3s[0].to_f**(t3s[1].to_f*(-1))]
#    ary << [tokens[0], t2s[0].to_f, t3s[0].to_f**(t3s[1].to_f*(-1))]
#    ary << [tokens[0], t2s[0].to_f, t3s[0].to_f, t3s[1].to_f*(-1)]
#    ary << [tokens[0], tokens[1], t2s[0], t3s[0], t3s[1]]
#    ary << [tokens[0], tokens[1]]
#    ary << [tokens[0], tokens[3]]
    
  end#f.readlines.each.with_index(5) do |line, i|
  
  puts
  p ary
    
#  puts f.class.name
#  
#  puts f.methods.sort
  
#  puts f.read
#  p f.read
  
  f.close
  
  puts
  puts "------------------------"
  puts "file closed => #{fname}"

  ################################
  # file: write
  ################################
  fname = "r.245-115.5#1.#{get_time_label}.out.dat"

  f = File.new(fname, "w")
  
  ary.each do |line|
    
    f.write("#{line[0]}\t#{line[1]}")
    
    f.write("\n")
    
  end#ary.each do |line|
    
  # close
  f.close
  
  puts
  puts "file written => #{fname}"
  
end#def gen_elec_conductivity

def gen_elec_conductivity_periodical

  ############################
  # prepare: data
  ############################
  fname = "r.245-115.5#1.elec-conductivity.periodical.dat"
  
  f = File.new(fname, "r")

  ary = Array.new
  
  lines = f.readlines
  
  lines.each.with_index(0) do |line, i|
#  f.readlines.each.with_index(0) do |line, i|
    
    #ref http://stackoverflow.com/questions/4130364/does-ruby-have-a-string-startswithabc-built-in-method
    if line.match(/^[A-Z]/)
      
      data_1 = line.strip
      data_2 = lines[i + 1] == nil ? line.strip : lines[i + 1].strip
      
      ary << [data_1, data_2]
#      ary << [line.strip, lines[i + 1].strip]
#      ary << [line.strip, lines[i + 1]]
#      ary << [line, lines[i + 1]]
      
    end
    
  end#f.readlines.each.with_index(5) do |line, i|
  
  puts
  p ary
    
  f.close
  
  puts
  puts "------------------------"
  puts "file closed => #{fname}"

  ################################
  # file: write
  ################################
  fname = "r.245-115.5#1.periodical.#{get_time_label}.out.dat"

  f = File.new(fname, "w")
  
  ary.each do |line|
    
    f.write("#{line[0]}\t#{line[1]}")
    
    f.write("\n")
    
  end#ary.each do |line|
    
  # close
  f.close
  
  puts
  puts "file written => #{fname}"
  
end#gen_elec_conductivity_periodical

def exec

#  gen_elec_conductivity
  gen_elec_conductivity_periodical
    
end

##############################
#
#   exec
#
##############################
if ARGV[0] == "period"
  
  gen_elec_conductivity_periodical
  
else
  
  gen_elec_conductivity
  
end

exec
