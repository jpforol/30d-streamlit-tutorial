def app():
    import streamlit as st
    import pandas as pd
    import numpy as np
    
    st.title("Dia 09 - st.line_chart")
    
    st.header('Gráfico de Linhas')
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    
    st.line_chart(chart_data)
    st.write(chart_data)
    