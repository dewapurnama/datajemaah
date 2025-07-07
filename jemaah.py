import streamlit as st
import psycopg2
from psycopg2 import OperationalError
import pandas as pd

# --- Function to connect and fetch data ---
@st.cache_data(show_spinner=True)  # cache the result for faster reload
def fetch_data():
    try:
        connection = psycopg2.connect(
          host=st.secrets["db_host"],
          database=st.secrets["db_name"],
          user=st.secrets["db_user"],
          password=st.secrets["db_password"],
          port=st.secrets["db_port"]
        )
        cursor = connection.cursor()
        
        query = """
        select * from ibbank.bankreportjournal where tx_code = 'HJOA' and kode_valuta = 'USD' and tx_date >= date '2025-06-01' and tx_date < '2025-06-30' 
        """
        
        cursor.execute(query)
        result = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]
        df = pd.DataFrame(result, columns=column_names)
        
        cursor.close()
        connection.close()
        return df
    
    except OperationalError as e:
        st.error(f"Database connection failed: {e}")
        return pd.DataFrame()  # return empty DataFrame on error

# --- Streamlit App Layout ---
st.title("📊 Jumlah Pendaftaran Jemaah")

df = fetch_data()

if not df.empty:
    st.success("Data fetched successfully!")
    st.dataframe(df)
else:
    st.warning("No data to display.")
