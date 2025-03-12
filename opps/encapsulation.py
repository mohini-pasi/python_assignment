class decodetech:
    f_name = None
    l_name= None
    __edu = None

    def __init__(self,f_name,l_name,__edu):
        self.f_name=f_name 
        self.l_name=l_name
        self.edu=__edu
    
    @classmethod
    def get_data(self):
        print(self.f_name,self.l_name,self.__edu)

    @staticmethod
    def static_value(f_name):
        print(f_name)
    
data = decodetech(f_name="mohini",l_name="pasi",__edu="BSC IT")
data.get_data()
print(data(__edu="mohini"))
    