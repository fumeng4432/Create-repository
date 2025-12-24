# 导入必要的库
import streamlit as st  # Streamlit Web框架
from datetime import datetime  # 日期时间处理模块
from PIL import Image  # Python图像处理库

# 设置页面配置
st.set_page_config(page_title="个人简历生成器", page_icon="📄", layout="wide")

# 页面标题
st.title("个人简历生成器")  # 显示主标题
st.markdown("**使用�权归个人所有**")  # 显示版权信息

# 创建两列布局
col1, col2 = st.columns(2)  # 创建左右两列

with col1:  # 左侧列开始
    st.header("个人信息表单")  # 左侧列标题
    
    # 图片上传功能
    st.subheader("上传头像")  # 上传头像子标题
    uploaded_file = st.file_uploader(  # 文件上传组件
        "选择图片文件",  # 组件标签
        type=['jpg', 'jpeg', 'png', 'gif', 'bmp'],  # 允许上传的图片格式
        help="支持格式: JPG, PNG, GIF, BMP"  # 帮助文本
    )
    
    # 姓名输入
    name = st.text_input("姓名", value="浮梦")  # 姓名输入框，默认值为"浮梦"
    
    # 性别选择
    gender = st.selectbox("性别", ["男", "女"], index=0)  # 性别下拉选择框，默认选择第一个选项"男"
    
    # 年龄输入
    age = st.text_input("年龄", value="22")  # 年龄输入框，默认值为"22"
    
    # 户籍输入
    household = st.text_input("户籍", value="广西")  # 户籍输入框，默认值为"广西"
    
    # 电话输入
    phone = st.text_input("电话", value="12345678910")  # 电话输入框，默认值为"12345678910"
    
    # 邮箱输入
    email = st.text_input("邮箱", value="123456789@qq.com")  # 邮箱输入框，默认值为"123456789@qq.com"
    
    # 出生日期
    birth_date = st.date_input("出生日期", value=datetime(2025, 1, 1))  # 日期选择器，默认值为2025年1月1日
    
    # 学历选择
    education = st.selectbox("学历", ["高中", "大专", "本科", "硕士", "博士", "其他"], index=2)  # 学历下拉选择框，默认选择"本科"
    
    # 专业输入
    major = st.text_input("专业", value="信息管理与信息系统")  # 专业输入框，默认值为"信息管理与信息系统"
    
    # 求职意向
    st.subheader("求职意向")  # 求职意向着标题
    job_intention = st.text_input("求职意向", placeholder="请输入求职意向")  # 求职意向输入框，有占位提示
    
    # 工作经历
    st.subheader("工作经历")  # 工作经历子标题
    work_experience = st.text_input("工作经历", value="在职师院被压榨过")  # 工作经历输入框，有默认值

with col2:  # 右侧列开始
    st.header("简历实时预览")  # 右侧列标题
    
    # 头像显示区域
    st.subheader("个人头像")  # 头像显示区域标题
    
    if uploaded_file is not None:  # 如果用户上传了文件
        try:
            # 打开并显示图片
            image = Image.open(uploaded_file)  # 使用PIL打开上传的图片
            st.image(image, width=150, caption="个人头像")  # 显示图片，宽度150像素，添加标题
            
        except Exception as e:  # 如果图片加载失败
            st.error(f"图片加载失败: {str(e)}")  # 显示错误信息
            st.info("请上传有效的图片文件")  # 显示提示信息
    else:  # 如果没有上传图片
        # 如果没有上传图片，显示占位符
        st.write("暂无头像")  # 显示文字提示
        st.info("请在左侧上传头像图片")  # 显示操作提示
    
    st.divider()  # 添加分隔线
    
    # 个人信息预览
    st.write(f"**姓名:** {name}")  # 显示姓名，加粗显示
    st.write(f"**性别:** {gender}")  # 显示性别
    st.write(f"**年龄:** {age}")  # 显示年龄
    st.write(f"**户籍:** {household}")  # 显示户籍
    st.write(f"**电话:** {phone}")  # 显示电话
    st.write(f"**邮箱:** {email}")  # 显示邮箱
    st.write(f"**出生日期:** {birth_date.strftime('%Y/%m/%d')}")  # 显示格式化后的出生日期
    st.write(f"**学历:** {education}")  # 显示学历
    st.write(f"**专业:** {major}")  # 显示专业
    
    if job_intention:  # 如果用户输入了求职意向
        st.write(f"**求职意向:** {job_intention}")  # 显示用户输入的求职意向
    else:  # 如果用户没有输入求职意向
        st.write(f"**求职意向:** 软件测试")  # 显示默认的求职意向"软件测试"
    
    st.write(f"**工作经历:** {work_experience}")  # 显示工作经历
    
    st.divider()  # 添加分隔线
    
    # 个人简介
    st.subheader("个人简介")  # 个人简介子标题
    personal_intro = st.text_area(  # 多行文本输入框
        "个人简介",  # 标签
        value="专业排名前10%，获国家奖学金。精通Python/Java，有腾讯后端实习经历。担任校科协主席，领导力与团队协作能力突出。",  # 默认值
        height=150  # 文本框高度
    )
    
    # 专业技能
    st.subheader("专业技能")  # 专业技能子标题
    skills = st.text_input(  # 单行文本输入框
        "专业技能",  # 标签
        value="Java, HTML/CSS, 机器学习, Python, Web, JavaScript"  # 默认值
    )

# 底部操作区域
st.divider()  # 添加分隔线
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])  # 创建底部按钮区域，3列布局，比例1:1:2

with col_btn1:  # 第一个按钮列
    if st.button("生成简历PDF"):  # 生成PDF按钮
        if uploaded_file is not None:  # 如果上传了头像
            st.success(f"简历PDF已生成！包含头像")  # 显示成功提示，包含头像
        else:  # 如果没有上传头像
            st.success("简历PDF已生成！(无头像)")  # 显示成功提示，不包含头像
        
with col_btn2:  # 第二个按钮列
    if st.button("保存为模板"):  # 保存模板按钮
        st.info("模板已保存！")  # 显示保存成功的提示信息

# 底部信息
st.caption("不要抄袭网页")  # 页面底部的小字提示
