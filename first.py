import streamlit as st

st.set_page_config(
    page_title="学生数字档案 - 浮梦",
    page_icon="📚",
    layout="wide"
)

# 添加 st.title（真正的Streamlit标题组件）
st.title("学生数字档案系统")  # ✅ 添加 st.title

# 初始化session state中的数据
if 'student_name' not in st.session_state:
    st.session_state.student_name = "浮梦"
if 'student_id' not in st.session_state:
    st.session_state.student_id = "第一批笨蛋学生"
if 'show_edit_form' not in st.session_state:
    st.session_state.show_edit_form = False

# 自定义CSS样式
st.markdown("""
<style>
/* 卡片栏样式 */
.title-card {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    padding: 1.5rem 2rem;
    border-radius: 12px;
    color: white;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 12px rgba(30, 60, 114, 0.2);
    border-left: 5px solid #4dabf7;
    position: relative;
}
.title-card h1 {
    color: white;
    margin-bottom: 0.5rem;
    font-weight: 700;
    text-align: center;
}
.title-divider {
    border-top: 2px solid rgba(255, 255, 255, 0.3);
    margin: 0.5rem 0;
}
/* 按钮样式 */
.edit-button {
    background: rgba(255, 255, 255, 0.2);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.4);
    padding: 0.4rem 1.2rem;
    border-radius: 20px;
    cursor: pointer;
    font-size: 0.9em;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 6px;
}
.edit-button:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
}
/* 表单样式 */
.edit-form {
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    margin-top: 1rem;
    border: 1px solid #e0e0e0;
}
.edit-form h3 {
    color: #1e3c72;
    margin-bottom: 1rem;
}
.form-buttons {
    display: flex;
    gap: 10px;
    margin-top: 1rem;
}
.submit-btn {
    background: #1e3c72;
    color: white;
    border: none;
    padding: 0.5rem 1.5rem;
    border-radius: 6px;
    cursor: pointer;
}
.cancel-btn {
    background: #f0f0f0;
    color: #666;
    border: none;
    padding: 0.5rem 1.5rem;
    border-radius: 6px;
    cursor: pointer;
}
/* 徽章样式 */
.id-badge {
    background: rgba(255, 255, 255, 0.2);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.9em;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}
/* 指标卡片样式 */
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 8px;
    color: white;
    text-align: center;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# 处理编辑表单提交
def handle_form_submit():
    if 'new_name' in st.session_state and 'new_id' in st.session_state:
        st.session_state.student_name = st.session_state.new_name
        st.session_state.student_id = st.session_state.new_id
    st.session_state.show_edit_form = False
    st.rerun()

def toggle_edit_form():
    st.session_state.show_edit_form = not st.session_state.show_edit_form
    st.rerun()

def cancel_edit():
    st.session_state.show_edit_form = False
    st.rerun()

# 卡片栏HTML
st.markdown(f"""
<div class="title-card">
    <h1>学生{st.session_state.student_name}的数字档案</h1>
    <div class="title-divider"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 0.5rem;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span class="id-badge">
                📚 数字档案系统
            </span>
            <span class="id-badge">
                🆔 {st.session_state.student_id}
            </span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
            <div style="font-size: 0.9em; opacity: 0.9; margin-right: 10px;">
                最后更新：2025-12-18
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 编辑按钮
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("✏️ 编辑档案信息", key="edit_button", 
                 help="点击编辑学生姓名和学号", 
                 use_container_width=True):
        st.session_state.show_edit_form = True

# 编辑表单（条件显示）
if st.session_state.show_edit_form:
    st.markdown('<div class="edit-form">', unsafe_allow_html=True)
    st.markdown('<h3>📝 编辑学生档案</h3>', unsafe_allow_html=True)
    
    # 表单字段
    col1, col2 = st.columns(2)
    with col1:
        new_name = st.text_input("学生姓名", value=st.session_state.student_name, 
                                key="new_name", placeholder="请输入学生姓名")
    with col2:
        new_id = st.text_input("学号", value=st.session_state.student_id, 
                              key="new_id", placeholder="请输入学号")
    
    # 表单按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="form-buttons">', unsafe_allow_html=True)
        col_left, col_mid, col_right = st.columns([1, 0.2, 1])
        with col_left:
            if st.button("✅ 确认更新", key="submit_form", use_container_width=True):
                handle_form_submit()
        with col_right:
            if st.button("❌ 取消", key="cancel_form", use_container_width=True):
                cancel_edit()
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ✅ 添加 st.text 组件示例
st.text("📋 以下是学生的详细档案信息：")  # ✅ 添加 st.text

# ✅ 添加 st.metric 组件示例
st.subheader("📈 学习指标")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric("综合评分", "85.6", "+2.3")  # ✅ 添加 st.metric
with metric_col2:
    st.metric("出勤率", "92%", "+5%")      # ✅ 添加 st.metric
with metric_col3:
    st.metric("任务完成", "78%", "-3%")     # ✅ 添加 st.metric
with metric_col4:
    st.metric("活跃度", "94%", "+8%")       # ✅ 添加 st.metric

st.divider()

# 基本信息显示
st.subheader("👤 个人信息")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write(f"👤 姓名：{st.session_state.student_name}")
    st.write(f"📇 学号：{st.session_state.student_id}")
    st.write(f"📅 注册时间：2023-09-01 11:31:11")
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

st.subheader("📊 技能矩阵")
skill_data = {
    "C++": 60,
    "Python": 70,
    "Java": 80
}

for skill, score in skill_data.items():
    status = "（技能水平上升）" if score >= 85 else "（技能水平下降）" if score < 70 else ""
    st.write(f"**{skill}：** {score}% {status}")
    st.progress(score / 100)

st.write(f"**Streamlit课程进度：** 75%")
st.progress(0.75)

st.divider()

st.subheader("📋 任务日志")
task_data = [
    ["日期", "任务", "状态", "难度"],
    ["2023-10-01", "学生数字档案", "已完成", "★★☆☆☆"],
    ["2023-10-12", "成绩管理系统", "进行中", "★★★☆☆"],
    ["2023-12-12", "数据周期展示", "未完成", "★★★★☆"]
]
st.table(task_data)

st.divider()

st.subheader("💻 最新代码成果")
code_content = '''import matplotlib.pyplot as plt

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
st.code(code_content, language="python")

st.divider()

# ✅ 再添加一个 st.text 示例
st.text("系统提示：所有数据均为模拟数据，仅用于演示目的。")  # ✅ 添加 st.text

st.success("📌 系统提示：下一个任务目标已解锁")
