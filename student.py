# 导入Streamlit库，用于创建Web应用程序界面
import streamlit as st
# 导入pandas库，用于数据处理和分析
import pandas as pd
# 导入numpy库，用于数值计算
import numpy as np
# 导入plotly.express库，用于创建交互式图表
import plotly.express as px
# 导入plotly.graph_objects库，用于创建高级图表对象
import plotly.graph_objects as go

# 设置页面配置，包括标题、图标、布局和侧边栏状态
st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 在侧边栏创建导航菜单标题
st.sidebar.title("导航菜单")
# 创建单选按钮，让用户选择功能页面
nav_option = st.sidebar.radio(
    "选择功能",
    ["项目首页", "数据分析", "成绩预测"]
)
########################################################################################################################
# 当用户选择"项目首页"时执行以下代码
if nav_option == "项目首页":
    # 设置页面标题
    st.title("学生成绩分析与预测系统")

    # 创建两列布局，比例为2:1，用于显示项目信息和图片
    col1, col2 = st.columns([2, 1])  # 调整列比例
    with col1:
        # 显示项目概述标题
        st.header("项目概述")
        # 使用HTML标签显示项目描述，字体较小
        st.markdown("<p>本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。</p>", unsafe_allow_html=True)

        # 显示主要特点标题
        st.header("主要特点")
        # 列出系统的主要特点
        st.write("• 📊 数据可视化：多维度展示学生学业数据")
        st.write("• 🎯 专业分析：按专业分类的详细统计分析")
        st.write("• 🧠 智能预测：基于机器学习模型的成绩预测")
        st.write("• 💡 学习建议：根据预测结果提供个性化反馈")

    with col2:
        # 初始化会话状态中的图片索引
        st.session_state.idx = st.session_state.get('idx', 0)
        # 定义要轮播的图片路径列表
        images = ["img/主页1.png", "img/主页2.png", "img/主页3.png"]
        # 显示当前图片
        st.image(images[st.session_state.idx], width="stretch")
        # 创建两列用于放置上一张和下一张按钮
        prev_col, next_col = st.columns([5, 1])

        # 实现图片轮播功能，支持任意数量的图片
        if prev_col.button("上一张"):
            st.session_state.idx = (st.session_state.idx - 1) % len(images)
            st.rerun()
        if next_col.button("下一张"):
            st.session_state.idx = (st.session_state.idx + 1) % len(images)
            st.rerun()

    # 添加分割线
    st.divider()

    # 显示项目目标标题
    st.header("🚀 项目目标")

    # 创建三列布局显示项目目标
    col1, col2, col3 = st.columns(3)

    with col1:
        # 显示第一个目标
        st.subheader("🎯 目标一")
        st.write("• 分析影响因素")
        st.write("• 探索相关性关系")
        st.write("• 建立成绩预测模型")

    with col2:
        # 显示第二个目标
        st.subheader("📈 目标二")
        st.write("• 可视化展示")
        st.write("• 多维度分析")
        st.write("• 学习模式识别")

    with col3:
        # 显示第三个目标
        st.subheader("🔮 目标三")
        st.write("• 成绩预测")
        st.write("• 个性化预测")
        st.write("• 及时干预预警")

    # 添加分割线
    st.divider()

    # 显示技术架构标题
    st.header("🏗️ 技术架构")

    # 定义技术架构数据
    tech_arch_data = [
        ("📥 数据收集", "Streamlit+Python"),
        ("🔧 数据处理", "Pandas+Numpy"),
        ("🤖 机器学习", "Scikit-learn"),
        ("📊 成果展示", "Seaborn+Matplotlib")
    ]

    # 创建四列布局显示技术架构
    cols = st.columns(4)
    for i, (tech, tools) in enumerate(tech_arch_data):
        with cols[i]:
            # 显示技术分类和对应工具
            st.write(tech)
            st.write(tools)

# 添加制作人信息
    st.divider()
    st.markdown("<p>制作人：浮梦</p>", unsafe_allow_html=True)

