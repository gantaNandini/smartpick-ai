import streamlit as st
from groq import Groq

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SmartPick AI – Product Recommendation Agent",
    page_icon="★",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS (color-theory: navy + violet + teal + pink) ─────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif !important;
}

/* ── Background ── */
.stApp {
    background: #F4F6FF !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #1A1A2E !important;
    border-right: none !important;
}
[data-testid="stSidebar"] * {
    color: #E2E8F0 !important;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stTextInput label,
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3, [data-testid="stSidebar"] p {
    color: #A0AEC0 !important;
    font-size: 12px !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
    font-weight: 700 !important;
}
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
    background: #2D3561 !important;
    border: 1px solid #3D4A7A !important;
    border-radius: 10px !important;
    color: #fff !important;
}
[data-testid="stSidebar"] .stSlider [data-testid="stSlider"] {
    color: #43CFAA !important;
}
[data-testid="stSidebar"] .stTextInput input {
    background: #2D3561 !important;
    border: 1px solid #3D4A7A !important;
    border-radius: 10px !important;
    color: #fff !important;
    padding: 10px 14px !important;
}
[data-testid="stSidebar"] .stTextInput input::placeholder {
    color: #718096 !important;
}

/* ── Main area headings ── */
h1 { font-size: 32px !important; font-weight: 900 !important; color: #1A1A2E !important; }
h2 { font-size: 22px !important; font-weight: 800 !important; color: #1A1A2E !important; }
h3 { font-size: 17px !important; font-weight: 700 !important; color: #1A1A2E !important; }

/* ── Primary button ── */
.stButton > button {
    background: linear-gradient(135deg, #6C63FF, #43CFAA) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    padding: 14px 28px !important;
    width: 100% !important;
    letter-spacing: 0.5px !important;
    transition: opacity 0.2s !important;
    font-family: 'Nunito', sans-serif !important;
}
.stButton > button:hover { opacity: 0.88 !important; }

/* ── Stat cards (metric) ── */
[data-testid="metric-container"] {
    background: #fff !important;
    border: 1.5px solid #E0E7FF !important;
    border-radius: 16px !important;
    padding: 18px 22px !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-size: 28px !important;
    font-weight: 900 !important;
    color: #6C63FF !important;
}
[data-testid="metric-container"] [data-testid="stMetricLabel"] {
    font-size: 13px !important;
    color: #6B7280 !important;
    font-weight: 600 !important;
}

/* ── Product cards ── */
.product-card {
    background: #fff;
    border: 1.5px solid #E0E7FF;
    border-radius: 18px;
    padding: 22px;
    position: relative;
    margin-bottom: 18px;
    transition: box-shadow 0.2s;
}
.product-card:hover { box-shadow: 0 8px 32px rgba(108,99,255,0.12); }
.rank-badge {
    position: absolute;
    top: 18px; right: 18px;
    width: 36px; height: 36px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
}
.product-category {
    font-size: 11px; font-weight: 800;
    letter-spacing: 1.5px; text-transform: uppercase;
    color: #6C63FF; margin-bottom: 6px;
}
.product-name {
    font-size: 18px; font-weight: 900;
    color: #1A1A2E; margin-bottom: 4px;
}
.product-price {
    font-size: 22px; font-weight: 900;
    color: #43CFAA; margin-bottom: 8px;
}
.star-row { font-size: 14px; color: #F59E0B; margin-bottom: 12px; }
.tag {
    display: inline-block;
    background: #F0F0FF; color: #6C63FF;
    font-size: 11px; font-weight: 800;
    padding: 4px 12px; border-radius: 20px; margin: 3px 3px 3px 0;
}
.tag-green { background: #ECFDF5 !important; color: #059669 !important; }
.tag-pink  { background: #FFF0F3 !important; color: #FF6584 !important; }
.verdict-box {
    background: linear-gradient(135deg, #F0F0FF, #E0E7FF);
    border-left: 4px solid #6C63FF;
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 13px; color: #4B5563;
    line-height: 1.6; margin-top: 12px;
}
.pros-cons {
    display: flex; gap: 12px; margin-top: 12px;
}
.pros, .cons {
    flex: 1; border-radius: 10px; padding: 10px 14px; font-size: 12px;
}
.pros { background: #ECFDF5; color: #065F46; border-left: 3px solid #43CFAA; }
.cons { background: #FFF5F5; color: #991B1B; border-left: 3px solid #FF6584; }
.pros strong, .cons strong { display: block; margin-bottom: 4px; font-size: 11px; letter-spacing: 1px; text-transform: uppercase; }

/* ── Spinner ── */
.stSpinner > div { border-top-color: #6C63FF !important; }

/* ── Divider ── */
hr { border-color: #E0E7FF !important; }

/* ── Info box ── */
.stAlert { border-radius: 14px !important; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
<div style="background:linear-gradient(135deg,#6C63FF22,#43CFAA22);border:1px solid #3D4A7A;border-radius:16px;padding:20px 18px 18px;margin-bottom:4px;text-align:center;">
  <div style="background:linear-gradient(135deg,#6C63FF,#43CFAA);border-radius:14px;width:52px;height:52px;display:flex;align-items:center;justify-content:center;font-size:26px;margin:0 auto 12px;">★</div>
  <div style="color:#fff;font-size:19px;font-weight:900;letter-spacing:0.5px;">SmartPick AI</div>
  <div style="color:#A0AEC0;font-size:12px;margin-top:6px;line-height:1.5;">AI-powered product recommendations based on reviews, ratings &amp; your budget</div>
  <div style="display:flex;justify-content:center;gap:8px;margin-top:14px;flex-wrap:wrap;">
    <span style="background:#6C63FF33;color:#A78BFA;font-size:10px;font-weight:800;padding:4px 10px;border-radius:20px;border:1px solid #6C63FF55;">⚡ LLaMA 3.3</span>
    <span style="background:#43CFAA22;color:#43CFAA;font-size:10px;font-weight:800;padding:4px 10px;border-radius:20px;border:1px solid #43CFAA44;">100% Free</span>
  </div>
</div>
""", unsafe_allow_html=True)

    groq_key = st.text_input("🔑 Groq API Key", type="password", placeholder="gsk_... (free at console.groq.com)")

    st.markdown("### Category")
    category = st.selectbox("", [
        "📱 Smartphones", "💻 Laptops", "🎧 Headphones",
        "📷 Cameras", "⌚ Smartwatches", "🖥️ Monitors",
        "🎮 Gaming Accessories", "🔌 Power Banks",
    ], label_visibility="collapsed")

    st.markdown("### Budget (₹)")
    budget = st.slider("", 1000, 200000, 30000, 1000, label_visibility="collapsed",
                       format="₹%d")
    st.markdown(f"<div style='color:#43CFAA;font-weight:800;font-size:15px;'>₹{budget:,}</div>", unsafe_allow_html=True)

    st.markdown("### Use Case")
    use_case = st.selectbox("", [
        "🎮 Gaming", "💼 Business / Work", "📚 Student",
        "🏃 Fitness & Sports", "🎨 Creative / Content", "🏠 Home Use",
    ], label_visibility="collapsed")

    st.markdown("### Priority")
    priority = st.selectbox("", [
        "⭐ Best Rated", "💰 Best Value for Money",
        "🔋 Battery Life", "📸 Camera Quality",
        "⚡ Performance / Speed", "🎨 Design & Build",
    ], label_visibility="collapsed")

    st.markdown("### Number of Results")
    num_results = st.slider("", 2, 6, 4, label_visibility="collapsed")

    st.markdown("")
    find_btn = st.button("✦ Find Best Products")

# ── Main Area ──────────────────────────────────────────────────────────────────

# Hero banner
st.markdown(f"""
<div style="
  background: linear-gradient(135deg, #1A1A2E 0%, #2D3561 60%, #3D4A7A 100%);
  border-radius: 22px;
  padding: 36px 40px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 20px;
">
  <div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
      <div style="background:linear-gradient(135deg,#6C63FF,#43CFAA);border-radius:12px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;font-size:22px;">★</div>
      <span style="background:#6C63FF22;color:#A78BFA;font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;padding:4px 14px;border-radius:20px;border:1px solid #6C63FF55;">AI Powered</span>
    </div>
    <div style="color:#fff;font-size:30px;font-weight:900;line-height:1.2;margin-bottom:8px;">SmartPick AI</div>
    <div style="color:#A0AEC0;font-size:14px;font-weight:500;">Powered by LLaMA 3.3 70B &nbsp;·&nbsp; Analyzes reviews, ratings & your preferences</div>
  </div>
  <div style="display:flex;gap:16px;flex-wrap:wrap;">
    <div style="background:#ffffff12;border:1px solid #ffffff22;border-radius:14px;padding:16px 22px;text-align:center;min-width:110px;">
      <div style="color:#43CFAA;font-size:26px;font-weight:900;">2,400+</div>
      <div style="color:#A0AEC0;font-size:12px;margin-top:2px;">Products</div>
    </div>
    <div style="background:#ffffff12;border:1px solid #ffffff22;border-radius:14px;padding:16px 22px;text-align:center;min-width:110px;">
      <div style="color:#FF6584;font-size:26px;font-weight:900;">₹{budget:,}</div>
      <div style="color:#A0AEC0;font-size:12px;margin-top:2px;">Your Budget</div>
    </div>
    <div style="background:#ffffff12;border:1px solid #ffffff22;border-radius:14px;padding:16px 22px;text-align:center;min-width:110px;">
      <div style="color:#A78BFA;font-size:26px;font-weight:900;">{num_results}</div>
      <div style="color:#A0AEC0;font-size:12px;margin-top:2px;">Top Picks</div>
    </div>
  </div>
</div>

<!-- Category pill row -->
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:24px;">
  <span style="background:#F0F0FF;color:#6C63FF;font-size:12px;font-weight:800;padding:6px 16px;border-radius:20px;border:1.5px solid #E0E7FF;">📦 {category.split(' ',1)[-1]}</span>
  <span style="background:#ECFDF5;color:#059669;font-size:12px;font-weight:800;padding:6px 16px;border-radius:20px;border:1.5px solid #D1FAE5;">{use_case}</span>
  <span style="background:#FFF0F3;color:#FF6584;font-size:12px;font-weight:800;padding:6px 16px;border-radius:20px;border:1.5px solid #FFD6DF;">{priority}</span>
</div>
""", unsafe_allow_html=True)

# ── Recommendation engine ──────────────────────────────────────────────────────
def get_recommendations(api_key: str, category: str, budget: int,
                        use_case: str, priority: str, n: int) -> str:
    client = Groq(api_key=api_key)

    prompt = f"""You are an expert product recommendation AI.
Give the top {n} product recommendations for:
- Category: {category}
- Budget: ₹{budget:,} (Indian Rupees)
- Use case: {use_case}
- Priority: {priority}

For each product, provide exactly this structure:

PRODUCT [number]
Name: [exact product name]
Price: ₹[price]
Rating: [X.X]/5 ([number] reviews)
Stars: [★★★★★ or partial stars]
Category Tag: [short category]
Tags: [tag1] | [tag2] | [tag3]
Pros: [pro1] | [pro2] | [pro3]
Cons: [con1] | [con2]
Verdict: [2-3 sentence buying advice]

Be specific with real product names and realistic Indian market prices.
Sort from best to worst match for the user's needs.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2500,
        temperature=0.7,
    )
    return response.choices[0].message.content


def parse_and_display(raw: str, n: int):
    ranks = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣"]
    rank_colors = ["#FFF3CD", "#E8E8E8", "#FFE8DC", "#EDE9FE", "#E0F4FF", "#F0FFF4"]

    # Split by PRODUCT keyword
    blocks = raw.split("PRODUCT ")
    blocks = [b for b in blocks if b.strip() and b[0].isdigit()]

    if not blocks:
        st.warning("Could not parse the AI response. Please try again.")
        st.code(raw)
        return

    cols = st.columns(2)
    for i, block in enumerate(blocks[:n]):
        col = cols[i % 2]
        lines = {line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip()
                 for line in block.strip().splitlines()
                 if ":" in line}

        name    = lines.get("Name", "Product")
        price   = lines.get("Price", "N/A")
        rating  = lines.get("Rating", "4.0/5")
        stars   = lines.get("Stars", "★★★★☆")
        cat_tag = lines.get("Category Tag", category.split(" ", 1)[-1])
        tags    = [t.strip() for t in lines.get("Tags", "").split("|") if t.strip()]
        pros    = [p.strip() for p in lines.get("Pros", "").split("|") if p.strip()]
        cons    = [c.strip() for c in lines.get("Cons", "").split("|") if c.strip()]
        verdict = lines.get("Verdict", "")

        rank_icon  = ranks[i] if i < len(ranks) else str(i + 1)
        rank_color = rank_colors[i] if i < len(rank_colors) else "#F4F6FF"

        tag_html = "".join(
            f'<span class="tag {"tag-green" if j == 1 else "tag-pink" if j == 2 else ""}">{t}</span>'
            for j, t in enumerate(tags[:4])
        )
        pros_html = "<br>".join(f"✓ {p}" for p in pros[:3])
        cons_html = "<br>".join(f"✗ {c}" for c in cons[:2])

        card_html = f"""
<div class="product-card">
  <div class="rank-badge" style="background:{rank_color};">{rank_icon}</div>
  <div class="product-category">{cat_tag}</div>
  <div class="product-name">{name}</div>
  <div class="product-price">{price}</div>
  <div class="star-row">{stars} &nbsp; {rating}</div>
  <div>{tag_html}</div>
  <div class="pros-cons">
    <div class="pros"><strong>✦ Pros</strong>{pros_html}</div>
    <div class="cons"><strong>✦ Cons</strong>{cons_html}</div>
  </div>
  <div class="verdict-box">💡 {verdict}</div>
</div>
"""
        col.markdown(card_html, unsafe_allow_html=True)


# ── Trigger ────────────────────────────────────────────────────────────────────
if find_btn:
    if not groq_key:
        st.error("⚠️ Please enter your Groq API key in the sidebar. Get one free at console.groq.com")
    else:
        with st.spinner("🤖 AI is analyzing thousands of products for you..."):
            try:
                raw = get_recommendations(groq_key, category, budget, use_case, priority, num_results)
                st.markdown(f"### Top {num_results} Picks — {category} under ₹{budget:,}")
                st.markdown(
                    f"<p style='color:#6B7280;font-size:13px;margin-bottom:20px;'>"
                    f"Optimized for: {use_case} · Priority: {priority}</p>",
                    unsafe_allow_html=True
                )
                parse_and_display(raw, num_results)
                st.success("✅ Recommendations ready! Scroll up to see all picks.")
            except Exception as e:
                st.error(f"❌ Error: {e}")
else:
    # Welcome screen
    st.markdown("""
<div style="background:#fff;border:1.5px solid #E0E7FF;border-radius:20px;padding:40px;text-align:center;margin-top:20px;">
  <div style="font-size:52px;margin-bottom:16px;">★</div>
  <h2 style="color:#1A1A2E;font-size:24px;margin-bottom:12px;">Your AI Shopping Assistant</h2>
  <p style="color:#6B7280;font-size:15px;max-width:480px;margin:0 auto 24px;line-height:1.7;">
    Set your category, budget, and preferences in the sidebar —
    then click <strong style="color:#6C63FF;">Find Best Products</strong> to get AI-powered recommendations.
  </p>
  <div style="display:flex;justify-content:center;gap:24px;flex-wrap:wrap;margin-top:24px;">
    <div style="background:#F0F0FF;border-radius:14px;padding:16px 24px;text-align:center;">
      <div style="font-size:24px;margin-bottom:6px;">📱</div>
      <div style="font-size:13px;font-weight:700;color:#6C63FF;">Phones</div>
    </div>
    <div style="background:#ECFDF5;border-radius:14px;padding:16px 24px;text-align:center;">
      <div style="font-size:24px;margin-bottom:6px;">💻</div>
      <div style="font-size:13px;font-weight:700;color:#059669;">Laptops</div>
    </div>
    <div style="background:#FFF0F3;border-radius:14px;padding:16px 24px;text-align:center;">
      <div style="font-size:24px;margin-bottom:6px;">🎧</div>
      <div style="font-size:13px;font-weight:700;color:#FF6584;">Headphones</div>
    </div>
    <div style="background:#FFFBEB;border-radius:14px;padding:16px 24px;text-align:center;">
      <div style="font-size:24px;margin-bottom:6px;">⌚</div>
      <div style="font-size:13px;font-weight:700;color:#D97706;">Watches</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)