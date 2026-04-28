# binary-search

É um algorítmo eficiente para encontrar um elemento específico em um vetor. Com um laço de repetição de complexidade O(n), no pior caso, para encontrar um valor específico em um vetor de 1.000.000 de posições com um laço simples, deveriam ser percorridas 1.000.000 de posições para encontrar o valor. Com a busca binária de complexidade log(n), são necessárias apenas 20 recursões para encontrar o valor específico, aproximadamente. Incrível não?

# Como funciona?

O algoritmo recebe um vetor como entrada, e utiliza estruturas condicionais para verificar se o *valor_alvo* está mais a esquerda ou a direita a partir de uma variável central que deve ser calculada, vou chama-la de *pivot*, se o valor que está na posição pivot for menor ou maior que ele, o algoritmo divide o vetor em dois e despreza a outra parte do vetor salvando novas posições de início e fim, ao mesmo tempo o valor central diferente é excluido também ao adicionar 1 ao inicio ou decrementar 1 ao fim, até que a condição: vetor[pivot] == valor_alvo, seja satisfeita. Caso o valor_alvo não esteja presente no vetor, o algoritmo deve parar a recursividade retornando -1.

# Pseudocodigo

Vou chamar as variáveis inicio e fim de min e max, respectivamente.

```
BuscaBinaria (vetor, alvo, min, max):
    pivot = (max+min)/2
    Se (max >= min):
        Se (vetor[pivot] == alvo):
            Retorne pivot
        Senão:
            Se (vetor[pivot] < alvo):
                min = pivot + 1
                Retorne BuscaBinaria (vetor, alvo, min, max)
            Senão:
                max = pivot - 1
                Retorne BuscaBinaria (vetor, alvo, min, max)
    Retorne -1
```

# Explicação do pseudocódigo:
1. Definir variáveis min e max, geralmente min é 0 pois na maioria das linguagens de programação o índice inicial do vetor é 0, max deve ser o tamanho do vetor -1 para ter o número da posição do último elemento nele.
   
2. Calcular pivot fazendo a uma média entre max e min, descartando decimais.
   
3. Verificar se o max >= min, caso essa condição não seja satisfeita, isso indica que o valor procurado não existe no vetor e o retorno é -1 para essa situação.

4. Se o valor do elemento for igual ao valor alvo, então o algoritmo deve retornar o pivot, o valor foi encontrado!

5. Caso contrário, se o valor do elemento na posição pivot atual for menor que o alvo, então a variável min deve ser atualizada com o valor do pivot, somado com , pois o valor do pivot também é menor que o alvo. Após isso, um retorno que espera a saída da chamada recursiva direta do algoritmo. Retorna ao 2.
   
6. Semelhante ao 5, mas, nesse caso o max que é atualizado com o valor do pivot com decremento 1 para excluir o pivot atual, bem como em 5. Após isso, a chamada recursiva. Retorna ao 2.
