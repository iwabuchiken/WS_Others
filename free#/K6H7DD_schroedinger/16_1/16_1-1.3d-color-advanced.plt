#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/16_1/16_1-1.3d-color-advanced.plt"
#	
#	2017/04/20 12:04:19
#

############################
#
# includes
#
############################
load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/lib_gnuplot/lib.plt"
load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/lib_gnuplot/cons.plt"


############################
#
# variables
#
############################

############################
#
# operations
#
############################
#ref http://www.gnuplot-cmd.com/plot/replot.html

#set isosamples samples_value

############################
#
# animation: setup
#
############################
if (exist("count") == 0 || count < 0) count = count_init #�ϐ��̏�����

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #�ϐ��̏�����

############################
#
# graph: 1
#
###########################


############################
#
# params setup
#
############################
# �\�ʂ̔}��ϐ��֐�
Fx(u,v)=sin(u)*cos(v)

Fy(u,v)=sin(u)*sin(v)
#Fy(u,v)=cos(u)*cos(v)

Fz(u,v)=cos(u)
#Fz(u,v)=cos(u)**2
#Fz(u,v)=cos(v)
#Fz(u,v)=cos(v)*cos(v)
#Fz(u,v)=cos(u)*cos(u)
#Fz(u,v)=cos(u)*sin(u)
#Fz(u,v)=cos(u)**2
#Fz(u,v)=sin(u)

#Y(u,v)=sqrt(5.0/(4.0*pi))*0.5*(3.0*cos(u)**2-1) # ���ʒ��a�֐�
#Fx(u,v)=sin(u)*cos(v)*abs(Y(u,v))
#Fy(u,v)=sin(u)*sin(v)*abs(Y(u,v))
#z(u,v)=cos(u)*abs(Y(u,v))

# ���̕���
sx=1.0
sy=1.0
sz=1.0

# �����p�̔�����
h=0.000001

# Fx,Fy,Fz��u�����v�ɂ��Δ���
dFxu(u,v)=(Fx(u+h,v)-Fx(u-h,v))/(2.0*h)
dFyu(u,v)=(Fy(u+h,v)-Fy(u-h,v))/(2.0*h)
dFzu(u,v)=(Fz(u+h,v)-Fz(u-h,v))/(2.0*h)
dFxv(u,v)=(Fx(u,v+h)-Fx(u,v-h))/(2.0*h)
dFyv(u,v)=(Fy(u,v+h)-Fy(u,v-h))/(2.0*h)
dFzv(u,v)=(Fz(u,v+h)-Fz(u,v-h))/(2.0*h)

# �@���x�N�g���̊e���� n = lu x lv
nx(u,v)=dFyu(u,v)*dFzv(u,v)-dFyv(u,v)*dFzu(u,v)
ny(u,v)=dFzu(u,v)*dFxv(u,v)-dFzv(u,v)*dFxu(u,v)
nz(u,v)=dFxu(u,v)*dFyv(u,v)-dFxv(u,v)*dFyu(u,v)

# ���̕����x�N�g��s�̒���
s_length=sqrt(sx**2+sy**2+sz**2)
# �@���x�N�g��n�̒���
n_length(u,v)=sqrt(nx(u,v)**2+ny(u,v)**2+nz(u,v)**2)

# ���̕����x�N�g��s�ƕ\�ʂ̖@���x�N�g��n�̓��ςŐF�����߂�
light(u,v)=(n_length(u,v)!=0.0 ? \
           (sx*nx(u,v)+sy*ny(u,v)+sz*nz(u,v))/(s_length*n_length(u,v)) :\
           light(u+h,v+h))


############################
#
# labels, ranges, frame setups
#
############################
##### title
#name = sprintf("16-1-1 Fy(u,v)=cos(u)*cos(v)")
#name = sprintf("16-1-3 Fz(u,v)=sin(u)")
name = sprintf("16-1-3 (%03d) Fz(u,v)=cos(v)", sequence)

set title title_session(name)

##### axis labels
set xlabel "x"
set ylabel "y"

set xrange [0:pi]
set yrange [0:2*pi]
set samples 100
set isosamples 100

# ��������p�����[�^�t�@�C�������
tablefile="table3.dat"
#set table tablefile
#splot 0
#unset table

#set xrange [-1:1]
#set yrange [-1:1]
#set zrange [-1:1]

a = 0.65
a = 1

set xrange [-a:a]
set yrange [-a:a]
set zrange [-a:a]

set pm3d depthorder

#set view 60,30
#set view 30 + sequence, 30
#set view 30, 0 + sequence
view_z = 55
set view view_z, 0 + sequence

# �F�g���̎w��
set palette defined ( 0 "dark-blue" , 1 "cyan")

splot tablefile using (Fx($1,$2)):(Fy($1,$2)):(Fz($1,$2)):(light($1,$2)) \
      with pm3d

############################
#
# save image
#
############################


#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
#set terminal gif

time_label = "20170423_173941"

#set output sprintf("image_%s/16_1-6.%s.%002d.gif", time_label, time_label, sequence)


############################
#
# animation: loop
#
############################
#if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (sequece < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (sequence < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#count = count_init
#sequence = sequence_init


