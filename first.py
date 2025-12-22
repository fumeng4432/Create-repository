import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
from streamlit.components.v1 import html

# 页面配置
st.set_page_config(
    page_title="餐厅评分系统",
    page_icon="🍽️",
    layout="wide"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 36px;
        font-weight: bold;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 30px;
    }
    .section-header {
        font-size: 24px;
        font-weight: bold;
        color: #4ECDC4;
        margin-bottom: 15px;
        border-bottom: 2px solid #4ECDC4;
        padding-bottom: 5px;
    }
    .restaurant-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .price-tag {
        background-color: #FFD166;
        color: #333;
        padding: 5px 10px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 5px;
    }
    .stat-box {
        background-color: #F8F9FA;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 5px solid #4ECDC4;
    }
    .recommendation-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# 应用标题
st.markdown('<div class="main-header">🍽️ 餐厅评分系统</div>', unsafe_allow_html=True)

# 创建两列布局
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.markdown('<div class="section-header">📊 不同类型餐厅价格分布</div>', unsafe_allow_html=True)
    
    # 创建餐厅价格数据
    restaurant_types = ['中式快餐', '西式餐厅', '日料', '火锅', '烧烤', '咖啡简餐']
    avg_prices = [35, 85, 120, 95, 80, 45]
    rating_scores = [4.2, 4.5, 4.8, 4.6, 4.3, 4.4]
    
    # 创建交互式图表
    fig = go.Figure()
    
    # 添加柱状图
    fig.add_trace(go.Bar(
        x=restaurant_types,
        y=avg_prices,
        name='平均价格',
        marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'],
        text=[f'¥{price}' for price in avg_prices],
        textposition='auto',
    ))
    
    # 添加评分折线图（次y轴）
    fig.add_trace(go.Scatter(
        x=restaurant_types,
        y=rating_scores,
        name='评分',
        yaxis='y2',
        line=dict(color='#333333', width=3),
        mode='lines+markers',
        marker=dict(size=10, symbol='star')
    ))
    
    fig.update_layout(
        title='不同类型餐厅价格与评分对比',
        xaxis_title='餐厅类型',
        yaxis_title='平均价格 (元)',
        yaxis2=dict(
            title='评分',
            overlaying='y',
            side='right',
            range=[3.5, 5.0]
        ),
        height=400,
        showlegend=True,
        plot_bgcolor='rgba(240, 242, 246, 0.8)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 用餐高峰时段
    st.markdown('<div class="section-header">⏰ 用餐高峰时段</div>', unsafe_allow_html=True)
    
    # 生成高峰时段数据
    hours = list(range(24))
    traffic = [5, 2, 1, 1, 1, 8, 15, 20, 25, 20, 15, 30, 40, 35, 30, 25, 40, 65, 80, 75, 60, 40, 20, 10]
    
    peak_df = pd.DataFrame({
        '小时': hours,
        '客流量': traffic
    })
    
    # 创建热力图
    fig2 = px.density_heatmap(
        peak_df,
        x='小时',
        y=['客流量'],
        nbinsx=24,
        title='24小时客流量分布',
        color_continuous_scale='Reds'
    )
    
    fig2.update_layout(height=200)
    st.plotly_chart(fig2, use_container_width=True)
    
    # 列出高峰时段
    st.markdown("**高峰时段：**")
    peak_hours = [(i, traffic[i]) for i in range(len(traffic)) if traffic[i] > 50]
    for hour, flow in peak_hours:
        st.markdown(f"- **{hour:02d}:00** - {flow}% 客流量")

with col2:
    st.markdown('<div class="section-header">🏪 餐厅详情</div>', unsafe_allow_html=True)
    
    # 餐厅详情卡片
    st.markdown("""
    <div class="restaurant-card">
        <div style="text-align: center; margin-bottom: 15px;">
            <h3 style="margin: 0; color: white;">🍜 美食汇餐厅</h3>
            <p style="margin: 5px 0; opacity: 0.9;">⭐ 评分: 4.8/5.0</p>
        </div>
        
        <div style="background: rgba(255, 255, 255, 0.2); padding: 10px; border-radius: 8px; margin-bottom: 10px;">
            <p style="margin: 5px 0;"><strong>🕐 营业时间:</strong> 00:00 - 24:00</p>
            <p style="margin: 5px 0;"><strong>👥 好友数:</strong> 0</p>
            <p style="margin: 5px 0;"><strong>💰 今日营业额:</strong> 4,775.0 元</p>
        </div>
        
        <div style="margin-top: 15px;">
            <p style="margin-bottom: 5px;"><strong>人均消费:</strong></p>
            <div style="display: flex; align-items: center;">
                <span class="price-tag">35元</span>
                <div style="flex-grow: 1; margin-left: 15px;">
                    <div style="background: rgba(255, 255, 255, 0.3); height: 10px; border-radius: 5px;">
                        <div style="background: #FFD166; width: 70%; height: 100%; border-radius: 5px;"></div>
                    </div>
                    <p style="margin: 5px 0 0 0; font-size: 12px; text-align: center;">当前消费程度</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 位置信息
    st.markdown('<div class="section-header">📍 位置信息</div>', unsafe_allow_html=True)
    
    # 创建地图HTML
    map_html = """
    <iframe 
        width="100%" 
        height="300" 
        frameborder="0" 
        scrolling="no" 
        marginheight="0" 
        marginwidth="0" 
        src="https://map.qq.com/m/place/search/%E9%A4%90%E5%8E%85/center=116.397428,39.90923/zoom=15">
    </iframe>
    """
    
    html(map_html, height=300)
    
    st.markdown("""
    <div style="background-color: #E8F4FD; padding: 10px; border-radius: 5px; margin-top: 10px;">
        <p style="margin: 0; font-size: 14px; color: #1890FF;">
            💡 <strong>提示：</strong>点击上方地图可查看餐厅位置，或使用
            <a href="https://lbs.qq.com/tool/getpoint/get-point.html" target="_blank">
                腾讯坐标拾取器
            </a>
            获取精确坐标
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown('<div class="section-header">🍽️ 今日午餐推荐</div>', unsafe_allow_html=True)
    
    # 推荐菜品
    recommendations = [
        {"name": "宫保鸡丁套餐", "price": 38, "rating": 4.7, "calories": 450, "type": "中式"},
        {"name": "日式照烧鸡排饭", "price": 42, "rating": 4.8, "calories": 520, "type": "日式"},
        {"name": "番茄牛肉意面", "price": 45, "rating": 4.6, "calories": 480, "type": "西式"},
        {"name": "健康蔬菜沙拉", "price": 32, "rating": 4.5, "calories": 320, "type": "轻食"}
    ]
    
    for i, rec in enumerate(recommendations):
        st.markdown(f"""
        <div class="recommendation-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin: 0;">{rec['name']}</h4>
                <span style="background: white; color: #f5576c; padding: 3px 10px; border-radius: 15px; font-weight: bold;">
                    ¥{rec['price']}
                </span>
            </div>
            <div style="margin-top: 10px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span>⭐ {rec['rating']}/5.0</span>
                    <span>🔥 {rec['calories']} 卡路里</span>
                </div>
                <div style="background: rgba(255, 255, 255, 0.3); height: 8px; border-radius: 4px; margin-bottom: 5px;">
                    <div style="background: white; width: {rec['rating']*20}%; height: 100%; border-radius: 4px;"></div>
                </div>
                <p style="margin: 0; font-size: 14px;">🏷️ 类型: {rec['type']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # 统计数据
    st.markdown('<div class="section-header">📈 今日统计</div>', unsafe_allow_html=True)
    
    stats_col1, stats_col2 = st.columns(2)
    
    with stats_col1:
        st.markdown("""
        <div class="stat-box">
            <h3 style="margin: 0; color: #4ECDC4;">1</h3>
            <p style="margin: 5px 0 0 0; font-size: 14px;">今日推荐早餐数量</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col2:
        st.markdown("""
        <div class="stat-box">
            <h3 style="margin: 0; color: #FF6B6B;">1</h3>
            <p style="margin: 5px 0 0 0; font-size: 14px;">其他推荐数量</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 评分分布
    st.markdown("### 📊 评分分布")
    ratings = [4.2, 4.5, 4.8, 4.6, 4.3, 4.4]
    avg_rating = np.mean(ratings)
    
    fig3 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_rating,
        title={'text': "平均评分"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 5], 'tickwidth': 1},
            'bar': {'color': "#4ECDC4"},
            'steps': [
                {'range': [0, 3], 'color': "lightgray"},
                {'range': [3, 4], 'color': "gray"},
                {'range': [4, 5], 'color': "darkgray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': avg_rating
            }
        }
    ))
    
    fig3.update_layout(height=250)
    st.plotly_chart(fig3, use_container_width=True)

# 底部信息
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 14px;">
    <p>🍽️ 餐厅评分系统 | 数据更新于: {}</p>
    <p>💡 提示：所有数据均为模拟数据，仅用于展示 purposes</p>
</div>
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)
