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

# Reset session state for restart
if "restart" not in st.session_state:
    st.session_state["restart"] = False

if st.session_state["restart"]:
    for key in list(st.session_state.keys()):
        del st.session_state[key]  # Clear all session state variables
    st.session_state["restart"] = False  # Reset restart flag

# Ensure all keys in `st.session_state` are initialized
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
if "finished" not in st.session_state:
    st.session_state["finished"] = False

# Pluralization logic
def pluralize(noun):
    if noun.endswith(('s', 'ss', 'sh', 'ch', 'x', 'z')) or (noun.endswith('o') and noun[-2] not in 'aeiou'):
        return noun + 'es'
    elif noun.endswith('y') and not noun[-2] in 'aeiou':
        return noun[:-1] + 'ies'
    return noun + 's'

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
available_nouns = [noun for noun in st.session_state["shuffled_nouns"] if noun not in st.session_state["answered_nouns"]]

if not available_nouns:
    st.write("🎉 You've completed all the nouns! Restart to practice again.")
else:
    selected_noun = st.selectbox(
        "Choose a noun to start:",
        [""] + available_nouns,  # Add an empty option as the first choice
        index=0,
    )
    if selected_noun:
        st.session_state["current_noun"] = selected_noun
        st.write(f"### Singular Noun: **{selected_noun}**")

# Step 2: User Input
st.subheader("Step 2: Type the Plural Form")
user_input = st.text_input("Enter the plural form:")

# Step 3: Check Answer
if st.button("Check Answer") and st.session_state["current_noun"]:
    correct_plural = pluralize(st.session_state["current_noun"])

    if st.session_state["current_noun"] not in st.session_state["answered_nouns"]:
        st.session_state["trials"] += 1
        st.session_state["answered_nouns"].add(st.session_state["current_noun"])  # Mark noun as answered

        if user_input.strip().lower() == correct_plural.lower():
            st.session_state["score"] += 1
            st.session_state["feedback"] = f"✅ Correct! The plural form of '{st.session_state['current_noun']}' is '{correct_plural}'."
        else:
            st.session_state["feedback"] = f"❌ Incorrect. The correct plural form of '{st.session_state['current_noun']}' is '{correct_plural}'."
    else:
        st.session_state["feedback"] = "⚠️ You've already answered this noun! Please select another one."

    # Display feedback
    st.success(st.session_state["feedback"])
    st.write(f"### {st.session_state['user_name']} Your Score: {st.session_state['score']} / {st.session_state['trials']}")

# Continue, Finish, and Restart Options
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("계속하려면 여기를 클릭하세요! (Click here to continue!)"):
        st.session_state["current_noun"] = ""  # Clear the current noun

with col2:
    if st.button("종료하려면 여기를 클릭하세요! (Click here to finish!)"):
        st.session_state["finished"] = True  # Mark as finished

with col3:
    if st.button("다시 시작하려면 여기를 클릭하세요! (Click here to restart!)"):
        st.session_state["restart"] = True  # Trigger restart

# Final Feedback
if st.session_state["finished"]:
    st.markdown("### 🎉 Thank you for playing!")
    st.markdown(f"### Final Score: {st.session_state['score']} / {st.session_state['trials']}")
    st.markdown(random.choice(final_encouragement).format(name=st.session_state["user_name"]))

if not available_nouns and not st.session_state["restart"]:
    st.markdown("### 끝! (THE END)")
    st.markdown(random.choice(final_encouragement).format(name=st.session_state["user_name"]))












