import pandas as pd
import streamlit as st
import plotly.express as px


def get_dataframe_from_excel():
    """从Excel读取销售数据并处理小时数列"""
    df = pd.read_excel(
        'supermarket_sales.xlsx',
        sheet_name='销售数据',
        skiprows=1,
        index_col='订单号'
    )
    # 从时间列提取小时数
    df["小时数"] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
    return df


def add_sidebar_func(df):
    """创建侧边栏筛选器并返回筛选后的数据"""
    with st.sidebar:
        st.header("请筛选数据:")
        # 城市筛选
        city = st.multiselect(
            "请选择城市:",
            options=df["城市"].unique(),
            default=df["城市"].unique()
        )
        # 顾客类型筛选
        customer_type = st.multiselect(
            "请选择顾客类型: ",
            options=df["顾客类型"].unique(),
            default=df["顾客类型"].unique()
        )
        # 性别筛选
        gender = st.multiselect(
            "请选择性别",
            options=df["性别"].unique(),
            default=df["性别"].unique()
        )
        # 应用筛选条件
        df_selection = df.query(
            "城市 == @city & 顾客类型 == @customer_type & 性别 == @gender"
        )
        return df_selection


def hourly_sales_chart(df):
    """生成按小时数划分的销售额柱状图"""
    sales_by_hour = df.groupby(by=["小时数"])["总价"].sum().reset_index()
    fig = px.bar(
        sales_by_hour,
        x="小时数",
        y="总价",
        title="<b>按小时数划分的销售额</b>"
    )
    # 调整图表样式（透明背景）
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="小时数",
        yaxis_title="总价"
    )
    return fig


def product_line_chart(df):
    """生成按产品类型划分的销售额横向条形图"""
    sales_by_product = df.groupby(by=["产品类型"])["总价"].sum().sort_values().reset_index()
    fig = px.bar(
        sales_by_product,
        x="总价",
        y="产品类型",
        orientation="h",
        title="<b>按产品类型划分的销售额</b>"
    )
    # 调整图表样式（透明背景）
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="总价",
        yaxis_title="产品类型"
    )
    return fig


def main():
    # 页面配置（宽布局+图标）
    st.set_page_config(page_title="销售表", page_icon="📊", layout="wide")

    # 读取数据并筛选
    sale_df = get_dataframe_from_excel()
    df_selection = add_sidebar_func(sale_df)

    # 计算核心指标
    total_sales = df_selection["总价"].sum()
    average_rating = df_selection["评分"].mean()
    average_sale_per_order = df_selection["总价"].mean()

    # 页面标题与分隔线
    st.title("📊 销量表")
    st.divider()

    # 展示核心指标（三列布局）
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("总销售额:")
        st.subheader(f"RMB ¥ {total_sales:,.2f}")
    with col2:
        st.subheader("顾客评分的平均值:")
        st.subheader(f"{average_rating:.1f} ⭐")
    with col3:
        st.subheader("每单的平均销售额:")
        st.subheader(f"RMB ¥ {average_sale_per_order:,.2f}")

    # 生成并展示图表（两列布局）
    hourly_fig = hourly_sales_chart(df_selection)
    product_fig = product_line_chart(df_selection)

    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.plotly_chart(hourly_fig, use_container_width=True)
    with col_chart2:
        st.plotly_chart(product_fig, use_container_width=True)

    # 添加分隔线
    st.divider()

    # 展示筛选后的数据表
    st.subheader("📋 筛选后的销售数据")

    # 显示数据基本信息
    st.write(f"**数据概览**: 共 {len(df_selection)} 条记录, {len(df_selection.columns)} 个字段")

    # 显示数据表
    st.dataframe(
        df_selection,
        use_container_width=True,
        height=400,  # 设置表格高度
        hide_index=False  # 显示索引（订单号）
    )


if __name__ == "__main__":
    main()