########################################################################################################################
# 当用户选择"数据分析"时执行以下代码
elif nav_option == "数据分析":
    # 设置页面标题
    st.title("📊 专业数据分析")

    # 从CSV文件读取学生数据
    df = pd.read_csv("student_data_adjusted_rounded.csv", encoding="utf-8")

    # 重命名数据框的列名，使用中文标签
    df.columns = ["学号", "性别", "专业", "每周学习时间", "上课出勤率", "期中考试分数", "平时作业分数", "期末考试分数"]

    # 按专业分组计算平均值统计信息
    major_stats = df.groupby("专业").agg({
        "每周学习时间": "mean",
        "期中考试分数": "mean",
        "期末考试分数": "mean"
    }).round(2)

    # 显示第一个分析内容：各专业男女性别比例
    st.subheader("1. 各专业男女性别比例")

    # 创建两列布局，左侧显示图表，右侧显示表格
    col_chart, col_table = st.columns([3, 2])

    with col_chart:
        # 计算各专业的男女人数
        gender_counts = df.groupby(["专业", "性别"]).size().unstack(fill_value=0)

        # 创建双层柱状图显示性别比例
        fig1 = go.Figure(data=[
            go.Bar(name='男', x=gender_counts.index, y=gender_counts.get('男', [0]*len(gender_counts)), marker_color='#1f77b4'),
            go.Bar(name='女', x=gender_counts.index, y=gender_counts.get('女', [0]*len(gender_counts)), marker_color='#ff7f0e')
        ])

        # 更新图表布局
        fig1.update_layout(title='各专业男女性别比例', barmode='group')
        # 在Streamlit中显示图表
        st.plotly_chart(fig1, use_container_width=True)

    with col_table:
        # 在右侧表格中显示性别分布数据
        st.write("### 性别分布数据")
        st.dataframe(gender_counts)

    # 添加分割线
    st.divider()

    # 显示第二个分析内容：各专业学习指标对比
    st.subheader("2. 各专业学习指标对比")

    # 创建两列布局，左侧显示图表，右侧显示表格
    col_chart, col_table = st.columns([3, 2])

    with col_chart:
        # 创建组合图表：折线图显示考试分数，柱状图显示学习时间
        fig2 = go.Figure()

        # 添加柱状图-学习时间左侧y轴
        fig2.add_trace(go.Bar(
            name='每周学习时间',
            x=major_stats.index,
            y=major_stats['每周学习时间'],
            marker_color='#B0E0E6',
            yaxis='y1'  # y1轴（左侧）
        ))

        # 添加折线图-考试分数右侧y2轴
        fig2.add_trace(go.Scatter(
            name='期中考试',
            x=major_stats.index,
            y=major_stats['期中考试分数'],
            mode='lines+markers',
            marker_color='#2ca02c',
            yaxis='y2'  # y2轴（右侧）
        ))
        fig2.add_trace(go.Scatter(
            name='期末考试',
            x=major_stats.index,
            y=major_stats['期末考试分数'],
            mode='lines+markers',
            marker_color='#d62728',
            yaxis='y2'  # y2轴（右侧）
        ))

        # 更新图表布局
        fig2.update_layout(
            title='各专业学习指标对比',
            xaxis_title='专业',
            yaxis2=dict(overlaying='y', side='right')
        )

        # 在Streamlit中显示图表
        st.plotly_chart(fig2, use_container_width=True)

    with col_table:
        # 在右侧表格中显示学习指标数据
        st.write("### 学习指标数据")
        st.dataframe(major_stats[['每周学习时间', '期中考试分数', '期末考试分数']])

    # 添加分割线
    st.divider()
########################################################################################################################
    # 显示第三个分析内容：各专业平均上课出勤率
    st.subheader("3. 各专业平均上课出勤率")

    # 创建两列布局，左侧显示图表，右侧显示表格
    col_chart, col_table = st.columns([3, 2])

    with col_chart:
        # 计算各专业的平均出勤率
        attendance_stats = df.groupby("专业")["上课出勤率"].mean().round(3)

        # 创建渐变色柱状图显示各专业出勤率
        fig3 = go.Figure(data=[
            go.Bar(
                x=attendance_stats.index,
                y=attendance_stats,
                marker=dict(
                    color=attendance_stats,
                    colorscale='Rainbow'
                )
            )
        ])

        # 更新图表布局
        fig3.update_layout(
            title='各专业平均出勤率',
            xaxis_title='专业',
            yaxis_title='出勤率',
            yaxis_range=[0.6, 1.0]  # 设置Y轴范围，使差异更明显
        )
        # 在Streamlit中显示图表
        st.plotly_chart(fig3, use_container_width=True)

    with col_table:
        # 创建出勤率排名表格
        st.write("### 出勤率排名")
        attendance_df = pd.DataFrame({
            '专业': attendance_stats.index,
            '平均出勤率': (attendance_stats * 100).round(1).astype(str) + '%'
        })
        # 添加排名并按出勤率降序排列
        attendance_df['排名'] = attendance_df.index.to_series().rank(ascending=False, method='min')
        attendance_df = attendance_df.sort_values('排名').reset_index(drop=True)
        # 重新排序列
        attendance_df = attendance_df[['排名', '专业', '平均出勤率']]
        st.dataframe(attendance_df, use_container_width=True)

    # 添加分割线
    st.divider()

    # 显示第四个分析内容：大数据管理专业专项分析
    st.subheader("4. 大数据管理专业专项分析")

    # 筛选大数据管理专业的数据
    big_data_df = df[df["专业"] == "大数据管理"]

    if not big_data_df.empty:
        # 计算统计数据
        avg_attendance = big_data_df["上课出勤率"].mean().round(3)
        avg_final_score = big_data_df["期末考试分数"].mean().round(2)
        avg_mid_score = big_data_df["期中考试分数"].mean().round(2)

        # 创建两列布局，左侧显示图表，右侧显示表格
        col_chart, col_table = st.columns([3, 2])

        with col_chart:
            # 创建两列布局显示指标
            col1, col2 = st.columns(2)

            with col1:
                # 显示平均上课出勤率
                st.metric(label="平均上课出勤率", value=f"{avg_attendance*100:.1f}%")

            with col2:
                # 显示期末考试平均分
                st.metric(label="期末考试平均分", value=avg_final_score)

            # 添加期末考试分数分布直方图
            fig4 = px.histogram(big_data_df, x="期末考试分数", nbins=20, title="大数据管理专业期末考试分数分布")
            st.plotly_chart(fig4, use_container_width=True)

        with col_table:
            # 显示大数据管理专业的详细数据
            st.write("### 大数据管理专业数据")
            st.dataframe(big_data_df[['学号', '性别', '每周学习时间', '上课出勤率', '期中考试分数', '期末考试分数']])
    else:
        # 如果没有大数据管理专业的数据，显示提示信息
        st.write("没有找到大数据管理专业的数据")

