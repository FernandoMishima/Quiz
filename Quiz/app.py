class Pergunta:
    def __init__(self, prompt, resposta):
        self.prompt = prompt
        self.resposta = resposta

perguntas = [
    "Onde o café foi descoberto?\n(a) Etiópia\n(b) Brasil\n(c) África do Sul\n(d) Itália\n(e) Bolívia\n\n",
    "Quando o Brasil foi descoberto?\n(a) 1482\n(b) 1488\n(c) 1492\n(d) 1496\n(e) 1500\n\n",
    "Primeiros 5 digitos do π?\n(a) 3,5467\n(b) 3,1543\n(c) 3,1415\n(d) 3,4216\n(e) 3,8790\n\n",
]

questoes = [
    Pergunta(perguntas[0], "a"),
    Pergunta(perguntas[1], "e"),
    Pergunta(perguntas[2], "c"),
]

def run_test(questoes):
    pontos = 0
    for prompt in questoes:
        resposta = input(prompt.prompt)
        if resposta == prompt.resposta:
            pontos += 1
    print("Você acertou " + str(pontos) + "/" + str(len(questoes)) + " perguntas.")

run_test(questoes)