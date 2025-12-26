# 导入pandas库，用于数据处理和分析
import pandas as pd
# 导入streamlit库，用于创建Web应用
import streamlit as st
# 导入plotly.express库，用于创建交互式图表
import plotly.express as px
# 导入plotly.graph_objects用于创建更多图表类型
import plotly.graph_objects as go


def get_dataframe_from_excel():
    """从Excel读取销售数据并处理小时数列"""
    # 使用pandas读取Excel文件
    df = pd.read_excel(
        # 指定Excel文件路径
        'supermarket_sales.xlsx',
        # 指定要读取的工作表名称
        sheet_name='销售数据',
        # 跳过第一行（通常用于跳过标题行）
        skiprows=1,
        # 将'订单号'列设置为索引列
        index_col='订单号'
    )
    # 从"时间"列提取小时数：先将时间字符串转换为datetime对象，然后提取小时部分
    df["小时数"] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
    # 返回处理后的数据框
    return df


def add_sidebar_func(df):
    """创建侧边栏筛选器并返回筛选后的数据（修正筛选语法）"""
    # 在侧边栏创建容器
    with st.sidebar:
        # 在侧边栏添加标题
        st.header("请筛选数据:")
        # 创建城市多选筛选器
        city = st.multiselect(
            # 筛选器标签
            "请选择城市:",
            # 可选项：从数据框中获取所有唯一的城市值
            options=df["城市"].unique(),
            # 默认值：选择所有城市
            default=df["城市"].unique()
        )
        # 创建顾客类型多选筛选器
        customer_type = st.multiselect(
            "请选择顾客类型: ",
            options=df["顾客类型"].unique(),
            default=df["顾客类型"].unique()
        )
        # 创建性别多选筛选器
        gender = st.multiselect(
            "请选择性别",
            options=df["性别"].unique(),
            default=df["性别"].unique()
        )
        # 使用query方法根据筛选条件过滤数据框
        # @符号用于引用局部变量（筛选器选择的列表）
        df_selection = df.query(
            "城市.isin(@city) & 顾客类型.isin(@customer_type) & 性别.isin(@gender)"
        )
        # 返回筛选后的数据框
        return df_selection


def hourly_sales_chart(df):
    """生成按小时数划分的销售额柱状图"""
    # 按小时数分组并计算每个小时的总销售额
    sales_by_hour = df.groupby(by=["小时数"])["总价"].sum().reset_index()
    # 使用plotly创建柱状图
    fig = px.bar(
        # 数据源
        sales_by_hour,
        # x轴数据：小时数
        x="小时数",
        # y轴数据：总价（销售额）
        y="总价",
        # 图表标题，使用HTML标签加粗
        title="<b>按小时数划分的销售额</b>"
    )
    # 更新图表布局样式
    fig.update_layout(
        # 设置图表背景为透明
        plot_bgcolor="rgba(0,0,0,0)",
        # 设置x轴标题
        xaxis_title="小时数",
        # 设置y轴标题
        yaxis_title="总价"
    )
    # 返回图表对象
    return fig


def product_line_chart(df):
    """生成按产品类型划分的销售额横向条形图"""
    # 按产品类型分组并计算总销售额，然后按值排序
    sales_by_product = df.groupby(by=["产品类型"])["总价"].sum().sort_values().reset_index()
    # 创建横向条形图
    fig = px.bar(
        sales_by_product,
        # x轴：总价（销售额）
        x="总价",
        # y轴：产品类型
        y="产品类型",
        # 设置为横向条形图
        orientation="h",
        title="<b>按产品类型划分的销售额</b>"
    )
    # 更新图表布局样式
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="总价",
        yaxis_title="产品类型"
    )
    # 返回图表对象
    return fig


def rating_distribution_chart(df):
    """生成评分分布折线图"""
    # 按评分分组并计算每个评分的订单数量
    rating_counts = df.groupby(by=["评分"]).size().reset_index(name="订单数量")
    rating_counts = rating_counts.sort_values("评分")
    
    # 创建折线图
    fig = px.line(
        rating_counts,
        x="评分",
        y="订单数量",
        title="<b>顾客评分分布折线图</b>",
        markers=True,  # 在数据点上添加标记
        line_shape="linear"  # 线性连接
    )
    
    # 添加数据点标签
    fig.update_traces(
        mode="lines+markers",  # 同时显示线和标记
        marker=dict(size=8),   # 标记大小
        line=dict(width=3)     # 线宽
    )
    
    # 更新图表布局样式
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="评分",
        yaxis_title="订单数量",
        xaxis=dict(
            tickmode='linear',  # 线性刻度
            tick0=0,            # 从0开始
            dtick=1             # 步长为1
        )
    )
    
    # 添加阴影区域（可选）
    fig.add_trace(
        go.Scatter(
            x=rating_counts["评分"],
            y=rating_counts["订单数量"],
            fill='tozeroy',
            fillcolor='rgba(135, 206, 250, 0.3)',
            line=dict(color='rgba(255,255,255,0)'),
            showlegend=False,
            name=''
        )
    )
    
    return fig


