
# coding: utf-8

# In[180]:



#Description : 
#Perceptron learning algorithm 

from numpy import *
import matplotlib.pyplot as plt
def naive_pla(datas,label):
    w=np.array([1,8])# Assume a w with vector (1,1)
    iteration=0
    while True:
        iteration+=1
        false=0
        k=0
        # find the wrong points
        for i in datas:
            predict=dot(w,i)#predcit = x*w1+y*w2, i is a vector point to the origin
            if sign(label[k])!=sign(predict):
                error=label[k]
                false+=1
                w=w+error*i
            k+=1
        print 'iteration %d  false point %d W:%s'% (iteration,false,w)
        if false==0:#If there is no false point
            break
    return w
        
dataset=[]
datachar=[]
#Load dataset
f=open('dataset.txt')
#Seperate the file into lines with the type list of each one
for line in f:
    line=line.split('\t')
    # Turn str into float
    for i in range(len(line)):
        line[i]=float(line[i])
    #Save the position to dataset and save the characteristic to datachar
    dataset.append(line[0:2])
    datachar.append(float(line[-1]))

f.close()
# save the data in an array
data=np.array(dataset)
char=np.array(datachar)
final=naive_pla(data,char)

#draw the scatter plot
i_pos=np.where(char==1)
i_neg=np.where(char==-1)
data_p=data[i_pos]#data_p and data_n are array type
data_n=data[i_neg]
#red point is for positive and blue for negative
plt.plot(data_p[:,0],data_p[:,1],'or')
plt.plot(data_n[:,0],data_n[:,1],'ob')
x1 = np.arange(0, 6, 0.1)  
x2 = (final[0] * x1 ) / (-final[1]) 
plt.plot(x1,x2)
plt.show()

