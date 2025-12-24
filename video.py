import streamlit as st

st.set_page_config(page_title="视频中心")

# 修复视频数组定义
video_arr = [
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/97/94/500001625109497/500001625109497-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&gen=playurlv3&os=cosovbv&og=hw&nbs=1&mid=0&uipk=5&oi=771356656&platform=html5&trid=a35b1df98f1f4bb4abe7a4281eb5d00h&deadline=1766566767&upsig=7f7ae10fbbf2d1a70fe5e031fd90e9d3&uparams=e,gen,os,og,nbs,mid,uipk,oi,platform,trid,deadline&bvc=vod&nettype=0&bw=656747&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
        'title': '喜羊羊与灰太狼-第一部-第1集'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/26/78/34738407826/34738407826-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=771356656&platform=html5&nbs=1&os=cosovbv&og=hw&mid=0&deadline=1766566856&uipk=5&trid=0effa531009b4179bf30735681c50dch&gen=playurlv3&upsig=44abb83d3ee4188cfe70953e13cf4593&uparams=e,oi,platform,nbs,os,og,mid,deadline,uipk,trid,gen&bvc=vod&nettype=0&bw=454518&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        'title': '喜羊羊与灰太狼-第一部-第2集'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/96/04/1599340496/1599340496-1-192.mp4?e=ig8euxZM2rNcNbRV7zdVhwdlhWdahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&platform=html5&trid=80c5ea3010564e8e9150d38f5b2c3f3h&uipk=5&mid=0&gen=playurlv3&og=hw&oi=771356656&deadline=1766566974&os=cosovbv&upsig=3cf4a0b2c08c8a5f0788563245655be5&uparams=e,nbs,platform,trid,uipk,mid,gen,og,oi,deadline,os&bvc=vod&nettype=0&bw=860710&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        'title': '喜羊羊与灰太狼-第一部-第3集'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/74/71/31520327174/31520327174-1-192.mp4?e=ig8euxZM2rNcNbR1nWdVhwdlhWRHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766567093&platform=html5&trid=f3f545bfd2d94a42b0b08bd0b16cad4h&gen=playurlv3&os=cosovbv&og=cos&uipk=5&nbs=1&mid=0&oi=771356656&upsig=49a38d71024dd89e0ea3b6a7e09348ae&uparams=e,deadline,platform,trid,gen,os,og,uipk,nbs,mid,oi&bvc=vod&nettype=0&bw=954176&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
        'title': '喜羊羊与灰太狼-第一部-第4集'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/59/03/34761540359/34761540359-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=5a77d7d7bca24296ba694e97b983534h&mid=0&nbs=1&uipk=5&oi=771356656&gen=playurlv3&platform=html5&deadline=1766566610&os=cosovbv&og=cos&upsig=8f61eebf54c10af4242c97c87fb669e2&uparams=e,trid,mid,nbs,uipk,oi,gen,platform,deadline,os,og&bvc=vod&nettype=0&bw=679039&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
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
