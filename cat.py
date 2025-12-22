import streamlit as st

# 页面基础配置
st.set_page_config(page_title='动物园', page_icon='🐒', layout="centered")

# 1. 添加美观的动物园标题（居中显示，搭配表情符号，更醒目）
st.markdown(
    "<h1 style='text-align: center; color: #2E8B57;'>🐒 可爱动物园相册 🐼</h1>",
    unsafe_allow_html=True
)
# 分割线，提升页面层次感
st.divider()

# 图片数组（沿用原有链接，可按需替换）
images = [
     'https://www.allaboutbirds.org/news/wp-content/uploads/2025/11/redpolls-alejandra-macneil-pennsylvania-307998561-1.77-social-1280x720.jpg',
    'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg',
    'https://images2.alphacoders.com/716/71660.jpg'
]
# 图片对应备注（贴合动物园主题，更生动）
image_captions = [
    "🕊️ 灵动小鸟",
    "🐶 微笑小狗",
    "🐱 呆萌猫咪"
]
total_images = len(images)

# 2. 初始化当前图片索引（保存状态，避免翻页后丢失）
if "current_img_idx" not in st.session_state:
    st.session_state.current_img_idx = 0  # 默认显示第一张图片

# 3. 定义翻页功能函数（支持循环切换）
def prev_image():
    st.session_state.current_img_idx = (st.session_state.current_img_idx - 1) % total_images

def next_image():
    st.session_state.current_img_idx = (st.session_state.current_img_idx + 1) % total_images

# 4. 显示当前图片（优化样式：居中、固定宽度，避免拉伸变形）
current_idx = st.session_state.current_img_idx
current_image = images[current_idx]
current_caption = image_captions[current_idx]

# 居中显示图片，设置合适宽度，提升美观度
st.image(
    current_image,
    caption=f"{current_caption}（第 {current_idx + 1} / {total_images} 张）",
    width=600,  # 固定图片宽度，更规整
    use_column_width=False
)

# 5. 优化按钮样式与布局（图片下方左右两侧，按钮更美观协调）
col1, _, col2 = st.columns([1, 2, 1])  # 三列布局，中间留白，按钮更贴左右两侧
with col1:
    # 美化按钮：设置颜色、填充度，更精致
    st.button(
        "⬅️ 上一张",
        on_click=prev_image,
        use_container_width=True,  # 按钮填满列宽，更协调
        type="secondary"  # 次级按钮样式，柔和不突兀
    )
with col2:
    st.button(
        "下一张 ➡️",
        on_click=next_image,
        use_container_width=True,
        type="secondary"
    )

# 底部装饰，提升页面完整性
st.divider()
st.markdown(
    "<p style='text-align: center; color: #696969;'>✨ 欢迎浏览动物园可爱瞬间 ✨</p>",
    unsafe_allow_html=True
)

