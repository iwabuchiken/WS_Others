require "gnuplot"

Gnuplot.open do |gp|
  Gnuplot::Plot.new( gp ) do |plot|
    plot.title  'test'
    plot.ylabel 'ylabel'
    plot.xlabel 'xlabel'
 
    # グラフ1個目
#    x = (-10..10).collect {|v| v.to_f}
#    y = (-10..10).collect {|v| v.to_f ** 2}
    x = (-100..100).collect {|v| v.to_f}
    y = (-100..100).collect {|v| v.to_f ** 2}
    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "lines"
      ds.notitle
    end
 
    # グラフ2個目
    x = (-100..100).collect {|v| v.to_f+50}
    y = (-100..100).collect {|v| v.to_f ** 2}
    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "lines"
      ds.notitle
    end
 
    # グラフ3個目
    x = (-100..100).collect {|v| v.to_f+100}
    y = (-100..100).collect {|v| v.to_f ** 2}
    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "lines"
      ds.notitle
    end
  end
end

##ref http://obelisk.hatenablog.com/entry/2016/04/10/152651 <== works
#Gnuplot.open do |gp|
#  Gnuplot::Plot.new(gp) do |plot|
#    
#    plot.xrange "[-3:3]"
#    
##    f = "x ** 4 + 2 * 5 ** 3 - 10 * x ** 2 + 5 * x  + 4"
#    f = "sin(x)"
#    
#    plot.data << Gnuplot::DataSet.new(f)
#  end
#  gets
#end

#ref http://qiita.com/tbpgr/items/5eed0a6ba172ce34560e <== not working
#Gnuplot.open do |gp|
#  Gnuplot::Plot.new( gp ) do |plot|
#    plot.title  "Array Plot Example"
#    plot.xlabel "x"
#    plot.ylabel "y"
#    plot.yrange "[0:5000]"
#
#    x = (0..50).map(&:to_f)
#    y = x.map{ |v| (v ** 2) + 3000 }
#    x2 = (0..50).map(&:to_f)
#    y2 = x.map{ |v| 2*v ** 2 + 2500 }
#
#    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
#      ds.with = "lines"
#      ds.linewidth = 2
#    end
##    plot.data << Gnuplot::DataSet.new( [x2, y2] ) do |ds|
##      ds.with = "lines"
##      ds.linewidth = 2
##    end
#  end
#end

puts "done"
