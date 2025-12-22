import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random
from datetime import datetime

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置页面配置
st.set_page_config(
    page_title="南宁美食数据仪表盘",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #e63946;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #457b9d;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #a8dadc;
        padding-bottom: 0.5rem;
    }
    .card {
        background-color: #f1faee;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    .metric-card {
        background-color: #a8dadc;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .restaurant-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #e63946;
    }
    .restaurant-name {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1d3557;
    }
    .restaurant-info {
        color: #457b9d;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown('<h1 class="main-header">🍜 南宁美食数据仪表盘</h1>', unsafe_allow_html=True)

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

# 加载数据
restaurant_df = create_restaurant_data()
price_df = create_monthly_price_data()
category_df = create_category_data()
visitor_df = create_visitor_data()
district_df = create_district_data()

# 侧边栏
with st.sidebar:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🎛️ 数据筛选")
    
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
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 显示统计信息
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("餐厅总数", len(restaurant_df))
    avg_rating = restaurant_df['rating'].mean()
    st.metric("平均评分", f"{avg_rating:.1f}")
    st.metric("数据更新时间", datetime.now().strftime("%Y-%m-%d"))
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 图表说明")
    st.info("""
    1. **价格走势图**: 显示5家餐厅12个月的价格变化
    2. **类别分布图**: 显示不同美食类别的店铺数量
    3. **访客量面积图**: 显示各类美食每月访客量变化
    4. **行政区分布图**: 显示餐厅在南宁各区的分布
    """)

# 主页面布局
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("最高评分", f"{restaurant_df['rating'].max():.1f}")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    avg_price = restaurant_df['avg_price'].mean()
    st.metric("平均价格", f"¥{avg_price:.0f}")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    total_reviews = restaurant_df['review_count'].sum()
    st.metric("总评论数", f"{total_reviews:,}")
    st.markdown("</div>", unsafe_allow_html=True)

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
st.markdown('<h2 class="sub-header">📈 餐厅价格走势（12个月）</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

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
    
    # 使用matplotlib创建折线图
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#e63946', '#457b9d', '#2a9d8f', '#e9c46a', '#f4a261']
    
    for i, restaurant in enumerate(selected_restaurants):
        restaurant_data = filtered_price_df[filtered_price_df['餐厅'] == restaurant]
        restaurant_data = restaurant_data.sort_values('月份序号')
        
        color_idx = i % len(colors)
        ax.plot(restaurant_data['月份'], restaurant_data['价格指数'], 
                marker='o', linewidth=2.5, label=restaurant, color=colors[color_idx])
    
    ax.set_title('南宁热门餐厅12个月价格走势', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('月份', fontsize=12)
    ax.set_ylabel('价格指数', fontsize=12)
    ax.legend(title='餐厅名称', loc='upper left', bbox_to_anchor=(1, 1))
    ax.grid(True, alpha=0.3)
    ax.set_xticks(range(len(filtered_price_df['月份'].unique())))
    ax.set_xticklabels(filtered_price_df['月份'].unique(), rotation=45)
    
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.warning("请至少选择一家餐厅以显示价格走势图")

st.markdown("</div>", unsafe_allow_html=True)

# 柱状图和面积图并排显示
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h2 class="sub-header">📊 美食类别分布</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # 创建柱状图
    fig, ax = plt.subplots(figsize=(8, 6))
    
    bars = ax.bar(category_df['美食类别'], category_df['店铺数量'], 
                  color=['#e63946', '#457b9d', '#2a9d8f', '#e9c46a', '#f4a261'])
    
    ax.set_title('南宁美食类别分布', fontsize=14, fontweight='bold')
    ax.set_xlabel('美食类别', fontsize=12)
    ax.set_ylabel('店铺数量', fontsize=12)
    
    # 在每个柱子上添加数值
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{int(height)}', ha='center', va='bottom', fontsize=10)
    
    ax.grid(True, alpha=0.3, axis='y')
    plt.xticks(rotation=15)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<h2 class="sub-header">📈 各类美食访客量趋势</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # 创建面积图
    fig, ax = plt.subplots(figsize=(8, 6))
    
    months = visitor_df['月份']
    categories = ['米粉类', '广西菜类', '烧烤类', '小吃类']
    colors = ['#e63946', '#457b9d', '#2a9d8f', '#e9c46a']
    
    # 创建堆叠面积图
    bottom_values = np.zeros(len(months))
    
    for i, category in enumerate(categories):
        values = visitor_df[category].values
        ax.fill_between(range(len(months)), bottom_values, bottom_values + values, 
                        alpha=0.7, label=category, color=colors[i])
        bottom_values += values
    
    ax.set_title('各类美食每月访客量变化', fontsize=14, fontweight='bold')
    ax.set_xlabel('月份', fontsize=12)
    ax.set_ylabel('访客量', fontsize=12)
    ax.legend(title='美食类别', loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_xticks(range(len(months)))
    ax.set_xticklabels(months, rotation=45)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("</div>", unsafe_allow_html=True)

# 行政区分布图
st.markdown('<h2 class="sub-header">🗺️ 南宁各行政区美食分布</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# 创建柱状图展示行政区分布
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(district_df['行政区'], district_df['店铺数量'], 
              color=['#e63946', '#457b9d', '#2a9d8f', '#e9c46a', '#f4a261', '#264653'])

ax.set_title('南宁各行政区美食店铺数量', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('行政区', fontsize=12)
ax.set_ylabel('店铺数量', fontsize=12)

# 在每个柱子上添加数值
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{int(height)}', ha='center', va='bottom', fontsize=10)

ax.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=15)
plt.tight_layout()
st.pyplot(fig)

st.markdown("</div>", unsafe_allow_html=True)

# 餐厅详细信息
st.markdown('<h2 class="sub-header">📋 餐厅详细信息</h2>', unsafe_allow_html=True)

# 显示筛选后的餐厅
if len(filtered_df) > 0:
    for idx, row in filtered_df.iterrows():
        st.markdown(f"""
        <div class="restaurant-card">
            <div class="restaurant-name">{row['name']} ⭐ {row['rating']}</div>
            <div class="restaurant-info">
                类别: {row['category']} | 人均: ¥{row['avg_price']} | 评论数: {row['review_count']}<br>
                招牌菜: {row['popular_dish']} | 开业年份: {row['open_year']}<br>
                地址: {row['address']} ({row['district']})
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("没有找到符合条件的餐厅，请调整筛选条件")

# 数据表格
st.markdown('<h2 class="sub-header">📊 完整数据表格</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

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

st.markdown("</div>", unsafe_allow_html=True)

# 页脚
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "南宁美食数据仪表盘 © 2023 | 数据仅供参考 | 最后更新: " + 
    datetime.now().strftime("%Y-%m-%d %H:%M") +
    "</div>", 
    unsafe_allow_html=True
)
