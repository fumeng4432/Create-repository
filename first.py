import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

# 设置页面配置
st.set_page_config(
    page_title="南宁美食数据仪表盘",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 标题
st.title("🍜 南宁美食数据仪表盘")

# 创建模拟数据
def create_restaurant_data():
    """创建餐厅基本信息"""
    restaurants = [
        {
            'name': '老友记粉店',
            'category': '米粉',
            'rating': 4.7,
            'avg_price': 25,
            'review_count': 1280,
            'address': '青秀区民族大道86号',
            'popular_dish': '老友粉',
            'open_year': 2015,
            'district': '青秀区'
        },
        {
            'name': '螺蛳粉大王',
            'category': '米粉',
            'rating': 4.5,
            'avg_price': 18,
            'review_count': 1560,
            'address': '兴宁区民生路42号',
            'popular_dish': '螺蛳粉',
            'open_year': 2018,
            'district': '兴宁区'
        },
        {
            'name': '桂小厨',
            'category': '广西菜',
            'rating': 4.8,
            'avg_price': 85,
            'review_count': 890,
            'address': '西乡塘区大学路100号',
            'popular_dish': '柠檬鸭',
            'open_year': 2012,
            'district': '西乡塘区'
        },
        {
            'name': '邕城食府',
            'category': '广西菜',
            'rating': 4.6,
            'avg_price': 120,
            'review_count': 760,
            'address': '良庆区五象大道28号',
            'popular_dish': '纸包鸡',
            'open_year': 2010,
            'district': '良庆区'
        },
        {
            'name': '复记老友',
            'category': '米粉',
            'rating': 4.4,
            'avg_price': 22,
            'review_count': 2100,
            'address': '江南区星光大道68号',
            'popular_dish': '老友伊面',
            'open_year': 2008,
            'district': '江南区'
        },
        {
            'name': '舒记粉店',
            'category': '米粉',
            'rating': 4.7,
            'avg_price': 20,
            'review_count': 1850,
            'address': '青秀区七星路128号',
            'popular_dish': '老友牛肉粉',
            'open_year': 2005,
            'district': '青秀区'
        },
        {
            'name': '瑶王府',
            'category': '广西菜',
            'rating': 4.5,
            'avg_price': 95,
            'review_count': 640,
            'address': '兴宁区朝阳路66号',
            'popular_dish': '恭城油茶',
            'open_year': 2016,
            'district': '兴宁区'
        },
        {
            'name': '中山路夜市烧烤',
            'category': '烧烤',
            'rating': 4.3,
            'avg_price': 65,
            'review_count': 3200,
            'address': '青秀区中山路美食街',
            'popular_dish': '烤生蚝',
            'open_year': 2000,
            'district': '青秀区'
        }
    ]
    return pd.DataFrame(restaurants)

def create_monthly_price_data():
    """创建每月价格走势数据"""
    months = ['1月', '2月', '3月', '4月', '5月', '6月', 
              '7月', '8月', '9月', '10月', '11月', '12月']
    
    restaurants = ['老友记粉店', '螺蛳粉大王', '桂小厨', '邕城食府', '复记老友', '舒记粉店']
    
    data = []
    for restaurant in restaurants:
        base_price = random.randint(15, 30) if '粉' in restaurant else random.randint(70, 120)
        
        for i, month in enumerate(months):
            # 模拟季节性价格波动
            seasonal_factor = 1.0
            if month in ['1月', '2月']:  # 春节旺季
                seasonal_factor = 1.15
            elif month in ['7月', '8月']:  # 暑假
                seasonal_factor = 1.08
            elif month in ['10月']:  # 国庆
                seasonal_factor = 1.12
            elif month in ['3月', '11月']:  # 淡季
                seasonal_factor = 0.95
            
            # 添加随机波动
            random_factor = random.uniform(0.98, 1.02)
            
            price = round(base_price * seasonal_factor * random_factor, 1)
            
            data.append({
                '餐厅': restaurant,
                '月份': month,
                '价格指数': price,
                '月份序号': i+1
            })
    
    return pd.DataFrame(data)

def create_category_data():
    """创建美食类别数据"""
    categories = ['米粉', '广西菜', '烧烤', '甜品', '小吃']
    counts = [45, 28, 32, 19, 52]
    avg_ratings = [4.5, 4.3, 4.2, 4.6, 4.4]
    avg_prices = [25, 85, 65, 18, 15]
    
    return pd.DataFrame({
        '美食类别': categories,
        '店铺数量': counts,
        '平均评分': avg_ratings,
        '平均价格': avg_prices
    })

def create_visitor_data():
    """创建每月访客量数据"""
    months = ['1月', '2月', '3月', '4月', '5月', '6月', 
              '7月', '8月', '9月', '10月', '11月', '12月']
    
    # 模拟不同类别店铺的访客量
    visitor_data = {
        '月份': months,
        '米粉类': [1200, 1500, 1300, 1400, 1600, 1550, 1650, 1700, 1450, 1600, 1400, 1550],
        '广西菜类': [800, 950, 850, 900, 1000, 980, 1020, 1050, 920, 1000, 880, 950],
        '烧烤类': [600, 700, 650, 680, 720, 750, 800, 850, 780, 820, 700, 750],
        '小吃类': [900, 1000, 950, 980, 1050, 1100, 1150, 1200, 1050, 1100, 950, 1000]
    }
    
    return pd.DataFrame(visitor_data)

def create_district_data():
    """创建行政区划数据"""
    districts = ['青秀区', '兴宁区', '西乡塘区', '江南区', '良庆区', '邕宁区']
    counts = [35, 28, 32, 24, 18, 12]
    
    return pd.DataFrame({
        '行政区': districts,
        '店铺数量': counts
    })

def create_map_data():
    """创建地图数据"""
    # 模拟南宁的地理位置数据
    map_data = pd.DataFrame({
        'lat': [22.8167, 22.8190, 22.8370, 22.7550, 22.7800, 22.8100, 22.8230, 22.8150],
        'lon': [108.3667, 108.3200, 108.2900, 108.3700, 108.3100, 108.3400, 108.3180, 108.3250],
        'name': ['老友记粉店', '螺蛳粉大王', '桂小厨', '邕城食府', '复记老友', '舒记粉店', '瑶王府', '中山路夜市烧烤'],
        'category': ['米粉', '米粉', '广西菜', '广西菜', '米粉', '米粉', '广西菜', '烧烤'],
        'rating': [4.7, 4.5, 4.8, 4.6, 4.4, 4.7, 4.5, 4.3],
        'size': [47, 45, 48, 46, 44, 47, 45, 43]
    })
    return map_data

# 加载数据
restaurant_df = create_restaurant_data()
price_df = create_monthly_price_data()
category_df = create_category_data()
visitor_df = create_visitor_data()
district_df = create_district_data()
map_df = create_map_data()

# 侧边栏
with st.sidebar:
    st.header("🎛️ 数据筛选")
    
    # 美食类别筛选
    categories = ['全部'] + list(restaurant_df['category'].unique())
    selected_category = st.selectbox("选择美食类别", categories)
    
    # 行政区筛选
    districts = ['全部'] + list(restaurant_df['district'].unique())
    selected_district = st.selectbox("选择行政区", districts)
    
    # 评分筛选
    min_rating, max_rating = st.slider(
        "选择评分范围", 
        min_value=4.0, 
        max_value=5.0, 
        value=(4.0, 5.0),
        step=0.1
    )
    
    # 价格筛选
    min_price, max_price = st.slider(
        "选择人均价格范围", 
        min_value=0, 
        max_value=150, 
        value=(10, 130),
        step=5
    )
    
    # 显示统计信息
    st.divider()
    st.metric("餐厅总数", len(restaurant_df))
    avg_rating = restaurant_df['rating'].mean()
    st.metric("平均评分", f"{avg_rating:.1f}")
    st.metric("数据更新时间", datetime.now().strftime("%Y-%m-%d"))
    
    st.divider()
    st.info("""
    **图表说明**
    1. **价格走势图**: 显示5家餐厅12个月的价格变化
    2. **类别分布图**: 显示不同美食类别的店铺数量
    3. **访客量面积图**: 显示各类美食每月访客量变化
    4. **美食地图**: 显示餐厅在南宁的分布位置
    """)

# 主页面布局
st.subheader("📊 关键指标")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.metric("最高评分", f"{restaurant_df['rating'].max():.1f}")

with col2:
    avg_price = restaurant_df['avg_price'].mean()
    st.metric("平均价格", f"¥{avg_price:.0f}")

with col3:
    total_reviews = restaurant_df['review_count'].sum()
    st.metric("总评论数", f"{total_reviews:,}")

# 应用筛选
filtered_df = restaurant_df.copy()
if selected_category != '全部':
    filtered_df = filtered_df[filtered_df['category'] == selected_category]

if selected_district != '全部':
    filtered_df = filtered_df[filtered_df['district'] == selected_district]

filtered_df = filtered_df[
    (filtered_df['rating'] >= min_rating) & 
    (filtered_df['rating'] <= max_rating) &
    (filtered_df['avg_price'] >= min_price) & 
    (filtered_df['avg_price'] <= max_price)
]

# 价格走势折线图
st.divider()
st.subheader("📈 餐厅价格走势（12个月）")

# 选择要显示的餐厅
available_restaurants = price_df['餐厅'].unique()
selected_restaurants = st.multiselect(
    "选择要显示的餐厅", 
    options=available_restaurants,
    default=available_restaurants[:5],
    key="line_chart_select"
)

if selected_restaurants:
    filtered_price_df = price_df[price_df['餐厅'].isin(selected_restaurants)]
    
    # 转换为宽格式，便于Streamlit绘制折线图
    price_pivot = filtered_price_df.pivot(index='月份序号', columns='餐厅', values='价格指数')
    
    # 按月份排序
    price_pivot = price_pivot.sort_index()
    
    # 使用Streamlit的line_chart
    st.line_chart(price_pivot)
    
    # 显示数据表格
    with st.expander("查看价格数据表格"):
        st.dataframe(price_pivot)
else:
    st.warning("请至少选择一家餐厅以显示价格走势图")

# 柱状图和面积图并排显示
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 美食类别分布")
    
    # 使用Streamlit的bar_chart
    # 设置索引为美食类别
    bar_chart_data = category_df.set_index('美食类别')['店铺数量']
    st.bar_chart(bar_chart_data)
    
    # 显示详细数据
    with st.expander("查看类别详细数据"):
        st.dataframe(category_df)

with col2:
    st.subheader("📈 各类美食访客量趋势")
    
    # 使用Streamlit的area_chart
    # 设置索引为月份
    area_chart_data = visitor_df.set_index('月份')[['米粉类', '广西菜类', '烧烤类', '小吃类']]
    st.area_chart(area_chart_data)
    
    # 显示详细数据
    with st.expander("查看访客量详细数据"):
        st.dataframe(visitor_df)

# 地图展示
st.divider()
st.subheader("🗺️ 南宁美食地图")

# 使用Streamlit的map功能
st.map(map_df)

# 显示地图上的餐厅信息
st.write("**地图上的餐厅:**")
cols = st.columns(4)
for i, (idx, row) in enumerate(map_df.iterrows()):
    with cols[i % 4]:
        st.write(f"**{row['name']}**")
        st.write(f"类别: {row['category']}")
        st.write(f"评分: {row['rating']}")

# 行政区分布图
st.divider()
st.subheader("🏙️ 南宁各行政区美食分布")

# 使用Streamlit的bar_chart
district_chart_data = district_df.set_index('行政区')['店铺数量']
st.bar_chart(district_chart_data)

# 显示详细数据
with st.expander("查看行政区详细数据"):
    st.dataframe(district_df)

# 餐厅详细信息
st.divider()
st.subheader("📋 餐厅详细信息")

# 显示筛选后的餐厅
if len(filtered_df) > 0:
    for idx, row in filtered_df.iterrows():
        with st.container():
            st.write(f"##### {row['name']} ⭐ {row['rating']}")
            st.write(f"**类别:** {row['category']} | **人均:** ¥{row['avg_price']} | **评论数:** {row['review_count']}")
            st.write(f"**招牌菜:** {row['popular_dish']} | **开业年份:** {row['open_year']}")
            st.write(f"**地址:** {row['address']} ({row['district']})")
            st.divider()
else:
    st.warning("没有找到符合条件的餐厅，请调整筛选条件")

# 数据表格
st.divider()
st.subheader("📊 完整数据表格")

# 格式化显示
display_df = filtered_df.copy()
display_df = display_df.rename(columns={
    'name': '餐厅名称',
    'category': '美食类别',
    'rating': '评分',
    'avg_price': '人均价格(元)',
    'review_count': '评论数',
    'address': '地址',
    'popular_dish': '招牌菜',
    'open_year': '开业年份',
    'district': '行政区'
})

# 重新排列列顺序
display_df = display_df[['餐厅名称', '美食类别', '评分', '人均价格(元)', '招牌菜', '评论数', '开业年份', '行政区', '地址']]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

# 页脚
st.divider()
st.caption(f"南宁美食数据仪表盘 © 2023 | 数据仅供参考 | 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
