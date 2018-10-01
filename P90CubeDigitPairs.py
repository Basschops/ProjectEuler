import itertools


cubeA = set()
cubeB=set()

squares = [[0,1],[0,4],[0,'a'],[1,'a'],[2,5],[3,'a'],['a',4],[8,1]]
#squares = [[0,1],[0,4],[0,9],[1,6],[2,5],[3,6],[4,9],[6,4],[8,1]]
#Seperate case for 09s?
# 7 IS NOT USED
# 6 can be used as 9
# in stead of either 6 or 9, placed 7
# 49 and 64 are essentially the same
available = {0,1,2,3,4,5,6,7,8,9}

# 2 sets that need to cover the numbers above.
# But the pairs given above should not be in the same dice
'''
0-3
1-3
2-1
3-1
4-3
5-1
7-5  (6-3 9-2)
8-1
'''

a = itertools.combinations(available, 6)

li = []
li2=[]
for s in a:
    li.append(list(s))
    li2.append(list(s))
print(len(li))
test = False
count = 0
for i in li:
    for j in li2:
        #print('next')
        sqs = 0
        test=False
        for k in squares:
            if 6 in i:
                i[i.index(6)]='a'
            if 9 in i:
                i[i.index(9)]='a'
            if 6 in j:
                j[j.index(6)]='a'
            if 9 in j:
                j[j.index(9)]='a'
                
            if (k[0] in i and k[1] in j) or (k[1] in i and k[0] in j):
                test=True
                sqs+=1
               
            else:
                test = False
                break
        #print(sqs)
        if test:
            count+=1
print(count)
            
    
