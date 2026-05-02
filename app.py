"""
수원화성문화제 통합 EDA 대시보드 — 뉴모피즘 디자인
공공데이터 + 인스타그램 SNS + 뉴스 정제 데이터 3중 통합
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from pathlib import Path

# =============================================================================
# 페이지 설정
# =============================================================================
st.set_page_config(
    page_title="수원화성문화제 통합 EDA 대시보드",
    page_icon="🏯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# 스타일 로드
# =============================================================================
DATA_DIR = Path(__file__).parent / "data"
STYLE_FILE = Path(__file__).parent / "style.css"

with open(STYLE_FILE, encoding='utf-8') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Plotly 뉴모피즘 테마
NEURO_BG = "#E0E5EC"
NEURO_TEXT = "#2D3748"
NEURO_PRIMARY = "#1F3864"
NEURO_ACCENT = "#ED7D31"
NEURO_DANGER = "#C53030"
NEURO_SUCCESS = "#2F855A"
NEURO_WARNING = "#DD6B20"

PLOTLY_THEME = dict(
    plot_bgcolor=NEURO_BG,
    paper_bgcolor=NEURO_BG,
    font=dict(family="맑은 고딕, Malgun Gothic, sans-serif", color=NEURO_TEXT, size=13),
    xaxis=dict(gridcolor="rgba(186, 190, 204, 0.3)", linecolor="rgba(186, 190, 204, 0.5)", tickfont=dict(color=NEURO_TEXT)),
    yaxis=dict(gridcolor="rgba(186, 190, 204, 0.3)", linecolor="rgba(186, 190, 204, 0.5)", tickfont=dict(color=NEURO_TEXT)),
    margin=dict(l=40, r=40, t=60, b=40),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=NEURO_TEXT)),
    hovermode="x unified",
)

# =============================================================================
# 데이터 로드 (캐시)
# =============================================================================
@st.cache_data
def load_marts():
    import unicodedata
    marts = {}
    for f in DATA_DIR.glob("*.csv"):
        key = unicodedata.normalize('NFC', f.stem)
        try:
            marts[key] = pd.read_csv(f, encoding='utf-8-sig')
        except Exception:
            try:
                marts[key] = pd.read_csv(f, encoding='cp949')
            except Exception:
                marts[key] = pd.read_csv(f)
    return marts

marts = load_marts()

# =============================================================================
# 헬퍼 함수
# =============================================================================
def kpi_card(label, value, delta=None, delta_type="neutral"):
    """뉴모피즘 KPI 카드"""
    delta_html = ""
    if delta is not None:
        arrow = "▲" if delta_type == "up" else ("▼" if delta_type == "down" else "—")
        delta_html = f'<div class="kpi-delta {delta_type}">{arrow} {delta}</div>'
    return f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        {delta_html}
    </div>
    """

def section_title(title, subtitle=None):
    sub = f'<div class="section-subtitle">{subtitle}</div>' if subtitle else ""
    st.markdown(f'<div class="section-title">{title}</div>{sub}', unsafe_allow_html=True)

def insight_box(title, content, type="info"):
    """인사이트 박스"""
    st.markdown(f"""
    <div class="insight-box {type}">
        <h4>{title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def quote_box(text, source="", negative=False):
    cls = "negative" if negative else ""
    src = f'<span class="source">— {source}</span>' if source else ""
    st.markdown(f"""
    <div class="quote-box {cls}">
        "{text}"
        {src}
    </div>
    """, unsafe_allow_html=True)

def style_fig(fig, title=None, height=400):
    fig.update_layout(**PLOTLY_THEME, height=height)
    if title:
        fig.update_layout(title=dict(text=title, font=dict(size=16, color=NEURO_PRIMARY)))
    return fig

# =============================================================================
# 헤더
# =============================================================================
st.markdown("""
<div class="neuro-header">
    <h1>🏯 수원화성문화제 통합 EDA 대시보드</h1>
    <p>공공데이터 · 인스타그램 SNS · 뉴스 정제 데이터 3중 통합 분석 · 2018~2025</p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# 사이드바 — 페이지 네비게이션
# =============================================================================
with st.sidebar:
    st.markdown("### 📊 페이지 선택")
    page = st.radio(
        "메뉴",
        [
            "🏠 EXECUTIVE SUMMARY",
            "1️⃣ 방문자 성과 (PART 1)",
            "2️⃣ KPI 분석 (PART 2)",
            "3️⃣ 관광 소비 (PART 3)",
            "4️⃣ 검색 트렌드 (PART 4)",
            "5️⃣ CCI 경쟁력 (PART 5)",
            "6️⃣ 페르소나 (PART 6)",
            "7️⃣ FSI 스코어카드 (PART 7)",
            "8️⃣ ★ 인스타 SNS (PART 8)",
            "9️⃣ ★ 뉴스 담론 (PART 9)",
            "🔺 ★ 3중 정합성 (PART 10)",
            "💡 인사이트·전략 (PART 11)",
        ],
        label_visibility="collapsed",
    )
    
    st.markdown("---")
    st.markdown("### 📁 데이터 출처")
    st.markdown("""
    - **공공**: 한국관광 데이터랩
    - **인스타**: 게시물 293건
    - **뉴스**: 6,251 문장 (123개 언론사)
    """)
    
    st.markdown("---")
    st.caption("ⓒ 2026 수원화성문화제 분석팀")

# =============================================================================
# 라우팅
# =============================================================================
from pages_logic import route
route(page, marts, st, kpi_card, section_title, insight_box, quote_box, style_fig,
      NEURO_PRIMARY, NEURO_ACCENT, NEURO_DANGER, NEURO_SUCCESS, NEURO_WARNING, NEURO_BG)
