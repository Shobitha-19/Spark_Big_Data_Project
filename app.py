import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Score Analytics", layout="wide")
st.title("🎓 Student Score Analytics Dashboard")
st.caption("Frontend interface connected to the PySpark Big Data analysis pipeline.")

# Sidebar: Database / Data Input Section
st.sidebar.header("📁 Data Source Selection")
data_source = st.sidebar.radio(
    "Choose data source:",
    ("Upload CSV Database", "Use Default Project Database")
)

df = None

if data_source == "Upload CSV Database":
    uploaded_file = st.sidebar.file_uploader("Upload student dataset (.csv)", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("Database loaded successfully!")
        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.info("👈 Please upload a student score CSV database from the sidebar to start analysis.")

else:
    # Fallback to the repository's Data folder
    try:
        df = pd.read_csv("Data/st_scores.csv")
        st.sidebar.success("Default database loaded!")
    except Exception as e:
        st.error(f"Error loading default database: {e}")

# Only run analytics if data is available
if df is not None:
    # Verify expected columns
    required_cols = {"Student", "Subject", "Test Score", "Class Score"}
    if not required_cols.issubset(set(df.columns)):
        st.warning(f"Note: Uploaded dataset is missing some expected columns: {required_cols - set(df.columns)}")

    # Interactive Filters
    st.sidebar.divider()
    st.sidebar.header("Interactive Filters")

    if "Subject" in df.columns:
        subject_filter = st.sidebar.selectbox("Select Subject", ["All"] + sorted(list(df["Subject"].unique())))
        if subject_filter != "All":
            df_filtered = df[df["Subject"] == subject_filter]
        else:
            df_filtered = df
    else:
        df_filtered = df

    # Key Metrics Row
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Total Records", len(df_filtered))
    
    if "Test Score" in df_filtered.columns:
        col_m2.metric("Average Test Score", f"{df_filtered['Test Score'].mean():.2f}")
    if "Class Score" in df_filtered.columns:
        col_m3.metric("Average Class Score", f"{df_filtered['Class Score'].mean():.2f}")

    st.divider()

    # Visualizations
    col1, col2 = st.columns(2)

    with col1:
        if "Subject" in df.columns and "Test Score" in df.columns:
            st.subheader("📊 Average Test Score by Subject")
            subj_avg = df.groupby("Subject")["Test Score"].mean().reset_index()
            st.bar_chart(subj_avg, x="Subject", y="Test Score")

    with col2:
        if "Student" in df_filtered.columns and "Test Score" in df_filtered.columns:
            st.subheader("👨‍🎓 Average Test Score by Student")
            st_avg = df_filtered.groupby("Student")["Test Score"].mean().reset_index()
            st.bar_chart(st_avg, x="Student", y="Test Score")

    st.divider()
    st.subheader("📋 Dataset View")
    st.dataframe(df_filtered, use_container_width=True)
