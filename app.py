from client import gerar_resposta

def main():
    mensagens = [
        {"role": "system", "content": "Você é um assistente amigável e prestativo."}
    ]

    print("🤖 Olá! Eu sou seu chatbot. Digite 'sair' pra encerrar.")
    
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            break

        mensagens.append({"role": "user", "content": pergunta})
        resposta = gerar_resposta(mensagens)
        mensagens.append({"role": "assistant", "content": resposta})

        print("Bot:", resposta)

if __name__ == "__main__":
    main()