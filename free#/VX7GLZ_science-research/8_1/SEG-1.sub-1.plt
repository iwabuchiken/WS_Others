#pause 0 "p0=$0 p1=$1 p2=$2"   #=> n.w.
#pause 0 "p0=@ARG0 p1=@ARG1 p2=@ARG2"   #=> n.w. "p0=@ARG0 p1=@ARG1 p2=@ARG2"
#pause 0 "p0=ARG0 p1=ARG1 p2=ARG2"
#ARG0   #=> invalid command
#@ARG0   #=> invalid command
pause 0 "p0=$0"
