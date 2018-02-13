=begin
#ref multiline comments https://www.thoughtco.com/commenting-ruby-code-2908193

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\26_Paraview\2_
ruby 2_1.rb

<Usage>
ruby 2_1.rb > tmp.data

ruby 2_1.rb > sample.vtk

=end

#ref add loadpath https://stackoverflow.com/questions/837123/adding-a-directory-to-load-path-ruby answered Jul 11 '09 at 3:26
dir_Main = File.expand_path(File.dirname(__FILE__))
$LOAD_PATH.unshift(dir_Main) unless $LOAD_PATH.include?(dir_Main)

dir_Lib = File.expand_path(File.dirname(__FILE__)) + "/" + "libs"
$LOAD_PATH.unshift(dir_Lib) unless $LOAD_PATH.include?(dir_Lib)

#require "libs/libs.rb"
require "libs.rb"

def test_range()
  
  grid = 10
  
  for ix in -grid..grid
    
    puts ix
    
  end
  
end#def test_range()

def test_LOADPATH
  
  libdir = File.expand_path(File.dirname(__FILE__))
  
#  puts $LOAD_PATH
  
  puts 
  
#  puts libdir
  
end

def vtk
  
  fname_Out = "data/test.#{get_Time_Current()}.vtk"
#  fname_Out = "data/test.#{get_Time_Current()}.data"
  f = open(fname_Out,"w")
  
  grid = 10
  dim = grid*2+1
  points = dim**3
  r = 0.8
  f.write("# vtk DataFile Version 1.0\n")
  f.write("test\n")
  f.write("ASCII\n")
  f.write("DATASET STRUCTURED_POINTS\n")
  
  #ref sprintf https://blog.udemy.com/ruby-sprintf/
  f.write( sprintf("DIMENSIONS %d %d %d\n",dim, dim, dim))
  f.write("ORIGIN 0.0 0.0 0.0\n")
  f.write("ASPECT_RATIO 1.0 1.0 1.0\n")
  
  f.write("\n")
  
  f.write( sprintf("POINT_DATA %s\n", points.to_s) )
  f.write("SCALARS scalars float\n")
  f.write("LOOKUP_TABLE default\n")
  
  for ix in -grid..grid
    for iy in -grid..grid
      for iz in -grid..grid
      x = ix.to_f/grid
      y = iy.to_f/grid
      z = iz.to_f/grid
      v = r*r - (x*x + y*y + z*z)
      
      if v < 0
      
        v = 0
      
      elsif 0 <= v and v < 0.1
      
        v = 0.1
      
      else#if (v < 0)
      
        v = 0.15
#        v = 0.2
        
      end#if (v < 0)
      
#      v = 0 if v < 0
      
#      puts v.to_s
      f.write( sprintf("%s\n", v.to_s) )
      
      end
    end
  end
  
  f.close
  
end

def vtk_orig
  
  
  grid = 10
  dim = grid*2+1
  points = dim**3
  r = 0.8
  puts "# vtk DataFile Version 1.0"
  puts "test"
  puts "ASCII"
  puts "DATASET STRUCTURED_POINTS"
  printf "DIMENSIONS %d %d %d\n",dim, dim, dim
  puts "ORIGIN 0.0 0.0 0.0"
  puts "ASPECT_RATIO 1.0 1.0 1.0"
  puts
  puts "POINT_DATA " + points.to_s
  puts "SCALARS scalars float"
  puts "LOOKUP_TABLE default"
  for ix in -grid..grid
    for iy in -grid..grid
      for iz in -grid..grid
      x = ix.to_f/grid
      y = iy.to_f/grid
      z = iz.to_f/grid
      v = r*r - (x*x + y*y + z*z)
      v = 0 if v < 0
      puts v.to_s
      end
    end
  end
end


#grid = 10
#dim = grid*2+1
#points = dim**3
#r = 0.8
#puts "# vtk DataFile Version 1.0"
#puts "test"
#puts "ASCII"
#puts "DATASET STRUCTURED_POINTS"
#printf "DIMENSIONS %d %d %d\n",dim, dim, dim
#puts "ORIGIN 0.0 0.0 0.0"
#puts "ASPECT_RATIO 1.0 1.0 1.0"
#puts
#puts "POINT_DATA " + points.to_s
#puts "SCALARS scalars float"
#puts "LOOKUP_TABLE default"
#for ix in -grid..grid
#  for iy in -grid..grid
#    for iz in -grid..grid
#    x = ix.to_f/grid
#    y = iy.to_f/grid
#    z = iz.to_f/grid
#    v = r*r - (x*x + y*y + z*z)
#    v = 0 if v < 0
#    puts v.to_s
#    end
#  end
#end


#vtk
#vtk_orig
test_range

#test_LOADPATH
