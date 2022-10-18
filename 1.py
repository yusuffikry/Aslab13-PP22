M_1 = []
for i in range(1,3):
    for j in range(1,3):
        a = int(input(f'Input nilai matriks pertama indeks {i},{j}: '))
        M_1.append(a)

M_2 = []
for k in range(1,3):
    for l in range(1,3):
        b = int(input(f'Input nilai matriks kedua indeks {k},{l}: '))
        M_2.append(b)

p = M_1[0]*M_2[0] + M_1[1]*M_2[2]
q = M_1[0]*M_2[1] + M_1[1]*M_2[3]
r = M_1[2]*M_2[0] + M_1[3]*M_2[2]
s = M_1[2]*M_2[1] + M_1[3]*M_2[3]

print('Hasil perkalian matriks')
print(f'|{M_1[0]} {M_1[1]}| X |{M_2[0]} {M_2[1]} = |{p} {q}|')
print(f'|{M_1[2]} {M_1[3]}|   |{M_2[2]} {M_2[3]} = |{r} {s}|')