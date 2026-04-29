def busca_binaria(vetor, alvo, min, max):
    pivot = int((min+max)/2)

    if (max >= min):
        if (vetor[pivot] == alvo):
            print(f"Valor encontrado na posição {pivot}")
            return 0
        elif (vetor[pivot] < alvo):
            min=pivot+1
            return busca_binaria(vetor, alvo, min, max)
        else:
            max=pivot-1
            return busca_binaria(vetor, alvo, min, max)

    print("Elemento não existe no vetor!")
    return -1 

# Encolha esse vetor clicando na seta para baixo à esquerda (⌵)
vetor_teste = [1000,
2000,
3000,
4000,
5000,
7000,
9000,
11000,
13000,
15000,
20000,
25000,
30000,
35000,
40000,
50000,
60000,
70000,
80000,
90000,
100000,
120000,
140000,
160000,
180000,
200000,
250000,
300000,
350000,
400000,
450000,
500000,
600000,
700000,
800000,
900000,
1000000,
1200000,
1400000,
1600000,
1800000,
2000000,
2500000,
3000000,
3500000,
4000000,
5000000,
6000000,
8000000,
10000000,
]


print( busca_binaria(vetor_teste,9000,0,len(vetor_teste)-1))
