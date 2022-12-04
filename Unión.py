import string


class Union():

    def __init__(self):
        
        self.blank='blank'
        self.right='right'
        self.left='left'
        self.static='static'
        self.finalState='q8'
        self.inicialState='q1'
        self.outputTape=[]
        for x in range(100):
            self.outputTape.append(self.blank)                     #Creating and filling outPutTape with blanks

        self.transitions=[
        #( Firts block )  --->  (     Second block       )    
        ['q1',"{",self.blank,        'q2',self.blank,'{',self.right,self.right],
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
        ['q2', '0', 'blank', 'q3', 'blank', '0', 'right', 'right'],
        ['q2', '1', 'blank', 'q3', 'blank', '1', 'right', 'right'],
        ['q2', '2', 'blank', 'q3', 'blank', '2', 'right', 'right'],
        ['q2', '3', 'blank', 'q3', 'blank', '3', 'right', 'right'],
        ['q2', '4', 'blank', 'q3', 'blank', '4', 'right', 'right'],
        ['q2', '5', 'blank', 'q3', 'blank', '5', 'right', 'right'],
        ['q2', '6', 'blank', 'q3', 'blank', '6', 'right', 'right'],
        ['q2', '7', 'blank', 'q3', 'blank', '7', 'right', 'right'],
        ['q2', '8', 'blank', 'q3', 'blank', '8', 'right', 'right'],
        ['q2', '9', 'blank', 'q3', 'blank', '9', 'right', 'right'],
        ['q3',',',self.blank,  'q2',self.blank,',',self.right,self.right],
        ['q3','}',self.blank,  'q4',self.blank,',',self.right,self.right],
        ['q2','}',self.blank,  'q4',self.blank,self.blank,self.right,self.static],
        ['q4','#',self.blank,  'q5',self.blank,self.blank,self.right,self.static],
        ['q5','{',self.blank,  'q6',self.blank,self.blank,self.right,self.static],
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
        ['q6', '0', 'blank', 'q7', 'blank', '0', 'right', 'right'],
        ['q6', '1', 'blank', 'q7', 'blank', '1', 'right', 'right'],
        ['q6', '2', 'blank', 'q7', 'blank', '2', 'right', 'right'],
        ['q6', '3', 'blank', 'q7', 'blank', '3', 'right', 'right'],
        ['q6', '4', 'blank', 'q7', 'blank', '4', 'right', 'right'],
        ['q6', '5', 'blank', 'q7', 'blank', '5', 'right', 'right'],
        ['q6', '6', 'blank', 'q7', 'blank', '6', 'right', 'right'],
        ['q6', '7', 'blank', 'q7', 'blank', '7', 'right', 'right'],
        ['q6', '8', 'blank', 'q7', 'blank', '8', 'right', 'right'],
        ['q6', '9', 'blank', 'q7', 'blank', '9', 'right', 'right'],
        ['q7',',',self.blank,  'q6',self.blank,',',self.right,self.right],
        ['q6','}',self.blank,  'q9',self.blank,self.blank,self.right,self.left],
        ['q9',self.blank,',',  'q8',self.blank,'}',self.static,self.right],
        ['q9',self.blank,'{',  'q10',self.blank,'{',self.static,self.right],
        ['q10',self.blank,self.blank,  'q8',self.blank,'}',self.static,self.right],
        ['q7','}',self.blank,  'q8',self.blank,'}',self.right,self.right],
    ] 

    def transportStr(self,tape):
        aux =[]
        for x in tape:
            aux.append(x)
        return aux
    def turingMachine(self,inputTape):
        inputTape=self.transportStr(inputTape)
        state=self.inicialState
        head1=0
        head2=0
        inputTape.append(self.blank)

        for i in range(len(inputTape)): #Iterating each letter from the input
            band=False
            for singleT in self.transitions:
                if singleT[0] == state  and singleT[2]==self.outputTape[head2] and singleT[1]==inputTape[head1]:
                    self.outputTape[head2]=singleT[5]
                    inputTape[head1]=singleT[4]
                    if singleT[6]==self.right:
                        head1+=1
                    if singleT[6]==self.left:
                        head1-=1
                    if singleT[7]==self.right:
                        head2+=1
                    if singleT[7]==self.left:
                        head2-=1
                    state=singleT[3]
                    band=True

            if(band==False):
                break
        if state==self.finalState:
            return True
        return False


    def ejecutar(self, conjunto):
        accepted=self.turingMachine(conjunto) #Write here your input {}#{}
        result=''
        print(self.outputTape)
        for char in self.outputTape:
            if char!=self.blank:
                result+=char
            if char==self.blank:
                break
        if accepted:
            return result
        else:
            return False
