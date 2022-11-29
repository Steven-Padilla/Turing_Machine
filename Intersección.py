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
    ['q3',',','{',blank,        'q1',',','{',blank,right,right,static],
    ['q4',blank,'{',',',        'q7',blank,'{','}',static,left,right],
    ['q4',blank,'{','{',        'q6',blank,'{','{',static,left,right],
    ['q6',blank,blank,blank,        'q7',blank,blank,'}',static,static,right],
    ['q5',',','{',blank,        'q1',',','{',',',right,right,right],
    ['q8',blank,'}',',',        'q7',blank,'}','}',static,static,right],
    ['q8',blank,'}','{',        'q9',blank,'}','{',static,static,right],
    ['q9',blank,'}',blank,        'q7',blank,'}','}',static,static,right],
] 



def fillT():
    listAux=list(string.ascii_lowercase)

# Creating transicion q1 -> q2 when tape one symbols are diferents
    result=[]
    for i in range(26):
        for j in range(26):
            if listAux[i] != listAux[j]: 
                result.append(['q1',listAux[i],listAux[j],blank,'q2',listAux[i],listAux[j],blank,static,right,static])
    for x in result:
        transitions.append(x)

#Creating transitions q2 -> q1 with all the alphabet
    result=[]
    for i in range(26):
        result.append(['q2',listAux[i],',',blank,'q1',listAux[i],',',blank,static,right,static])
        transitions.append(result[i])
#Creating transitions q2 -> q3 with all the alphabet
    result=[]
    for i in range(26):
        result.append(['q2',listAux[i],'}',blank,        'q3',listAux[i],'}',blank,right,left,static])
        transitions.append(result[i])

#Creating transitions q3 -> q8 with all alphabet
    result=[]
    for j in range(26):
        result.append(['q3','}',listAux[j],blank,        'q8','}',listAux[j],blank,right,right,left])
    for x in result:
        transitions.append(x)


#Creating transitions q3 -> q3 with all alphabet + comma
    result=[]
    listComma=listAux.copy()
    listComma.append(',')
    for j in range(27):
        result.append(['q3',',',listComma[j],blank,        'q3',',',listComma[j],blank,static,left,static])
    for x in result:
        transitions.append(x)

#Creating transitions q1 -> q4 with all alphabet 
    result=[]
    for j in range(26):
        result.append(['q1','}',listAux[j],blank,        'q4','}',listAux[j],blank,right,left,left])
    for x in result:
        transitions.append(x)


#Creating transitions q1 -> q5 with all alphabet 
    result=[]
    for i in range(26):
        for j in range(26):
            if listAux[i] == listAux[j]: 
                result.append(['q1',listAux[i],listAux[j],blank,'q5',listAux[i],listAux[j],listAux[i],right,left,right])
    for x in result:
        transitions.append(x)


#Creating transition q5 -> q5 with all alphabeth + comma
    result=[]
    listComma=listAux.copy()
    listComma.append(',')
    for j in range(27):
        result.append(['q5',',',listComma[j],blank,        'q5',',',listComma[j],blank,static,left,static])
    for x in result:
        transitions.append(x)

#Creating transitions q5 -> q7 with all alphabet 
    result=[]
    listCor=listAux.copy()
    listCor.append('{')
    listCor.append(',')
    for j in range(28):
        result.append(['q5','}',listCor[j],blank,        'q7','}',listCor[j],'}',right,static,right])
    for x in result:
        transitions.append(x)

# #Creating transitions q1 -> q7 with all alphabet 
    result=[]
    listComma=listAux.copy()
    listComma.append('}')
    for j in range(27):
        result.append(['q1',listComma[j],'}',blank,        'q7',listComma[j],'}','}',static,right,right])
    for x in result:
        transitions.append(x)


def transportStr(tape):
    aux =[]
    for x in tape:
        aux.append(x)
    return aux



def turing_intersection(inputTape1,inputTape2):
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
    x="{a,c,f,g,v,a}"
    y="{a,t,s,k,v}"
    accepted=turing_intersection(x,y) #Write here your input {}#{}
    result=''
    for char in outputTape:
        if char!=blank:
            result+=char
        if char==blank:
            break
    if accepted:
        print (f'Intersection of {x} with {y}: \n {result}')
    else:
        print(f'String NOT Accepted: {result}')
    
main()
