import streamlit as st
import pandas as pd
import random

# CSV 파일 로드
csv_url = "https://raw.githubusercontent.com/kwonsungja/Final-Project/main/regular_Nouns_real.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(csv_url)
    df.columns = df.columns.str.lower()
    df["singular"] = df["singular"].str.strip()
    return df

df = load_data()

# 상태 초기화
if "restart" not in st.session_state:
    st.session_state["restart"] = False

if st.session_state["restart"]:
    st.session_state.clear()
    st.session_state["restart"] = False

# 상태 변수 초기화
if "shuffled_nouns" not in st.session_state:
    st.session_state["shuffled_nouns"] = df["singular"].unique().tolist()
    random.shuffle(st.session_state["shuffled_nouns"])
if "answered_nouns" not in st.session_state:
    st.session_state["answered_nouns"] = set()
if "current_noun" not in st.session_state:
    st.session_state["current_noun"] = ""
if "score" not in st.session_state:
    st.session_state["score"] = 0
if "trials" not in st.session_state:
    st.session_state["trials"] = 0
if "feedback" not in st.session_state:
    st.session_state["feedback"] = ""
if "user_name" not in st.session_state:
    st.session_state["user_name"] = ""
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""  # Step 2 입력란 초기화
if "finished" not in st.session_state:
    st.session_state["finished"] = False

# 복수형 변환 함수
def pluralize(noun):
    if noun.endswith(('s', 'ss', 'sh', 'ch', 'x', 'z')) or (noun.endswith('o') and noun[-2] not in 'aeiou'):
        return noun + 'es'
    elif noun.endswith('y') and not noun[-2] in 'aeiou':
        return noun[:-1] + 'ies'
    return noun + 's'

# 앱 레이아웃
st.title("NounSmart: Practice Regular Plural Nouns")

# Step 0: 사용자 이름 입력
st.subheader("👤 Enter Your Name")
user_name = st.text_input("Your Name:", value="", placeholder="Type your name here")

if user_name:
    st.session_state["user_name"] = user_name
    st.write(f"### Welcome, **{user_name}**! Let's get started 🎉")

# Step 1: 명사 선택
st.subheader("Step 1: Select a Singular Noun")
available_nouns = [noun for noun in st.session_state["shuffled_nouns"] if noun not in st.session_state["answered_nouns"]]

selected_noun = st.selectbox(
    "Choose a noun to start:",
    [""] + available_nouns,  # 빈 옵션 추가
    index=0,
    key="selectbox_key",  # selectbox의 고유 키 추가
)

if selected_noun:
    # 새 명사를 선택하면 Step 2 입력란 초기화
    if st.session_state["current_noun"] != selected_noun:
        st.session_state["current_noun"] = selected_noun
        st.session_state["user_input"] = ""  # 입력란 초기화
        st.experimental_rerun()  # 강제로 UI 갱신

    st.write(f"### Singular Noun: **{selected_noun}**")

# Step 2: 복수형 입력
st.subheader("Step 2: Type the Plural Form")
user_input = st.text_input(
    "Enter the plural form:",
    value=st.session_state["user_input"],  # 항상 현재 상태 값을 사용
    key="text_input_key",  # 고유 키 추가
)

# Step 3: 정답 확인
if st.button("Check Answer") and st.session_state["current_noun"]:
    correct_plural = pluralize(st.session_state["current_noun"])

    if st.session_state["current_noun"] not in st.session_state["answered_nouns"]:
        st.session_state["trials"] += 1
        st.session_state["answered_nouns"].add(st.session_state["current_noun"])

        if user_input.strip().lower() == correct_plural.lower():
            st.session_state["score"] += 1
            st.session_state["feedback"] = f"✅ Correct! The plural form of '{st.session_state['current_noun']}' is '{correct_plural}'."
        else:
            st.session_state["feedback"] = f"❌ Incorrect. The correct plural form of '{st.session_state['current_noun']}' is '{correct_plural}'."
    else:
        st.session_state["feedback"] = "⚠️ You've already answered this noun! Please select another one."

    st.success(st.session_state["feedback"])
    st.write(f"### {st.session_state['user_name']} Your Score: {st.session_state['score']} / {st.session_state['trials']}")

# 계속하기, 종료 및 재시작 버튼
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("계속하려면 여기를 클릭하세요! (Click here to continue!)"):
        st.session_state["user_input"] = ""

with col2:
    if st.button("종료하려면 여기를 클릭하세요! (Click here to finish!)"):
        st.session_state["finished"] = True

with col3:
    if st.button("다시 시작하려면 여기를 클릭하세요! (Click here to restart!)"):
        st.session_state["restart"] = True

# 최종 피드백
if st.session_state["finished"]:
    st.markdown("### 🎉 Thank you for playing!")
    st.markdown(f"### Final Score: {st.session_state['score']} / {st.session_state['trials']}")

if not available_nouns and not st.session_state["restart"]:
    st.markdown("### 끝! (THE END)")







