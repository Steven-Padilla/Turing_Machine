import string

blank='blank'
right='right'
left='left'
static='static'
finalState='q7'
alphabeth=list(string.ascii_lowercase)
inicialState='q0'
outputTape=[]                     #Creating and filling outPutTape with blanks
for i in range (200):
    outputTape.append(blank)




transitions=[
    #( Firts block )  --->  (     Second block       )    
    ['q0','{','{',blank,        'q1','{','{','{',right,right,right],
    ['q5',  ','  ,  '{'  ,blank,        'q1',  ','  , '{' ,blank,right,right,static],
    ['q6',  '}'  ,  '{'  ,',',        'q7',  '}'  , '{' ,'}',right,static,right],
    ['q5',  '}'  ,  '{'  ,blank,        'q8',  '}'  , '{' ,blank,static,static,left],
    ['q5',  '}'  ,  ','  ,blank,        'q8',  '}'  , ',' ,blank,static,static,left],
    ['q8',  '}'  ,  '{'  ,',',        'q7',  '}'  , '{' ,'}',static,static,static],
    ['q8',  '}'  ,  ','  ,',',        'q7',  '}'  , ',' ,'}',static,static,static],
    ['q9',  '}'  ,  '{'  ,blank,        'q7',  '}'  , '{' ,'}',static,static,static],
    ['q9',  '}'  ,  ','  ,blank,        'q7',  '}'  , ',' ,'}',static,static,static],
    ['q10',  '}'  , '}'   ,blank,        'q7',  '}'  , '}' ,'}',right,static,right],
    
] 



def fillT():
    listAux=list(string.ascii_lowercase)
    result=[]


#Creating transitions q10 -> q10 with all alphabet + ","
    result=[]
    listComma=listAux.copy()
    listComma.append(',')
    for i in range(27):
        result.append(['q10',listComma[i],"}",blank,        'q10',listComma[i],'}',listComma[i],right,static,right])
        transitions.append(result[i])


#Creating transition q8 -> q9 with alphabet and ",","{"
    result=[]
    aux=[',','{']
    listCor= listAux.copy()
    listCor.append('{')
    for i in range(2):
        for j in range(27):
            result.append(['q8',"}",aux[i],listCor[j],        'q9','}',aux[i],listCor[j],static,static,right])
    for x in result:
        transitions.append(x)


#Creating transition q1 -> q7 with all alphabet + }
    result=[]
    listCor=listAux.copy()
    listCor.append('}')
    for i in range(27):
        result.append(['q1','}',listCor[i],blank,        'q7','}',listCor[i],'}',right,static,right])
        transitions.append(result[i])


#Creating q1 -> q10
    result=[]
    for i in range(26):
        result.append(['q1',listAux[i],'}',blank,        'q10',listAux[i],'}',listAux[i],right,static,right])
        transitions.append(result[i])
        

    
#Creating transition q1 -> q6 with all alphabet
    result=[]
    for i in range(26):
        result.append(['q1','}',listAux[i],blank,        'q6','}',listAux[i],blank,static,left,left])
        transitions.append(result[i])




#Creating transition q4 -> q7 with all alphabet
    result=[]
    for i in range(26):
        result.append(['q4','}',listAux[i],blank,        'q7','}',listAux[i],'}',right,static,right])
        transitions.append(result[i])



#Creating transition q4 -> q1 with all alphabet
    result=[]
    for i in range(26):
        result.append(['q4',',',listAux[i],blank,        'q1',',',listAux[i],',',right,static,right])
        transitions.append(result[i])


#Creating transition q3 -> q4 with all alphabet
    result=[]
    for i in range(26):
        result.append(['q3',listAux[i],'{',blank,        'q4',listAux[i],'{',listAux[i],right,right,right])
        transitions.append(result[i])

#Creating transitions q3 -> q3 with all alphabet + comma
    result=[]
    listComma=listAux.copy()
    listComma.append(',')
    for i in range(26):
        for j in range(27):
            result.append(['q3',listAux[i],listComma[j],blank,        'q3',listAux[i],listComma[j],blank,static,left,static])
    for x in result:
        transitions.append(x)


#Creating transitions q2 -> q3 with all the alphabet
    result=[]
    for i in range(26):
        result.append(['q2',listAux[i],'}',blank,        'q3',listAux[i],'}',blank,static,left,static])
        transitions.append(result[i])

#Creating transitions q2 -> q1 with all the alphabet
    result=[]
    for i in range(26):
        result.append(['q2',listAux[i],',',blank,        'q1',listAux[i],',',blank,static,right,static])
        transitions.append(result[i])

#Creating transicion q1 -> q2 when tape one symbols are diferents
    result=[]
    for i in range(26):
        for j in range(26):
            if listAux[i] != listAux[j]: 
                result.append(['q1',listAux[i],listAux[j],blank,'q2',listAux[i],listAux[j],blank,static,right,static])
    for x in result:
        transitions.append(x)

#Creating transicion q1 -> q5 when tape one symbols are the same
    result=[]
    for i in range(26):
        for j in range(26):
            if listAux[i] == listAux[j]: 
                result.append(['q1',listAux[i],listAux[j],blank,'q5',listAux[i],listAux[j],blank,right,left,static])
        transitions.append(result[i])
        # print(str(result[i])+',')


#Creating transitions q5 -> q5 with all the alphabet + comma
    result=[]
    listAux.append(',')
    for i in range(27):
        result.append(['q5',',',listAux[i],blank,'q5',',',listAux[i],blank,static,left,static])
        transitions.append(result[i])


def transportStr(tape):
    aux =[]
    for x in tape:
        aux.append(x)
    return aux



def turingMachine(inputTape1,inputTape2):
    inputTape1=transportStr(inputTape1)
    inputTape2=transportStr(inputTape2)
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
    accepted=turingMachine("{a}","{}") #Write here your input {}#{}
    result=''
    for char in outputTape:
        if char!=blank:
            result+=char
        if char==blank:
            break
    if accepted:
        print (f'Turing Machine is done: \n {result}')
    else:
        print(f'String NOT Accepted: {result}')
    
main()
