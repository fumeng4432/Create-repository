import pandas as pd
import streamlit as st
import plotly.express as px

def get_dataframe_from_excel():

    df = pd.read_excel('supermarket_sales.xlsx',
                       sheet_name='销售数据',
                       skiprows=1,
                       index_col='订单号')

    df["小时数"] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
    return df

def add_sidebar_func(df):

    with st.sidebar:
        st.header("请筛选数据:")
        city_unique = df["城市"].unique()
        city = st.multiselect(
            "请选择城市:",
            options=city_unique,
            default=city_unique,
        )
        customer_type_unique = df["顾客类型"].unique()
        customer_type = st.multiselect(
            "请选择顾客类型: ",
            options=customer_type_unique,
            default=customer_type_unique,
        )
        gender_unique = df["性别"].unique()
        gender = st.multiselect(
            "请选择性别",
            options=gender_unique,
            default=gender_unique,
        )
        df_selection = df.query(
            "城市 == @city & 顾客类型 == @customer_type & 性别 == @gender"
        )
        return df_selection

def product_line_chart(df):
    sales_by_product_line = (
        df.groupby(by=["产品类型"])["总价"].sum().sort_values()
    )
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="总价",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>"
    )
    return fig_product_sales

sale_df = get_dataframe_from_excel()
df_selection = add_sidebar_func(sale_df)
product_fig = product_line_chart(df_selection)
st.plotly_chart(product_fig)
