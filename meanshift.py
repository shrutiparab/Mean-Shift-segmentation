import numpy as np
import cv2
import os
import sys
from numpy import array
import math
from PIL import Image
import PIL
from scipy.misc import imshow
import scipy.misc
import matplotlib

def e_dist(point, matrix):
    sum=0
    for i in range(0,5):
        #print point
        #print matrix
        sum = sum + math.pow(point[i]-matrix[i],2)
        
    return np.sqrt(sum)

os.system('cls')
#myimage = cv2.imread('D:\Gayatri\MS folder\CVIP\Projects\Image_Butterfly.jpg')
myimage = cv2.imread('C:\Projects\CVIP_Project\Image_Butterfly.jpg')

#print (myimage.shape)

#print(myimage)


d = np.shape(myimage)
a= d[0]
b= d[1]

m=0

matrix = np.empty([a*b,5],dtype=int)
#matrix1 = np.empty([a*b,5],dtype=int)
final=np.zeros([a,b,3],dtype=int)
eucledian = np.ones([a*b],dtype=float)
position = np.empty([a*b],dtype=int)


print(matrix.shape)

for x in range(0,a):
    for y in range(0,b):
        matrix[m,0]=myimage[x,y,0]
        matrix[m,1]=myimage[x,y,1]
        matrix[m,2]=myimage[x,y,2]
        matrix[m,3]=x
        matrix[m,4]=y
        m=m+1
       
color=255 
threshold1 = 80
threshold2 = 50
s1=0
s2=0
s3=0
s4=0
s5=0
mean=np.empty([1,5],dtype=float)   

#label=np.zeros([a,b],dtype=float)
#label=label*255
#print(matrix)  
#point = matrix[i*a+j]
point = matrix[0]

flag=1
count=0
color=255
while(count<80):
            matrix1 = np.empty([a*b,5],dtype=int)   
            l=0
            for k in range(0,np.shape(matrix)[0]): 
                eucledian [k] = e_dist(point,matrix[k])                
                if(eucledian[k]<=threshold1):
                    matrix1[l]=matrix[k]
                    position[l]=k
                    l=l+1
                    
             
            s1=0
            s2=0
            s3=0
            s4=0
            s5=0       
            for m in range(0,l):        
               s1=s1+matrix1[m,0]
               s2=s2+matrix1[m,1]
               s3=s3+matrix1[m,2]
               s4=s4+matrix1[m,3]
               s5=s5+matrix1[m,4]
            mean[0,0]=s1/l
            mean[0,1]=s2/l
            mean[0,2]=s3/l
            mean[0,3]=s4/l
            mean[0,4]=s5/l
               
            
            if(e_dist(point,mean[0])<=threshold2):
              for m in range(0,l):
                 final[matrix1[m,3],matrix1[m,4],0]=mean[0,0]      
                 final[matrix1[m,3],matrix1[m,4],1]=mean[0,1]
                 final[matrix1[m,3],matrix1[m,4],2]=mean[0,2]
              
              color=color-100
              for n in range(0,l):
                  matrix = np.delete(matrix,position[n],0)
                  position = position-1
              if(np.shape(matrix)[0]==0):
                  flag=0
                  break
              else:
                  point=matrix[0]
                  print "point"
                  print point
                     
            else:
              point=mean[0]
              
            count=count+1
            
       
cv2.imshow("final",np.uint8(final))
   
        