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
