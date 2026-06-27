import streamlit as st

st.title('Formulario')
with st.form('Formulario'):
    nome = st.text_input('Insira seu nome completo:')
    if nome == "":
        st.warning('preencha os campos obrigatorios')
    idade = st.number_input('Insira sua idade:', value = None)
    if idade == None:
        st.warning('preencha os campos obrigatorios')
    pergunta = st.radio('Você concorda com os termos de uso?',['Concordo', 'Não concordo'], index = None)
    if pergunta == 'Não concordo':
        st.write('você não concordou com os termos')
    salvar = st.form_submit_button('Enviar formulario')
    st.write('Seu nome é:')
    st.write('Sua idade é:')
    st.write('Formulario enviado com sucesso:')






