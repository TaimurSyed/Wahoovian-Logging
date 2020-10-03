# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 08:24:54 2020

@author: SyedT


*****************************************
Our program begins!
*****************************************
[[11  1]
 [ 8  0]]
*****************************************
Beginning our matrix operations!
*****************************************
[[0. 1. 2.]
 [3. 4. 5.]
 [6. 7. 8.]]

The operation takes a square matrix as its input, and returns a square matrix with the same dimensions.
The output matrix will be the transpose of the input matrix, but with every value in the matrix negated.

The function you write to implement this will be named wahoovian(), and it will take one input parameter, a matrix using the appropriate data type defined by your 3rd party matrix library. It will return a matrix object with values as described above.
If the input matrix is not square, the function will return the input matrix unchanged. If the input matrix has zero rows and columns, the the function will return the input matrix unchanged.
"""

import numpy as np
import logging

def wahoovian(matrix) :
    
    logging.info("Entering function")
    
 #0 rows and 0 columns
    if np.shape(matrix)[0]==0 and np.shape(matrix)[1]==0:
        logging.info("Exiting function")
        return matrix
    if np.shape(matrix)[0] != np.shape(matrix)[1]: # not square
        logging.warning("Not a square")
        logging.info("Exiting function")
        return matrix
    else:
        matrix = np.negative(matrix)
        matrix =  np.transpose(matrix)
        logging.info("Exiting function")
        return matrix

    
    

       

