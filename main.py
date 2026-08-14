import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="centered"
)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f3f2ef;
    }

    /* Main container */
    .block-container {
        max-width: 900px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .header {
        background: white;
        padding: 30px 35px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 28px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .logo {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 45px;
        height: 45px;
        background: #0A66C2;
        color: white;
        border-radius: 6px;
        font-size: 25px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .title {
        color: #191919;
        font-size: 32px;
        font-weight: 700;
        margin: 0;
    }

    .subtitle {
        color: #666666;
        font-size: 16px;
        margin-top: 8px;
    }

    /* Labels */
    label {
        font-weight: 600 !important;
        color: #191919 !important;
    }

    /* Generate button */
    .stButton > button {
        width: 100%;
        height: 48px;
        background-color: #0A66C2;
        color: white;
        border: none;
        border-radius: 24px;
        font-size: 16px;
        font-weight: 600;
        margin-top: 15px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #004182;
        color: white;
        border: none;
    }

    /* Generated post card */
    .post-header {
        background: white;
        padding: 18px 22px;
        border-radius: 14px 14px 0 0;
        border-bottom: 1px solid #e0e0e0;
        margin-top: 30px;
    }

    .post-title {
        color: #0A66C2;
        font-size: 19px;
        font-weight: 700;
    }

    .post-subtitle {
        color: #666666;
        font-size: 13px;
        margin-top: 3px;
    }

    .post-content {
        background: white;
        padding: 22px;
        border-radius: 0 0 14px 14px;
        border: 1px solid #e0e0e0;
        border-top: none;
        line-height: 1.7;
        color: #191919;
        font-size: 16px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777777;
        font-size: 13px;
        margin-top: 35px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- OPTIONS ----------------
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# ---------------- MAIN APP ----------------
def main():

    # Header
    st.markdown("""
<div class="header">
    <div class="logo">in</div>

    <div class="title">
        LinkedIn Post Generator
    </div>

    <div class="subtitle">
        Turn your ideas into engaging professional posts with AI
    </div>
</div>
""", unsafe_allow_html=True)


    # Load tags
    fs = FewShotPosts()
    tags = fs.get_tags()


    # Selection section
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox(
            "Topic",
            options=tags
        )

    with col2:
        selected_length = st.selectbox(
            "Length",
            options=length_options
        )

    with col3:
        selected_language = st.selectbox(
            "Language",
            options=language_options
        )


    # Generate
    if st.button("✨ Generate Post"):

        with st.spinner("Creating your LinkedIn post..."):

            post = generate_post(
                selected_length,
                selected_language,
                selected_tag
            )


        # Output
        st.markdown("""
        <div class="post-header">
            <div class="post-title">Generated Post</div>
            <div class="post-subtitle">
                AI-generated content based on your preferences
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="post-content">
                {post.replace(chr(10), "<br>")}
            </div>
            """,
            unsafe_allow_html=True
        )


    # Footer
    st.markdown("""
    <div class="footer">
        Built with Python • Streamlit • LLaMA • Groq
    </div>
    """, unsafe_allow_html=True)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    main()
