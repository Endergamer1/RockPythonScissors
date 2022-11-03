#Write a function that takes two arguments one int n and a list of ints excluded
#n sums from 0 to n and is positional only
#ints excluded is keyword only and not necessary

def SumExcl(n: int, excluded: int =()) -> int:
        x: range = range(0, n + 1)
        sum: int = 0
        for b in x:
                if b in excluded:
                        pass
                else:
                        sum = sum + b
        return sum

Test = SumExcl(7, (1,2,4,7))
print(Test)