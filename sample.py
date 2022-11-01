from komet import TailPrint

tprint = TailPrint(10, 0.25)

for i in range(102):
    tprint(i, end=" * " if i % 2 == 0 else "\n")


tprint = TailPrint(5)  # override by previous instance (singleton)
for i in range(200, 250):
    tprint(i)
