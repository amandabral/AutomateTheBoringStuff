#Defining basic lists

list=['1','2','4','8']
print (list)

#Defining lists of other types
biglist=[['abc','def','ghi'],[0.1,0.2,0.3],[1,0.1,'abc']]

for list in biglist:
    for ele in list:
        print (ele,end='')
        print (', ',end='')
    print ('\n')

#Using + operator to add elements to the list
list=['a']
list+='b'
print (list)

#Using * operator to add copies of current contents of array to it
list=[2]
list*=4
print (list)
