if (exist("n")==0 || n<0) n=0 #�ϐ��̏�����

DATA = "tree.data"
set print DATA
set angle degree
ratio = 0.7
dang  = 15
min_len = n<=max_n/2 ? ratio**n : ratio**(max_n-n)

#call "tree_sub2.plt" "0" "0" "90" "1"  

title(n) =   n<=max_n/2 ? sprintf("n = %d",n) : sprintf("n = %d", max_n-n)  #�^�C�g����
unset label 
set label title(n)  font 'Times,20'  at -1.4 , 3.3
plot DATA with line linecolor rgbcolor "blue"

if (n<max_n)  n=n+1; reread