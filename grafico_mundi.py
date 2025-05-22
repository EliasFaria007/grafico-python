import plotly.express as px
import pandas as pd

# 1. Carrega os dados de COVID-19
df = pd.read_csv("../grafico-pyton/covid_19_data.csv")

# 2. Pré-processamento dos dados (agrupa por país e soma os casos)
df_agrupado = df.groupby('Country/Region', as_index=False).agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum'
}).reset_index()

# 3. Cria o gráfico de dispersão geográfica para COVID-19
fig = px.choropleth(
    df_agrupado,
    locationmode='country names',
    locations='Country/Region',
    color='Confirmed',
    hover_name='Country/Region',
    hover_data=['Deaths', 'Recovered'],
    scope='world',
    title='Casos de COVID-19 por Países',
    color_continuous_scale=px.colors.sequential.Plasma, # Mudança de cores para uma paleta mais intuitiva
    labels={'Confirmed': 'Casos Confirmados', 'Deaths': 'Mortes', 'Recovered': 'Recuperados'},  # Adiciona rótulos mais intuitivos      
    projection='natural earth',  # Projeção mais natural
    template='plotly_dark'  # Tema escuro para melhor visualização
)

# 4. Personalizações adicionais
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="gray",
    showcountries=True,
    countrycolor="lightgray",
    showland=True,
    landcolor="lightgray",
    showlakes=True,
    lakecolor="lightgray",
    showrivers=True,
    rivercolor="lightgray",
    projection_type="natural earth",    
    bgcolor='rgba(0,0,0,0)',  # Fundo transparente
    resolution=50  # Resolução do mapa
)

fig.update_layout(
    margin={"r":0,"t":40,"l":0,"b":0},
    coloraxis_colorbar=dict(
        title="Casos Confirmados",
        thickness=20
    ),
    title_x=0.5,  # Centraliza o título
    title_y=0.95,  # Ajusta a posição do título
    title_font=dict(
        size=20,
        color="white"
    )
)

fig.show()