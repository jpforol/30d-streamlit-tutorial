def app():
    import streamlit as st
    
    st.title('Dia 10 - st.selectbox')
    
    st.header('st.selectbox')
    
    option = st.selectbox(
        'Qual a sua cor favorita?',
        ('Azul', 'Vermelho', 'Verde')
    )
    
    st.write('Sua cor favorita é ', option)
    