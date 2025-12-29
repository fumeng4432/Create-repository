import streamlit as st  # 导入Streamlit库，用于创建Web应用
import pickle  # 导入pickle库，用于模型序列化和反序列化
import pandas as pd  # 导入pandas库，用于数据处理
# 设置页面的标题、图标和布局
st.set_page_config(
    page_title="医疗费用预测系统",  # 设置网页标题
    page_icon="🏥",  # 设置网页图标
    layout="centered"  # 设置页面居中布局
)
def introduce_page():  # 定义系统简介页面函数
    """当选择简介页面时，将呈现该函数的内容"""  # 函数文档字符串
    st.title("🏥 医疗费用预测系统")  # 显示页面标题
    st.sidebar.success("单击左侧导航栏的\"预测医疗费用\"开始使用")  # 在侧边栏显示成功提示
    st.markdown("""  # 使用markdown显示系统介绍内容
    ---
    ## 🔍 系统介绍
    本应用利用先进的机器学习技术，基于随机森林回归算法，为保险公司提供精准的医疗费用预测服务。
    ## 📊 模型算法
    - **算法类型**：随机森林回归（Random Forest Regression）
    - **特征维度**：年龄、BMI、子女数量、性别、吸烟状况、区域
    - **预测精度**：经过严格验证的高准确性模型
    """)  # 系统介绍内容
def predict_page():  # 定义预测页面函数
    """当选择预测费用页面时，将呈现该函数的内容"""  # 函数文档字符串
    st.title("💸 医疗费用预测")  # 显示预测页面标题
    st.markdown("""  # 使用markdown显示使用说明
    ---
    ## 📋 使用说明
    请输入被保险人的详细信息，系统将基于机器学习模型预测其未来医疗费用支出。
    ---
    """)
    # 创建两列布局，左侧为输入表单，右侧为说明
    col1, col2 = st.columns([2, 1])  # 创建2:1比例的两列布局
    with col1:  # 在第一列中创建输入表单
        with st.form('user_inputs', clear_on_submit=False):  # 创建用户输入表单
            st.subheader("📝 被保险人信息")  # 添加表单子标题
            # 基本信息
            st.write("### 基本信息")  # 显示基本信息标题
            age = st.number_input('年龄', min_value=0, max_value=120, value=30, help="被保险人的实际年龄")  # 年龄输入框
            sex = st.radio('性别', options=['男性', '女性'], horizontal=True)  # 性别选择按钮，水平排列
            bmi = st.number_input('BMI指数', min_value=0.0, max_value=50.0, value=22.0, step=0.1, help="体重指数 = 体重(kg) ÷ 身高(m)的平方")  # BMI输入框
            # 家庭与生活习惯
            st.write("### 家庭与生活习惯")  # 显示家庭与生活习惯标题
            children = st.number_input("子女数量:", step=1, min_value=0, max_value=10, value=0, help="被保险人的子女数量")  # 子女数量输入框
            smoke = st.radio("是否吸烟", ("是", "否"), horizontal=True)  # 吸烟状况选择按钮
            # 区域信息
            st.write("### 区域信息")  # 显示区域信息标题
            region = st.selectbox('居住区域', ('东南部', '西南部', '东北部', '西北部'))  # 区域选择下拉框
            submitted = st.form_submit_button('🔍 预测费用', use_container_width=True)  # 提交按钮
    with col2:  # 在第二列中添加说明信息
        st.subheader("ℹ️ 信息说明")  # 显示信息说明标题
        st.info("""  # 显示信息提示框
          输入要求：
        年龄：0-120岁
        BMI：0-50，正常范围18.5-24
        子女数量：0-10个
        性别：男性/女性
        吸烟状况：是/否
        区域：中国四大地理区域
        """)
    if submitted:  # 如果表单被提交
        with st.spinner('📊 正在分析数据并预测费用...'):  # 显示加载动画
            format_data = [age, sex, bmi, children, smoke, region]  # 将原始输入数据存储到列表
            # 初始化数据预处理格式中与性别相关的变量
            sex_female, sex_male = 0, 0  # 初始化性别变量
            # 根据用户输入的性别数据更改对应的值
            if sex == '女性':  # 如果性别是女性
                sex_female = 1  # 设置女性变量为1
            elif sex == '男性':  # 如果性别是男性
                sex_male = 1  # 设置男性变量为1
            smoke_yes, smoke_no = 0, 0  # 初始化吸烟变量
            # 根据用户输入的吸烟数据更改对应的值
            if smoke == '是':  # 如果吸烟状况是"是"
                smoke_yes = 1  # 设置吸烟是变量为1
            elif smoke == '否':  # 如果吸烟状况是"否"
                smoke_no = 1  # 设置吸烟否变量为1
            region_northeast, region_southeast, region_northwest, region_southwest = 0, 0, 0, 0  # 初始化区域变量
            # 根据用户输入的区域数据更改对应的值
            if region == '东北部':  # 如果区域是东北部
                region_northeast = 1  # 设置东北部变量为1
            elif region == '东南部':  # 如果区域是东南部
                region_southeast = 1  # 设置东南部变量为1
            elif region == '西北部':  # 如果区域是西北部
                region_northwest = 1  # 设置西北部变量为1
            elif region == '西南部':  # 如果区域是西南部
                region_southwest = 1  # 设置西南部变量为1
            format_data = [age, bmi, children, sex_female, sex_male,  # 重新构建格式化数据列表
                          smoke_no, smoke_yes,
                          region_northeast, region_southeast, region_northwest,
                          region_southwest]
            # 使用pickle的load方法从磁盘文件反序列化加载一个之前保存的随机森林回归模型
            with open('rfr_model.pkl', 'rb') as f:  # 打开模型文件
                rfr_model = pickle.load(f)  # 加载模型
            format_data_df = pd.DataFrame(data=[format_data], columns=rfr_model.feature_names_in_)  # 创建DataFrame
            # 使用模型对格式化后的数据format_data进行预测,返回预测的医疗费用
            predict_result = rfr_model.predict(format_data_df)[0]  # 使用模型进行预测
        st.subheader("💰 预测结果")  # 显示预测结果子标题
        # 创建结果展示卡片
        result_col1, result_col2 = st.columns([1, 2])  # 创建结果展示列
        with result_col1:  # 在第一列显示预测结果
            st.metric(  # 显示指标卡片
                label="预测医疗费用",  # 标签
                value=f"¥{round(predict_result, 2):,.2f}",  # 显示预测值，格式化为人民币
                delta=None  # 不显示变化值
            )
# 在左侧添加侧边栏并设置单选按钮
st.sidebar.title("📌 导航菜单")  # 设置侧边栏标题
nav = st.sidebar.radio(  # 创建侧边栏单选按钮
    "选择功能",  # 按钮标签
    ["系统简介", "预测医疗费用"],  # 选项列表
    index=0  # 默认选中第一个选项
)
# 根据选择的结果，展示不同的页面
if nav == "系统简介":  # 如果选择系统简介
    introduce_page()  # 显示简介页面
else:  # 否则
    predict_page()  # 显示预测页面
