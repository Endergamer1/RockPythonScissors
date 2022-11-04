#Write a function that applies the Power of to a string
# ex. Base = string and exp = int 

def PowerOfString(Base: str, Exp: int):
        result = Base * (len(Base) ** Exp)
        print(result)

PowerOfString("Hell", 5)