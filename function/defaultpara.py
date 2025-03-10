def greeting (firstname:str,lastname:str,gender: str = None)->str:
    return f"hello {firstname} {lastname}, gender {gender}"

data=greeting(firstname="mohini",lastname="pasi",gender = "female")
print(data)