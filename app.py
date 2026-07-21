import streamlit as st
from core.analyzer import analyze_repository
from core.github import clone_repo
from core.scanner import scan_repo
from core.parser import load_files
from core.llm import generate_summary

st.set_page_config(
    page_title="Edge AI Project Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Edge AI Project Copilot")

st.markdown(
    """
Analyze an Edge AI GitHub repository and generate deployment guidance.
"""
)

# ------------------------
# Session State
# ------------------------

if "repo_path" not in st.session_state:
    st.session_state.repo_path = None

if "folder_tree" not in st.session_state:
    st.session_state.folder_tree = []

if "important_files" not in st.session_state:
    st.session_state.important_files = {}

if "analysis" not in st.session_state:
    st.session_state.analysis = {}

if "summary" not in st.session_state:
    st.session_state.summary = ""
# ------------------------
# Left Panel
# ------------------------

left, right = st.columns([1, 2])

with left:

    github_url = st.text_input(
        "GitHub Repository URL",
        placeholder="https://github.com/xxx/xxx"
    )

    analyze = st.button(
        "🚀 Analyze Repository",
        use_container_width=True
    )

    if analyze:

        if github_url == "":

            st.warning("Please input a GitHub URL.")

        else:

            with st.spinner("Cloning Repository..."):

                repo_path = clone_repo(github_url)

            st.success("Repository cloned successfully!")

            folder_tree = scan_repo(repo_path)

            important_files = load_files(repo_path)

            analysis = analyze_repository(
                important_files
            )
            with st.spinner("Generating AI Summary..."):

                summary = generate_summary(
                    analysis,
                    important_files
                )

            st.session_state.summary = summary

            st.session_state.repo_path = repo_path
            st.session_state.folder_tree = folder_tree
            st.session_state.important_files = important_files
            st.session_state.analysis = analysis

# ------------------------
# Right Panel
# ------------------------

with right:

    tabs = st.tabs(
        [
            "📄 Summary",
            "🧠 Edge AI Analysis",
            "📂 Folder",
            "📑 Important Files"
        ]
    )

    # ------------------------

    with tabs[0]:

        if st.session_state.repo_path is None:

            st.info("Waiting for analysis...")

        else:

            st.success("Repository Analysis Finished.")

            st.write("Repository Path:")

            st.code(st.session_state.repo_path)

            st.markdown("### Project Summary")

            if st.session_state.summary:

                st.markdown(st.session_state.summary)

            else:

                st.info("Waiting for analysis...")

#             st.write(
#                 """
# This repository has been successfully cloned.

# Next version will use LLM to automatically generate:

# - Project Overview
# - Hardware Platform
# - AI Models
# - Deployment Guide
# - Quick Start
# """
#             )

    # ------------------------

    with tabs[1]:

        st.subheader("🧠 Edge AI Repository Analysis")

        if not st.session_state.analysis:

            st.info("Click 'Analyze Repository' to start.")

        else:

            analysis = st.session_state.analysis

            categories = [
                ("🖥 Hardware Platform", "Hardware"),
                ("🤖 AI Models", "AI Models"),
                ("⚡ Inference Framework", "Inference"),
                ("🚀 Deployment", "Deployment")
            ]

            for title, key in categories:

                st.markdown(f"### {title}")

                values = analysis.get(key, [])

                if not values:

                    st.warning("Not Found")

                else:

                    cols = st.columns(3)

                    for i, value in enumerate(values):

                        with cols[i % 3]:
                            st.success(value)

                st.divider()
    
    with tabs[2]:

        if st.session_state.folder_tree:

            st.code(
                "\n".join(
                    st.session_state.folder_tree
                )
            )

    # ------------------------

    with tabs[3]:

        files = st.session_state.important_files

        if len(files) == 0:

            st.info("No important files found.")

        else:

            for filename, content in files.items():

                st.subheader(filename)

                st.code(
                    content[:3000],
                    language="text"
                )