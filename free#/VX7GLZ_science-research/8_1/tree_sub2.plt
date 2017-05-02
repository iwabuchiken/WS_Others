print $0, $1   #=> 'column() called from invalid context'
#print ($0), ($1)   #=> 'column() called from invalid context'

print $0 + $3*cos($2), $1 + $3*sin($2)
print "\n"

if(min_len < $3) call "tree_sub2.plt" \
  "$0 + $3*cos($2)" "$1 + $3*sin($2)" "$2+dang" "ratio*$3"
if(min_len < $3) call "tree_sub2.plt" \
  "$0 + $3*cos($2)" "$1 + $3*sin($2)" "$2-dang" "ratio*$3"
