# Trabalho de Visualização da Informação
#importar as bibliotecas
import matplotlib.pyplot as plt; plt.rcdefaults()
import plotly.express as px
import pandas as pd
import matplotlib.dates as mdates


# Gráfico que mostra os países que mais tiveram  casos confirmados do covid 19 2020/2021
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




# cressimento dos casos por tempo

# Carregar os dados
df = pd.read_csv(
    "../grafico-pyton/covid_19_data.csv",
    parse_dates=['ObservationDate'],  # Certifique-se do nome correto da coluna
    dayfirst=True
)

# Processar os dados
daily_cases = df.groupby('ObservationDate').agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum'
})

# Configurações do gráfico
plt.figure(figsize=(14, 7))
plt.style.use('seaborn-v0_8')  # Estilo moderno compatível com versões recentes do matplotlib

# Gráfico principal (Casos Confirmados)
ax = daily_cases['Confirmed'].plot(
    color='#E63946',  # Vermelho moderno
    linewidth=2.5,
    marker='o',
    markersize=6,
    markevery=7,  # Mostrar marcadores a cada 7 dias
    alpha=0.9,
    label='Casos Confirmados'
)

# Adicionar mortes e recuperados (opcional)
daily_cases['Deaths'].plot(
    ax=ax,
    color='#1D3557',  # Azul escuro
    linestyle='--',
    linewidth=1.5,
    label='Mortes'
)
daily_cases['Recovered'].plot(
    ax=ax,
    color='#2A9D8F',  # Verde água
    linestyle='-.',
    linewidth=1.5,
    label='Recuperados'
)

# Personalização avançada
ax.set_title('Evolução Temporal dos Casos de COVID-19', pad=20, fontsize=16, fontweight='bold')
ax.set_xlabel('Data', fontsize=12, labelpad=10)
ax.set_ylabel('Número de Casos', fontsize=12, labelpad=10)

# Formatar eixo de datas
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45, ha='right')

# Adicionar grid e legendas
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(frameon=True, framealpha=0.9, shadow=True)

# Adicionar anotação com data da última atualização
last_date = daily_cases.index[-1].strftime('%d/%m/%Y')
plt.annotate(f'Última atualização: {last_date}',
            xy=(0.98, 0.02), xycoords='axes fraction',
            ha='right', va='bottom', fontsize=10)

# Ajustar layout e salvar
plt.tight_layout()
plt.savefig('evolucao_covid19.png', dpi=300, bbox_inches='tight', transparent=False)
plt.show()



# grafico Pizza

# Carrega os dados
df = pd.read_csv("../grafico-pyton/covid_19_data.csv")

# Soma os valores totais de cada categoria
confirmados = df['Confirmed'].sum()
mortes = df['Deaths'].sum()
recuperados = df['Recovered'].sum()

# Dados para o gráfico
labels = ['Confirmados', 'Mortes', 'Recuperados']
sizes = [confirmados, mortes, recuperados]
colors = ['#66b3ff', '#ff9999', '#99ff99']  # Cores mais acessíveis

# Cria o gráfico de pizza
plt.figure(figsize=(8, 6))
patches, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct=lambda p: '{:.1f}%\n({:,.0f})'.format(p, p * sum(sizes)/100),
    startangle=90,
    textprops={'fontsize': 12}
)

# Ajusta a legenda e título
plt.legend(patches, labels, loc="best")
plt.title('Distribuição de Casos de COVID-19', pad=20, fontweight='bold')
plt.axis('equal')  # Garante que o gráfico seja um círculo

# Melhora a formatação dos textos
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')

# Mostra o gráfico
plt.tight_layout()
plt.show()
