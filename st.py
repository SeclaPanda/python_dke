import io
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as lite

def read_sqlite_table():

    conn = lite.connect('db.sqlite3')
    cur = conn.cursor()

    def get_posts():
        df = pd.read_sql_query("SELECT * FROM Заказ_клиента", conn)
        st.table(data=df)

    get_posts()
    

st.title('Интернет-магазин продуктов')

st.sidebar.title('Выберите нужную опцию')
link1 = "https://mariaaltisheva-dke-app-p70owt.streamlit.app/Просмотр_баз_данных"
st.button('Просмотр баз данных', on_click=read_sqlite_table)
st.button(f'<a target="_blank" href="{link1}">Hyperlink in Streamlit dataframe</a>',)
st.button('Редактировать заказ клиента')
st.button('Создать отчет по продажам')
st.button('Создать запрос на поставку')
st.button('Создать отчет по закупкам')
st.button('Выход')
#view.on_click()