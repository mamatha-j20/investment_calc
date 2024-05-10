import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="bbot_investment",
    page_icon="💰",
)

# Set the Streamlit theme and HTML markup
st.markdown(
    """
    <style>
    body {
        color: #191919;
        background-color: #abd151;
    }
    .section-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .output-box {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Simple Interest Calculator
def simple_interest(principal, rate, time):
    roi = (principal * rate * time) / 100
    return principal + roi, roi

# Compound Interest Calculator
def compound_interest(principal, rate, time):
    amount = principal * ((1 + rate / 100) ** time)
    return amount, amount - principal

# SIP Calculator
def sip_investment(principal, rate, time, period):
    if period == "Years":
        time = time * 12  # Convert years to months
    amount = 0
    monthly_rate = rate / 100 / 12  # Convert annual rate to monthly rate
    for t in range(int(time)):
        amount += principal
        amount *= 1 + monthly_rate
    if period == "Years":
        return amount, amount - (principal * (time / 12))  # Return total amount and ROI
    else:
        return amount, amount - principal  # Return total amount and ROI

# NPS Calculator
def nps_investment(principal, rate, time, period):
    if period == "Months":
        time = time / 12
    amount = principal * ((1 + rate / 100) ** time)
    return amount, amount - principal

# Lumpsum Calculator
def lumpsum_investment(principal, rate, time, period):
    if period == "Months":
        time = time / 12
    amount = principal * ((1 + rate / 100) ** time)
    return amount, amount - principal

# Investment Calculator
def investment_return(principal, rate, time, period):
    if period == "Months":
        time = time / 12
    amount = principal * ((1 + rate / 100) ** time)
    return amount, amount - principal

st.title("Return On Investment Calculator")

# Divide the page into three columns
col1, col2, col3 = st.columns([1,1.5, 1.5])

# Input section on the left side
with col1:
    st.markdown("<div class='section-title'>Input</div>", unsafe_allow_html=True)
    principal = st.number_input("Principal Amount", min_value=0.0)
    rate = st.number_input("Rate of Interest (%)", min_value=0.0)
    time = st.number_input("Time", min_value=0.0)
    period = st.selectbox("Time Period", ["Years", "Months"])

    button_clicked = st.button("Calculate ROI")

# Output section in the middle
with col2:
    if button_clicked:
        principal_si, roi_si = simple_interest(principal, rate, time)
        principal_ci, roi_ci = compound_interest(principal, rate, time)
        principal_nps, roi_nps = nps_investment(principal, rate, time, period)
        principal_lumpsum, roi_lumpsum = lumpsum_investment(principal, rate, time, period)
        principal_investment, roi_investment = investment_return(principal, rate, time, period)

        st.markdown("<div class='section-title'>ROI</div>", unsafe_allow_html=True)
        st.write("<div class='output-box'>", unsafe_allow_html=True)
        st.write(f"Simple Interest ROI: {roi_si:.2f}")
        st.write(f"Principal with ROI: {principal_si:.2f}")
        st.write(" ")
        st.write(f"Compound Interest ROI: {roi_ci:.2f}")
        st.write(f"Principal with ROI: {principal_ci:.2f}")
        st.write(" ")
        st.write(f"NPS ROI: {roi_nps:.2f}")
        st.write(f"Principal with ROI: {principal_nps:.2f}")
        st.write(" ")
        st.write(f"Lumpsum ROI: {roi_lumpsum:.2f}")
        st.write(f"Principal with ROI: {principal_lumpsum:.2f}")
        st.write(" ")
        st.write(f"Investment ROI: {roi_investment:.2f}")
        st.write(f"Principal with ROI: {principal_investment:.2f}")
        st.write("</div>", unsafe_allow_html=True)

        # Create a bar graph to show ROI of each plan
        fig, ax = plt.subplots()
        plans = ['Simple Interest', 'Compound Interest', 'NPS', 'Lumpsum', 'Investment']
        rois = [roi_si, roi_ci, roi_nps, roi_lumpsum, roi_investment]
        ax.bar(plans, rois, color=['blue', 'orange', 'green', 'red', 'purple'])
        ax.set_xlabel('Financial Plans')
        ax.set_ylabel('ROI')
        ax.set_title('ROI of Each Financial Plan')
        ax.set_xticklabels(plans, rotation=45, ha='right')
        ax.grid(axis='y')

        # Display the bar graph
        st.pyplot(fig)

# SIP section on the right side
with col3:
    if button_clicked:
        principal_sip, roi_sip = sip_investment(principal, rate, time, period)

        st.markdown("<div class='section-title'>SIP ROI</div>", unsafe_allow_html=True)
        st.write("<div class='output-box'>", unsafe_allow_html=True)
        st.write(f"SIP ROI: {roi_sip:.2f}")
        st.write(f"Principal with ROI: {principal_sip:.2f}")

        # Calculate year-wise amounts and create a plot
        years = np.arange(0, time + 1, 1)
        amounts = []
        for year in years:
            amount, _ = sip_investment(principal, rate, year, "Years")
            amounts.append(amount)

        plt.figure(figsize=(8, 6))  # Adjust the size here
        plt.plot(years, amounts)
        plt.xlabel('Years')
        plt.ylabel('Amount')
        plt.title('Year-wise Amount for SIP')
        plt.grid(True)
        st.pyplot(plt)
        st.write("</div>", unsafe_allow_html=True)
