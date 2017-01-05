
require 'sqlite3'

=begin

file:         use_sqlite.rb
created at:   2017/01/05 18:00:48

<Usage>
C:\WORKS_2\WS\WS_Others\JVEMV6\12#\use_sqlite.rb

pushd C:\WORKS_2\WS\WS_Others\JVEMV6\12#
use_sqlite.rb

=end

=begin

sqlite3 C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\Lib\data\ifm11_backup_20160110_080900.bk
SELECT * FROM ifm11 WHERE file_name = '2017-01-05_10-47-41_000.jpg' ;

=end

FPATH = "C:/WORKS_2/WS/WS_Others/prog/D-5/2#"

#ref http://stackoverflow.com/questions/837123/adding-a-directory-to-load-path-ruby
libdir = File.expand_path(File.dirname(FPATH))

$LOAD_PATH.unshift(FPATH) unless $LOAD_PATH.include?(libdir)

require 'utils.20161228_123529'

def test_sqlite
  
  #debug
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] starting ..."
  
  
  fname = "C:/WORKS_2/WS/Eclipse_Luna/Cake_IFM11/app/Lib/data/ifm11_backup_20160110_080900.bk"
  
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

def test_sqlite_2
  
  fname = "C:/WORKS_2/WS/Eclipse_Luna/Cake_IFM11/app/Lib/data/ifm11_backup_20160110_080900.bk"
  
  #ref http://www.ownway.info/Ruby/sqlite3-ruby/about
  db = SQLite3::Database.new(fname)
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] db => opened: #{fname}"
  
  ################################
  #	
  #	db
  #
  ################################
  sql = "UPDATE ifm11 SET tags = '-' WHERE file_name = '2017-01-05_10-47-41_000.jpg';"
#  sql = "SELECT * FROM ifm11 WHERE _id > 18586"
  
  cursor = db.execute(sql)
#  cursor = db.execute("SELECT * FROM ifm11 WHERE _id < 10")
#  cursor = db.execute("SELECT * FROM ifm11 WHERE key1 = ? AND key2 = ?", [key1, key2])
  
  #debug
  p cursor
  
#  cursor.each do |tuple|
#    puts tuple[0]  # value1 の値
#    puts tuple[1]  # value2 の値
#  end
  
  # db を使い MySQL を操作する
  db.close
  
  #debug
  "[#{File.basename(__FILE__)}:#{__LINE__}] db => closed"
  
end#test_sqlite_2

def update_single_record
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] updating..."
  
  ################################
  #	
  #	read file
  #
  ################################
  f = File.open("data.txt", "r")
  
  line = f.readlines
#  line = f.read
  
  ################################
  #	
  #	close file
  #
  ################################
  f.close
  
  ################################
  #	
  #	build sql statement
  #
  ################################
  fname = line[0].split("=")[1]
  tags = line[3].split("=")[1]
  
  p line
  
  #ref http://ref.xaio.jp/ruby/classes/string/percent
  sql = "UPDATE ifm11 SET tags = '%s' WHERE file_name = '%s';" % [tags, fname]
  sql = "UPDATE ifm11 SET tags = '-' WHERE file_name = '2017-01-05_10-47-41_000.jpg';"
#  sql = "UPDATE ifm11 SET tags = \"%s\" WHERE file_name = \"%s\";" % [tags, fname]
#  sql = "UPDATE ifm11 SET tags = %s WHERE file_name = %s;" % tags, fname
#  sql = "UPDATE ifm11 SET tags = %s WHERE file_name = %s;" % tags, fname
  
  #debug
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] sql => #{sql}"

  # execute
  fname = "C:/WORKS_2/WS/Eclipse_Luna/Cake_IFM11/app/Lib/data/ifm11_backup_20160110_080900.bk"
  
  #ref http://www.ownway.info/Ruby/sqlite3-ruby/about
  db = SQLite3::Database.new(fname)

  cursor = db.execute("UPDATE ifm11 SET tags = '?' WHERE file_name = '?';" % [tags, fname])
#  cursor = db.execute(sql)
  
  p cursor  
  
  # close db
  db.close
  
end#update_single_record

def exec

  update_single_record
  
#  test_sqlite_2
#  test_sqlite
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done!"
  
  
end#exec

exec
