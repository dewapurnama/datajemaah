import streamlit as st
import psycopg2
from psycopg2 import OperationalError
import pandas as pd

# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

df = conn.query("""
    SELECT * 
    FROM ibbank.bankreportjournal 
    WHERE tx_code = 'HJOA' 
      AND kode_valuta = 'USD' 
      AND tx_date >= DATE '2025-06-01' 
      AND tx_date < DATE '2025-06-30'
""", ttl="10m")

st.dataframe(df)
