'''
pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\26_Paraview\2_
python 2_1.py



'''
import os
import sys

sys.path.append('.')
sys.path.append('..')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm/libs_mm')

sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')

sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')  # libs
from libs import libs

# from libs_mm import cons_mm

def build_VTK_File():
    
    fname_In = "data/paradata.%s.vtk" % (libs.get_TimeLabel_Now())
    
    fout = open(fname_In, "w")
    
    grid = 10
    dim = grid*2+1
    points = dim**3
    r = 0.8
    
    fout.write("# vtk DataFile Version 1.0\n")
    fout.write("test\n")
    fout.write("ASCII\n")
    fout.write("DATASET STRUCTURED_POINTS\n")
    
    #ref sprintf https://blog.udemy.com/ruby-sprintf/
    fout.write( "DIMENSIONS %d %d %d\n" % (dim, dim, dim))
#     fout.write( sprintf("DIMENSIONS %d %d %d\n",dim, dim, dim))
    fout.write("ORIGIN 0.0 0.0 0.0\n")
    fout.write("ASPECT_RATIO 1.0 1.0 1.0\n")
    
    fout.write("\n")
    
    fout.write( "POINT_DATA %s\n" % (points))
    fout.write("SCALARS scalars float\n")
    fout.write("LOOKUP_TABLE default\n")

    '''###################
        data        
    ###################'''
    for ix in range(-grid, grid + 1) :
        
        for iy in range(-grid, grid + 1) :
            
            for iz in range(-grid, grid + 1) :

                x = ix * 1.0 / grid
                y = iy * 1.0 / grid
                z = iz * 1.0 / grid
#                 x = ix.to_f/grid
#                 y = iy.to_f/grid
#                 z = iz.to_f/grid
                v = r*r - (x*x + y*y + z*z)

                if v < 0: 
                    
                    v = 0
                
                    fout.write("%d\n" % (v))
                else:
                    
                    fout.write("%.7f\n" % (v))
                

    
    fout.close()
    
#/def build_VTK_File():

def execute():

    build_VTK_File()

    print()

    print("[%s:%d] done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    return 1
    
#/def execute():


execute()
