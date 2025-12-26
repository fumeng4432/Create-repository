import streamlit as st

# 1. 页面基础配置
st.set_page_config(
    page_title="广西职业师范学院官网",
    layout="wide",  # 宽布局适配侧边栏+内容
    page_icon="🏫"
)

# 侧边栏导航
with st.sidebar:
    st.markdown("### 🧭 导航栏")
    st.markdown("#### 当前页：首页")
    st.link_button("数字档案", "https://tanshiji1.streamlit.app/")
    st.link_button("南宁美食数据仪表", "https://tanshiji3.streamlit.app/")
    st.link_button("相册", "https://tanshiji4.streamlit.app/")
    st.link_button("音乐播放器", "https://tanshiji5.streamlit.app/")
    st.link_button("视频播放", "https://tanshiji6.streamlit.app/")

# 3. 首页内容（含选项卡、列容器、扩展器）
st.title("主页")

# 🔥 修复点：已更新为正确的Streamlit参数
st.image(
    "https://www.gxvnu.edu.cn/lib/images/n_ba.png",
    caption="广西职业师范学院校园风貌",
    use_container_width=True  # 替代已弃用的 use_column_width
)

# 用「选项卡」分模块展示内容
tab1, tab2, tab3 = st.tabs(["学校简介", "师资力量", "专业设置"])

with tab1:
    st.markdown("""
    广西职业师范学院（原广西经济管理干部学院）坐落于广西首府南宁市风景秀丽的邕江之滨、相思湖畔，是自治区人民政府直属、自治区教育厅主管的公办全日制普通本科学校，致力于培养区域经济社会发展所需要的高素质应用型、技术技能型人才和职业教育师资。
    """)
    # 用「扩展器」隐藏详细内容（点击展开）
    with st.expander("📜 查看历史沿革"):
        st.markdown("""
        学校随着广西的解放而诞生，其前身为创建于1951年5月的广西省行政干部训练班。其后，为适应不同历史时期广西经济建设需要，学校历经了广西人民革命大学、广西行政干部学校、广西经济干部学校、广西经济管理干部学院等历史沿革，并于2019年5月经教育部批准设置为广西职业师范学院。

        在不同历史时期，学校聚焦"服务广西经济建设"发展主线，不忘初心、勇担办学使命，为广西经济建设和社会发展作出了不可磨灭的突出贡献，享有良好的办学声誉和广泛的社会影响。
        """)

with tab2:
    # 用「列容器」分栏展示师资信息
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 师资队伍概况")
        st.markdown("""
        - 专职教师队伍：硕士、博士学位教师427人
        - 高水平团队：自治区教学名师、模范教师等领衔的教学团队1项，广西高校高水平创新团队1个
        """)
    with col2:
        st.markdown("### 教学科研成果")
        st.markdown("""
        - 教学成果奖：国家级1项、自治区级57项
        - 科研项目：近五年纵向科研立项285项（其中国家级1项）
        """)

with tab3:
    st.markdown("### 专业与实践资源")
    st.markdown("""
    - 学科覆盖：经济学、管理学、工学等8大学科，12个二级学院（部）
    - 特色项目：教育部"新工科"项目1个、自治区级一流课程4门
    - 实践基地：100+校内外实习实训基地，与广西中职学校共建职业教育实习基地
    """)

# 4. 添加页脚信息（可选）
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p> 2025 广西职业师范学院 | 联系方式: 12345678910</p>
        <p>地址：广西南宁市西乡塘区</p>
    </div>
    """,
    unsafe_allow_html=True
)