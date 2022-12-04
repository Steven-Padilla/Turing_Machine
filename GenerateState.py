import string

blank='blank'
right='right'

x=list(string.ascii_lowercase) +["0","1","2","3","4","5","6","7","8","9"]

result=[]
for i in range(len(x)):
    result.append(['q2',x[i],blank,  'q3',blank,x[i],right,right])
    print(str(result[i])+',')