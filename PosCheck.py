def PosCheck(x):
        if x > 0:
                return True
        elif x < 0:
                return False
        else:
                return "Neutral"

print ("-10 is Positive: " + str(PosCheck(-10)))
print ("0 is Positive: " + str(PosCheck(0)))
print ("5 is Positive: " + str(PosCheck(5)))
print ("20 is Positive: " + str(PosCheck(20)))


