def app():
    import streamlit as st
    
    st.title('Dia 11 - st.multiselect')
    
    st.header('st.multiselect')
    
    options = st.multiselect(
        'Quais são suas cores favoritas?',
        ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
        ['Amarelo', 'Vermelho']
    )
    
    st.write('Você selecionou:', options)
    