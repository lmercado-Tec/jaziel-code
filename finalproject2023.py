import pandas as pd
import yfinance as yf
import streamlit as st

# para para descargar los datos y limpiarlos
def obtener_precios_activos(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date)
    df = df[['Adj Close']].dropna()
    return df

# inputs
symbol = st.text_input("Ingrese el símbolo del activo: ")
start_date = st.text_input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
end_date = st.text_input("Ingrese la fecha de fin (YYYY-MM-DD): ")

if st.button("Buscar"):
    #df = yf.download(symbol, start=start_date, end=end_date)
    #precios = df[['Adj Close']].dropna()
    ticker = yf.Ticker(symbol)
    
    # - accurate time-series count:
    ticker_history = ticker.history(start=start_date, end=end_date)
    st.write(start_date)
    st.write(end_date)
    st.write(ticker_history)
    
    #Mostrar los primeros 5 y los últimos 5 datos
    #primeros_5 = precios.head(5)
    #ultimos_5 = precios.tail(5)
    
    # Mostrar los resultados
    st.write("\nPrimeros 5 datos:")
   #st.write(primeros_5)

    st.write("\nÚltimos 5 datos:")
    #st.write(ultimos_5)
    
    

#if symbol not None and start_date not None and end_date not None:
    # Obtener los precios  y limpiar la base de datos
    #precios = obtener_precios_activos(symbol, start_date, end_date)

    # Mostrar los primeros 5 y los últimos 5 datos
    #primeros_5 = precios.head(5)
    #ultimos_5 = precios.tail(5)

    # Mostrar los resultados
    #st.write("\nPrimeros 5 datos:")
    #st.write(primeros_5)

    #st.write("\nÚltimos 5 datos:")
    #st.write(ultimos_5)
