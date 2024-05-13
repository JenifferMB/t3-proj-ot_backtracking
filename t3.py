import sys


def res_dom(pecas):
    val_pecas = {}
    for i, (a, b) in enumerate(pecas):
        if a not in val_pecas:
            val_pecas[a] = []
        if b not in val_pecas:
            val_pecas[b] = []
        val_pecas[a].append((b, i))
        val_pecas[b].append((a, i))

    total_pecas = {}
    for a, b in pecas:
        total_pecas[a] = total_pecas.get(a, 0) + 1
        total_pecas[b] = total_pecas.get(b, 0) + 1

    pecas_pares = 0
    for p in total_pecas.values():
        if p % 2 != 0:
            pecas_pares += 1

    if pecas_pares not in (0, 2):
        return False, None

    comeco = []
    for v, p in total_pecas.items():
        if p % 2 != 0:
            comeco.append(v)
    if not comeco:
        comeco = [pecas[0][0]]

    memoizacao = {}

    def add_tentativa(val_atual, prox_valor, index, tentativa, usado, memoizacao, val_pecas):
        if usado[index]:
            return False, None

        tentativa.append((val_atual, prox_valor))
        usado[index] = True
        memoizacao_key = tuple(usado)

        resultado, final_tentativa = backtrack(prox_valor, tentativa, usado, memoizacao_key, memoizacao, val_pecas)
        if resultado:
            memoizacao[memoizacao_key] = (True, final_tentativa)
            return True, final_tentativa

        tentativa.pop()
        usado[index] = False
        return False, None

    def backtrack(val_atual, tentativa, usado, memoizacao_key, memoizacao, val_pecas):
        if memoizacao_key in memoizacao:
            return memoizacao[memoizacao_key]

        if len(tentativa) == len(pecas):
            return True, tentativa

        for prox_valor, index in val_pecas[val_atual]:
            if not usado[index]:
                resultado, final_tentativa = add_tentativa(val_atual, prox_valor, index, tentativa, usado, memoizacao, val_pecas)
                if resultado:
                    return True, final_tentativa

        memoizacao[memoizacao_key] = (False, None)
        return False, None

    for peca_inicial in comeco:
        for prox_valor, index in val_pecas[peca_inicial]:
            usado = [False] * len(pecas)
            tentativa = [(peca_inicial, prox_valor)]
            usado[index] = True
            memoizacao_key = tuple(usado)
            resultado, final_tentativa = backtrack(prox_valor, tentativa, usado, memoizacao_key, memoizacao, val_pecas)
            if resultado:
                return True, final_tentativa

    return False, None

def leitura_arquivo(nomeArq):
    with open(nomeArq, 'r') as arquivo:
        linhas = arquivo.readlines()
        num_pecas = int(linhas[0].strip())
        pecas = [tuple(map(int, linha.strip().split())) for linha in linhas[1:num_pecas+1]]
    return pecas


if len(sys.argv) < 2:
    print("Para utilizar o programa, execute: python t3.py <nome_arquivo>")
    sys.exit(1)
    
nomeArq = sys.argv[1]
pecas = leitura_arquivo(nomeArq)
    
tem_solucao, solucao = res_dom(pecas)
if tem_solucao:
    print(''.join(f"{a}-{b} " for a, b in solucao))
else:
    print("Não existe solução")
