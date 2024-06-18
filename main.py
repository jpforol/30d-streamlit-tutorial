import streamlit as st
from streamlit_option_menu import option_menu

from scenes import dia01, dia02, dia03, dia04, dia05, dia06, dia07, dia08, dia09, dia10
from scenes import dia11, dia12, dia13, dia14#, dia15#, dia16#, dia17#, dia18#, dia19#, dia20
#from scenes import dia21#, dia22#, dia23#, dia24#, dia25#, dia26#, dia27#, dia28#, dia29#, dia30

with st.sidebar:
    selected = option_menu("Main Menu", ["Dia 01", "Dia 02", "Dia 03", "Dia 04", "Dia 05",
                                         "Dia 06", "Dia 07", "Dia 08", "Dia 09", "Dia 10",
                                         "Dia 11", "Dia 12", "Dia 13", "Dia 14", "Dia 15",
                                         "Dia 16", "Dia 17", "Dia 18", "Dia 19", "Dia 20",
                                         "Dia 21", "Dia 22", "Dia 23", "Dia 24", "Dia 25",
                                         "Dia 26", "Dia 27", "Dia 28", "Dia 29", "Dia 30",])

if selected == 'Dia 01':
    dia01.app()
if selected == 'Dia 02':
    dia02.app()
if selected == 'Dia 03':
    dia03.app()
if selected == 'Dia 04':
    dia04.app()
if selected == 'Dia 05':
    dia05.app()
if selected == 'Dia 06':
    dia06.app()
if selected == 'Dia 07':
    dia07.app()
if selected == 'Dia 08':
    dia08.app()
if selected == 'Dia 09':
    dia09.app()
if selected == 'Dia 10':
    dia10.app()
if selected == 'Dia 11':
    dia11.app()
if selected == 'Dia 12':
    dia12.app()
if selected == 'Dia 13':
    dia13.app()
if selected == 'Dia 14':
    dia14.app()
if selected == 'Dia 15':
    dia15.app()
if selected == 'Dia 16':
    dia16.app()
if selected == 'Dia 17':
    dia17.app()
if selected == 'Dia 18':
    dia18.app()
if selected == 'Dia 19':
    dia19.app()
if selected == 'Dia 20':
    dia20.app()
if selected == 'Dia 21':
    dia21.app()
if selected == 'Dia 22':
    dia22.app()
if selected == 'Dia 23':
    dia23.app()
if selected == 'Dia 24':
    dia24.app()
if selected == 'Dia 25':
    dia25.app()
if selected == 'Dia 26':
    dia26.app()
if selected == 'Dia 27':
    dia27.app()
if selected == 'Dia 28':
    dia28.app()
if selected == 'Dia 29':
    dia29.app()
if selected == 'Dia 30':
    dia30.app()