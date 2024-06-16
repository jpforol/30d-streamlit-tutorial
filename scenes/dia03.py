def app():
    import streamlit as st
    
    st.title('Dia 03 - Botões')
    st.header('st.button')

    if st.button('Say Hello'):
        st.write('Why hello there')
    if st.button('Say goodbye'):
        st.write('Goodbye')