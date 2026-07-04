import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

st.line_chart(dados_vendas, x = 'faturamento', y = 'investimento')
modelo_investimento = LinearRegression()
modelo_investimento.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])

qtde_investido = st.number_input('investimento')
#qtde_investido = st.slider('Total investido', 0, 600, 50)
faturamento_final = modelo_investimento.predict([[qtde_investido]])


st.write(faturamento_final)
#st.metric(f'seu faturamento seria' ,f'{min(faturamento_final[0], 0):.1f}')
# objetivo: previsão de FATURAMENTO baseado nos investimentos