import streamlit as st
import pandas as pd

# 여기서부터 자유롭게 작성하세요
st.title("2026년 나의 음악 청취 기록")
st.write("Apple Music 리플레이를 참고하여 2026년 10월까지의 나의 음악 청취 기록을 정리함.")

category = st.selectbox("카테고리", ["월별 가장 많이 들은 앨범", "월별 음악 청취 시간"])
if category == "월별 가장 많이 들은 앨범":
    st.header("월별 가장 많이 들은 앨범")
    st.write("월별 가장 많이 들은 앨범을 테이블로 정리함.")

    album_data = pd.DataFrame({
        "월": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        "앨범": ["Don't Be Dumb", "The Fall-Off", "The Fall-Off", "LOVESICK", "POP IS CRYIN'", "POP IS CRYIN'", "POP IS CRYIN'", "dinnermode", "BARS", "MONOLITH"],
        "아티스트": ["A$AP Rocky", "J. Cole", "J. Cole", "키드밀리", "비와이", "비와이", "비와이", "SUMIN", "팔로알토", "창모"],
        "장르": ["랩", "힙합/랩", "힙합/랩", "힙합/랩", "K-Pop", "K-Pop", "K-Pop", "R&B/소울", "힙합", "힙합/랩"]
    })
    st.table(album_data)
else:
    st.header("월별 음악 청취 시간")
    st.write("월별 음악 청취 시간을 차트로 정리함.")

    time_data = pd.DataFrame({
        "청취 시간 (분)": [1877, 1625, 1506, 1670, 1959, 965, 2804, 1465, 2451, 2420]
        },
        index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
    st.line_chart(time_data)
