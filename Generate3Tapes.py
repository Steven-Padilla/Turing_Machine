import string

blank='blank'
right='right'
left='left'
static='static'
listAux=list(string.ascii_lowercase)
result=[]

#Creating transitions q7 -> q7 with all alphabet + ","
result=[]
listAux.append(',')
for i in range(27):
    result.append(['q7',listAux[i],"}",blank,        'q7',listAux[i],'}',listAux[i],right,static,right])
    print(str(result[i])+',')



#Creating transition q8 -> q9 with alphabet and ",","{"
# result=[]
# aux=[',','{']
# listAux.append('{')
# for i in range(2):
#     for j in range(27):
#         result.append(['q8',"}",aux[i],listAux[j],        'q9','}',aux[i],listAux[j],static,static,right])
# for x in result:
#     print(str(x)+',')


#Creating transition q1 -> q7 with all alphabet + }
# result=[]
# listAux.append('}')
# for i in range(27):
#     result.append(['q1','}',listAux[i],blank,        'q7','}',listAux[i],'}',right,static,right])
#     print(str(result[i])+',')
# for i in range(26):
#     result.append(['q1',listAux[i],'}',blank,        'q7',listAux[i],'}',listAux[i],right,static,right])
#     print(str(result[i])+',')
    




#Creating transition q1 -> q6 with all alphabet
# result=[]
# for i in range(26):
#     result.append(['q1','}',listAux[i],blank,        'q6','}',listAux[i],blank,static,left,left])
#     print(str(result[i])+',')




#Creating transition q4 -> q7 with all alphabet
# result=[]
# for i in range(26):
#     result.append(['q4','}',listAux[i],blank,        'q7','}',listAux[i],'}',right,static,right])
#     print(str(result[i])+',')

#Creating transition q4 -> q1 with all alphabet
# for i in range(26):
#     result.append(['q4',',',listAux[i],blank,        'q1',',',listAux[i],',',right,static,right])
#     print(str(result[i])+',')



#Creating transition q3 -> q4 with all alphabet
# for i in range(26):
#     result.append(['q3',listAux[i],'{',blank,        'q4',listAux[i],'{',listAux[i],right,right,right])
#     print(str(result[i])+',')

#Creating transitions q3 -> q3 with all alphabet + comma
# listComma=listAux.copy()
# listComma.append(',')
# for i in range(26):
#     for j in range(27):
#         result.append(['q3',listAux[i],listComma[j],blank,        'q3',listAux[i],listComma[j],blank,static,left,static])

# for x in result:
#     print(str(x)+',')


#Creating transitions q2 -> q3 with all the alphabet
# for i in range(26):
#     result.append(['q2',listAux[i],'}',blank,        'q3',listAux[i],'}',blank,static,left,static])
#     print(str(result[i])+',')


#Creating transitions q2 -> q1 with all the alphabet
# for i in range(26):
#     result.append(['q2',listAux[i],',',blank,        'q1',listAux[i],',',blank,static,right,static])
#     print(str(result[i])+',')


#Creating transicion q1 -> q2 when tape one symbols are diferents
# for i in range(26):
#     for j in range(26):
#         if listAux[i] != listAux[j]: 
#             result.append(['q1',listAux[i],listAux[j],blank,        'q2',listAux[i],listAux[j],blank,static,right,static])
#     for x in result:
#         print(str(x)+',')

#Creating transicion q1 -> q5 when tape one symbols are the same
# for i in range(26):
#     for j in range(26):
#         if listAux[i] == listAux[j]: 
#             result.append(['q1',listAux[i],listAux[j],blank,        'q5',listAux[i],listAux[j],blank,right,left,static])
#     print(str(result[i])+',')


#Creating transitions q5 -> q5 with all the alphabet + comma
# listAux.append(',')
# for i in range(27):
#     result.append(['q5',',',listAux[i],blank,        'q5',',',listAux[i],blank,static,left,static])
#     print(str(result[i])+',')