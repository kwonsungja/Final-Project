import streamlit as st
import pandas as pd
import random

# Load the CSV file
csv_url = "https://raw.githubusercontent.com/kwonsungja/Final-Project/main/regular_Nouns_real.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(csv_url)
    df.columns = df.columns.str.lower()
    df["singular"] = df["singular"].str.strip()
    return df

df = load_data()

# Pluralization logic
def pluralize(noun):
    if noun.endswith(('s', 'ss', 'sh', 'ch', 'x', 'z')) or (noun.endswith('o') and noun[-2] not in 'aeiou'):
        return noun + 'es'
    elif noun.endswith('y') and not noun[-2] in 'aeiou':
        return noun[:-1] + 'ies'
    return noun + 's'

# Initialize session state
if "shuffled_nouns" not in st.session_state:
    all_nouns = df["singular"].unique().tolist()
    random.shuffle(all_nouns)
    st.session_state["shuffled_nouns"] = all_nouns
    st.session_state["current_noun"] = ""
    st.session_state["score"] = 0
    st.session_state["trials"] = 0
    st.session_state["feedback"] = ""
    st.session_state["user_name"] = ""  # Add user name to session state
    st.session_state["user_s"] = ""
    st.session_state["user_es"] = ""
    st.session_state["current_ies"] = ""
    st.session_state["final_stage"] = False

# Encouragement messages
final_encouragement = [
    "Well done, {name}! Keep practicing to master plural nouns!",
    "Great effort, {name}! You're making amazing progress!",
    "Fantastic work, {name}! Stay motivated and keep learning!"
]

# App Layout
st.title("NounSmart: Practice Regular Plural Nouns")

# Step 0: User Name Input
st.subheader("👤 Enter Your Name")
user_name = st.text_input("Your Name:", value=st.session_state["user_name"], placeholder="Type your name here")

if user_name:
    st.session_state["user_name"] = user_name
    st.write(f"### Welcome, **{user_name}**! Let's get started 🎉")

# Step 1: Select a Noun
st.subheader("Step 1: Select a Singular Noun")
selected_noun = st.selectbox("Choose a noun to start:", st.session_state["shuffled_nouns"])

if selected_noun:
    st.session_state["current_noun"] = selected_noun
    st.write(f"### Singular Noun: **{selected_noun}**")

# Step 2: User Input
st.subheader("Step 2: Type the Plural Form")
user_input = st.text_input("Enter the plural form:")

# Step 3: Check Answer
if st.button("Check Answer"):
    correct_plural = pluralize(st.session_state["current_noun"])
    st.session_state["trials"] += 1

    if user_input.strip().lower() == correct_plural.lower():
        st.session_state["score"] += 1
        st.session_state["feedback"] = f"✅ Correct! The plural form of '{st.session_state['current_noun']}' is '{correct_plural}'."
    else:
        st.session_state["feedback"] = f"❌ Incorrect. The correct plural form of '{st.session_state['current_noun']}' is '{correct_plural}'."

    # Display feedback
    st.success(st.session_state["feedback"])
    st.write(f"### {st.session_state['user_name']} Your Score: {st.session_state['score']} / {st.session_state['trials']}")

# Continue and Finish Options
col1, col2 = st.columns(2)
with col1:
    if st.button("계속하려면 여기를 클릭하세요! (Click here to continue!)"):
        # Prepare for the next noun
        st.session_state["user_s"] = ""
        st.session_state["user_es"] = ""
        st.session_state["current_ies"] = ""
        st.experimental_rerun()

with col2:
    if st.button("종료하려면 여기를 클릭하세요! (Click here to end!)"):
        st.session_state["final_stage"] = True
        st.experimental_rerun()

# Final Message after Game Ends
if st.session_state["final_stage"]:
    st.markdown("### 끝! (THE END)")
    st.markdown(random.choice(final_encouragement).format(name=st.session_state["user_name"]))
