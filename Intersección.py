import string
class Interseccion():
    
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
            ['q3',',','{',self.blank,        'q1',',','{',self.blank,self.right,self.right,self.static],
            ['q4',self.blank,'{',',',        'q7',self.blank,'{','}',self.static,self.left,self.right],
            ['q4',self.blank,'{','{',        'q6',self.blank,'{','{',self.static,self.left,self.right],
            ['q6',self.blank,self.blank,self.blank,        'q7',self.blank,self.blank,'}',self.static,self.static,self.right],
            ['q5',',','{',self.blank,        'q1',',','{',',',self.right,self.right,self.right],
            ['q8',self.blank,'}',',',        'q7',self.blank,'}','}',self.static,self.static,self.right],
            ['q8',self.blank,'}','{',        'q9',self.blank,'}','{',self.static,self.static,self.right],
            ['q9',self.blank,'}',self.blank,        'q7',self.blank,'}','}',self.static,self.static,self.right],
        ] 

    def fillT(self):
        listAux=list(string.ascii_lowercase) + ["0","1","2","3","4","5","6","7","8","9"]

    # Creating transicion q1 -> q2 when tape one symbols are diferents
        result=[]
        for i in range(len(listAux)):
            for j in range(len(listAux)):
                if listAux[i] != listAux[j]: 
                    result.append(['q1',listAux[i],listAux[j],self.blank,'q2',listAux[i],listAux[j],self.blank,self.static,self.right,self.static])
        for x in result:
            self.transitions.append(x)

    #Creating self.transitions q2 -> q1 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q2',listAux[i],',',self.blank,'q1',listAux[i],',',self.blank,self.static,self.right,self.static])
            self.transitions.append(result[i])
    #Creating self.transitions q2 -> q3 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q2',listAux[i],'}',self.blank,        'q3',listAux[i],'}',self.blank,self.right,self.left,self.static])
            self.transitions.append(result[i])

    #Creating self.transitions q3 -> q8 with all alphabet
        result=[]
        for j in range(len(listAux)):
            result.append(['q3','}',listAux[j],self.blank,        'q8','}',listAux[j],self.blank,self.right,self.right,self.left])
        for x in result:
            self.transitions.append(x)


    #Creating self.transitions q3 -> q3 with all alphabet + comma
        result=[]
        listComma=listAux.copy()
        listComma.append(',')
        for j in range(len(listComma)):
            result.append(['q3',',',listComma[j],self.blank,        'q3',',',listComma[j],self.blank,self.static,self.left,self.static])
        for x in result:
            self.transitions.append(x)

    #Creating self.transitions q1 -> q4 with all alphabet 
        result=[]
        for j in range(len(listAux)):
            result.append(['q1','}',listAux[j],self.blank,        'q4','}',listAux[j],self.blank,self.right,self.left,self.left])
        for x in result:
            self.transitions.append(x)


    #Creating self.transitions q1 -> q5 with all alphabet 
        result=[]
        for i in range(len(listAux)):
            for j in range(len(listAux)):
                if listAux[i] == listAux[j]: 
                    result.append(['q1',listAux[i],listAux[j],self.blank,'q5',listAux[i],listAux[j],listAux[i],self.right,self.left,self.right])
        for x in result:
            self.transitions.append(x)


    #Creating transition q5 -> q5 with all alphabeth + comma
        result=[]
        listComma=listAux.copy()
        listComma.append(',')
        for j in range(len(listComma)):
            result.append(['q5',',',listComma[j],self.blank,        'q5',',',listComma[j],self.blank,self.static,self.left,self.static])
        for x in result:
            self.transitions.append(x)

    #Creating self.transitions q5 -> q7 with all alphabet 
        result=[]
        listCor=listAux.copy()
        listCor.append('{')
        listCor.append(',')
        for j in range(len(listCor)):
            result.append(['q5','}',listCor[j],self.blank,        'q7','}',listCor[j],'}',self.right,self.static,self.right])
        for x in result:
            self.transitions.append(x)

    # #Creating self.transitions q1 -> q7 with all alphabet 
        result=[]
        listComma=listAux.copy()
        listComma.append('}')
        for j in range(len(listComma)):
            result.append(['q1',listComma[j],'}',self.blank,        'q7',listComma[j],'}','}',self.static,self.right,self.right])
        for x in result:
            self.transitions.append(x)


    def transportStr(self,tape):
        aux =[]
        for x in tape:
            aux.append(x)
        return aux



    def turing_intersection(self,inputTape1,inputTape2):
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
                



    def ejecutar(self, conjunto1, conjunto2):
        self.fillT()
        accepted=self.turing_intersection(conjunto1,conjunto2) #Write here your input {}#{}
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
            
            
