#pip install requests
import requests

def buscar_pokempn(nome):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            nome_pokemon = dados["name"].capitalize()
            altura = dados["height"] / 10
            peso = dados["weight"] / 10
            tipos = [t["type"]["name"] for t in dados["types"]]
            tipos_formatados = ", ".joins(tipos)

            return(f"Nome: {nome_pokemon}\n"
                   f"Altura: {altura}m\n"
                   f"Peso: {peso} kg/n"
                   f"Tipo(s): {tipos_formatados}")
        
        else:
            return "A Rottomdex não encontrou esse pokemon... Tente novamente!"
    except:
        return "Erro ao conectar ao sistema da Rottomdex."
    
    def responder(mensagem):
        mensagem = mensagem.lower()
        if "oi" in mensagem or "olá" in mensagem:
            return "Olá, treinador! Essa é a Rottomdex, digite um nome de um pokémon: "
        elif mensagem == "sair":
            return "Até mais, treinador! Desligando a Rottomdex..."
        else:
            return buscar_pokemon(mensagem)
        
#corpo do programa
print("RottomDex (digite 'sair' para encerrar)\n")