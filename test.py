import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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