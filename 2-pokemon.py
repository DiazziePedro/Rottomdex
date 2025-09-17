import requests

def buscar_pokemon(nome):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            nome_pokemon = dados["name"].capitalize()
            altura = dados["height"] / 10
            peso = dados["weight"] / 10
            tipos = [t["type"]["name"] for t in dados["types"]]
            tipos_formatados = ", ".join(tipos)

            return (f"Nome: {nome_pokemon}\n"
                    f"Altura: {altura} m\n"
                    f"Peso: {peso} kg\n"
                    f"Tipo(s): {tipos_formatados}")
        else:
            return "A Rotomdex não encontrou esse pokemon... Tente novamente!"
    except:
        return "Erro ao conectar ao sistema da Rotomdex."

def responder(mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return "Olá, treinador! Essa é a Rotomdex, digite um nome de um pokémon: "
    elif mensagem == "sair":
        return "Até mais, treinador! Desligando a Rotomdex..."
    else:
        return buscar_pokemon(mensagem)

# Programa principal
print("Rotomdex (digite 'sair' para encerrar)\n")

while True:
    user_input = input("Você: ")
    resposta = responder(user_input)

    print("Bot:", resposta)

    if user_input.lower() == "sair":
        break