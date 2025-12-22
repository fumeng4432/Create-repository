import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')

# 图片数组（沿用你原来的链接，无需修改）
images = [
    'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
    'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg',
    'https://images2.alphacoders.com/716/71660.jpg'
]
total_images = len(images)

# 1. 初始化当前图片索引（保存状态，避免翻页后丢失）
if "current_img_idx" not in st.session_state:
    st.session_state.current_img_idx = 0  # 默认显示第一张图片

# 2. 定义翻页功能函数（支持循环切换）
def prev_image():
    st.session_state.current_img_idx = (st.session_state.current_img_idx - 1) % total_images

def next_image():
    st.session_state.current_img_idx = (st.session_state.current_img_idx + 1) % total_images

# 3. 显示当前图片（先显示图片，再放按钮，保证按钮在图片下方）
current_image = images[st.session_state.current_img_idx]
st.image(
    current_image,
    caption=f"当前图片：第 {st.session_state.current_img_idx + 1} / {total_images} 张"  # 简单备注，无额外样式
)

# 4. 用两列布局实现按钮左右排列（图片下方，左侧上一张，右侧下一张，无额外样式）
col1, col2 = st.columns(2)
with col1:
    # 左侧按钮：上一张
    st.button("上一张", on_click=prev_image, use_container_width=False)
with col2:
    # 右侧按钮：下一张（通过设置对齐方式，让按钮靠右显示，更贴合“左右两侧”视觉）
    st.button("下一张", on_click=next_image, use_container_width=False)
