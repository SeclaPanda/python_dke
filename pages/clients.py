import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as lite

st.title('Просмотр баз данных')

def client():

    conn = lite.connect('./db.sqlite3')
    cur = conn.cursor()

    df = pd.read_sql_query("SELECT * FROM Клиент", conn)
    st.table(data=df)


def client_order():

    conn = lite.connect('./db.sqlite3')
    cur = conn.cursor()

    df = pd.read_sql_query("SELECT * FROM Заказ_клиента", conn)
    st.table(data=df)


def warehouse():

    conn = lite.connect('./db.sqlite3')
    cur = conn.cursor()

    df = pd.read_sql_query("SELECT * FROM Склад", conn)
    st.table(data=df)

def suppliers():

    conn = lite.connect('./db.sqlite3')
    cur = conn.cursor()

    df = pd.read_sql_query("SELECT * FROM Поставщик", conn)
    st.table(data=df)

def suppliers_order():

    conn = lite.connect('./db.sqlite3')
    cur = conn.cursor()

    df = pd.read_sql_query("SELECT * FROM Заказ_поставщика", conn)
    st.table(data=df)


st.button('Клиенты', on_click=client)
st.button('Заказы клиентов', on_click=client_order)
st.button('Склад', on_click=warehouse)
st.button('Поставщики', on_click=suppliers)
st.button('Заказы поставщикам', on_click=suppliers_order)
st.button('Назад')


