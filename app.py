import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Personal Finance Intelligence",
    page_icon="💰",
    layout="wide"
)

# ---------------- PROFESSIONAL UI DESIGN ----------------

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f4f8ff 0%, #ffffff 55%, #eef5ff 100%);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #e6f0ff 0%, #dceafb 100%);
    }

    h1, h2, h3 {
        color: #12355b !important;
        font-weight: 800 !important;
    }

    .hero {
        background: linear-gradient(135deg, #12355b, #2474b8);
        padding: 28px;
        border-radius: 18px;
        color: white;
        box-shadow: 0 6px 18px rgba(18,53,91,0.18);
        margin-bottom: 22px;
    }

    .hero-title {
        font-size: 35px;
        font-weight: 800;
    }

    .hero-subtitle {
        font-size: 16px;
        margin-top: 8px;
        color: #e7f2ff;
    }

    .metric-card {
        background: white;
        border-radius: 16px;
        padding: 22px;
        min-height: 145px;
        border: 1px solid #d8e6f7;
        box-shadow: 0 5px 16px rgba(18,53,91,0.09);
    }

    .metric-icon {
        font-size: 34px;
        margin-bottom: 8px;
    }

    .metric-label {
        color: #5b7594;
        font-size: 15px;
        font-weight: 700;
    }

    .metric-value {
        color: #12355b;
        font-size: 30px;
        font-weight: 800;
        margin-top: 5px;
    }

    .income-card {
        border-top: 6px solid #2eaf68;
    }

    .expense-card {
        border-top: 6px solid #e85b65;
    }

    .saving-card {
        border-top: 6px solid #3578d4;
    }

    .section-box {
        background: white;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #d8e6f7;
        box-shadow: 0 4px 14px rgba(18,53,91,0.06);
    }

    .success-box {
        background: #e9fff2;
        border: 1px solid #91dfb3;
        border-radius: 14px;
        padding: 20px;
        color: #087443;
        font-weight: 700;
    }

    .warning-box {
        background: #fff7df;
        border: 1px solid #f0d17b;
        border-radius: 14px;
        padding: 20px;
        color: #8a6200;
        font-weight: 700;
    }

    .danger-box {
        background: #fff0f0;
        border: 1px solid #efaaaa;
        border-radius: 14px;
        padding: 20px;
        color: #a52a2a;
        font-weight: 700;
    }

    .suggestion-box {
        background: linear-gradient(135deg, #eaf4ff, #dcecff);
        border: 1px solid #afd2f7;
        border-radius: 16px;
        padding: 22px;
        color: #12355b;
        min-height: 220px;
        box-shadow: 0 4px 14px rgba(18,53,91,0.06);
    }

    .suggestion-title {
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .footer-box {
        background: #edf3fb;
        border-radius: 12px;
        padding: 16px;
        color: #4c6785;
        font-size: 13px;
    }

    .stButton > button {
        width: 100%;
        background: #12355b;
        color: white;
        border-radius: 9px;
        font-weight: 800;
        border: none;
    }

    .stButton > button:hover {
        background: #2474b8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- MAIN HEADER ----------------

st.markdown("""
<div class="hero">
    <div class="hero-title">💰 Personal Finance & Investment Intelligence system</div>
    <div class="hero-subtitle">
        Analyze your financial situation, track savings and get intelligent investment recommendations..
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR INPUTS ----------------

st.sidebar.header("📝 Financial Details")

income = st.sidebar.number_input(
    "Monthly Income (₹)",
    min_value=0,
    value=50000,
    step=1000
)

expenses = st.sidebar.number_input(
    "Monthly Expenses (₹)",
    min_value=0,
    value=35000,
    step=1000
)

desired_savings = st.sidebar.number_input(
    "Desired Monthly Savings (₹)",
    min_value=0,
    value=10000,
    step=1000
)

st.sidebar.markdown("---")
analyze = st.sidebar.button("🔍 Analyze Finances")

# ---------------- ANALYSIS ----------------

if analyze:

    savings = income - expenses
    savings_percentage = (savings / income * 100) if income > 0 else 0

    # ---------------- FINANCIAL SUMMARY ----------------

    st.subheader("📊 Financial Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card income-card">
            <div class="metric-icon">💰</div>
            <div class="metric-label">Monthly Income</div>
            <div class="metric-value">₹{income:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card expense-card">
            <div class="metric-icon">👛</div>
            <div class="metric-label">Monthly Expenses</div>
            <div class="metric-value">₹{expenses:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card saving-card">
            <div class="metric-icon">🐷</div>
            <div class="metric-label">Monthly Savings</div>
            <div class="metric-value">₹{savings:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ---------------- SAVINGS ANALYSIS ----------------

    st.subheader("🎯 Savings Analysis")

    if savings >= desired_savings:
        st.markdown("""
        <div class="success-box">
            ✅ You achieved your desired savings goal!
        </div>
        """, unsafe_allow_html=True)
    elif savings > 0:
        st.markdown("""
        <div class="warning-box">
            ⚠️ You are saving, but below your desired goal.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="danger-box">
            ❌ Your expenses are higher than your income.
        </div>
        """, unsafe_allow_html=True)

    st.write(f"**Savings Percentage:** {savings_percentage:.1f}%")
    st.progress(min(max(savings_percentage / 100, 0), 1))

    st.divider()

    # ---------------- INVESTMENT OPTIONS ----------------

    st.subheader("💰 Investment Comparison")

    investment_amount = max(savings, 0)

    investment_options = {
        "Savings Account": 0.03,
        "RD": 0.065,
        "Debt Mutual Fund": 0.07,
        "Gold ETF": 0.08,
        "Index Fund": 0.10,
        "Equity Mutual Fund": 0.12
    }

    results = []

    for investment, rate in investment_options.items():
        profit = investment_amount * rate
        total_value = investment_amount + profit

        results.append({
            "Investment": investment,
            "Return Rate": f"{rate * 100:.1f}%",
            "Invested Amount": investment_amount,
            "Estimated Profit": profit,
            "Estimated Total Value": total_value
        })

    investment_df = pd.DataFrame(results)

    display_df = investment_df.copy()

    for column in [
        "Invested Amount",
        "Estimated Profit",
        "Estimated Total Value"
    ]:
        display_df[column] = display_df[column].apply(
            lambda value: f"₹{value:,.0f}"
        )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ---------------- CHART AND SUGGESTION ----------------

          # ---------------- CHART AND SUGGESTION ----------------

    chart_col, suggestion_col = st.columns([1.6, 1])

    with chart_col:
        st.subheader("📈 Estimated Investment Returns")

        chart_data = investment_df[
            ["Investment", "Estimated Profit"]
        ].set_index("Investment")

        st.bar_chart(
            chart_data,
            horizontal=True,
            height=280
        )

    with suggestion_col:
        st.subheader("🏆 Investment Suggestion")
        


        if investment_amount <= 0:
            st.markdown("""
            <div class="suggestion-box">
                <div class="suggestion-title">💡 Build Savings First</div>
                Your current savings are not positive.
                Build an emergency fund and improve monthly savings
                before considering investments.
            </div>
            """, unsafe_allow_html=True)
        else:
            best_option = investment_df.loc[
                investment_df["Estimated Profit"].idxmax()
            ]

            st.markdown(f"""
            <div class="suggestion-box">
                <div class="suggestion-title">💡 Highest Estimated Return</div>
                <b>Investment:</b> {best_option["Investment"]}<br><br>
                <b>Investment Amount:</b> ₹{best_option["Invested Amount"]:,.0f}<br>
                <b>Estimated 1-Year Profit:</b> ₹{best_option["Estimated Profit"]:,.0f}<br>
                <b>Estimated Total Value:</b> ₹{best_option["Estimated Total Value"]:,.0f}
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ---------------- INVESTMENT METRICS ----------------

    st.subheader("🔎 Selected Investment Summary")

    if investment_amount > 0:
        best_option = investment_df.loc[
            investment_df["Estimated Profit"].idxmax()
        ]

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "Investment Amount",
            f"₹{best_option['Invested Amount']:,.0f}"
        )

        col5.metric(
            "Estimated 1-Year Profit",
            f"₹{best_option['Estimated Profit']:,.0f}"
        )

        col6.metric(
            "Estimated Total Value",
            f"₹{best_option['Estimated Total Value']:,.0f}"
        )

    # ---------------- EXPLANATION ----------------

    st.subheader("📌 Financial Explanation")

    st.markdown("""
    <div class="footer-box">
        This system compares different investment options using assumed
        annual return rates. Actual returns may vary depending on market
        conditions, risk, investment duration and other factors.
        <br><br>
        <b>Disclaimer:</b> This is an educational project.
        Returns are illustrative assumptions and are not guaranteed
        financial advice.
    </div>
    """, unsafe_allow_html=True)

else:
    st.info(
        "👈 Enter your financial details in the sidebar and click "
        "'Analyze Finances' to begin."
    )
