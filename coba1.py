#jika belum ada install dengan pip install pymatrix
import pymatrix as px
# import numpy as np

#buat list matrix
list = [[1,2,3], [1,2,3], [1,2,3]]
#jadikan list menjadi matrix
matrixku = px.Matrix.from_list(list)
#determinan
buat1 = matrixku.det()
#untuk adjoin
buat2 = matrixku.adjoint()
#untuk tranpose
buat3 = matrixku.trans()
#untuk inverse
buat4 = matrixku.inv()