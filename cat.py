import streamlit as st
import time

# 页面基础配置
st.set_page_config(page_title='链接式自动轮播相册', page_icon='📷')

# 1. 【核心修改：在这里填写你的图片链接】
# 替换下面的示例链接为你自己的图片网络链接，按顺序排列即可（可添加/删除链接）
IMAGE_LINKS = [
    "https://pic.nximg.cn/file/20241108/31448844_113540543102_2.jpg",  # 示例链接1
    "https://pic.nximg.cn/file/20221222/33331825_004931935127_2.jpg",  # 示例链接2
    "https://pic.nximg.cn/file/20221222/33331825_004931935127_2.jpg",  # 示例链接3
    "https://pic.nximg.cn/file/20220901/33331825_093421113128_2.jpg",  # 替换为你的第4张图片链接
    "https://pic.nximg.cn/file/20220901/33331825_093421113128_2.jpg"   # 替换为你的第5张图片链接
]
total_images = len(IMAGE_LINKS)

# 2. 初始化状态（通过查询参数保存当前索引，避免刷新丢失）
query_params = st.query_params
if "current_img_idx" not in query_params:
    st.query_params.current_img_idx = 0  # 默认显示第一张
current_idx = int(query_params.current_img_idx)

# 3. 自动切换逻辑（每隔0.5秒切换下一张）
def auto_switch():
    # 计算下一张索引，实现循环轮播
    next_idx = (current_idx + 1) % total_images
    # 更新查询参数
    st.query_params.current_img_idx = next_idx
    # 等待0.5秒（控制切换间隔，可修改数值调整速度）
    time.sleep(2)
    # 重新运行脚本，实现页面刷新切换图片
    st.rerun()

# 4. 手动翻页功能（与自动轮播兼容）
def prev_image():
    prev_idx = (current_idx - 1) % total_images
    st.query_params.current_img_idx = prev_idx
    st.rerun()

def next_image():
    next_idx = (current_idx + 1) % total_images
    st.query_params.current_img_idx = next_idx
    st.rerun()

# 5. 轮播图展示
st.title('📷 链接式自动轮播相册（0.5秒/张）')
st.divider()

if total_images > 0:
    # 显示当前图片（直接使用网络链接）
    current_img_link = IMAGE_LINKS[current_idx]
    st.image(
        current_img_link,
        caption=f"当前图片：第 {current_idx + 1} 张（自动切换中，可手动点击按钮干预）",
        use_column_width=True
    )

    # 手动翻页按钮布局
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.button("⬅️ 上一张", on_click=prev_image, use_container_width=True)
    with col3:
        st.button("下一张 ➡️", on_click=next_image, use_container_width=True)
    with col2:
        st.markdown(f"<div style='text-align: center; margin-top: 8px;'>第 {current_idx + 1} / {total_images} 张</div>",
                    unsafe_allow_html=True)

    # 启动自动切换（放在最后，避免干扰按钮点击）
    auto_switch()

else:
    st.warning("请先在IMAGE_LINKS列表中填写有效的图片网络链接！")

st.divider()
st.info("提示：1. 可在IMAGE_LINKS中添加/删除/修改图片链接；2. 修改time.sleep(0.5)调整自动切换间隔；3. 支持JPG/PNG/GIF等主流图片格式链接")
