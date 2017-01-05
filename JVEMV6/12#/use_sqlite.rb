
require 'sqlite3'

=begin

file:         use_sqlite.rb
created at:   2017/01/05 18:00:48

<Usage>
C:\WORKS_2\WS\WS_Others\JVEMV6\12#\use_sqlite.rb

pushd C:\WORKS_2\WS\WS_Others\JVEMV6\12#
use_sqlite.rb

=end

#FPATH = "C:/WORKS_2/WS/WS_Others/prog/D-5/2\#"
FPATH = "C:/WORKS_2/WS/WS_Others/prog/D-5/2#"

#ref http://stackoverflow.com/questions/837123/adding-a-directory-to-load-path-ruby
libdir = File.expand_path(File.dirname(FPATH))

##debug
#p libdir  

#libdir = File.expand_path(File.dirname(__FILE__))
$LOAD_PATH.unshift(FPATH) unless $LOAD_PATH.include?(libdir)
#$LOAD_PATH.unshift(libdir) unless $LOAD_PATH.include?(libdir)
#
require 'utils.20161228_123529'

##debug
#$LOAD_PATH.each do |elem|
#  
#  p elem
#  
#end

def test_sqlite
  
  #debug
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] starting ..."
  
  
#  fname = "sqlite3:C:/WORKS_2/WS/Eclipse_Luna/Cake_IFM11/app/Lib/data/ifm11_backup_20160110_080900.bk"
  fname = "C:/WORKS_2/WS/Eclipse_Luna/Cake_IFM11/app/Lib/data/ifm11_backup_20160110_080900.bk"
#  fname = "test_sqlite.sqlite3"
  
  #ref http://www.ownway.info/Ruby/sqlite3-ruby/about
  db = SQLite3::Database.new(fname)
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] db => opened: #{fname}"
  
  # select
  cursor = db.execute("SELECT * FROM ifm11 WHERE _id > 18586")
#  cursor = db.execute("SELECT * FROM ifm11 WHERE _id < 10")
#  cursor = db.execute("SELECT * FROM ifm11 WHERE key1 = ? AND key2 = ?", [key1, key2])
  
  #debug
  p cursor
  
  cursor.each do |tuple|
    puts tuple[0]  # value1 の値
    puts tuple[1]  # value2 の値
  end
  
  # db を使い MySQL を操作する
  db.close
  
end#test_sqlite



def exec

#  p get_time_label("display")
  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] calling ... => test_sqlite"
  
  
  test_sqlite_2
#  test_sqlite
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done!"
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done"
  
  
end#exec

exec
