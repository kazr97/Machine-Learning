#!/usr/bin/env python
# coding: utf-8

# In[19]:


from numpy import *
import operator

def createDateSet():#构造数据集
    group=array([[1.0,1.1],[1.0,1.0],[0.9,0.8],[1.1,0.9],[1.0,1.2],[1.3,0.9],[0.0,0.0],[0.0,0.1],[0.1,0.1],[-0.1,0.0],[0.2,0.1]])
    labels=['A','A','A','A','A','A','B','B','B','B','B']
    return group,labels

def classify(inX,dataSet,labels,k):#预测数据，数据集，数据标签，k值
    #print(dataSet)
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet#tile函数，tile(A,B)为重复A元素B次，B为元组时为行与列
    print(diffMat)#将inX拉长为dataSet的长度并减去dataSet,即x1-x2,y1-y2
    
    sqSiffMat=diffMat ** 2
    #print(sqSiffMat)#将差平方
    
    sqDistances=sqSiffMat.sum(axis=1)
    #print(sqDistances)#平方后求和
    
    distances=sqDistances ** 0.5#开根号
    sortedDistIndicies=distances.argsort()#从小到大
    print(sortedDistIndicies)
    
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]#拿到标签
        classCount[voteIlabel]=classCount.get(voteIlabel,0) + 1#该标签次数+1
        
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)#reverse从大到小，key为排序依据
    return sortedClassCount[0][0]

def simpletest():
    dataSet,labels=createDateSet()
    print(classify([1,0.9],dataSet,labels,2))
    print(classify([0.2,0.3],dataSet,labels,3))

     


# In[ ]:




