import string

class Complemento():
    def __init__(self):
        self.right='right'
        self.left='left'
        self.static='static'
        self.finalState=['q3','q5','q6']
        self.inicialState='q0'
        self.blank='blank'
        self.outputTape=[]                     #Creating and filling outPutTape with blanks
        for i in range (200):
            self.outputTape.append(self.blank)
        
        self.transitions=[
        #( Firts block )  --->  (     Second block       )    
            ['q0','{','{',        'q1','{','{',self.right,self.right],  
        ] 
    def fillT(self):
        listAux=list(string.ascii_lowercase) + ["0","1","2","3","4","5","6","7","8","9"]
        result=[]
        
    #Creating transicion q1 -> q2 when tape one symbols are diferents
        result=[]
        for i in range(len(listAux)):
            for j in range(len(listAux)):
                if listAux[i] != listAux[j]: 
                    result.append(['q1',listAux[i],listAux[j],'q2',listAux[i],listAux[j],self.static,self.right])
        for x in result:
            self.transitions.append(x)
        
    #Creating transitions q2 -> q1 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q2',listAux[i],',',        'q1',listAux[i],',',self.static,self.right])
            self.transitions.append(result[i])
            
    #Creating transitions q2 -> q3 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q2',listAux[i],'}',        'q3',listAux[i],'}',self.static,self.static])
            self.transitions.append(result[i])
            
    #Creating transicion q1 -> q4 when tape one symbols are equals
        result=[]
        for i in range(len(listAux)):
            for j in range(len(listAux)):
                if listAux[i] == listAux[j]: 
                    result.append(['q1',listAux[i],listAux[j],    'q4',listAux[i],listAux[j],self.right,self.static])
        for x in result:
            self.transitions.append(x)
    
    #Creating transitions q4 -> q7 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q4',',',listAux[j],       'q7',',',listAux[j],self.right,self.static])
            self.transitions.append(result[i])
            
    #Creating transitions q7 -> q7 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q7',listAux[i],listAux[j],       'q7',listAux[i],listAux[j],self.static,self.left])
            self.transitions.append(result[i]) 
    
    #Creating transitions q7 -> q1 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q7',listAux[i],'{',       'q1',listAux[i],'{',self.static,self.right])
            self.transitions.append(result[i]) 
            
    #Creating transitions q4 -> q5 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q4','}',listAux[j],        'q5','}',listAux[j],self.static,self.static])
            self.transitions.append(result[i])
            
    #Creating transitions q1 -> q6 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q1','}',listAux[j],        'q6','}',listAux[j],self.static,self.static])
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
        if state==self.finalState[1] or state==self.finalState[2]:
            return True
        return False
        
    def ejecutar(self,conjunto,universo):
        self.fillT()
        accepted=self.turingMachine(conjunto,universo) #Write here your input {}#{}
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
prueba = Complemento()
print(prueba.ejecutar('{a,i,u}','{a,e,i,o,u}'))