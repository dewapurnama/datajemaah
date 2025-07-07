import streamlit as st
import psycopg2
from psycopg2 import OperationalError
import pandas as pd

# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('select * from ibbank.bankreportjournal where tx_code = 'HJOA' and kode_valuta = 'USD' and tx_date >= date '2025-06-01' and tx_date < '2025-06-30'', ttl="10m")

st.dataframe(df)
