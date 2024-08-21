####IMmportando as Bibliotecas necessárias
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import scipy 
from PIL import Image 
st.set_page_config(page_title = 'Analise das contratações de profissionais de Dados', layout = 'wide')
##### Leitura do Argquivo CSV
df = pd.read_csv(r'../jobs_Data/global_ai_ml_data_salaries.csv')


####Limpeza e cópia do arquivo original
df['experience_level'] = df['experience_level'].str.strip()
df['job_title'] = df['job_title'].str.strip()
df1 = df.copy()
df1.loc[df1['remote_ratio']== 100, 'remote_ratio'] = 'Home Office'
df1.loc[df1['remote_ratio']== 0, 'remote_ratio'] = 'Presencial'
df1.loc[df1['remote_ratio']== 50, 'remote_ratio'] = 'Hibrido' 
df1['remote_ratio'] = df1['remote_ratio'].astype(str)
st.header("")
image = Image.open('logo.JPEG')
st.sidebar.image(image, width=200)

st.sidebar.markdown("Fonte:")
st.sidebar.markdown("https://www.kaggle.com/datasets/msjahid/global-ai-ml-and-data-science-salaries")
st.sidebar.markdown("------")
st.sidebar.markdown("Produzido por")

st.sidebar.markdown("Jeferson Oliveira")
st.sidebar.markdown("jeferson.sov@gmail.com")
st.sidebar.markdown("------")
st.sidebar.markdown("Agradecimentos")
st.sidebar.markdown("Comunidade DS")
#st.markdown(" ## :blue[Análise das contratações de profissionais da área de Dados dos ultimos 5 anos]")


########### Layout streamlit#####

#### Top 10 profissões que mais receberam contratação nos últimos 5 anos
df1_jobs = df1.groupby('job_title').size()
df1_jobs.sort_values(ascending = False).head(10)    

st.markdown('### Análise das contratações de profissionais da área de Dados dos ultimos 5 anos')
tab1,tab2,tab3 = st.tabs(['Contratações nos últimos 5 anos','Home Office','Salários'])
with tab1:
    
    with st.container():
        col1, col2 = st.columns(2)
        with col2:
            with st.container():
                df_DS = df1.loc[:,['job_title', 'company_size','work_year']].groupby(['work_year','company_size']).count().reset_index()
                plt.figure(figsize=(10,6))
                sns.barplot(x='work_year', y='job_title', hue='company_size',  data=df_DS, palette='viridis')
                st.markdown('#### Total de Cargos por Porte da Empresa por ano')
        # Adicionando detalhes ao gráfico
                plt.xlabel('Ano')
                plt.ylabel('Contratações')
                plt.legend(title='Porte da Empresa')
                plt.grid(True)
                st.pyplot(plt, use_container_width=True)
            with st.container():
                st.markdown('#### Crescimento dos 3 maiores Cargos nos últimos 5 anos')
                linhas = ((df1['job_title'] == 'Data Scientist') | (df1['job_title'] == 'Data Engineer') | (df1['job_title'] == 'Data Analyst'))
                df1_auxiliar = df1.loc[linhas,['work_year', 'job_title']].groupby(['work_year','job_title']).size().reset_index(name = 'Contratacoes')
            # Plotar os pontos  
                fig2, ax = plt.subplots()
                sns.set_theme(style="whitegrid")
                sns.lineplot(x='work_year', y='Contratacoes', hue='job_title', data=df1_auxiliar)
                ax.set_xticks(np.arange(min(df1_auxiliar['work_year']), max(df1_auxiliar['work_year'])+1, 1))
                st.pyplot(fig2)
###### TOP 10 maiores contrataçãos nos ultimos 5 anos
        with col1:
            with st.container():
                df_DS = df1.loc[:,['job_title', 'experience_level','work_year']].groupby(['work_year','experience_level']).count().reset_index()
                plt.figure(figsize=(10,6))
                sns.barplot(x='work_year', y='job_title', hue='experience_level',  data=df_DS, palette='viridis')
            with st.container():
                st.markdown('#### Total de Cargos por nível de Experiência por ano')
            # Adicionando detalhes ao gráfico
                plt.xlabel('Ano')
                plt.ylabel('Contratações')
                plt.legend(title='Nível')
                plt.grid(True)
                st.pyplot(plt, use_container_width=True)
            with st.container():
                df_top = df1['job_title'].value_counts().reset_index()
                df_top.columns = ['job_title', 'count']  # Rename columns
                df_top = df_top.sort_values(by='count', ascending=False)
                df_top = df_top.head(10)
                st.write('#### Top 10 cargos que mais receberam contratações')
                st.table(df_top)
