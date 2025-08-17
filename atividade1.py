inicio = "q1"
estados = ["q1", "q2", "q3"]
aceitacao = ["q2"]
alfabeto = ["0", "1"]
transicoes = {
    "q1" : {"0": "q1", "1": "q2"},
    "q2" : {"0": "q3", "1": "q2"},
    "q3" : {"0": "q2", "1": "q2"}
}
entrada = input().split()
print(entrada)

for palavra in entrada:
    atual = inicio
    for c in palavra:
        if c not in alfabeto:
            atual = None
            break
        atual = transicoes[atual][c]
        print(atual)
    if atual in aceitacao:
        print("aceita")
    else:
        print("rejeita")