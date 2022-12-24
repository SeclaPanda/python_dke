import io
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as lite

st.title('Интернет-магазин продуктов')

st.sidebar.title('Выберите нужную опцию')

#st.button(f'<a target="_blank" href="{link1}">Hyperlink in Streamlit dataframe</a>')
#st.button('Создать заказ клиента')
#st.button('Редактировать заказ клиента')
#st.button('Создать отчет по продажам')
#st.button('Создать запрос на поставку')
#st.button('Создать отчет по закупкам')
#st.button('Выход')

link1 = "https://mariaaltisheva-dke-app-p70owt.streamlit.app/Просмотр_баз_данных"
df = pd.DataFrame(
    {
        "url": [
            f'<a target="_blank" href="{link1}">Просмотр баз данных</a>',
        ],
        "label": ["Ссылка"]
    }
)

st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)