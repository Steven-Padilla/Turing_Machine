import string

blank='blank'
right='right'

x=list(string.ascii_lowercase)

result=[]
for i in range(26):
    result.append(['q6',x[i],blank,  'q7',blank,x[i],right,right])
    print(str(result[i])+',')