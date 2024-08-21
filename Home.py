import streamlit as st
st.set_page_config(page_title = "Home")
from PIL import Image 
st.header("")
image = Image.open('logo.JPEG')
st.sidebar.image(image, width=200)

st.sidebar.markdown("Fonte: ")
st.sidebar.markdown("https://www.kaggle.com/datasets/msjahid/global-ai-ml-and-data-science-salaries")
st.sidebar.markdown("------")
st.sidebar.markdown("Produzido por")

st.sidebar.markdown("Jeferson Oliveira")
st.sidebar.markdown("jeferson.sov@gmail.com")
st.sidebar.markdown("------")
st.sidebar.markdown("Agradecimentos")
st.sidebar.markdown("Comunidade DS")
st.markdown(" ## :blue[Análise das contratações de profissionais da área de Dados dos ultimos 5 anos]")
 

st.write("""Olá o meu objetivo com esse Dashboard é de contribuir com informações sobre a área de dados que tem sido muito falada nos últimos tempos
Além de ler sobre a área por conta de uma necessidade profissional de aprimoramento resolvi ir atrás de alguns dados para fazer minhas análises
além de estudar e aprimorar as habilidades que tenho aprendido com o curso ana Comunidade DS.

Eu não tenho o objetivo de esgotar o assunto mas de oferecer informações interessantes a respeito da área 
tendo me baseando em dados do Kaggle. São mais de 26000 linhas de informações e contém informações tais como:

- Profissões
- Ano de Contratação
- Regime de trabalho: Home Office, Híbrido, Presencial
- Salário anual em dólares
- Tamanho da empresa que realizou a contratação
- Localização da empresa
- Localização do profissional
            
Essas são as principais informações que eu considerei após fazer análise exploratória. Resolvi confeccionar 
os gráficos diante do que considerei importante visualizar consciente que essa análise é só mais uma de outras fontes de informações
que juntas podem contribuir para escolhas pessoais de especialização nessa área, ou mesmo iniciar no mundo de Dados.

Na aba de insigths escrevi as minhas análises a partir de cada um dos gráficos confeccionados considerando
o crescimento das contratações, trabalho Home Office e salário. Fiz análise baseado nas três profissões que mais
apareceram: Cientista de Dados, Engenheiro de Dados e Analista de Dados.

Em conclusões escrevi dois possíveis caminhos, a partir dos insigths dos dados, de prós e contra se é que podemos dizer isso!

Obrigado por visitar essa página, boa leitura!! Espero contribuir para sua jornada!!""")