=begin

C:\WORKS_2\WS\WS_Others\bk-\bk-216_math-of-information\4_1\4_1.rb

pushd C:\WORKS_2\WS\WS_Others\bk-\bk-216_math-of-information\4_1\
ruby 4_1.rb

<Usage>

<info>
written at:
      
      2017/10/11 18:14:59

=end

########################################
# @param size_X >= 1, integer
#
# @return
#     [ 
#       [0.42672, 0.22414, 0.34914] #=> sum is 1.0
#       [0.34862, 0.45872, 0.19266]
#       [0.04082, 0.63265, 0.32653]
#     ]   #=> size_X = 3 (e.g.)
# 
# 
########################################
def get_Transition_Matrix(size_X)

  ####################
  # build array
  ####################
  ary_Trans = Array.new()
#  ary_Trans = Array.new(size_X)
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] size_X is #{size_X}"
  
  #ref http://zetcode.com/lang/rubytutorial/arrays/
  size_X.times do |i|
    
#    puts "[#{File.basename(__FILE__)}:#{__LINE__}] i is #{i}"
    
    
    temp = Array.new(size_X){|j| rand(100) }
#    temp = Array.new(size_X){|i| rand(100) }
      
    sum = temp.inject(0, :+)

    j = temp.map {|elem|  sprintf("%06.5f", (elem * 1.0 / sum)).to_f}
#    j = temp.map {|elem|  (elem * 1.0 / sum).round(5)}
#    j = temp.map {|elem|  elem * 1.0 / sum}
      
#    puts "[#{File.basename(__FILE__)}:#{__LINE__}] temp is :"
    
#    p temp
      
    ary_Trans << j
#    ary_Trans << temp
      
  end

#  p ary_Trans
  
  puts
  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] ary_Trans[0][0] : #{ary_Trans[0][0]}"
  
  # return
  return ary_Trans
  
##  temp = [rand(100), rand(100), rand(100), rand(100), rand(100)]
#  #ref https://stackoverflow.com/questions/4908413/how-to-initialize-an-array-in-one-step-using-ruby answered Feb 5 '11 at 17:43
#  temp = Array.new(size_X){|i| rand(100) }
#  
#  sum = temp.inject(0, :+)
#  
#  p temp
#  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] sum = #{sum}"
#  
#  #ref https://stackoverflow.com/questions/5689152/how-are-array-each-and-array-map-different asked Apr 16 '11 at 19:50
#  j = temp.map {|elem|
#    
#    elem * 1.0 / sum
#    
#  }
#  
#  puts j
#  
#  sum_j = j.inject(0, :+)
#  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] sum of j = #{sum_j}"
  
  
end#get_Transition_Matrix

def markov_Chain
  
  size_X = 3
  
  mat = get_Transition_Matrix(size_X)

  ####################
  # report
  ####################
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] matrix is : "

  mat.each do |elem|
    
    p elem
    
  end
    
#  p mat
  
end#markov_Chain

def exec

  markov_Chain
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done"
    
end

exec
