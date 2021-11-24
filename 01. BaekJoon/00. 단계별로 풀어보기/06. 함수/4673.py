def SelfNumbers(n):
    generatedNum = set(range(1, n+1))
    notSelfNum = set()

    for n in generatedNum:
        for x in str(n):
            n += int(x)
        notSelfNum.add(n)
    
    selfNum = generatedNum.difference(notSelfNum)

    for v in sorted(selfNum):
        print(v)

SelfNumbers(10000)