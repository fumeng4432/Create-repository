import streamlit as st

# 设置页面配置
st.set_page_config(page_title='音乐播放', page_icon='🎵')

# 定义音乐数据
images = [
    'https://p1.music.126.net/mW53BkMgGy37I7yVrUg-aQ==/109951163117902077.jpg',
    'https://p2.music.126.net/ixIs5kkukgNYMmeDsc35_g==/29686813955450.jpg',
    'https://p2.music.126.net/sZ-rACbFrybF0x_lI6XNMw==/109951169297766755.jpg'
]

audio_files = [
    'https://music.163.com/song/media/outer/url?id=28059417.mp3',
    'https://music.163.com/song/media/outer/url?id=191254.mp3',
    'https://music.163.com/song/media/outer/url?id=2122308127.mp3'
]

song_names = [
    "他不懂",
    "天下",
    "不眠之夜"
]

artists = [
    "张杰",
    "张杰",
    "张杰"
]

# 初始化当前播放索引
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

current_index = st.session_state.current_index

# 页面标题
st.title("音乐播放器")

# 显示专辑封面和歌曲信息
col1, col2 = st.columns([1, 1.5])

with col1:
    st.image(images[current_index], width=250)

with col2:
    st.header(song_names[current_index])
    st.subheader(f"歌手: {artists[current_index]}")

st.divider()

# 控制按钮
col3, col4 = st.columns(2)

with col3:
    if st.button('上一首', disabled=current_index == 0):
        st.session_state.current_index -= 1
        st.rerun()

with col4:
    if st.button('下一首', disabled=current_index == len(images) - 1):
        st.session_state.current_index += 1
        st.rerun()

# 音频播放器
st.audio(audio_files[current_index])

# 播放列表
st.subheader("播放列表")

for i, audio_url in enumerate(audio_files):
    if i == current_index:
        st.markdown(f"**{i+1}. {song_names[i]}** (正在播放)")
    else:
        st.markdown(f"{i+1}. {song_names[i]}")