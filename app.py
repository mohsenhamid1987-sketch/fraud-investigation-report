import streamlit as st
import pandas as pd
from datetime import datetime
from fpdf import FPDF

# Page Configuration
st.set_page_config(page_title="Threat Intelligence & Fraud Investigation Portal", layout="wide")

# Custom CSS for Hero Background Image & Clean Light Corporate Theme
st.markdown("""
    <style>
    /* Main App Background (Clean light for the rest of the page) */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Hero Banner with Fixed Background Image only in the top section */
    .hero-banner {
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.90)), 
                    url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 45px 35px;
        border-radius: 12px;
        border-left: 6px solid #f59e0b;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    }
    
    .hero-banner h1 {
        color: #ffffff;
        font-size: 28px;
        font-weight: 800;
        margin: 0 0 10px 0;
        letter-spacing: -0.5px;
    }
    
    .hero-banner p {
        color: #cbd5e1;
        font-size: 14px;
        margin: 0;
    }

    /* Section Headers */
    h2 {
        color: #0f172a;
        font-size: 18px;
        font-weight: 600;
        border-bottom: 1px solid #cbd5e1;
        padding-bottom: 8px;
        margin-top: 30px;
    }
    
    /* Inputs & Textareas Styling for Light Theme */
    input, textarea, select {
        color: #0f172a !important;
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 6px !important;
    }

    /* Submit / Generate PDF Button */
    .stButton>button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #ffffff;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        padding: 14px 28px;
        width: 100%;
        font-size: 16px;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #d97706 100%, #b45309 100%);
        color: #ffffff;
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4);
    }
    
    label { color: #334155 !important; font-weight: 600 !important; font-size: 13px !important; }
    </style>
""", unsafe_allow_html=True)

# 1. Hero Banner with Image Background
st.markdown("""
    <div class="hero-banner">
        <h1>Threat Intelligence & Fraud Defense Portal</h1>
        <p>Leverage curated intelligence for proactive fraud defense and automated risk oversight &nbsp;|&nbsp; <b>Lead Investigator: Mohsen Hassan, CFE</b></p>
    </div>
""", unsafe_allow_html=True)

# MCC Options List
mcc_list = [
    "5999 - Miscellaneous and Specialty Retail Stores",
    "5411 - Grocery Stores and Supermarkets",
    "5812 - Eating Places and Restaurants",
    "5967 - Direct Marketing - Incoming Telemarketing Merchants",
    "6012 - Financial Institutions - Merchandise, Services, and Debt Repayment",
    "7995 - Betting, Casino Gaming Chips, and Lotteries",
    "4816 - Computer Network/Information Services",
    "5732 - Electronics Stores"
]

