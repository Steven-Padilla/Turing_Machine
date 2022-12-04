import string

class Diferencia():
    def __init__(self):
        
        self.blank='blank'
        self.right='right'
        self.left='left'
        self.static='static'
        self.finalState='q7'
        self.inicialState='q0'
        self.outputTape=[]                     #Creating and filling outPutTape with blanks
        for i in range (200):
            self.outputTape.append(self.blank)
        self.transitions=[
        #( Firts block )  --->  (     Second block       )    
        ['q0','{','{',self.blank,        'q1','{','{','{',self.right,self.right,self.right],
        ['q5',  ','  ,  '{'  ,self.blank,        'q1',  ','  , '{' ,self.blank,self.right,self.right,self.static],
        ['q6',  '}'  ,  '{'  ,',',        'q7',  '}'  , '{' ,'}',self.right,self.static,self.right],
        ['q5',  '}'  ,  '{'  ,self.blank,        'q8',  '}'  , '{' ,self.blank,self.static,self.static,self.left],
        ['q5',  '}'  ,  ','  ,self.blank,        'q8',  '}'  , ',' ,self.blank,self.static,self.static,self.left],
        ['q8',  '}'  ,  '{'  ,',',        'q7',  '}'  , '{' ,'}',self.static,self.static,self.static],
        ['q8',  '}'  ,  ','  ,',',        'q7',  '}'  , ',' ,'}',self.static,self.static,self.static],
        ['q9',  '}'  ,  '{'  ,self.blank,        'q7',  '}'  , '{' ,'}',self.static,self.static,self.static],
        ['q9',  '}'  ,  ','  ,self.blank,        'q7',  '}'  , ',' ,'}',self.static,self.static,self.static],
        ['q10',  '}'  , '}'   ,self.blank,        'q7',  '}'  , '}' ,'}',self.right,self.static,self.right],
    ] 



    def fillT(self):
        listAux=list(string.ascii_lowercase) + ["0","1","2","3","4","5","6","7","8","9"]
        result=[]
        
    #Creating transitions q10 -> q10 with all alphabet + ","
        result=[]
        listComma=listAux.copy()
        listComma.append(',')
        for i in range(len(listComma)):
            result.append(['q10',listComma[i],"}",self.blank,        'q10',listComma[i],'}',listComma[i],self.right,self.static,self.right])
            self.transitions.append(result[i])

    #Creating transition q8 -> q9 with alphabet and ",","{"
        result=[]
        aux=[',','{']
        listCor= listAux.copy()
        listCor.append('{')
        for i in range(len(aux)):
            for j in range(len(listCor)):
                result.append(['q8',"}",aux[i],listCor[j],        'q9','}',aux[i],listCor[j],self.static,self.static,self.right])
        for x in result:
            self.transitions.append(x)


    #Creating transition q1 -> q7 with all alphabet + }
        result=[]
        listCor=listAux.copy()
        listCor.append('}')
        for i in range(len(listCor)):
            result.append(['q1','}',listCor[i],self.blank,        'q7','}',listCor[i],'}',self.right,self.static,self.right])
            self.transitions.append(result[i])


    #Creating q1 -> q10
        result=[]
        for i in range(len(listAux)):
            result.append(['q1',listAux[i],'}',self.blank,        'q10',listAux[i],'}',listAux[i],self.right,self.static,self.right])
            self.transitions.append(result[i])



    #Creating transition q1 -> q6 with all alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q1','}',listAux[i],self.blank,        'q6','}',listAux[i],self.blank,self.static,self.left,self.left])
            self.transitions.append(result[i])




    #Creating transition q4 -> q7 with all alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q4','}',listAux[i],self.blank,        'q7','}',listAux[i],'}',self.right,self.static,self.right])
            self.transitions.append(result[i])



    #Creating transition q4 -> q1 with all alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q4',',',listAux[i],self.blank,        'q1',',',listAux[i],',',self.right,self.static,self.right])
            self.transitions.append(result[i])


    #Creating transition q3 -> q4 with all alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q3',listAux[i],'{',self.blank,        'q4',listAux[i],'{',listAux[i],self.right,self.right,self.right])
            self.transitions.append(result[i])

    #Creating transitions q3 -> q3 with all alphabet + comma
        result=[]
        listComma=listAux.copy()
        listComma.append(',')
        for i in range(len(listAux)):
            for j in range(len(listComma)):
                result.append(['q3',listAux[i],listComma[j],self.blank,        'q3',listAux[i],listComma[j],self.blank,self.static,self.left,self.static])
        for x in result:
            self.transitions.append(x)


    #Creating transitions q2 -> q3 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q2',listAux[i],'}',self.blank,        'q3',listAux[i],'}',self.blank,self.static,self.left,self.static])
            self.transitions.append(result[i])

    #Creating transitions q2 -> q1 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q2',listAux[i],',',self.blank,        'q1',listAux[i],',',self.blank,self.static,self.right,self.static])
            self.transitions.append(result[i])

    #Creating transicion q1 -> q2 when tape one symbols are diferents
        result=[]
        for i in range(len(listAux)):
            for j in range(len(listAux)):
                if listAux[i] != listAux[j]: 
                    result.append(['q1',listAux[i],listAux[j],self.blank,'q2',listAux[i],listAux[j],self.blank,self.static,self.right,self.static])
        for x in result:
            self.transitions.append(x)

    #Creating transicion q1 -> q5 when tape one symbols are the same
        result=[]
        for i in range(len(listAux)):
            for j in range(len(listAux)):
                if listAux[i] == listAux[j]: 
                    result.append(['q1',listAux[i],listAux[j],self.blank,'q5',listAux[i],listAux[j],self.blank,self.right,self.left,self.static])
            self.transitions.append(result[i])
            # print(str(result[i])+',')


    #Creating transitions q5 -> q5 with all the alphabet + comma
        result=[]
        listComma=listAux.copy()
        listComma.append(',')
        for i in range(len(listComma)):
            result.append(['q5',',',listComma[i],self.blank,'q5',',',listComma[i],self.blank,self.static,self.left,self.static])
            self.transitions.append(result[i])


    def transportStr(self,tape):
        aux =[]
        for x in tape:
            aux.append(x)
        return aux



    def turingMachine(self,inputTape1,inputTape2):
        inputTape1=self.transportStr(inputTape1)
        inputTape2=self.transportStr(inputTape2)
        state=self.inicialState
        head1=0
        head2=0
        head3=0
        inputTape1.append(self.blank)
        inputTape2.append(self.blank)
        while len(inputTape1) != head1 and len(inputTape2) !=head2: #Iterating each letter from the input
            # for j in range(len(inputTape2)):
                band=False
                for singleT in self.transitions:
                    if singleT[0] == state  and singleT[3]==self.outputTape[head3] and singleT[1]==inputTape1[head1] and singleT[2]==inputTape2[head2] :
                        inputTape1[head1]=singleT[5]
                        inputTape2[head2]=singleT[6]
                        self.outputTape[head3]=singleT[7]
                        if singleT[8]==self.right:
                            head1+=1
                        if singleT[8]==self.left:
                            head1-=1
                        if singleT[9]==self.right:
                            head2+=1
                        if singleT[9]==self.left:
                            head2-=1
                        if singleT[10]==self.right:
                            head3+=1
                        if singleT[10]==self.left:
                            head3-=1
                        state=singleT[4]
                        band=True


                if(band==False):
                    break
        if state==self.finalState:
            return True
        return False




    def ejecutar(self,conjunto1,conjunto2):

        self.fillT()
        accepted=self.turingMachine(conjunto1,conjunto2) #Write here your input {}#{}
        result=''
        for char in self.outputTape:
            if char!=self.blank:
                result+=char
            if char==self.blank:
                break
        if accepted:
            return result
        else:
            return False

