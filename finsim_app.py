import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="FinSim Prototype", layout="centered", page_icon="🧭")

st.title("🧭 FinSim: Level 1")
st.subheader("The Salary Reality Check")
st.markdown("---")

# Section 1: The "Take-Home Illusion"
st.write("### Step 1: Input Your Target Salary")
ctc = st.number_input("Enter your target Annual CTC (₹)", min_value=100000, value=600000, step=50000)

# Simulating standard deductions (Taxes, PF, etc.) to show the illusion
in_hand_monthly = (ctc * 0.82) / 12  

st.info(f"**Actual In-Hand Monthly Salary:** ₹{in_hand_monthly:,.0f}")
st.caption("*Notice how it's lower than CTC/12? This is the take-home illusion.*")
st.markdown("---")

# Section 2: Interactive Budgeting
st.write("### Step 2: Build Your Monthly Budget")
st.write("Drag the sliders to allocate your in-hand salary.")

col1, col2 = st.columns(2)

with col1:
    rent = st.slider("🏠 Rent & Utilities (₹)", 0, int(in_hand_monthly), int(in_hand_monthly * 0.3), step=500)
    food = st.slider("🍔 Food & Dining (₹)", 0, int(in_hand_monthly), int(in_hand_monthly * 0.2), step=500)

with col2:
    lifestyle = st.slider("🎬 Lifestyle & OTT (₹)", 0, int(in_hand_monthly), int(in_hand_monthly * 0.15), step=500)
    emi = st.slider("🎓 Education Loan EMI (₹)", 0, int(in_hand_monthly), int(in_hand_monthly * 0.15), step=500)

total_expenses = rent + food + lifestyle + emi
savings = in_hand_monthly - total_expenses
savings_rate = (savings / in_hand_monthly) * 100 if in_hand_monthly > 0 else 0

st.markdown("---")

# Section 3: Visual Feedback & Live Alert System
st.write("### Step 3: Wealth Building Potential")

# Dynamic Expense Bar
expense_ratio = min(100, int((total_expenses / in_hand_monthly) * 100)) if in_hand_monthly > 0 else 100
st.progress(expense_ratio, text=f"Total Income Consumed: {expense_ratio}%")

# Conditional Logic for Gamification
if savings_rate >= 20:
    st.success(f"✅ **Safe Zone!** You are saving {savings_rate:.1f}% of your income. (Target: >20%)")
    st.write(f"With ₹{savings:,.0f} saved monthly, Level 3 (Market Simulator) is now unlocked.")
elif savings_rate > 0:
    st.warning(f"⚠️ **Caution!** You are only saving {savings_rate:.1f}%. Cut down on Lifestyle or Dining to reach 20%.")
else:
    st.error(f"🚨 **Debt Trap Alert!** You are spending ₹{abs(savings):,.0f} more than you earn. Adjust your sliders immediately.")

# Level 3 Teaser (For the Pitch)
if st.button("Unlock Level 3: Market Simulator"):
    st.toast("Connecting to NSE live data feeds... (Coming in full version!)")
    st.line_chart(pd.DataFrame({"Portfolio Value": [10000, 10500, 10200, 11000, 10800, 12500]}))
    st.write("*In Level 3, users will practice strategy backtesting and learn strict drawdown management without losing real capital.*")