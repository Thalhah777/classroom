import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

dates = pd.date_range(start='2020-01-01', periods=100, freq='D')
data = pd.DataFrame({'date': dates, 'value': [x + (x**0.5) for x in range(100)]})
data.set_index('date', inplace=True)

train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]

model = ARIMA(train, order=(5, 1, 0)) 
model_fit = model.fit()
forecast = model_fit.forecast(steps=len(test))

plt.figure(figsize=(10,6))
plt.plot(train, label='Training Data')
plt.plot(test, label='Actual Data', color='green')
plt.plot(test.index, forecast, label='Forecasted Data', color='red')
plt.legend()
plt.title('Time Series Forecasting using ARIMA')
plt.show()

