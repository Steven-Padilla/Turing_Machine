import string
import time
blank='blank'
right='right'
left='left'
static='static'
finalState='q5'
inicialState='q0'
listAux=list(string.ascii_lowercase)
result=[]
outputTape=[]       #Creating and filling outPutTape with blanks
inputTape2=[]
for i in range (200):
    inputTape2.append(blank)
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
                result.append(['q1',listAux[i],blank,blank,        'q2','&',listAux[i],listAux[i],right,static,static])
    for x in result:
        transitions.append(x)
    #Creating transitions q2 -> q2 with all the alphabet
    result=[]
    for i in range(26):
        for j in range(26):
            for k in range(26):
                if listAux[i] != listAux[k]: 
                    result.append(['q2',listAux[i],listAux[j],listAux[k],        'q2',listAux[i],listAux[j],listAux[k],right,static,static])
                    
                elif listAux[i] == listAux[k]:
                    result.append(['q2',listAux[i],listAux[j],listAux[k],        'q2','!',listAux[j],listAux[k],right,static,static])
                result.append(['q2',',',listAux[j],listAux[k],        'q2',',',listAux[j],listAux[k],right,static,static]) 
                result.append(['q2','}',listAux[j],listAux[k],        'q3','}',listAux[j],listAux[k],left,static,static])
                result.append(['q2','!',listAux[j],listAux[k],        'q2','!',listAux[j],listAux[k],right,static,static]) 

    for x in result:
        transitions.append(x)

    #Creating transitions q3 -> q3 with all the alphabet
    result=[]
    for i in range(26):
        for j in range(26):
            for k in range(26):
                result.append(['q3','!',listAux[j],listAux[k],        'q3','!',listAux[j],listAux[k],left,static,static])
                result.append(['q3',',',listAux[j],listAux[k],        'q3',',',listAux[j],listAux[k],left,static,static])
                result.append(['q3',listAux[i],listAux[j],listAux[k],        'q3',listAux[i],listAux[j],listAux[k],left,static,static])
                result.append(['q3','&',listAux[j],listAux[k],        'q4','&',listAux[j],listAux[k],right,right,static])
    for x in result:
        transitions.append(x)

    #Creating transitions q4 -> q6 with all the alphabet
    result=[]
    for k in range(26):
        result.append(['q4',',',blank,listAux[k],        'q6',',',',',listAux[k],right,right,right])
        result.append(['q4','}',blank,listAux[k],        'q5','}','}',listAux[k],right,right,right])
    for x in result:
        transitions.append(x)

    #Creating transitions q6 -> q6 with all the alphabet
    result=[]
    for i in range(26):
        for j in range(26):
            result.append(['q6','!',blank,blank,        'q6','!',blank,blank,right,static,static])
            result.append(['q6',',',blank,blank,        'q6',',',blank,blank,right,static,static])
            result.append(['q6',listAux[i],blank,blank,        'q2','&',listAux[i],listAux[i],right,static,static])
            result.append(['q6','}',blank,blank,        'q5','}','}',blank,right,right,right])
            result.append(['q6','}',',',blank,        'q5','}','}',blank,right,right,right])
    for x in result:
        transitions.append(x)


def transportStr(tape):
    aux =[]
    for x in tape:
        aux.append(x)
    return aux

def turing_intersection(inputTape1):
    inputTape1=transportStr(inputTape1)
    state=inicialState
    head1=0
    head2=0
    head3=0
    inputTape1.append(blank)
    inputTape2.append(blank)
    print(str(inputTape1)+'\n'+str(inputTape2) )
    while len(inputTape1) != head1 and len(inputTape2) !=head2: #Iterating each letter from the input
        # for j in range(len(inputTape2)):
            band=False
            for singleT in transitions:
                if singleT[0] == state  and singleT[3]==outputTape[head3] and singleT[1]==inputTape1[head1] and singleT[2]==inputTape2[head2] :
                    inputTape1[head1]=singleT[5]
                    inputTape2[head2]=singleT[6]
                    outputTape[head3]=singleT[7]
                    if singleT[8]==right:
                        head1+=1
                    if singleT[8]==left:
                        head1-=1
                    if singleT[9]==right:
                        head2+=1
                    if singleT[9]==left:
                        head2-=1
                    if singleT[10]==right:
                        head3+=1
                    if singleT[10]==left:
                        head3-=1
                    state=singleT[4]
                    band=True
                    print(f'Estado: {state}')
                    print(f'Cabeza 1: {inputTape1[head1]}')
                    print(f'Cabeza 2: {inputTape2[head2]}')
                    print(f'Cabeza 3: {outputTape[head3]}')
                    # time.sleep(1)


            if(band==False):
                break
    if state==finalState:
        return True
    return False
            

def generatePDF():
    file=open ('Transitions.txt','w')
    for singleT in transitions:
        file.write(str(singleT)+',\n')
    file.close()


def main():

    fillT()
    generatePDF()
    # for x in transitions:
    #     print(str(x)+',')
    x="{a,a,c,c,b,e,c,d}"
    accepted=turing_intersection(x)
    result=''
    for char in inputTape2:
        if char!=blank:
            result+=char
        if char==blank:
            break
    if accepted:
        print (f'String with no duplicated items of {x}: \n {result}')
    else:
        print(f'String NOT Accepted: {result}')
    
main()