with tab2:
     with st.container():
        col1, col2 = st.columns(2)
        with col1: 
            with st.container(): 
                st.markdown(' #### Percentual de contratações por modalidade de trabalho')
                df1_aux = df1.loc[:,['job_title','remote_ratio']].groupby('remote_ratio').count().reset_index()
                df1_aux['percent'] = df1_aux['job_title']/ df1_aux['job_title'].count()
                fig1 = px.pie(df1_aux, values = 'percent', names= 'remote_ratio', color = 'remote_ratio', 
                        color_discrete_map={'Presencial': 'darkblue', 'Home Office': 'royalblue', 'Hibrido': 'cyan' })
                fig1.update_traces(textposition = 'outside', textinfo = 'percent')
                st.plotly_chart(fig1,use_conteiner_width = True)
            with st.container():
                st.markdown('##### Cargos com maiores contratações Home Office')
                lines = (df1['remote_ratio']=='Home Office')
                df_aux1 =df1.loc[lines,'job_title'].count()
                df_aux = pd.DataFrame({'Remoto': df1[lines]['job_title'].groupby(df1[lines]['job_title']).count()}).reset_index()
                df_aux = df_aux.sort_values(by = 'Remoto', ascending = False)
                top10 = df_aux.head(10)
                fig5 = px.funnel(top10,x = 'Remoto', y = 'job_title')
                st.plotly_chart(fig5, use_container_width= True)
            with st.container():
                # Distribuição da contratação de Engenheiro de Dados em regime de trabalho remoto por tamanho da empresa e nível 
                st.markdown('##### Proporção de Home Office para Engenheiro de Dados por tamanho de empresa e nível de experiencia ')
                linhaDE = ((df1['job_title'] == 'Data Engineer') & (df1['remote_ratio'] == 'Home Office'))
                df_ax3 = df1.loc[linhaDE,['job_title', 'experience_level', 'company_size']].groupby(['company_size','experience_level'])['job_title'].count().reset_index()
                df_ax3.rename(columns={'job_title': 'hiring'}, inplace=True)
                df_ax4 = {'tamanho': ['S', 'M' , 'L'],
                        'EN': [2,34,11],
                        'MI': [2,381,15],
                        'SE': [1,1010,19],
                        'EX': [0,76,0]}
                df_ax4 = pd.DataFrame(df_ax4)
                # Calcula as porcentagens relativas
                df_relative = df_ax4.set_index('tamanho')
                df_relative = df_relative.div(df_relative.sum(axis=1), axis=0) * 100

                # Plotando o gráfico de colunas 100% empilhadas
                fig5, ax = plt.subplots(figsize=(10, 6))
                df_relative.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
                # Adiciona rótulos e título

                ax.set_xlabel('Tamanho da empresa')
                ax.set_ylabel('Percentual de contratacoes')
                ax.legend(title='Nível', bbox_to_anchor=(1.05, 1), loc='upper left')
                ax.set_xticks(range(len(df_relative.index)))
                ax.set_xticklabels(df_relative.index, rotation=0)
            
                st.pyplot(fig5)            

        with col2:
            with st.container():
                st.markdown('#### Percentual de contrataçãoes Home Office por ano')
                # Contratações HomeOffice 2020
                lines_remote2020 = (df1['remote_ratio'] == 'Home Office') & (df1['work_year'] == 2020)
                count_remote2020 = df1[lines_remote2020]['remote_ratio'].count()
                line_2020 = (df1['work_year'] == 2020)
                count_total2020 = df1[line_2020]['remote_ratio'].count()
                df1_2020 = pd.DataFrame({'Remote': [count_remote2020],
                                            'All Modalities': [count_total2020],'Year': [2020],
                                            'Remote_percent': [round(count_remote2020 / count_total2020*100,2)]})
                #Contratações HomeOffice 2021
                lines_remote2021 = (df1['remote_ratio'] == 'Home Office') & (df1['work_year'] == 2021)
                count_remote2021 = df1[lines_remote2021]['remote_ratio'].count()
                line_2021 = (df1['work_year'] == 2021)
                count_total2021 = df1[line_2021]['remote_ratio'].count()
                df1_2021 = pd.DataFrame({'Remote': [count_remote2021],
                                            'All Modalities': [count_total2021],
                                            'Year': [2021],
                                            'Remote_percent': [round(count_remote2021 / count_total2021*100,2)]})

                #Contratações HomeOffice 2022
                lines_remote2022 = (df1['remote_ratio'] == 'Home Office') & (df1['work_year'] == 2022)
                count_remote2022 = df1[lines_remote2022]['remote_ratio'].count()
                line_2022 = (df1['work_year'] == 2022)
                count_total2022 = df1[line_2022]['remote_ratio'].count()
                df1_2022 = pd.DataFrame({'Remote': [count_remote2022],
                                            'All Modalities': [count_total2022],
                                            'Year': [2022],
                                            'Remote_percent': [round(count_remote2022 / count_total2022*100,2)]})

                #Contratações HomeOffice 2023
                lines_remote2023 = (df1['remote_ratio'] == 'Home Office') & (df1['work_year'] == 2023)
                count_remote2023 = df1[lines_remote2023]['remote_ratio'].count()
                line_2023 = (df1['work_year'] == 2023)
                count_total2023 = df1[line_2023]['remote_ratio'].count()
                df1_2023 = pd.DataFrame({'Remote': [count_remote2023],
                                            'All Modalities': [count_total2023],
                                            'Year': [2023],
                                            'Remote_percent': [round(count_remote2023 / count_total2023*100,2)]})

                #Contratações HomeOffice 2024
                lines_remote2024 = (df1['remote_ratio'] == 'Home Office') & (df1['work_year'] == 2024)
                count_remote2024 = df1[lines_remote2024]['remote_ratio'].count()
                line_2024 = (df1['work_year'] == 2024)
                count_total2024 = df1[line_2024]['remote_ratio'].count()
                df1_2024 = pd.DataFrame({'Remote': [count_remote2024],
                                            'All Modalities': [count_total2024],
                                            'Year': [2024],
                                            'Remote_percent': [round(count_remote2024 / count_total2024*100,2)]})

                #Percentual de Contratações HomeOffice nos últimos 5 anos
                df_concat = pd.concat([df1_2020, df1_2021, df1_2022, df1_2023, df1_2024], axis = 0)
                fig3 = px.bar(df_concat, x='Year', y='Remote_percent', text = 'Remote_percent')
                fig3.update_traces(textposition = 'outside')
                st.plotly_chart(fig3,use_conteiner_width = True)
            with st.container():
                # Distribuição da contratação de cientista de Dados em regime de trabalho remoto por tamanho da empresa e nível 
                st.markdown('##### Proporção de Home Office para Cientista de Dados por tamanho de empresa e nível de experiencia')
                linhaDS = ((df1['job_title'] == 'Data Scientist') & (df1['remote_ratio'] == 'Home Office'))
                df_ax1 = df1.loc[linhaDS,['job_title', 'experience_level', 'company_size']].groupby(['company_size','experience_level'])['job_title'].count().reset_index()
                df_ax1.rename(columns={'job_title': 'hiring'}, inplace=True)
                df_ax2 = {'tamanho': ['S', 'M' , 'L'],
                        'EN': [4,35,10],
                        'MI': [0,357,21],
                        'SE': [0,1112,30],
                        'EX': [1,58,5]}
                df_ax2 = pd.DataFrame(df_ax2)
                # Calcula as porcentagens relativas
                df_relative = df_ax2.set_index('tamanho')
                df_relative = df_relative.div(df_relative.sum(axis=1), axis=0) * 100

                # Plotando o gráfico de colunas 100% empilhadas
                fig4, ax = plt.subplots(figsize=(10, 6))
                df_relative.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
                # Adiciona rótulos e título

                ax.set_xlabel('Tamanho da empresa')
                ax.set_ylabel('Percentual de contratacoes')
                ax.legend(title='Nível', bbox_to_anchor=(1.05, 1), loc='upper left')
                ax.set_xticks(range(len(df_relative.index)))
                ax.set_xticklabels(df_relative.index, rotation=0)
                
                st.pyplot(fig4)
            with st.container():
            # Distribuição da contratação de Analista de Dados em regime de trabalho remoto por tamanho da empresa e nível 
                st.markdown('##### Proporção de Home Office para Analista de Dados por tamanho de empresa e nível de experiencia')
                linhaDA = ((df1['job_title'] == 'Data Analyst') & (df1['remote_ratio'] == 'Home Office'))
                df_ax6 = df1.loc[linhaDA,['job_title', 'experience_level', 'company_size']].groupby(['company_size','experience_level'])['job_title'].count().reset_index()
                df_ax6.rename(columns={'job_title': 'hiring'}, inplace=True)
                df_ax7 = {'tamanho': ['S', 'M' , 'L'],
                        'EN': [6,228,10],
                        'MI': [1,209,7],
                        'SE': [9,695,6],
                        'EX': [0,8,0]}
                df_ax7 = pd.DataFrame(df_ax7)
                # Calcula as porcentagens relativas
                df_relative = df_ax4.set_index('tamanho')
                df_relative = df_relative.div(df_relative.sum(axis=1), axis=0) * 100

                # Plotando o gráfico de colunas 100% empilhadas
                fig6, ax = plt.subplots(figsize=(10, 6))
                df_relative.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
                # Adiciona rótulos e título

                ax.set_xlabel('Tamanho da empresa')
                ax.set_ylabel('Percentual de contratacoes')
                ax.legend(title='Nível', bbox_to_anchor=(1.05, 1), loc='upper left')
                ax.set_xticks(range(len(df_relative.index)))
                ax.set_xticklabels(df_relative.index, rotation=0)
                st.pyplot(fig6)
