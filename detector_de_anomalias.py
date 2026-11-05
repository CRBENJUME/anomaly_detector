import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# ==============================
# 1. Descargar datos
# ==============================
symbol = "^NDX"
intervalo = "1m"
periodo = "2d"
data = yf.download(symbol, interval=intervalo, period=periodo)

# ==============================
# 2. Calcular Log Returns
# ==============================
data["Log_Return"] = np.log(data["Close"] / data["Close"].shift(1))

# ==============================
# 3. Rolling Mean & Std
# ==============================
window = 50  # ventana móvil
k = 2        # número de desviaciones estándar

data["Rolling_Mean"] = data["Log_Return"].rolling(window).mean()
data["Rolling_Std"] = data["Log_Return"].rolling(window).std()

data["Upper_Threshold"] = data["Rolling_Mean"] + k * data["Rolling_Std"]
data["Lower_Threshold"] = data["Rolling_Mean"] - k * data["Rolling_Std"]

# ==============================
# 4. Detectar anomalías
# ==============================
data["Anomaly"] = 0
data.loc[data["Log_Return"] > data["Upper_Threshold"], "Anomaly"] = 1
data.loc[data["Log_Return"] < data["Lower_Threshold"], "Anomaly"] = -1

# ==============================
# 5. Gráfica
# ==============================
plt.figure(figsize=(20,10))

plt.plot(data.index, data["Log_Return"],
         label="Log Return", color="gray", alpha=0.6)

plt.plot(data.index, data["Upper_Threshold"],
         linestyle="--", label="Upper Threshold (Venta)", color="brown")

plt.plot(data.index, data["Lower_Threshold"],
         linestyle="--", label="Lower Threshold (Compra)", color="green")

# Marcar anomalías
plt.scatter(data.index[data["Anomaly"] == 1],
            data["Log_Return"][data["Anomaly"] == 1],
            color="orange", label="Anomalía Alcista", zorder=5)

plt.scatter(data.index[data["Anomaly"] == -1],
            data["Log_Return"][data["Anomaly"] == -1],
            color="red", label="Anomalía Bajista", zorder=5)

plt.title(f"Anomalías en Rendimientos Logarítmicos - {symbol} {intervalo}")
plt.legend()
plt.grid(True)
plt.show()
