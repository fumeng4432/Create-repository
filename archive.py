import streamlit as st

# 页面配置：设置页面标题、图标和布局方式
st.set_page_config(
    page_title="学生数字档案 - 浮梦",  # 页面标题
    page_icon="📚",  # 页面图标
    layout="wide"  # 宽屏布局
)

# 初始化session state中的数据
# session_state用于在不同页面组件之间持久化数据
if 'student_name' not in st.session_state:
    st.session_state.student_name = "浮梦"  # 默认学生姓名
if 'student_id' not in st.session_state:
    st.session_state.student_id = "第一批笨蛋学生"  # 默认学号
if 'show_edit_form' not in st.session_state:
    st.session_state.show_edit_form = False  # 控制编辑表单的显示状态

# 处理编辑表单提交
def handle_form_submit():
    """处理表单提交：更新学生姓名和学号"""
    if 'new_name' in st.session_state and 'new_id' in st.session_state:
        st.session_state.student_name = st.session_state.new_name  # 更新姓名
        st.session_state.student_id = st.session_state.new_id  # 更新学号
    st.session_state.show_edit_form = False  # 隐藏表单
    st.rerun()  # 刷新页面


def toggle_edit_form():
    """切换编辑表单的显示状态"""
    st.session_state.show_edit_form = not st.session_state.show_edit_form
    st.rerun()


def cancel_edit():
    """取消编辑：隐藏表单而不保存更改"""
    st.session_state.show_edit_form = False
    st.rerun()


# 主标题卡片栏
# 显示学生姓名和学号的蓝色卡片
st.markdown(f"### 学生{st.session_state.student_name}的数字档案")
st.divider()

# 显示系统信息和学号
col1, col2 = st.columns(2)
with col1:
    st.write("📚 数字档案系统")
    st.write(f"🆔 {st.session_state.student_id}")
with col2:
    st.write("最后更新：2025-12-18")

# 编辑按钮
if st.button("✏️ 编辑档案信息", key="edit_button", help="点击编辑学生姓名和学号"):
    st.session_state.show_edit_form = True

# 编辑表单（条件显示）
# 仅在show_edit_form为True时显示的表单
if st.session_state.show_edit_form:
    st.write("---")
    st.write("### 📝 编辑学生档案")

    # 表单字段：姓名和学号输入框
    col1, col2 = st.columns(2)  # 两列布局
    with col1:
        new_name = st.text_input("学生姓名", value=st.session_state.student_name,
                                 key="new_name", placeholder="请输入学生姓名")
    with col2:
        new_id = st.text_input("学号", value=st.session_state.student_id,
                               key="new_id", placeholder="请输入学号")

    # 表单按钮：确认更新和取消
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ 确认更新", key="submit_form", use_container_width=True):
            handle_form_submit()  # 提交表单
    with col2:
        if st.button("❌ 取消", key="cancel_form", use_container_width=True):
            cancel_edit()  # 取消编辑

st.divider()  # 水平分割线

# 基本信息显示
# 使用四列布局展示学生基本信息
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("基础信息")  # 子标题
    st.write(f"👤 姓名：{st.session_state.student_name}")  # 动态显示姓名
    st.write(f"📇 学号：{st.session_state.student_id}")  # 动态显示学号
    st.write(f"📅 注册时间：2023-09-01 11:31:11")  # 固定注册时间
with col2:
    st.subheader("状态信息")
    st.write(f"🧠 精神状态：正常")
    st.write(f"❤️ 健康度：良好（安全值：高）")
with col3:
    st.subheader("系统状态")
    st.write(f"🟢 在线状态：在线")
    st.write(f"⚡ 连接状态：已加速")
with col4:
    st.subheader("日志时间")
    st.write(f"📝 最后更新：2025-12-18 18:00:00")

st.divider()

# 技能矩阵
# 显示技能水平和进度条
st.subheader("📊 技能矩阵")
skill_data = {
    "C++": 60,
    "Python": 70,
    "Java": 80
}

for skill, score in skill_data.items():
    # 根据分数判断技能趋势
    status = "（技能水平上升）" if score >= 85 else "（技能水平下降）" if score < 70 else ""
    st.write(f"**{skill}：** {score}% {status}")  # 显示技能名称和百分比
    st.progress(score / 100)  # 显示进度条

st.write(f"**Streamlit课程进度：** 75%")
st.progress(0.75)

st.divider()

# 任务日志
# 以表格形式显示任务列表
st.subheader("📋 任务日志")
task_data = [
    ["日期", "任务", "状态", "难度"],  # 表头
    ["2023-10-01", "学生数字档案", "已完成", "★★☆☆☆"],
    ["2023-10-12", "成绩管理系统", "进行中", "★★★☆☆"],
    ["2023-12-12", "数据周期展示", "未完成", "★★★★☆"]
]
st.table(task_data)  # 显示表格

st.divider()

# 最新代码成果
# 显示代码片段
st.subheader("💻 最新代码成果")
code_content = '''''import matplotlib.pyplot as plt 

def detect_vulnerability(input_data): 
    """漏洞检测函数""" 
    if input_data == "admin": 
        return "ACCESS_GRANTED" 
    else: 
        return "SHOULD_BE_BLOCKED" 
x = [1, 2, 3, 4, 5] 
y = [10, 20, 15, 25, 30] 
plt.plot(x, y) 
plt.title("数据趋势图") 
plt.show() 
'''
st.code(code_content, language="python")  # 高亮显示Python代码

st.divider()
st.success("📌 系统提示：下一个任务目标已解锁")  # 成功提示信息