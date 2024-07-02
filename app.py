import streamlit as st
import plotly.express as px
from dataset import df,df1,df2
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores, grafico_vendas_vendedores

st.set_page_config(layout='wide')
st.title("Dashboard de Vendas :shopping_trolley:")

st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]
#print(df)

aba1, aba2, aba3, aba4 = st.tabs(['Dataset', 'Receita', 'Vendedores','Mini-Graficos'])
with aba1:
    st.dataframe(df)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(grafico_map_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores)
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores)
with aba4:
    coluna1,coluna2 = st.columns(2)
    with coluna1:
        
        st.dataframe(
                df1,
                column_config={
                    "name": "App name",
                    "stars": st.column_config.NumberColumn(
                        "Github Stars",
                        help="Number of stars on GitHub",
                        format="%d ⭐",
                    ),
                    "url": st.column_config.LinkColumn("App URL"),
                    "views_history": st.column_config.LineChartColumn(
                        "Views (past 30 days)", y_min=0, y_max=5000
                    ),
                },
                hide_index=True,
                )
    with coluna2:
        edited_df = st.data_editor(df2)

        favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
        st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
    