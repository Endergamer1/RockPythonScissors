#Write a function that takes one int n and multiplies all integers in the range(1, n + 1)
#Write another function that takes an argument of a sequence type and returns product of all int in the list.

def ProductN(n: int) -> int:
        x = range(1, n + 1)
        result: int = 1
        for b in x:
                result *= b
        return result

def ProductSeq(n: int) -> int:
        result: int = 1
        for b in n:
                result *= b
        return result

Test1 = ProductN(20)
print(Test1)

Test2 = ProductSeq((1,4,6,1,8,223,7))
print(Test2)
                