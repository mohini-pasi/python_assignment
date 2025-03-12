# class Dcodetech:
#     first_name=None
#     last_name=None
#     education=None

#     def __init__(self,name,last_name,education):
#         self.first_name=name
#         self.last_name=last_name
#         self.education=education
    
#     def get_data(self):
#         print(self.first_name)

# class python(Dcodetech):
#     def __init__(self):
#         pass
#     def temp_method(self):
#         return self.first_name
#     def get_data(self):
#         return(self.education)

# data=Dcodetech(name="mohini",last_name="pasi",education="bscit")
# py=python()
# print(py.temp_method())

class Dcodetech:
    first_name=None
    last_name=None
    education=None

    def __init__(self,name,last_name,education):
        self.first_name=name
        self.last_name=last_name
        self.education=education
    
    def get_data(self):
        print(self.first_name)

class python(Dcodetech):
    def __init__(self,name,last_name,education):
        super().__init__(self,name,last_name,education)
        pass
    def temp_method(self):
        return super().get_data()

    def get_data(self):
        return(self.education)

py=python(name="mohini",last_name="pasi",education="bscit")
print(py.temp_method())