# 2. Main Investigation Form
with st.form("threat_investigation_form"):
    
    st.header("1. Investigation Details")
    c1, c2, c3 = st.columns(3)
    with c1:
        inv_number = st.text_input("Investigation Number", value="INV-2026-099")
        inv_type = st.selectbox("Investigation Type", [
            "Fraud Rate Exceeded Threshold",
            "Chargeback Spike / ECP Violation",
            "Transaction Decline Rate Alert",
            "Card-Testing / Bot Attack",
            "Digital Skimming / Malware Alert",
            "Compliance / Standards Violation"
        ])
        inv_date = str(st.date_input("Investigation Date", datetime.today()))
    with c2:
        merchant_name = st.text_input("Merchant Name", value="Global E-Commerce Outlet")
        merchant_id = st.text_input("Merchant ID", value="MID-554321980")
        mcc = st.selectbox("MCC (Merchant Category Code)", mcc_list)
    with c3:
        acquirer = st.selectbox("Responsible Acquirer", [
            "Global Acquiring Bank",
            "First Atlantic Commerce",
            "Worldpay Processing",
            "Checkout.com Acquiring",
            "Cybersource Financial"
        ])
        investigator = st.text_input("Responsible Investigator", value="Mohsen Hassan, CFE")
        inv_status = st.selectbox("Investigation Status", ["Open", "Under Review", "Closed / Resolved"])

    st.header("2. Reason for Investigation & Threat Trigger")
    reason_trigger = st.selectbox("Trigger Alert Category", [
        "Monthly fraud rate exceeded established Acquirer threshold",
        "Chargeback count & ratio increased significantly",
        "Transaction decline rate exceeded acceptable limits",
        "Potential violation of Standards identified",
        "Notification of compliance violation received from scheme"
    ])
    reason_notes = st.text_area("Reason Notes & Specific Details", value="Monthly fraud rate exceeded threshold accompanied by abnormal card-testing velocity.")

    st.header("3. Detailed Event Analysis & Metrics")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        total_tx = st.number_input("Total Tx Count", value=5000)
        total_val = st.number_input("Total Tx Value ($)", value=250000.0)
    with m2:
        fraud_tx = st.number_input("Fraud Tx Count", value=150)
        fraud_val = st.number_input("Fraud Tx Value ($)", value=12500.0)
    with m3:
        cb_count = st.number_input("Chargeback Count", value=45)
        cb_val = st.number_input("Chargeback Value ($)", value=4500.0)
    with m4:
        decline_rate = st.number_input("Decline Rate (%)", value=4.2)

    f_rate = (fraud_tx / total_tx * 100) if total_tx > 0 else 0.0
    cb_rate = (cb_count / total_tx * 100) if total_tx > 0 else 0.0
    st.info(f"⚡ **Calculated Threat KPIs:** Fraud Rate = **{f_rate:.2f}%** | Chargeback Rate = **{cb_rate:.2f}%**")

    analysis_notes = st.text_area("Analysis & Evidence Notes", value="Anomalous automated bot traffic targeting checkout endpoints. Absence of 3DS step-up verification.")

    st.header("4. Findings & Risk Assessment")
    f_col1, f_col2 = st.columns([3, 1])
    with f_col1:
        identified_issue = st.selectbox("Primary Identified Issue", [
            "Excessive fraudulent volume & missing velocity filters",
            "Compromised payment gateway security / missing 3DS",
            "High chargeback exposure leading to ECP risk",
            "Merchant non-compliance with data security standards"
        ])
        issues_notes = st.text_area("Identified Issues Notes", value="Massive card-testing vulnerability and elevated fraud ratios.")
        
        root_cause = st.selectbox("Root Cause Category", [
            "Unprotected gateway API / Checkout endpoints",
            "Lack of multi-factor or 3DS authentication",
            "Weak merchant credential management",
            "Inadequate transaction monitoring and alerting"
        ])
        
        standards_involved = st.selectbox("Standards / Program Involved", [
            "Security Development Program (SDP)",
            "Excessive Chargeback Program (ECP)",
            "Data Security Standard (DSS) Compliance",
            "Global Fraud Monitoring Standards"
        ])
    with f_col2:
        risk_assessment = st.selectbox("Risk Assessment Level", ["Low", "Medium", "High"], index=2)

    st.header("5. Corrective Actions & Monitoring")
    c_action_1 = st.selectbox("Corrective Action 1", [
        "Implement mandatory 3DS authentication",
        "Enhanced Merchant transaction monitoring",
        "Adjustment of fraud and chargeback monitoring thresholds",
        "Temporary suspension of Merchant processing",
        "Merchant education and compliance remediation"
    ])
    action_status = st.selectbox("Action Status", ["Pending", "Completed"])
    action_notes = st.text_area("Corrective Action Notes", value="Enforced 3DS integration and tightened real-time velocity rules.")

    st.header("6. Conclusion & Ongoing Monitoring")
    conclusion_status = st.selectbox("Investigation Conclusion", [
        "Issue resolved and merchant returned to compliance",
        "Investigation ongoing with temporary restrictions",
        "Merchant terminated / processing privileges revoked"
    ])
    conclusion_notes = st.text_area("Conclusion Summary Notes", value="Merchant is currently under temporary restriction pending final 3DS verification.")
    
    monitoring_freq = st.selectbox("Monitoring Frequency", ["Daily", "Weekly", "Monthly"], index=0)
    followup_req = st.selectbox("Further Investigation Required", ["No", "Yes"], index=0)

    st.header("7. Approvals & Sign-off")
    a1, a2 = st.columns(2)
    with a1:
        prepared_by = st.text_input("Prepared By", value="Mohsen Hassan, CFE")
    with a2:
        approved_by = st.selectbox("Approved By", [
            "Head of Risk & Compliance",
            "Director of Fraud Operations",
            "Chief Risk Officer (CRO)",
            "Global Acquiring Risk Manager"
        ])

    submitted = st.form_submit_button("📥 Generate & Download PDF Report")

# PDF Generation Logic
if submitted:
    class PDFReport(FPDF):
        def header(self):
            self.set_fill_color(17, 24, 39)
            self.rect(0, 0, 210, 25, 'F')
            self.set_text_color(255, 255, 255)
            self.set_font('helvetica', 'B', 12)
            self.cell(0, 15, "THREAT INTELLIGENCE & FRAUD INVESTIGATION REPORT", 0, 1, 'C')
            self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_font('helvetica', 'I', 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 10, "Confidential - Internal Enterprise Use Only | Investigator: Mohsen Hassan, CFE", 0, 0, 'C')

    pdf = PDFReport()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    effective_width = 190
    
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(effective_width, 10, f"Investigation Summary: {inv_number}", 0, 1)
    
    pdf.set_font("helvetica", "", 10)
    pdf.cell(effective_width, 6, f"Date: {inv_date} | Type: {inv_type}", 0, 1)
    pdf.cell(effective_width, 6, f"Merchant: {merchant_name} (ID: {merchant_id}) | MCC: {mcc}", 0, 1)
    pdf.cell(effective_width, 6, f"Acquirer: {acquirer} | Status: {inv_status}", 0, 1)
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(effective_width, 8, "2. Reason for Investigation", 0, 1)
    pdf.set_font("helvetica", "", 10)
    pdf.cell(effective_width, 6, f"Trigger: {reason_trigger}", 0, 1)
    pdf.multi_cell(effective_width, 6, f"Notes: {reason_notes}")
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(effective_width, 8, "3. Event Analysis & Metrics", 0, 1)
    pdf.set_font("helvetica", "", 10)
    pdf.cell(effective_width, 6, f"Total Transactions: {total_tx:,} (${total_val:,.2f})", 0, 1)
    pdf.cell(effective_width, 6, f"Fraud Transactions: {fraud_tx:,} (${fraud_val:,.2f}) - Rate: {f_rate:.2f}%", 0, 1)
    pdf.cell(effective_width,
