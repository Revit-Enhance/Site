import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RevitEnhance | Coming Soon",
    page_icon="🔷",
    layout="centered",
)

# Hide Streamlit chrome and set background
st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    .stApp { background: linear-gradient(135deg, #1e1650 0%, #2d2163 40%, #4a3a9e 75%, #5847b8 100%); }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
        font-family: 'Segoe UI', sans-serif;
        background: transparent;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        text-align: center;
        padding: 2rem;
    }

    .page-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
    }

    .logo-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.6rem;
        margin-bottom: 0.5rem;
    }

    .logo-icon {
        width: 64px;
        height: 64px;
        background: linear-gradient(135deg, #a89edc, #d0caee);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        font-weight: 900;
        color: #2d2163;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }

    .logo-text {
        font-size: 2.6rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.5px;
    }

    .logo-text span { color: #c4b8f0; }

    .tagline {
        font-size: 1rem;
        color: #b0a4e3;
        margin-bottom: 3rem;
        letter-spacing: 0.5px;
    }

    .divider {
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #a89edc, #5847b8);
        border-radius: 2px;
        margin: 0 auto 2.5rem auto;
    }

    .badge {
        display: inline-block;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.18);
        color: #d0caee;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 3px;
        text-transform: uppercase;
        padding: 0.4rem 1.2rem;
        border-radius: 100px;
        margin-bottom: 1.5rem;
    }

    .main-heading {
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.15;
        margin-bottom: 1rem;
    }

    .accent {
        background: linear-gradient(90deg, #c4b8f0, #a89edc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .sub-heading {
        font-size: 1.1rem;
        color: #b0a4e3;
        max-width: 440px;
        line-height: 1.7;
        margin-bottom: 3rem;
    }

    .contact-label {
        font-size: 0.75rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #7a6fc0;
        margin-bottom: 0.6rem;
    }

    .contact-email {
        font-size: 1.1rem;
        font-weight: 600;
        color: #d0caee;
        text-decoration: none;
        border-bottom: 1px solid rgba(200,190,240,0.3);
        padding-bottom: 2px;
    }

    .contact-email:hover {
        color: #ffffff;
        border-color: #ffffff;
    }

    .footer {
        margin-top: 5rem;
        font-size: 0.75rem;
        color: #4e4490;
    }
</style>
</head>
<body>
<div class="page-wrapper">

    <div class="logo-wrapper">
        <div class="logo-icon">Re</div>
        <div class="logo-text">Revit<span>Enhance</span></div>
    </div>
    <div class="tagline">Enhance your Revit workflows</div>

    <div class="divider"></div>

    <div class="badge">🚀 Coming Soon</div>

    <div class="main-heading">
        Something <span class="accent">powerful</span><br>is on its way.
    </div>

    <div class="sub-heading">
        We're building tools to supercharge your Revit workflows.<br>
    </div>

    <div class="contact-label">Get in touch</div>
    <a class="contact-email" href="mailto:contact@rvtenhance.dev">contact@rvtenhance.dev</a>

    <div class="footer">© 2025 RevitEnhance · rvtenhance.dev</div>

</div>
</body>
</html>
""", height=800, scrolling=False)
