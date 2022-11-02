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
            n -= 1
            i = range(n)
            for b in i:
                x += b
    return x

test = SumN(-6)

print(test)


