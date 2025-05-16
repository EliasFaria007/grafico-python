import plotly.express as px
import pandas as pd
estados=["RO","AC","AM","RR","PA","AP","TO","MA","PI","CE","RN","PB","PE",
"AL","SE","BA","MG","ES","RJ","SP","PR","SC","RS","MS","MT","GO","DF"]
regioes=["Norte","Norte","Norte","Norte","Norte","Norte","Norte","Nordeste","Nordeste"
,"Nordeste","Nordeste","Nordeste","Nordeste","Nordeste","Nordeste","Nordeste",
"Sudeste","Sudeste","Sudeste","Sudeste","Sul","Sul","Sul","Centro-Oeste",
"Centro-Oeste","Centro-Oeste","Centro-Oeste"]
populacao=[1777225,881935,4144597,605761,8602865,845731,1572866,7075181,
3273227,9132078,3506853,4018127,9557071,3337357,2298696,14873064,21168791,4018650,17264943,
45919049,11433957,7164788,11377239,2778986,3484466,7018354,3015268]
df=pd.DataFrame(dict(estados=estados,regioes=regioes,populacao=populacao))
df["Brasil"]="Brasil"
fig=px.sunburst(df, path=["Brasil", "regioes", "estados"], values="populacao")
fig.show()
# Grafico em blocos, substituindo a chamada do método sunburst por: px.treemap