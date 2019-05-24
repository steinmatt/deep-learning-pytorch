###################
# VECTOR CLASS
###################
    
class Vector:
    
    def __init__(self, list_of_nb):
        self.entries = list_of_nb
        self.length = len(list_of_nb)
        
    def norm(self):
        s=0
        for i in range(0,self.length):
            s+= self.entries[i]**2
        return s**0.5
    
    def threshold(self , max_val ):
        for i in range(0,self.length):
            if self.entries[i]>max_val:
                self.entries[i]=max_val
                
    def display(self ):
        for i in range(0,self.length):
            print(self.entries[i])
    
    def multiply_by_scalar_(self,scalar):
        for i in range(0,self.length):
            self.entries[i] = self.entries[i] * scalar
    
    def multiply_by_scalar(self,scalar):       
        my_list=[]       
        for i in range(0,self.length):
            my_list.append( self.entries[i] * scalar )           
        new_v = Vector(my_list)       
        return new_v
    
    def dot(self,other_vector):
        s=0
        for i in range(0,self.length):
            s += self.entries[i] * other_vector.entries[i]
        return s
    
    def add_(self,other_vector):       
        for i in range(0,self.length):
            self.entries[i] += other_vector.entries[i]
            
    def add(self,other_vector):  
        my_list=[]
        for i in range(0,self.length):
            my_list.append( self.entries[i] + other_vector.entries[i] )
        new_v = Vector(my_list)
        return new_v

            
###################
# MATRIX CLASS
###################


class Matrix:
    
    def __init__(self, list_of_lists):
        self.entries = list_of_lists
        self.height =  len(list_of_lists)
        self.width =   len(list_of_lists[0])
        
    def display(self):
        for i in range(0, self.height):
            print(self.entries[i])
            
    def scalar_mult(self,scalar):
        for i in range(0,self.height):
            for j in range(0,self.width):
                self.entries[i][j] *= scalar
                
##############
# A Function
##############

def version():
    print('This is version 0.3 of the linalg package')
            

                