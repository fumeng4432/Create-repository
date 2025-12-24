import streamlit as st

st.set_page_config(page_title="视频中心")

# 修复视频数组定义
video_arr = [
    {
        'url': 'https://l00.xyz/G9hp6',
        'title': '喜羊羊与灰太狼-第一部-第1集'
    },
    {
        'url': 'https://00l.xyz/VzZ7j',
        'title': '喜羊羊与灰太狼-第一部-第2集'
    },
    {
        'url': 'https://00l.xyz/BUQVX',
        'title': '喜羊羊与灰太狼-第一部-第3集'
    },
    {
        'url': 'https://00l.xyz/BBLdM',
        'title': '喜羊羊与灰太狼-第一部-第4集'
    },
    {
        'url': 'https://00l.xyz/cC4xd',
        'title': '喜羊羊与灰太狼-第一部-第5集'
    },
]

# 初始化索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前视频标题
st.title(video_arr[st.session_state['ind']]['title'])

# 显示当前视频
st.video(video_arr[st.session_state['ind']]['url'])

def playVideo(i):
    """播放指定索引的视频"""
    st.session_state['ind'] = int(i)

# 在视频下方创建三列布局的按钮
st.subheader("选择集数")

# 创建三列
num_cols = 3
cols = st.columns(num_cols)

# 创建按钮并分配到三列中
for i in range(len(video_arr)):
    col_index = i % num_cols
    with cols[col_index]:
        st.button(
            f'第{i+1}集',
            on_click=playVideo,
            args=(i,),  # 注意这里是元组，不是列表
            key=f'btn_{i}',  # 添加key避免重复
            use_container_width=True  # 让按钮填满列的宽度
        )
