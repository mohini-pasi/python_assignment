class decodetech:
    f_name = None
    l_namec= None
    edu = None

    def __init__(self,f_name,l_name,edu):
        self.f_name=f_name 
        self.l_name=l_name
        self.edu=edu
    
    def get_data(self):
        if self.edu == "BSC IT" or self.edu == "BSC CS" or self.edu == "BE":
            return ["python","datascience","web dev"]
        else:
            return None
        
data = decodetech(f_name ="aaa",l_name="bbb",edu="BSC IT")
print(data.get_data())