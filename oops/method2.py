class decodetech:
    f_name = None
    l_name= None
    edu = None

    def __init__(self,f_name,l_name,edu):
        self.f_name=f_name 
        self.l_name=l_name
        self.edu=edu
    
    @classmethod
    def get_data(self):
        print(self.f_name,self.l_name,self.edu)

    @staticmethod
    def static_value(f_name):
        print(f_name)
    
data = decodetech(f_name="mohini",l_name="pasi",edu="BSC IT")
data.get_data()
data.static_value(f_name="mohini")
    