# 当用户选择"成绩预测"时执行以下代码
elif nav_option == "成绩预测":
    # 设置页面标题
    st.title("期末成绩预测")

    # 添加分割线
    st.divider()

    # 初始化会话状态，用于存储预测结果
    if "predicted_score" not in st.session_state:
        st.session_state.predicted_score = None

    # 创建输入表单标题
    st.subheader("输入学生学习数据")
    # 学号输入框
    student_id = st.text_input("学号", "20230101")

    # 专业选择下拉菜单
    major = st.selectbox(
        "专业",
        ["工商管理", "人工智能", "财务管理", "电子商务", "大数据管理"]
    )

    # 各项指标的滑块输入
    midterm_score = st.slider("期中考试成绩", 0, 100, 75)
    attendance = st.slider("上课出勤率", 0, 100, 90)
    homework_completion = st.slider("作业完成率", 0, 100, 90)
    study_hours = st.slider("每周学习时长（小时）", 0, 50, 20)

    # 预测按钮
    if st.button("预测成绩"):
        # 加载机器学习模型
        import joblib
        model = joblib.load('score_prediction_model.pkl')

        # 准备输入数据
        input_data = [[midterm_score, attendance/100, homework_completion/100, study_hours]]

        # 进行预测
        prediction = model.predict(input_data)[0]
        predicted_score = round(prediction)

        # 将预测结果存储到会话状态
        st.session_state.predicted_score = predicted_score

        # 添加分割线
        st.divider()

        # 在分割线下方显示烟花图片和预测结果
        st.subheader("预测结果")

        # 根据预测成绩选择对应的图片
        if predicted_score >= 90:
            firework_image = "img/优秀.png"  # 优秀对应1.png
        elif predicted_score >= 80:
            firework_image = "img/良好.png"  # 良好对应2.png
        elif predicted_score >= 60:
            firework_image = "img/及格.png"  # 及格对应3.png
        else:
            firework_image = "img/不及格.png"  # 不及格对应4.png

        # 居中显示烟花图片
        _, col, _ = st.columns([1, 1, 1])
        col.image(firework_image, width=400)

        # 显示预测结果
        if st.session_state.predicted_score is not None:
            predicted_score = st.session_state.predicted_score

            st.success(f"预测期末成绩: {predicted_score}分")

            # 显示预测结果分析标题
            st.subheader("预测结果分析")

            # 根据预测成绩显示不同的评价
            if predicted_score >= 90:
                st.markdown("<span style='color: green; font-size: 18px;'>🎉 优秀！继续保持！</span>", unsafe_allow_html=True)
            elif predicted_score >= 80:
                st.markdown("<span style='color: blue; font-size: 18px;'>👍 良好！再加把劲！</span>", unsafe_allow_html=True)
            elif predicted_score >= 60:
                st.markdown("<span style='color: orange; font-size: 18px;'>⚠️ 及格！需要努力！</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span style='color: red; font-size: 18px;'>❌ 不及格！需要加倍努力！</span>", unsafe_allow_html=True)