def city_sales_comparison_chart(df):
    """生成城市销售额对比折线图"""
    # 按城市和小时数分组计算销售额
    city_hour_sales = df.groupby(by=["城市", "小时数"])["总价"].sum().reset_index()
    
    # 创建折线图，按城市分组
    fig = px.line(
        city_hour_sales,
        x="小时数",
        y="总价",
        color="城市",
        title="<b>各城市销售额对比折线图（按小时）</b>",
        markers=True,
        line_shape="spline"  # 平滑曲线
    )
    
    # 更新图表布局样式
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="小时数",
        yaxis_title="销售额",
        legend_title="城市"
    )
    
    return fig


def create_star_rating(rating):
    """创建星星评分显示"""
    full_stars = int(rating)
    half_star = 1 if rating - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    
    stars = "★" * full_stars
    if half_star:
        stars += "½"
    stars += "☆" * empty_stars
    
    return stars


def main():
    # 设置Streamlit页面配置
    # page_title：浏览器标签页标题
    # page_icon：浏览器标签页图标
    # layout：页面布局方式（"wide"为宽屏布局）
    st.set_page_config(page_title="销售表", page_icon="📊", layout="wide")

    # 从Excel文件读取数据
    sale_df = get_dataframe_from_excel()
    # 通过侧边栏筛选器获取筛选后的数据
    df_selection = add_sidebar_func(sale_df)

    # 计算核心业务指标
    # 总销售额：对"总价"列求和
    total_sales = df_selection["总价"].sum()
    # 平均评分：对"评分"列求平均值
    average_rating = df_selection["评分"].mean()
    # 每单平均销售额：总销售额除以订单数量
    average_sale_per_order = df_selection["总价"].mean()
    
    # 创建星星评分显示
    star_rating = create_star_rating(average_rating)

    # 页面主标题
    st.title("📊 销售仪表板")
    # 添加分隔线
    st.divider()

    # 创建三列布局展示核心指标
    col1, col2, col3 = st.columns(3)
    # 在第一列中显示总销售额
    with col1:
        # 指标标题
        st.subheader("总销售额:")
        # 格式化显示总销售额：千位分隔符，保留两位小数
        st.subheader(f"RMB ¥ {total_sales:,.2f}")
    # 在第二列中显示平均评分
    with col2:
        st.subheader("顾客平均评分:")
        # 使用星星显示评分
        st.subheader(f"{average_rating:.1f}")
        st.subheader(f"{star_rating}")
    # 在第三列中显示每单平均销售额
    with col3:
        st.subheader("每单平均销售额:")
        # 格式化显示每单平均销售额：千位分隔符，保留两位小数
        st.subheader(f"RMB ¥ {average_sale_per_order:,.2f}")

    # 生成四个图表
    hourly_fig = hourly_sales_chart(df_selection)
    product_fig = product_line_chart(df_selection)
    rating_fig = rating_distribution_chart(df_selection)
    city_fig = city_sales_comparison_chart(df_selection)

    # 创建两列布局展示图表
    col_chart1, col_chart2 = st.columns(2)
    # 在第一列中显示小时销售额图表
    with col_chart1:
        # 显示图表，use_container_width=True让图表宽度适配容器
        st.plotly_chart(hourly_fig, use_container_width=True)
    # 在第二列中显示产品类型销售额图表
    with col_chart2:
        st.plotly_chart(product_fig, use_container_width=True)
    
    # 添加分隔线
    st.divider()
    st.subheader("📈 评分与城市对比分析")
    
    # 创建另外两列布局展示新增的折线图
    col_chart3, col_chart4 = st.columns(2)
    with col_chart3:
        st.plotly_chart(rating_fig, use_container_width=True)
    with col_chart4:
        st.plotly_chart(city_fig, use_container_width=True)

    # 添加分隔线
    st.divider()

    # 展示筛选后的数据表格
    st.subheader("📋 筛选后的销售数据")

    # 显示数据基本信息：记录条数和字段数量
    st.write(f"**数据概览**: 共 {len(df_selection)} 条记录, {len(df_selection.columns)} 个字段")
    
    # 添加一些统计信息
    st.write(f"**评分统计**: 最高 {df_selection['评分'].max():.1f} 分, 最低 {df_selection['评分'].min():.1f} 分, 标准差 {df_selection['评分'].std():.2f}")

    # 显示数据表格
    st.dataframe(
        # 要显示的数据框
        df_selection,
        # 宽度适配容器
        use_container_width=True,
        # 设置表格高度为400像素
        height=400,
        # 显示索引列（订单号）
        hide_index=False
    )


# Python标准写法：当脚本直接运行时执行main函数
if __name__ == "__main__":
    main()
