import streamlit as st
from transformers import pipeline
import torch

# usa GPU se tiver, senão CPU
device = 0 if torch.cuda.is_available() else -1

# gerador local (distilgpt2 é leve; trocar por modelo melhor se tiver GPU)
gerador = pipeline(
    "text-generation",
    model="distilgpt2",
    device=device,            # -1 = CPU, 0 = primeira GPU
)

st.write("### CHAT BOT VASCAÍNO 💢💢💢💢")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# mostrar histórico
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

mensagem_usuario = st.chat_input("Fala Vascão, em que posso ajudar?")

def build_prompt(messages):
    # monta um prompt simples com histórico
    s = ""
    for m in messages:
        if m["role"] == "user":
            s += f"Usuário: {m['content']}\n"
        else:
            s += f"Assistente: {m['content']}\n"
    s += "Assistente: "
    return s

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})

    prompt = build_prompt(st.session_state["lista_mensagens"])

    # gerar (usamos max_new_tokens para gerar só a continuação)
    out = gerador(
        prompt,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=gerador.tokenizer.eos_token_id,  # evita warning no GPT2
    )

    generated = out[0]["generated_text"]

    # se o gerador retornou o prompt + continuação, remove o prefixo do prompt
    if generated.startswith(prompt):
        resposta_ia = generated[len(prompt):].strip()
    else:
        # fallback: tenta cortar a parte "Assistente:" se existir
        resposta_ia = generated.split("Assistente:")[-1].strip()

    # exibir e salvar
    st.chat_message("assistant").write(resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})
