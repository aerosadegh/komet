from comet import TailPrint


tprint = TailPrint(7)

for i in range(50):
    tprint(i)