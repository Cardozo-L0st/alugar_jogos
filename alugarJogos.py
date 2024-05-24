import streamlit as st

#Título de identificação no topo da página
st.set_page_config(page_title="Interface para alugar jogos")

st.write("Segundo projeto feito com StreamLit")
st.divider()

#Título semântico da página
st.header("Alugar jogos")

#Jogo1
st.subheader("Fate/Stay Night")
st.image("fate-stay_night.jpeg", "Capa do jogo Fate/Stay Night")
st.button("Alugar",1)
#Jogo2
st.subheader("The Eminence in Shadow")
st.image("The-Eminence-in-Shahow-game.jpg", "Capa do jogo the eminence in shadow",)
st.button("Alugar",2)
#Jogo3
st.subheader("Tensei Shitara Sllime Datta Ken")
st.image("tensei_shitara-slime.jpg", "Capa do jogo Tensei Shitara slime Datta ken")
st.button("Alugar",3)