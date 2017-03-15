
#列表
#a_input=int(input("please give me a number"))
#if a_input==1:
 #   print("this input number is : say 1")
#elif a_input==2:
   #  print("this input number is : say 2")
#else:
  #  print("good luck")

#a_tuple=(1,2,3,4)
#a_list=[1,2,32,4]
#for index in  range(len(a_list)):
    #print('index=',index,'number in list:',a_list[index])


#// list
#a=[1,2,3,4,5,6,2,9,45]
#a.append(9)
#a.insert(1,8)
##a.remove(9)
#print(a[3:5])
#print (a.index(2))
#a.sort(reverse=True)
#print(a)

#多維 
#a=[1,2,3,4,5]
#multi=[[1,2,3],[2,3,4],[3,4,5]]
#print(multi[1][2])

#a=[1,2,3,4,5]
#d={'apple':[1,2,3],'pear':{1:3,3:'a'}, 'orange':3}
#d2={1:'a','c':'b'}
#print(d['apple'])
#print(a[1])

##del d['pear']  ##delete pear

#print(d['pear'][3])


#from time import time,localtime
#from time import *
#print(localtime())
#print(time())
#print(gettime())
#print(t.localtime())
#t.time()

##爬蟲
#from urllib3.request import urlopen

#f =urllib3.urlopen('http://www.so.com/').read()

#print(f)


#------ break ,continue
#a=True
#while a:
#while True:
 #   b=input('type something')
  #  if b=='1':
   #     continue #break #a=False
    #else:
     #   pass
   # print('still run')
#print("finish run")

#----try catch
#try:
#    file=open('tree','r')
#except Exception as e:
#    print('there is no file name as it')
#    response=input('do u want to create it')
#    if response=='y':
#        file=open('eee','w')
#    else:
 #       pass
#else:
 #   file.read('ssss',r)
  #  file.close()
#def fun1(x,y):
#    return(x+y)
#------import copy
#a=[1,2,3]
#b=a
#id(a)
#-----copy.copy()

import pickle
d={'da':11,2:[23,1,5],'23':{1:2,'d':'sad'}}
'''
file=open('pickle_example.pickle','wb')
pickle.dump(d,file)
file.close()

'''
with open('pickle_example.pickle','rb') as file:
#file=open('pickle_example.pickle','rb')
    d1=pickle.load(file)
#file.close()
print(d1)

