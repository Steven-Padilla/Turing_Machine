import string

blank='blank'
right='right'
left='left'
static='static'
listAux=list(string.ascii_lowercase)
result=[]
outputTape=[]

for i in range (200):
    outputTape.append(blank)

transitions=[
    #( First block )  --->  (     Second block       )    
    ['q0','{',blank,blank,        'q1','{','{',blank,right,right,right],
]
#Creating transitions q7 -> q7 with all alphabet + ","
result=[]
listAux.append(',')
# for i in range(27):
#     result.append(['q7',listAux[i],"}",blank,        'q7',listAux[i],'}',listAux[i],right,static,right])
#     print(str(result[i])+',')
def fillT():
    #creating transitions q1 -> q2 with all alphabet
    result=[]
    for i in range(26):
        for j in range(26):
            for k in range(26):
                result.append(['q1',listAux[i],listAux[j],listAux[k],        'q2','&',listAux[j],listAux[k],right,static,static])
    for x in result:
        transitions.append(x)
    print(str (result[i])+',')
    #Creating transitions q2 -> q2 with all the alphabet
    result=[]
    for i in range(26):
        for j in range(26):
            for k in range(26):
                if listAux[i] != listAux[k]: 
                    result.append(['q2',listAux[i],listAux[j],listAux[k],        'q2',listAux[i],listAux[j],listAux[k],right,static,static])
                    
    for x in result:
        transitions.append(x)
    

def main():
    fillT()
    print(transitions)
            
