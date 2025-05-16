import yfinance as yf
import matplotlib.pyplot as plt

tesla = yf.download('TSLA', start='2010-01-01')
ibm = yf.download('IBM', start='2010-01-01')

# exibir grafico
plt.figure(figsize=(12,6))
plt.plot(ibm.index, ibm['Adj.Close'], label='IBM', color='blue')
plt.title('ações da IBM')
plt.xlabel('data')
plt.ylabel('preço ($)');
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(12,6))
plt.plot(tesla.index, tesla['Adj.Close'], label='Tesla', color='red')
plt.title('ações da Tesla')
plt.ylabel('preço ($)')
plt.xlabel('data')
plt.grid(True)
plt.legend()
plt.show()