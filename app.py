import streamlit as st
import pandas as pd
from datetime import datetime
from fpdf import FPDF

# Page Configuration
st.set_page_config(page_title="Threat Intelligence & Fraud Investigation Portal", layout="wide")

# Custom CSS for Enterprise Dark UI & Clear Input Text Colors
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        padding: 35px;
        border-radius: 12px;
        border: 1px solid #374151;
        border-left: 6px solid #f59e0b;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
    }
    
    .hero-banner h1 {
        color: #ffffff;
        font-size: 28px;
        font-weight: 800;
        margin: 0 0 10px 0;
    }
    
    .hero-banner p {
        color: #9ca3af;
        font-size: 14px;
        margin: 0;
    }

    /* Section Headers */
    h2 {
        color: #f3f4f6;
        font-size: 18px;
        font-weight: 600;
        border-bottom: 1px solid #374151;
        padding-bottom: 8px;
        margin-top: 30px;
    }
    
    /* Inputs & Textareas - Clear text color for visibility */
    input, textarea, select {
        color: #111827 !important;
        background-color: #f9fafb !important;
    }

    /* Submit / Generate PDF Button */
    .stButton>button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #0b0f19;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        padding: 14px 28px;
        width: 100%;
        font-size: 16px;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        color: #000000;
    }
    
    label { color: #d1d5db !important; font-weight: 500 !important; font-size: 13px !important; }
    </style>
""", unsafe_allow_html=True)

# 1. Hero Banner (Platform Style - Clean Header)
st.markdown("""
    <div class="hero-banner">
        <h1>Threat Intelligence & Fraud Defense Portal</h1>
        <p>Leverage curated intelligence for proactive fraud defense and automated risk oversight &nbsp;|&nbsp; <b>Lead Investigator: Mohsen Hassan, CFE</b></p>
    </div>
""", unsafe_allow_html=True)

# 2. Main Investigation Form
with st.form("threat_investigation_form"):
    
    st.header("1. Investigation Details")
    c1, c2, c3 = st.columns(3)
    with c1:
        inv_number = st.text_input("Investigation Number", value="INV-2026-099")
        inv_type = st.selectbox("Investigation Type", ["Card Testing", "Digital Skimming", "Payment Fraud", "Compliance Violation"])
        inv_date = str(st.date_input("Investigation Date", datetime.today()))
    with c2:
        merchant_name = st.text_input("Merchant Name", value="Global E-Commerce Outlet")
        merchant_id = st.text_input("Merchant ID", value="MID-554321980")
        mcc = st.text_input("MCC Code", value="5967")
    with c3:
        acquirer = st.text_input("Responsible Acquirer", value="Acquiring Global Bank")
        investigator = st.text_input("Responsible Investigator", value="Mohsen Hassan, CFE")
        inv_status = st.selectbox("Investigation Status", ["Open", "Under Review", "Resolved"])

    st.header("2. Reason for Investigation & Threat Trigger")
    reason = st.text_area("Trigger Alert Description", value="Monthly fraud rate exceeded established ecosystem threshold with abnormal card-testing velocity detected from high-risk BINs.")

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

    analysis = st.text_area("Detailed Findings & Evidence", value="Anomalous automated bot traffic targeting checkout endpoints. Absence of 3DS step-up verification.")

    st.header("4. Findings & Risk Assessment")
    f_col1, f_col2 = st.columns([3, 1])
    with f_col1:
        issues = st.text_area("Identified Issues", value="Massive card-testing vulnerability and elevated fraud ratios.")
        root_cause = st.text_input("Root Cause", value="Unprotected gateway API endpoints.")
        standards = st.text_input("Standards Involved", value="Global Security & Excessive Fraud Monitoring Standards")
    with f_col2:
        risk_level = st.radio("Risk Assessment Level", ["Low", "Medium", "High"], index=2)

    st.header("5. Corrective Actions & Monitoring")
    action_1 = st.text_input("Corrective Action 1", value="Implement dynamic bot mitigation and mandatory 3DS.")
    monitoring_freq = st.selectbox("Ongoing Monitoring Frequency", ["Daily", "Weekly", "Monthly"], index=0)

    st.header("6. Approvals & Sign-off")
    a1, a2 = st.columns(2)
    with a1:
        prepared_by = st.text_input("Prepared By", value="Mohsen Hassan, CFE")
    with a2:
        approved_by = st.text_input("Approved By", value="Head of Risk Intelligence")

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
            self.cell(0, 10, f"Confidential - Internal Enterprise Use Only | Investigator: Mohsen Hassan, CFE", 0, 0, 'C')

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
    pdf.multi_cell(effective_width, 6, reason)
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(effective_width, 8, "3. Event Analysis & Metrics", 0, 1)
    pdf.set_font("helvetica", "", 10)
    pdf.cell(effective_width, 6, f"Total Transactions: {total_tx:,} (${total_val:,.2f})", 0, 1)
    pdf.cell(effective_width, 6, f"Fraud Transactions: {fraud_tx:,} (${fraud_val:,.2f}) - Rate: {f_rate:.2f}%", 0, 1)
    pdf.cell(effective_width, 6, f"Chargebacks: {cb_count} (${cb_val:,.2f}) - Rate: {cb_rate:.2f}%", 0, 1)
    pdf.cell(effective_width, 6, f"Decline Rate: {decline_rate}%", 0, 1)
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(effective_width, 8, "4. Findings & Risk Assessment", 0, 1)
    pdf.set_font("helvetica", "", 10)
    pdf.multi_cell(effective_width, 6, f"Identified Issues: {issues}")
    pdf.multi_cell(effective_width, 6, f"Root Cause: {root_cause}")
    pdf.cell(effective_width, 6, f"Risk Assessment Level: {risk_level}", 0, 1)
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(effective_width, 8, "5. Corrective Actions & Approvals", 0, 1)
    pdf.set_font("helvetica", "", 10)
    pdf.cell(effective_width, 6, f"Action Implemented: {action_1}", 0, 1)
    pdf.cell(effective_width, 6, f"Monitoring Frequency: {monitoring_freq}", 0, 1)
    pdf.cell(effective_width, 6, f"Prepared By: {prepared_by} | Approved By: {approved_by}", 0, 1)

    # Output PDF bytes safely
    pdf_output = pdf.output(dest='S')
    if isinstance(pdf_output, str):
        pdf_bytes = pdf_output.encode('latin1')
    else:
        pdf_bytes = bytes(pdf_output)

    st.success("🎉 Report generated successfully! Click below to download your official PDF.")
    st.download_button(
        label="📄 Download Investigation PDF Report",
        data=pdf_bytes,
        file_name=f"{inv_number}_Report.pdf",
        mime="application/pdf"
    )