with tab3:
    with st.container():
        ### Salários

        #linhas = ((df1['job_title'] == 'Data Scientist') ) & (df1['remote_ratio'] == 'Home Office')

        df_ax = pd.DataFrame({ 'salary': df1[linhas]['salary_in_usd'] ,
                            'job_title': df1[linhas]['job_title'] ,
                            'experience_level':df1[linhas]['experience_level'],
                                'company_Size': df1[linhas]['company_size']})
        maior_salario = df_ax['salary'].max()
        df_ax = df_ax.loc[df_ax['salary']!= maior_salario,:]

        # Distribuição de salarios de maneira geral considerando empresas de pequeno medio e grande porte 
        #fig = px.box(df_ax, x='job_title', y='salary', color='experience_level', points='all')
        #st.plotly_chart(fig, use_container_width=True)

        #Distribuição salarial por tamanho da empresa para cientista de dados na modalidade remoto
        linhaS = (df_ax['company_Size'] == 'S')
        df_axS = df_ax.loc[linhaS,:]
        figS = px.box(df_axS, x='job_title', y='salary', color='experience_level', points='all', title= 'Salario anual em $ para empresas de pequeno porte')
        figS.update_layout(title={ 'font': {'size': 24}})
        
        linhaM = (df_ax['company_Size'] == 'M')
        df_axM = df_ax.loc[linhaM,:]
        figM = px.box(df_axM, x='job_title', y='salary', color='experience_level', points='all', title=' Salario anual em $ para empresas de Médio porte')
        figM.update_layout(title={ 'font': {'size': 24}})

        linhaL = (df_ax['company_Size'] == 'L')
        df_axL = df_ax.loc[linhaL,:]
        figL = px.box(df_axL, x='job_title', y='salary', color='experience_level', points='all', title='salario anual em $ para empresas de Grande Porte')
        figL.update_layout(title={ 'font': {'size': 24}})

        st.plotly_chart(figS, use_container_width=True)
        st.plotly_chart(figM, use_container_width=True)
        st.plotly_chart(figL, use_container_width=True)

       


print ('estou aqui')
