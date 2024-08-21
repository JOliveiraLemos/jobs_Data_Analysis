import streamlit as st
st.set_page_config(page_title = 'Insights', layout = 'wide')
from PIL import Image
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
st.markdown(" ## Análise das contratações de profissionais da área de Dados dos ultimos 5 anos")


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('## :blue[ Crescimento da área de dados]')
        st.write(
        """ 
        A análise mostrou que de fato o número de contratações aumentou significativamente 
        para as profissões que trabalham com dados. As maiores contratações nos últimos 5 anos 
        foram para Cientista de Dados, Engenheiro de Dados e Analista de Dados.

        As contratações de cientista de dados, por exemplo, aumentaram cerca de 8 vezes em 3 anos saindo de 
        algo em torno de 500 em 2022 para 4000 em 2024.Isso indica o quanto a área de dados se 
        mostra promissora. Entretanto é preciso ressaltar que o número de contratações por nível 
        de experiência (EN: Júnio, MI: Médio, SE: Sênior, EX: Executivo) é muito maior para 
        profissionais nível Sênior. Num primeiro momento pode parecer ruim para aqueles que estão nos níveis iniciais da carreira, mas a análise desse gráfico  juntamente com o gráfico do número de contratações por porte da empresa
        mostra que empresas de medio porte contrataram muito mais do que as de grande porte chegando a ter 7 vezes mais profissionais 
        em 2024 e, portanto tais contratações estariam mais concentradas em empresas de médio porte. Esses dois fatos são indicativos de uma busca de expansão por parte de médias empresas ancorando 
        suas decisões de negócios em análises de dados. O alto volume de contratações de profissionais mais experientes bem como a concentração de vagas em empresas de médio porte, pode 
        ser um indicativo de que as empresas queiram profissionais
        mais experientes para iniciarem seus projetos e estruturarem o setor de Dados e, posteriormente aumentem o time diversificando o nível dos profissionais conforme
        os projetos vão surgindo. Sendo assim, pode haver maiores oportunidades para niveis iniciais conforme os setores vão se estruturando 
        nas empresas a médio e longo prazo""")

        st.markdown('## :blue[ Trabalho Home Office]')
        st.write("""
              
            Em relação ao trabalho remoto vemos que em torno de 25% dos cargos são mantidos nessa modalidade de trabalho. Além disso 
            a quantidade de cargo em regime totalmente remoto caiu consideravelmente a partir de 2022. As profissões de Cientista de Dados, 
            Engenheiro de Dados e Analista de Dados são as que mais possuem essa possibilidade. O gráfico de barras empilhadas mostra
            a proporção de distribuição de trabalho remoto para profissionais Executivo, Senior, Junio e Medio. É possível perceber que, para empresas de grande porte,
            há uma divisão mais equilibrada no sentido de que um profissional em níveis iniciais pode ter essa flexibilização tanto quanto profissionais 
            senior.O mesmo não acontece para empresas de medio porte. A proporção de profissionais senior em regime remoto é muito maior do 
            que para profissionais de outros níveis.
            Esse padrão se repete para as três profissões que mais receberam contratações: Cientista de Dados, Engenheiro de Dados e Analista de Dados. 
            Tal fato pode indicar somente uma diferença de cultura entre as empresas, ou pelo fato de buscarem expansão as empresas de médio 
            porte prefiram o modelo presencial por motivos internos que podem estar relacionados ao processo de crescimento.
            
            As empresas de pequeno porte fizeram contratações muito pequenas, com valor máximo de 9 cargos para Home Office nos ultimos anos
            e o grafico de barras empilhadas estando em termos percentuais pode dar a impressão errada de grandes oportunidades remotas
            para níveis iniciais. Na verdade, parece muito mais que as poucas contratações que tiveram foram casos 
            bem específicos se constituindo muito mais como exceção. O gráfico foi mantido pois poderia gerar dúvida por não serem mantidos nas
            análises""")


    with col2:
            st.markdown('## :blue[ Salários]')
            st.write(""" 
                Por fim, no que diz respeito a salários é possível perceber por meio da presença de outliers no gráfico box plot  que
                há situações de ganhos anuais em dólares muito acima da média. São casos isolados, mas pode ser o seu.

                Para as três profissões analisadas, os dados mostraram que as empresas de médio porte oferecem maiores salários 
                em comparação às de grande porte. Os salários foram avaliados sem filtro de Home Office, ou seja, todas as modalidades
                de trabalho estão presentes. Nesse sentido atingir um salário de $400k anual em empresas de medio porte como cientista 
                de dados, por exemplo, seria mais provável do que almejar essa faixa salarial em empresas de grande porte que seria um
                caso bem isolado como pode ser visto no gráfico box plot na aba salários.""")
            st.markdown('## :blue[ Conclusão]')    
            st.write("""
                    Como conclusão dos insights considerando trabalho Home Office e salarios mais altos, os dados sugerem dois caminhos:
                    
                    1) Se o objetivo é ter salários maiores então buscar uma empresa de médio porte pode ser o caminho uma vez que
                    existe maior faixa salarial disponível. Em contrapartida a probabilidade de ter trabalho remoto em níveis iniciais 
                    é menor em comparação a empresas de grande porte. Isso se conquistaria com o tempo.
                    
                    2) Se o objetivo é já iniciar de modo remoto, então as empresas que oferecem isso com maior probabilidade seriam
                    as grandes empresas que mantem uma proporção maior de profissionais de nível inicial nessa modalidade de trabalho. A contraposição
                    são faixas salariais mais baixas. """)
            st.write("""
                O caminho depende muito do que cada indivíduo quer para si.
                Acredito que a melhor escolha é aquilo que faz mais sentido para cada um!
                Espero ter contribuído com sua jornada!!
                        Obrigado
                        Até mais!!""")