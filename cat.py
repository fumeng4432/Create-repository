import streamlit as st
import time

st.set_page_config(page_title='动物园', page_icon='🐒')

# 图片数组（沿用你原来的链接，无需修改）
images = [
    'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
    'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg',
    'https://images2.alphacoders.com/716/71660.jpg'
]
total_images = len(images)

# 1. 初始化当前图片索引（保存状态，避免刷新丢失）
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0

# 2. 手动翻页功能函数（上一张/下一张，支持循环切换）
def prev_img():
    # 循环逻辑：当前是第1张，点击上一张跳转到最后1张
    st.session_state.current_idx = (st.session_state.current_idx - 1) % total_images

def next_img():
    # 循环逻辑：当前是最后1张，点击下一张跳转到第1张
    st.session_state.current_idx = (st.session_state.current_idx + 1) % total_images

# 3. 自动切换功能（2秒切换下一张）
def auto_switch():
    time.sleep(2)  # 间隔2秒，可修改数值调整切换速度
    next_img()  # 调用下一张函数
    st.rerun()  # 刷新页面实现切换

# 4. 手动翻页按钮（无额外样式，保持原生默认样式）
st.button("上一张", on_click=prev_img)
st.button("下一张", on_click=next_img)

# 5. 显示当前图片（沿用你原来的st.image，仅展示单张当前图片）
current_img = images[st.session_state.current_idx]
st.image(
    current_img,
    caption=f"当前图片：第 {st.session_state.current_idx + 1} / {total_images} 张"  # 简单备注，无额外样式
)

# 启动自动切换（放在最后，避免干扰手动按钮操作）
auto_switch()
