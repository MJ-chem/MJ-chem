import streamlit as st
import pandas as pd

if "ID" not in st.session_state: # 페이지 새로고침 시 오류가 뜨는 것을 막을 수 있는 코드
    st.session_state["ID"] = "Noname"

ID = st.session_state["ID"] 
with st.sidebar:
    st.caption(f'{ID}님 안녕하세요')

data = pd.read_csv("공공자전거.csv")
data = data.copy().fillna(0) # 결측치 처리
data.loc[:,'size'] = 5*(data['LCD']+data['QR'])+6 # 따릉이 수량 합산한 column 추가, 원의 크기가 너무 작아서 5배
# data['size'] = 5*(data['LCD']+data['QR'])+6
data

st.title('공공자전거 어디있지?')

color = {'QR':'#37eb91', # 색상표 구글에 검색하면 다른 색깔로 입력 가능
         'LCD':'#ebbb37'} # {}딕셔너리
data.loc[:,'color'] = data.copy().loc[:,'운영방식'].map(color)
# data['color'] = data.copy()['운영방식'].map(color)


st.map(data, 
       latitude="위도",
       longitude="경도",
       zoom = 7, # 지도의 확대/축소, 안쓰면 자동으로 어느 정도 조절해 줌
       size="size", 
       color="color")
