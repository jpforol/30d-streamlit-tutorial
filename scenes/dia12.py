def app():
    import streamlit as st
    
    st.title('Dia 12 - st.checkbox')
    
    st.header('st.checkbox')
    
    st.write('O que você gostaria de pedir?')
    
    icecream = st.checkbox('Sorvete')
    coffee = st.checkbox('Café')
    cola = st.checkbox('Regrigerante')
    
    if icecream:
        st.write("Sucesso! Aqui está o seu sorverte.")
    
    if coffee:
        st.write("Ok, aqui está o seu café.")
        
    if cola:
        st.write("Aqui está seu refrigerante!")
    
    