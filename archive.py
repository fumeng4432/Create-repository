import streamlit as st

# 页面配置
st.set_page_config(
    page_title="学生数字档案 - 浮梦",
    page_icon="📚",
    layout="wide"
)

# 初始化session state
if 'student_name' not in st.session_state:
    st.session_state.student_name = "浮梦"
if 'student_id' not in st.session_state:
    st.session_state.student_id = "第一批笨蛋学生"
if 'show_edit_form' not in st.session_state:
    st.session_state.show_edit_form = False


# 处理表单提交
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


# ==================== 顶部导航栏 ====================
st.markdown("### 导航菜单")
# 创建5列布局用于导航按钮
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 学生档案", use_container_width=True):
        st.info("当前页面：学生档案")

with col2:
    # 直接使用链接按钮跳转到美食仪表页面
    st.link_button("🍜 美食仪表", "https://tanshiji3.streamlit.app/", use_container_width=True)

with col3:
    # 直接使用链接按钮跳转到相册页面
    st.link_button("🖼️ 相册", "https://tanshiji4.streamlit.app/", use_container_width=True)

with col4:
    # 直接使用链接按钮跳转到音乐播放器页面
    st.link_button("🎵 音乐播放", "https://tanshiji5.streamlit.app/", use_container_width=True)

with col5:
    # 直接使用链接按钮跳转到视频播放页面
    st.link_button("🎬 视频播放", "https://tanshiji6.streamlit.app/", use_container_width=True)

st.divider()

# ==================== 主内容区域 ====================

# 标题区域
st.markdown(f"### 学生{st.session_state.student_name}的数字档案")

# 使用列容器
left_col, right_col = st.columns([3, 1])

with left_col:
    # 选项卡组件
    tab1, tab2, tab3 = st.tabs(["基本信息", "技能矩阵", "任务日志"])

    with tab1:
        # 基本信息 - 使用扩展器
        with st.expander("📋 个人资料", expanded=True):
            col_a, col_b = st.columns(2)

            with col_a:
                st.write(f"**姓名:** {st.session_state.student_name}")
                st.write(f"**学号:** {st.session_state.student_id}")
                st.write(f"**注册时间:** 2023-09-01")

            with col_b:
                st.write(f"**精神状态:** 正常")
                st.write(f"**健康度:** 良好")
                st.write(f"**在线状态:** 在线")

        with st.expander("📊 系统信息"):
            col_c, col_d = st.columns(2)

            with col_c:
                st.write("**连接状态:** 已加速")
                st.write("**最后更新:** 2025-12-18")

            with col_d:
                st.write("**数据版本:** v2.1")
                st.write("**存储空间:** 85% 可用")

    with tab2:
        # 技能矩阵
        st.write("**C++：** 60%")
        st.progress(0.6)

        st.write("**Python：** 70%")
        st.progress(0.7)

        st.write("**Java：** 80%")
        st.progress(0.8)

        st.write("**Streamlit课程进度：** 75%")
        st.progress(0.75)

    with tab3:
        # 任务日志
        task_data = [
            ["日期", "任务", "状态", "难度"],
            ["2023-10-01", "学生数字档案", "已完成", "★★☆☆☆"],
            ["2023-10-12", "成绩管理系统", "进行中", "★★★☆☆"],
            ["2023-12-12", "数据周期展示", "未完成", "★★★★☆"]
        ]
        st.table(task_data)

with right_col:
    # 侧边栏 - 操作区域
    st.markdown("### 操作面板")

    if st.button("✏️ 编辑档案", use_container_width=True):
        toggle_edit_form()

    # 编辑表单（条件显示）
    if st.session_state.show_edit_form:
        st.divider()
        st.write("**编辑档案信息**")

        new_name = st.text_input("学生姓名",
                                 value=st.session_state.student_name,
                                 key="new_name")
        new_id = st.text_input("学号",
                               value=st.session_state.student_id,
                               key="new_id")

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("✅ 确认", use_container_width=True):
                handle_form_submit()
        with col_btn2:
            if st.button("❌ 取消", use_container_width=True):
                cancel_edit()

    st.divider()

    # 状态信息
    st.markdown("### 状态信息")
    st.write("**最后活动:** 18:00")
    st.write("**今日登录:** 3次")
    st.write("**消息:** 2条未读")

st.divider()

# ==================== 底部扩展器 ====================
with st.expander("💻 最新代码成果"):
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
plt.show()'''
    st.code(code_content, language="python")

st.divider()
st.success("📌 系统提示：下一个任务目标已解锁")
