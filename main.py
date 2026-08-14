import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* ---------- APP BACKGROUND ---------- */

.stApp {
    background-color: #f3f2ef;
}

.block-container {
    max-width: 950px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ---------- HEADER ---------- */

.header-card {
    background-color: white;
    padding: 32px 35px;
    border-radius: 16px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    text-align: center;
    margin-bottom: 28px;
}

.logo {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: #0A66C2;
    color: white;
    width: 48px;
    height: 48px;
    border-radius: 7px;
    font-size: 27px;
    font-weight: 700;
    margin-bottom: 12px;
}

.app-title {
    font-size: 31px;
    font-weight: 700;
    color: #191919;
    margin-bottom: 7px;
}

.app-subtitle {
    font-size: 16px;
    color: #666666;
}


/* ---------- SECTION ---------- */

.section-card {
    background-color: white;
    padding: 25px 28px;
    border-radius: 16px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 2px 7px rgba(0, 0, 0, 0.05);
}

.section-title {
    font-size: 19px;
    font-weight: 650;
    color: #191919;
    margin-bottom: 5px;
}

.section-description {
    font-size: 14px;
    color: #666666;
    margin-bottom: 20px;
}


/* ---------- SELECT BOX LABELS ---------- */

label {
    color: #191919 !important;
    font-weight: 600 !important;
}


/* ---------- GENERATE BUTTON ---------- */

.stButton > button {
    width: 100%;
    height: 48px;
    background-color: #0A66C2;
    color: white;
    border: none;
    border-radius: 24px;
    font-size: 16px;
    font-weight: 600;
    margin-top: 18px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #004182;
    color: white;
    border: none;
}


/* ---------- OUTPUT HEADER ---------- */

.output-header {
    background-color: white;
    padding: 20px 24px;
    margin-top: 28px;
    border-radius: 16px 16px 0 0;
    border: 1px solid #e0e0e0;
    border-bottom: none;
}

.output-title {
    color: #0A66C2;
    font-size: 20px;
    font-weight: 700;
}

.output-description {
    color: #666666;
    font-size: 13px;
    margin-top: 4px;
}


/* ---------- OUTPUT BOX ---------- */

.post-box {
    background-color: white;
    padding: 24px;
    border-radius: 0 0 16px 16px;
    border: 1px solid #e0e0e0;
    border-top: 1px solid #eeeeee;
    color: #191919;
    font-size: 16px;
    line-height: 1.7;
}


/* ---------- INFO ---------- */

.info-card {
    background-color: #e8f3ff;
    border-left: 4px solid #0A66C2;
    padding: 12px 16px;
    border-radius: 8px;
    color: #191919;
    font-size: 14px;
    margin-top: 18px;
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #777777;
    font-size: 13px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# OPTIONS
# --------------------------------------------------

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# --------------------------------------------------
# MAIN APP
# --------------------------------------------------

def main():

    # ---------- HEADER ----------

    st.markdown("""
<div class="header-card">
    <div class="logo">in</div>
    <div class="app-title">LinkedIn Post Generator</div>
    <div class="app-subtitle">
        Turn your ideas into engaging professional posts with AI
    </div>
</div>
""", unsafe_allow_html=True)


    # ---------- LOAD DATA ----------

    fs = FewShotPosts()
    tags = fs.get_tags()


    # ---------- INPUT SECTION ----------

    st.markdown("""
<div class="section-card">
    <div class="section-title">Create your post</div>
    <div class="section-description">
        Choose your topic, preferred length, and language.
    </div>
</div>
""", unsafe_allow_html=True)


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


    # ---------- GENERATE BUTTON ----------

    if st.button("✨  Generate Post"):

        with st.spinner("Creating your post with AI..."):

            post = generate_post(
                selected_length,
                selected_language,
                selected_tag
            )


        # ---------- OUTPUT HEADER ----------

        st.markdown("""
<div class="output-header">
    <div class="output-title">Generated Post</div>
    <div class="output-description">
        Your AI-generated LinkedIn post is ready.
    </div>
</div>
""", unsafe_allow_html=True)


        # ---------- OUTPUT ----------

        st.markdown(
            f"""
<div class="post-box">
{post.replace(chr(10), "<br>")}
</div>
""",
            unsafe_allow_html=True
        )


        # ---------- CHARACTER COUNT ----------

        character_count = len(post)

        st.markdown(
            f"""
<div class="info-card">
    <b>{character_count}</b> characters generated
    • Topic: <b>{selected_tag}</b>
    • Language: <b>{selected_language}</b>
</div>
""",
            unsafe_allow_html=True
        )


        # ---------- COPY / EDIT AREA ----------

        st.write("")

        st.text_area(
            "Edit your post",
            value=post,
            height=220,
            help="You can edit the generated post before publishing it."
        )


    # ---------- FOOTER ----------

    st.markdown("""
<div class="footer">
    Built with Python • Streamlit • LLaMA • Groq
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    main()
