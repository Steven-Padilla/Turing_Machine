import string

blank='blank'
right='right'
left='left'
static='static'
finalState='q8'
alphabeth=list(string.ascii_lowercase)
inicialState='q1'
outputTape=[]                     #Creating and filling outPutTape with blanks
for i in range (200):
    outputTape.append(blank)

transitions=[
    #( Firts block )  --->  (     Second block       )    
    ['q1',"{",blank,        'q2',blank,'{',right,right],
    ['q2', 'a', 'blank', 'q3', 'blank', 'a', 'right', 'right'],
    ['q2', 'b', 'blank', 'q3', 'blank', 'b', 'right', 'right'],
    ['q2', 'c', 'blank', 'q3', 'blank', 'c', 'right', 'right'],
    ['q2', 'd', 'blank', 'q3', 'blank', 'd', 'right', 'right'],
    ['q2', 'e', 'blank', 'q3', 'blank', 'e', 'right', 'right'],
    ['q2', 'f', 'blank', 'q3', 'blank', 'f', 'right', 'right'],
    ['q2', 'g', 'blank', 'q3', 'blank', 'g', 'right', 'right'],
    ['q2', 'h', 'blank', 'q3', 'blank', 'h', 'right', 'right'],
    ['q2', 'i', 'blank', 'q3', 'blank', 'i', 'right', 'right'],
    ['q2', 'j', 'blank', 'q3', 'blank', 'j', 'right', 'right'],
    ['q2', 'k', 'blank', 'q3', 'blank', 'k', 'right', 'right'],
    ['q2', 'l', 'blank', 'q3', 'blank', 'l', 'right', 'right'],
    ['q2', 'm', 'blank', 'q3', 'blank', 'm', 'right', 'right'],
    ['q2', 'n', 'blank', 'q3', 'blank', 'n', 'right', 'right'],
    ['q2', 'o', 'blank', 'q3', 'blank', 'o', 'right', 'right'],
    ['q2', 'p', 'blank', 'q3', 'blank', 'p', 'right', 'right'],
    ['q2', 'q', 'blank', 'q3', 'blank', 'q', 'right', 'right'],
    ['q2', 'r', 'blank', 'q3', 'blank', 'r', 'right', 'right'],
    ['q2', 's', 'blank', 'q3', 'blank', 's', 'right', 'right'],
    ['q2', 't', 'blank', 'q3', 'blank', 't', 'right', 'right'],
    ['q2', 'u', 'blank', 'q3', 'blank', 'u', 'right', 'right'],
    ['q2', 'v', 'blank', 'q3', 'blank', 'v', 'right', 'right'],
    ['q2', 'w', 'blank', 'q3', 'blank', 'w', 'right', 'right'],
    ['q2', 'x', 'blank', 'q3', 'blank', 'x', 'right', 'right'],
    ['q2', 'y', 'blank', 'q3', 'blank', 'y', 'right', 'right'],
    ['q2', 'z', 'blank', 'q3', 'blank', 'z', 'right', 'right'],
    ['q3',',',blank,  'q2',blank,',',right,right],
    ['q3','}',blank,  'q4',blank,',',right,right],
    ['q2','}',blank,  'q4',blank,',',right,right],
    ['q4','#',blank,  'q5',blank,blank,right,static],
    ['q5','{',blank,  'q6',blank,blank,right,static],
    ['q6', 'a', 'blank', 'q7', 'blank', 'a', 'right', 'right'],
    ['q6', 'b', 'blank', 'q7', 'blank', 'b', 'right', 'right'],
    ['q6', 'c', 'blank', 'q7', 'blank', 'c', 'right', 'right'],
    ['q6', 'd', 'blank', 'q7', 'blank', 'd', 'right', 'right'],
    ['q6', 'e', 'blank', 'q7', 'blank', 'e', 'right', 'right'],
    ['q6', 'f', 'blank', 'q7', 'blank', 'f', 'right', 'right'],
    ['q6', 'g', 'blank', 'q7', 'blank', 'g', 'right', 'right'],
    ['q6', 'h', 'blank', 'q7', 'blank', 'h', 'right', 'right'],
    ['q6', 'i', 'blank', 'q7', 'blank', 'i', 'right', 'right'],
    ['q6', 'j', 'blank', 'q7', 'blank', 'j', 'right', 'right'],
    ['q6', 'k', 'blank', 'q7', 'blank', 'k', 'right', 'right'],
    ['q6', 'l', 'blank', 'q7', 'blank', 'l', 'right', 'right'],
    ['q6', 'm', 'blank', 'q7', 'blank', 'm', 'right', 'right'],
    ['q6', 'n', 'blank', 'q7', 'blank', 'n', 'right', 'right'],
    ['q6', 'o', 'blank', 'q7', 'blank', 'o', 'right', 'right'],
    ['q6', 'p', 'blank', 'q7', 'blank', 'p', 'right', 'right'],
    ['q6', 'q', 'blank', 'q7', 'blank', 'q', 'right', 'right'],
    ['q6', 'r', 'blank', 'q7', 'blank', 'r', 'right', 'right'],
    ['q6', 's', 'blank', 'q7', 'blank', 's', 'right', 'right'],
    ['q6', 't', 'blank', 'q7', 'blank', 't', 'right', 'right'],
    ['q6', 'u', 'blank', 'q7', 'blank', 'u', 'right', 'right'],
    ['q6', 'v', 'blank', 'q7', 'blank', 'v', 'right', 'right'],
    ['q6', 'w', 'blank', 'q7', 'blank', 'w', 'right', 'right'],
    ['q6', 'x', 'blank', 'q7', 'blank', 'x', 'right', 'right'],
    ['q6', 'y', 'blank', 'q7', 'blank', 'y', 'right', 'right'],
    ['q6', 'z', 'blank', 'q7', 'blank', 'z', 'right', 'right'],
    ['q7',',',blank,  'q6',blank,',',right,right],
    ['q6','}',blank,  'q9',blank,blank,right,left],
    ['q9',blank,',',  'q8',blank,'}',static,right],
    ['q7','}',blank,  'q8',blank,'}',right,right],
    
    
        
] 

def transportStr(tape):
    aux =[]
    for x in tape:
        aux.append(x)
    return aux
def turingMachine(inputTape):
    inputTape=transportStr(inputTape)
    state=inicialState
    head1=0
    head2=0
    inputTape.append(blank)

    for i in range(len(inputTape)): #Iterating each letter from the input
        band=False
        for singleT in transitions:
            if singleT[0] == state  and singleT[2]==outputTape[head2] and singleT[1]==inputTape[head1]:
                outputTape[head2]=singleT[5]
                inputTape[head1]=singleT[4]
                if singleT[6]==right:
                    head1+=1
                if singleT[6]==left:
                    head1-=1
                if singleT[7]==right:
                    head2+=1
                if singleT[7]==left:
                    head2-=1
                state=singleT[3]
                band=True
                
        if(band==False):
            break
    if state==finalState:
        return True
    return False
            




    
accepted=turingMachine("{a}#{z,x,y,a}") #Write here your input {}#{}
result=''
for char in outputTape:
    if char!=blank:
        result+=char
    if char==blank:
        break
if accepted:
    print (f'Turing Machine is done: \n {result}')
else:
    print(f'String not Accepted')