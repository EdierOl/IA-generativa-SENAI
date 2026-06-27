import streamlit as st

curso = st.selectbox('Selecione o curso desejado', ('Python', 'Java', 'C#', 'C++'))

tecnologias = st.multiselect('Selecione as tecnologias que gostaria de estudar: ', ('HTML', 'CSS', 'SQL', 'Git'))
