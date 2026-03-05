# client.py - versão com IA local

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Escolha do modelo local (pode mudar por outro mais leve)
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
# ou troque por:
# model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("⏳ Carregando o modelo (isso pode demorar na primeira vez)...")

# Baixa e carrega o modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32)

print("✅ Modelo carregado!")

def gerar_resposta(mensagens):
    # Junta todas as mensagens do usuário em um texto só
    entrada_texto = "\n".join([msg["content"] for msg in mensagens if msg["role"] == "user"])
    entrada = tokenizer.encode(entrada_texto + "\nResposta:", return_tensors="pt")

    # Gera a resposta
    saida = model.generate(
        entrada,
        max_length=250,
        temperature=0.7,
        do_sample=True,
        top_p=0.9
    )

    resposta = tokenizer.decode(saida[0], skip_special_tokens=True)
    resposta = resposta.split("Resposta:")[-1].strip()
    return resposta