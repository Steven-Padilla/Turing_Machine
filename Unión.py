import string

blank='blank'
right='right'
left='left'
static='static'
alphabeth=list(string.ascii_lowercase)
same1tape=''
inicialState='q1'
outputTape=[]                     #Creating and filling outPutTape with blanks
for i in range (200):
    outputTape.append(blank)

transitions=[
    #( Firts block )  --->  (     Second block       )    
    ['q1',"{",blank,        'q2',blank,'{',right,right],
    ['q2',alphabeth,blank,  'q3',blank,same1tape,right,right],
    ['q3',',',blank,  'q2',blank,',',right,right],
    ['q3','}',blank,  'q4',blank,'}',right,right],
    
] 

def transportStr(tape):
    aux =[]
    for x in tape:
        aux.append(x)
    return aux
def turing_Union(inputTape):
    inputTape=transportStr(inputTape)
    state=inicialState
    head1=0
    head2=0
    aux=''
    band=False
    # inputTape.insert(0,blank)
    inputTape.append(blank)

    for i in range(len(inputTape)): #Iterating each letter from the input
        aux=inputTape[i]
        for singleT in transitions:
            if singleT[0] == state  and singleT[2]==outputTape[head2]:
                print(len(singleT[1]))
                if len(singleT[1])==1:
                    if singleT[1]==inputTape[head1] :
                        outputTape[head2]=singleT[5]
                        inputTape[head1]=singleT[4]
                        if singleT[6]==right:
                            head1+=1
                        if singleT[6]==left:
                            head1-=1
                        if singleT[7]==right:
                            head2+=1
                        state=singleT[3]
                        band=True
                else:
                    for x in singleT[1]:
                        if x==inputTape[head1]:
                            outputTape[head2]=aux
                            inputTape[head1]=singleT[4]
                            if singleT[6]==right:
                                head1+=1
                            if singleT[6]==left:
                                head1-=1
                            if singleT[7]==right:
                                head2+=1
                            state=singleT[3]
                            band=True
                break
            else:
                print('Sin transición')
                band=False
            if band==False:
                i=10000000




    
turing_Union("{a,b,c,}")
print(outputTape)
