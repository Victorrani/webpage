import streamlit as st

# Configurações iniciais
st.set_page_config(page_title="Meus GIFs", page_icon=":camera_flash:")

# Título do site
st.title("Bem-vindo ao Meu Site de GIFs!")
st.write("Aqui você pode ver alguns dos meus GIFs favoritos.")

# Exibindo os GIFs
st.subheader("GIF 1")
st.image("/home/victor/Desktop/akara/gifs/akara_ch13.gif", use_container_width=True)

st.subheader("GIF 2")
st.image("/home/victor/Desktop/akara/gifs/akara_true_color.gif", use_container_width=True)

# Rodapé ou mensagem de despedida
st.write("Obrigado por visitar!")

