x = list(input("Input array ke 1: ").split())
y = list(input("Input array ke 2: ").split())

z = []

for i in x:
    for j in y:
        if i == j:
            z.append(i)
print(f"terdapat {len(z)} duplikat yaitu {z}")

