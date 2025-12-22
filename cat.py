import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')

# 图片数组（沿用你原来的链接，无需修改）
images = [
    'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
    'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg',
    'https://images2.alphacoders.com/716/71660.jpg'
]
total_images = len(images)

# 1. 初始化当前图片索引（用session_state保存状态，翻页后不丢失）
if "current_img_idx" not in st.session_state:
    st.session_state.current_img_idx = 0  # 默认显示第一张图片

# 2. 定义翻页功能函数（支持循环切换）
def prev_image():
    # 循环逻辑：当前是第一张，点击上一张跳转到最后一张
    st.session_state.current_img_idx = (st.session_state.current_img_idx - 1) % total_images

def next_image():
    # 循环逻辑：当前是最后一张，点击下一张跳转到第一张
    st.session_state.current_img_idx = (st.session_state.current_img_idx + 1) % total_images

# 3. 添加上一张/下一张按钮（原生默认样式，无额外修饰）
st.button("上一张", on_click=prev_image)
st.button("下一张", on_click=next_image)

# 4. 显示当前图片（仅展示单张图片，保留你原来的st.image使用方式）
current_image = images[st.session_state.current_img_idx]
st.image(
    current_image,
    caption=f"当前图片：第 {st.session_state.current_img_idx + 1} / {total_images} 张"  # 简单备注，无额外样式
)
