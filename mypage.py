import streamlit as st

# Configurações iniciais
st.set_page_config(page_title="Meus GIFs", page_icon=":camera_flash:")

# Título do site
st.title("App dedicado ao ciclone Akará")
st.write("Como primeiro teste será adicionado gifs.")

# Exibindo os GIFs
st.subheader("GIF ch13")
st.image("gifs/ch13/akara_ch13.gif", use_container_width=True)


#st.subheader("GIF True Color")
#st.image("/home/victor/USP/webpage/gifs/true_color/akara_true_color.gif", use_container_width=True)

# Rodapé ou mensagem de despedida
st.write("Obrigado por visitar!")

