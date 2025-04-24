import streamlit as st
import requests

st.set_page_config(page_title="QRNG ANU", layout="centered")
st.title("🔮 Números Quânticos da ANU")
st.write("Gerador de números aleatórios baseado em física quântica, direto da ANU 🇦🇺")

def gerar_numero_aleatorio():
    url = "https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados["data"][0]
    else:
        return "Erro ao conectar com a ANU."

if st.button("Gerar número quântico"):
    numero = gerar_numero_aleatorio()
    st.success(f"Número gerado: {numero}")
