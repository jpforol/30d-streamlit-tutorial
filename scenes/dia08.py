def app():
    import streamlit as st
    from datetime import time, datetime
    
    st.title("Dia 08 - st.slider")
    
    st.header("st.slider")
    
    # Exemplo 1
    st.subheader('Slider')
    
    age = st.slider('Quantos anos você tem?', 0, 130, 25)
    st.write("Eu tenho ", age, " anos.")
    
    # Exemplo 2
    st.subheader('Slider de intervalo')
    
    values = st.slider(
        "Escolha um intervalo de valores",
        0.0, 100.00, (25.0, 75.0))
    st.write('Valores:', values)
    
    # Exemplo 3
    st.subheader('Slider de Data e Hora')
    
    start_time = st.slider(
        "Quando você vai começar?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm"
    )
    st.write("Início:", start_time)
    
    # Exemplo 4
    st.subheader("Slider de Intervalo de tempo")
    
    appointment = st.slider(
        "Agende um compromisso:",
        value=(time(11, 30), time(12, 45)))
    st.write("O compromisso foi agendado para:", appointment)