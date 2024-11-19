import streamlit as st

# Configurações iniciais
st.set_page_config(page_title="South Atlantic Cyclones", page_icon=":cyclone:")

# Título principal
st.title("Ciclones Atlântico Sul")
st.write("Visualize informações e mídias sobre diferentes ciclones do Atlântico Sul.")

# Criando abas para organizar os ciclones
tab1, tab2 = st.tabs(["Ciclone Akará", "Outro Ciclone (Em desenvolvimento)"])

# Informações do Ciclone Akará
with tab1:
    st.header("Ciclone Akará")
    
    # Subseções para o canal CH13
    st.subheader("Canal CH13")
    st.image("gifs/ch13/akara_ch13.gif", caption="GIF - Ciclone Akará CH13", use_container_width=True)
    #st.image("gifs/ch13/akara_ch13_image.jpg", caption="Imagem - Ciclone Akará CH13", use_container_width=True)
    
    # Subseções para True Color
    st.subheader("True Color")
    st.image("gifs/true_color/akara_true_color.gif", caption="GIF - Ciclone Akará True Color", use_container_width=True)
    #st.image("gifs/true_color/akara_true_color_image.jpg", caption="Imagem - Ciclone Akará True Color", use_container_width=True)

# Informações de outro ciclone
with tab2:
    st.header("Outro Ciclone")
    st.write("Adicione informações e mídia de outros ciclones aqui.")
