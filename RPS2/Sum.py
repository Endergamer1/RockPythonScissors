#Write a function that takes int argument n that returns a sum from 0 to n if n >= 0.
#If n < 0 then returns sum from n to 0.
#Write a script that tests this function for a few different n's, e.g., 0, 5, 10, -5, etc

def SumN(n: int) -> int:
    x: int = 0
    if n >= 0:
            n += 1
            i = range(n)
            for b in i:
                x += b

    elif n < 0:
            i = range(n,0)
            for b in i:
                x += b
    else:
        print("I AM LOSING MY FUCKING MIND")

    return x

Test1 = SumN(0)
Test2 = SumN(5)
Test3 = SumN(10)
Test4 = SumN(-5)


print(Test1)
print(Test2)
print(Test3)
print(Test4)


