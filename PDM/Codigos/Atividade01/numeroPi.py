from mpmath import mp

# Precisão inicial
precisao = 10

while True:
    mp.dps = precisao
    print(str(mp.pi))
    precisao += 10  # aumenta 10 casas a cada loop
