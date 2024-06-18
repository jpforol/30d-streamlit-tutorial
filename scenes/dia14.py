def app():
    import pandas as pd
    from ydata_profiling import ProfileReport
    import streamlit as st
    
    from streamlit_pandas_profiling import st_profile_report
    
    st.header('`streamlit_pandas_profiling`')
    df = pd.read_csv('titanic_dataset.csv')
    report = ProfileReport(df)
    
    st_profile_report(report)
