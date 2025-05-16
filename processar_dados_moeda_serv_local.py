import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do servidor local
series = pd.read_csv(
    r"../grafico-pyton/USD_BRL_hist.csv",
    header=0,
    index_col=0,
    parse_dates=True,
).squeeze()

# exibir grafico
series.plot()
plt.show()