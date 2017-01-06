# encoding: utf-8

require 'sqlite3'
require 'csv'

=begin

file:         use_sqlite.rb
created at:   2017/01/05 18:00:48

<Usage>
C:\WORKS_2\WS\WS_Others\JVEMV6\12#\use_sqlite_2.rb

pushd C:\WORKS_2\WS\WS_Others\JVEMV6\12#
use_sqlite_2.rb

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

def generate_entries_file
  
#  puts "[#{File.basename(__FILE__)}:#{__LINE__}] generating..."

  ################################
  # 
  # files list
  #
  ################################
  dpath = "C:/Users/iwabuchiken/data/images/iphone"
  type = "files"
  
  files = get_dir_list(dpath, type, sort = true)

  p files.size  
  p files[0]
  
  ################################
  # 
  # write: csv
  #
  ################################
#  csv_data = CSV.write($FNAME_ENTRIES, headers: true, encoding: 'utf-8', col_sep: "\t")  #=> w.
  
#  CSV.open('test.csv','w', encoding: 'utf-8', col_sep: "\t") do |test|
  #ref http://qiita.com/shizuma/items/7719172eb5e8c29a7d6e
#  p CSV.generate do |csv|  #=> "`generate': no block given"
  result = CSV.generate do |csv|
    
    csv << ["A","B","C"]
    csv << ["milk","coffee","water"]
    
#  CSV.open('test.csv','w') do |test|
#   test << ["A","B","C"]
#   test << ["milk","coffee","water"]
  end
  
  p result
  
  # write file
  f = File.open("abc.csv", 'w')
  
  f.puts(" UTF-8 に変換できなかった場合は")
  
  f.close
  
#  File.open("abc.csv", 'w') do |file|
##  File.open("intro.#{get_time_label("serial")}.csv", 'w') do |file|
##  File.open("intro.csv", 'w') do |file|
#    
#    #debug
#    puts "[#{File.basename(__FILE__)}:#{__LINE__}] file => opened"
#    
#    
#    file.write("このクラスは CSV ファイルやデータに対する完全なインターフェイスを提供します。")
##    file.write(result)
##    file.write(intro_csv)
#    
#  end
  
  #debug
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] write csv => done"
  
  
#  ################################
#  # 
#  # build sql statement
#  #
#  ################################
#  # execute
#  fname_db = $FNAME_DB
#  #  fname_db = "C:/WORKS_2/WS/Eclipse_Luna/Cake_IFM11/app/Lib/data/#ifm11_backup_20160110_080900.bk.for-use"
#  #  fname = "C:/WORKS_2/WS/Eclipse_Luna/Cake_IFM11/app/Lib/data/ifm11_backup_20160110_080900.bk"
#  
#  #ref http://www.ownway.info/Ruby/sqlite3-ruby/about
#  db = SQLite3::Database.new(fname_db)
  
  
end#generate_entries_file

def test_file_io
  
end

def exec

  ################################
  # 
  # validate: parameters
  #
  ################################
#  p ARGV.size
  
  if ARGV.size < 1
    
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] arguments needed"
    
#    show_help
    
    return
    
  end

  ################################
  # 
  # one entry
  #
  ################################
  if ARGV[0] == "f"

#    #test    #=> 
#    puts "[#{File.basename(__FILE__)}:#{__LINE__}] writing a file..."
#        
#    File.open("xyz.csv", 'w') do |file|
#      
#      file.write("出力は以下のような感じ。")
#    #    file.write(intro_csv)
#      
#    end
    
#    generate_entries_file

    dpath = "C:/Users/iwabuchiken/data/images/iphone"
    type_name = "files"
    
    sort = true
    
    files_list = get_dir_list(dpath, type_name, sort)
#    files_list = get_dir_list(dpath, type_name, sort = true)
#    files = get_dir_list(dpath, type_name, sort = true)
#    files = get_dir_list(dpath, type, sort = true)
  
    p files_list.size  
    p files_list[0]
#    p files.size  
#    p files[0]

        
    File.open("abc.#{get_time_label()}.csv", 'w') do |file|
#    File.open("abc.csv", 'w') do |file|
#    File.open("xyz.csv", 'w') do |file|
      
      file.write("出力は以下のような感じ。")
    #    file.write(intro_csv)
      
    end

    #debug
    puts "[#{File.basename(__FILE__)}:#{__LINE__}] write csv => done"

    
    return
    
  end
  
  puts "[#{File.basename(__FILE__)}:#{__LINE__}] done!"
  
  
end#exec

exec
