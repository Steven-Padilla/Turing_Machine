import string
class DesecharRepetidos():
    def __init__(self):
        self.blank='blank'
        self.right='right'
        self.left='left'
        self.static='self.static'
        self.finalState='q5'
        self.inicialState='q0'
        self.listAux=list(string.ascii_lowercase)+["0","1","2","3","4","5","6","7","8","9"]
        self.result=[]
        self.outputTape=[]       #Creating and filling self.outPutTape with blanks
        self.inputTape2=[]
        for i in range (200):
            self.inputTape2.append(self.blank)
        for i in range (200):
            self.outputTape.append(self.blank)
        self.transitions=[
            #( First block )  --->  (     Second block       )    
            ['q0','{',self.blank,self.blank,        'q1','{','{',self.blank,self.right,self.right,self.right],
        ]
    def fillT(self):
        #creating transitions q1 -> q2 with all alphabet
        result=[]
        for i in range(len(self.listAux)):
            for j in range(len(self.listAux)):
                for k in range(len(self.listAux)):
                    result.append(['q1',self.listAux[i],self.blank,self.blank,        'q2','&',self.listAux[i],self.listAux[i],self.right,self.static,self.static])
        for x in result:
            self.transitions.append(x)
        #Creating self.transitions q2 -> q2 with all the alphabet
        result=[]
        for i in range(len(self.listAux)):
            for j in range(len(self.listAux)):
                for k in range(len(self.listAux)):
                    if self.listAux[i] != self.listAux[k]: 
                        result.append(['q2',self.listAux[i],self.listAux[j],self.listAux[k],        'q2',self.listAux[i],self.listAux[j],self.listAux[k],self.right,self.static,self.static])
                        
                    elif self.listAux[i] == self.listAux[k]:
                        result.append(['q2',self.listAux[i],self.listAux[j],self.listAux[k],        'q2','!',self.listAux[j],self.listAux[k],self.right,self.static,self.static])
                    result.append(['q2',',',self.listAux[j],self.listAux[k],        'q2',',',self.listAux[j],self.listAux[k],self.right,self.static,self.static]) 
                    result.append(['q2','}',self.listAux[j],self.listAux[k],        'q3','}',self.listAux[j],self.listAux[k],self.left,self.static,self.static])
                    result.append(['q2','!',self.listAux[j],self.listAux[k],        'q2','!',self.listAux[j],self.listAux[k],self.right,self.static,self.static]) 

        for x in result:
            self.transitions.append(x)

        #Creating self.transitions q3 -> q3 with all the alphabet
        result=[]
        for i in range(len(self.listAux)):
            for j in range(len(self.listAux)):
                for k in range(len(self.listAux)):
                    result.append(['q3','!',self.listAux[j],self.listAux[k],        'q3','!',self.listAux[j],self.listAux[k],self.left,self.static,self.static])
                    result.append(['q3',',',self.listAux[j],self.listAux[k],        'q3',',',self.listAux[j],self.listAux[k],self.left,self.static,self.static])
                    result.append(['q3',self.listAux[i],self.listAux[j],self.listAux[k],        'q3',self.listAux[i],self.listAux[j],self.listAux[k],self.left,self.static,self.static])
                    result.append(['q3','&',self.listAux[j],self.listAux[k],        'q4','&',self.listAux[j],self.listAux[k],self.right,self.right,self.static])
        for x in result:
            self.transitions.append(x)

        #Creating self.transitions q4 -> q6 with all the alphabet
        result=[]
        for k in range(len(self.listAux)):
            result.append(['q4',',',self.blank,self.listAux[k],        'q6',',',',',self.listAux[k],self.right,self.right,self.right])
            result.append(['q4','}',self.blank,self.listAux[k],        'q5','}','}',self.listAux[k],self.right,self.right,self.right])
        for x in result:
            self.transitions.append(x)

        #Creating self.transitions q6 -> q6 with all the alphabet
        result=[]
        for i in range(len(self.listAux)):
            for j in range(len(self.listAux)):
                result.append(['q6','!',self.blank,self.blank,        'q6','!',self.blank,self.blank,self.right,self.static,self.static])
                result.append(['q6',',',self.blank,self.blank,        'q6',',',self.blank,self.blank,self.right,self.static,self.static])
                result.append(['q6',self.listAux[i],self.blank,self.blank,        'q2','&',self.listAux[i],self.listAux[i],self.right,self.static,self.static])
                result.append(['q6','}',self.blank,self.blank,        'q7','}',self.blank,self.blank,self.right,self.left,self.right])
        for x in result:
            self.transitions.append(x)

        result=[]
        for i in range(len(self.listAux)):
            result.append(['q7',self.blank,self.listAux[i],self.blank,        'q8',self.blank,self.listAux[i],self.blank,self.static,self.right,self.static])
            result.append(['q7',self.blank,',',self.blank,        'q5',self.blank,'}',self.blank,self.static,self.right,self.static])
        for x in result:
            self.transitions.append(x)

        result=[]
        result.append(['q8',self.blank,self.blank,self.blank,        'q5',self.blank,'}',self.blank,self.static,self.static,self.static])

    def transportStr(self,tape):
        aux =[]
        for x in tape:
            aux.append(x)
        return aux

    def turing_intersection(self,inputTape1):
        inputTape1=self.transportStr(inputTape1)
        state=self.inicialState
        head1=0
        head2=0
        head3=0
        inputTape1.append(self.blank)
        self.inputTape2.append(self.blank)
        while len(inputTape1) != head1 and len(self.inputTape2) !=head2: #Iterating each letter from the input
            # for j in range(len(self.inputTape2)):
                band=False
                for singleT in self.transitions:
                    if singleT[0] == state  and singleT[3]==self.outputTape[head3] and singleT[1]==inputTape1[head1] and singleT[2]==self.inputTape2[head2] :
                        inputTape1[head1]=singleT[5]
                        self.inputTape2[head2]=singleT[6]
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
                


    def ejecutar(self, conjunto):
        self.fillT()

        accepted=self.turing_intersection(conjunto)
        result=''
        for char in self.inputTape2:
            if char!=self.blank:
                result+=char
            if char==self.blank:
                break
        if accepted:
            return result
        else:
            return False
# print(DesecharRepetidos().ejecutar("{a,a,c,a,a,b,b,a,d,1,2,1,1,3,1,2,4}"))
