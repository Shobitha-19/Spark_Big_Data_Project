import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Score Analytics", layout="wide")
st.title("🎓 Student Score Analytics Dashboard")
st.caption("Frontend interface connected to the PySpark Big Data analysis pipeline.")

@st.cache_data
def load_data():
    # Reads the st_scores.csv file from your repo's Data folder
    return pd.read_csv("Data/st_scores.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("Interactive Filters")
subject_filter = st.sidebar.selectbox("Select Subject", ["All"] + sorted(list(df["Subject"].unique())))

if subject_filter != "All":
    df_filtered = df[df["Subject"] == subject_filter]
else:
    df_filtered = df

# Metrics Row
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Total Records", len(df_filtered))
col_m2.metric("Average Test Score", f"{df_filtered['Test Score'].mean():.2f}")
col_m3.metric("Average Class Score", f"{df_filtered['Class Score'].mean():.2f}")

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Test Score by Subject")
    subj_avg = df.groupby("Subject")["Test Score"].mean().reset_index()
    st.bar_chart(subj_avg, x="Subject", y="Test Score")

with col2:
    st.subheader("👨‍🎓 Average Test Score by Student")
    st_avg = df_filtered.groupby("Student")["Test Score"].mean().reset_index()
    st.bar_chart(st_avg, x="Student", y="Test Score")

st.divider()
st.subheader("📋 Underlying Dataset")
st.dataframe(df_filtered, use_container_width=True)