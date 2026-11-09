import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Fraud & Loss Control Investigation Report", layout="wide")

# Custom CSS for Sleek Enterprise Fintech UI (Inspired by Threat Intel Portals)
st.markdown("""
    <style>
    /* Global App Background & Font */
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Top Enterprise Banner */
    .fintech-header {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #374151;
        border-left: 6px solid #f59e0b;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
    
    .fintech-header h1 {
        color: #ffffff;
        font-size: 24px;
        font-weight: 700;
        margin: 0 0 6px 0;
        letter-spacing: -0.5px;
    }
    
    .fintech-header p {
        color: #9ca3af;
        font-size: 13px;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Section Headers Styling */
    h2 {
        color: #f3f4f6;
        font-size: 18px;
        font-weight: 600;
        border-bottom: 1px solid #374151;
        padding-bottom: 10px;
        margin-top: 35px;
        letter-spacing: 0.5px;
    }
    
    h3 {
        color: #e5e7eb;
        font-size: 15px;
    }
    
    /* Input Fields & Text Areas Dark Modern Theme */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea {
        background-color: #1f2937;
        color: #f9fafb;
        border-radius: 8px;
        border: 1px solid #4b5563;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #f59e0b;
        box-shadow: 0 0 0 1px #f59e0b;
    }

    /* Metric / Info Box Styling */
    .stInfo {
        background-color: rgba(245, 158, 11, 0.1);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-left: 4px solid #f59e0b;
        color: #fcd34d;
        border-radius: 8px;
    }
    
    /* Submit Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #0b0f19;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        padding: 12px 28px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.2);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        box-shadow: 0 6px 16px rgba(245, 158, 11, 0.35);
        color: #000000;
    }
    
    /* Labels */
    label {
        color: #d1d5db !important;
        font-weight: 500 !important;
        font-size: 13px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sleek Enterprise Header
st.markdown("""
    <div class="fintech-header">
        <h1>FRAUD AND LOSS CONTROL INVESTIGATION REPORT</h1>
        <p>THREAT INTELLIGENCE & RISK COMPLIANCE PORTAL &nbsp;|&nbsp; <b>Investigator: Mohsen Hassan, CFE</b></p>
    </div>
""", unsafe_allow_html=True)

st.caption("Report Classification: Confidential – Internal Enterprise Use Only")

# Main Form
with st.form("fraud_report_complete_form"):
    
    # ---------------------------------------------------------
    # 1. Investigation Details
    # ---------------------------------------------------------
    st.header("1. Investigation Details")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        inv_number = st.text_input("Investigation Number", value="INV-2026-001")
        inv_type = st.selectbox("Investigation Type", ["Fraud", "Chargeback", "Decline", "Compliance Violation"])
        inv_date = st.date_input("Investigation Date", datetime.today())
        
    with col2:
        merchant_name = st.text_input("Merchant Name", value="Example Merchant LLC")
        merchant_id = st.text_input("Merchant ID", value="MID-987654321")
        mcc = st.text_input("MCC (Merchant Category Code)", value="5999")
        
    with col3:
        acquirer = st.text_input("Responsible Acquirer", value="Global Acquiring Bank")
        investigator = st.text_input("Responsible Investigator", value="Mohsen Hassan, CFE")
        inv_status = st.selectbox("Investigation Status", ["Open", "Under Review", "Closed"])

    st.markdown("---")

    # ---------------------------------------------------------
    # 2. Reason for Investigation
    # ---------------------------------------------------------
    st.header("2. Reason for Investigation")
    reason = st.text_area(
        "Describe the event or monitoring alert that triggered the investigation:",
        value="Monthly fraud rate exceeded the established risk threshold and compliance alert notification was triggered."
    )

    st.markdown("---")

    # ---------------------------------------------------------
    # 3. Detailed Event Description and Analysis
    # ---------------------------------------------------------
    st.header("3. Detailed Event Description and Analysis")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        total_tx_count = st.number_input("Total Transaction Count", min_value=0, value=1000)
        total_tx_val = st.number_input("Total Transaction Value ($)", min_value=0.0, value=50000.0)
    with m2:
        fraud_tx_count = st.number_input("Fraud Transaction Count", min_value=0, value=25)
        fraud_tx_val = st.number_input("Fraud Transaction Value ($)", min_value=0.0, value=2500.0)
    with m3:
        cb_count = st.number_input("Chargeback Count", min_value=0, value=10)
        cb_val = st.number_input("Chargeback Value ($)", min_value=0.0, value=1000.0)
    with m4:
        decline_rate = st.number_input("Decline Rate (%)", min_value=0.0, max_value=100.0, value=3.5)

    # Automated calculations display
    fraud_rate_count = (fraud_tx_count / total_tx_count * 100) if total_tx_count > 0 else 0.0
    fraud_rate_val = (fraud_tx_val / total_tx_val * 100) if total_tx_val > 0 else 0.0
    cb_rate_count = (cb_count / total_tx_count * 100) if total_tx_count > 0 else 0.0

    st.info(f"📊 **Calculated Threat Metrics:** Fraud Rate (Count) = **{fraud_rate_count:.2f}%** | Fraud Rate (Value) = **{fraud_rate_val:.2f}%** | Chargeback Rate = **{cb_rate_count:.2f}%**")

    analysis_notes = st.text_area(
        "Findings, Monitoring Alerts, Root Cause & Evidence Reviewed:",
        value="Spike in high-risk e-commerce transactions originating from anomalous BIN profiles. Lack of robust 3DS verification."
    )

    st.markdown("---")

    # ---------------------------------------------------------
    # 4. Investigation Findings
    # ---------------------------------------------------------
    st.header("4. Investigation Findings")
    col_f1, col_f2 = st.columns([3, 1])
    
    with col_f1:
        identified_issues = st.text_area("Identified Issue(s)", value="Excessive fraudulent volume and absence of velocity check rules.")
        root_cause = st.text_input("Root Cause", value="Gateway security loophole / missing 3DS integration.")
        impact = st.text_area("Impact on Merchant or Acquirer", value="Financial exposure and potential scheme program penalties.")
        standards_involved = st.text_input("Standards or Program Requirements Involved", value="SDP Security Guidelines / Excessive Chargeback Monitoring Program")
    
    with col_f2:
        risk_assessment = st.radio("Risk Assessment", ["Low", "Medium", "High"], index=2)

    st.markdown("---")

    # ---------------------------------------------------------
    # 5. Corrective Actions
    # ---------------------------------------------------------
    st.header("5. Corrective Actions")
    st.write("Actions required or implemented to address the findings:")
    
    action_1 = st.text_input("Action 1", value="Enforce mandatory 3DS authentication")
    status_1 = st.selectbox("Status 1", ["Pending", "Completed"], index=0, key="s1")
    
    action_2 = st.text_input("Action 2", value="Tighten real-time fraud monitoring thresholds")
    status_2 = st.selectbox("Status 2", ["Pending", "Completed"], index=1, key="s2")

    st.markdown("---")

    # ---------------------------------------------------------
    # 6. Investigation Conclusion
    # ---------------------------------------------------------
    st.header("6. Investigation Conclusion")
    conclusion = st.text_area(
        "Conclusion Summary:",
        value="Investigation active. Merchant under temporary processing restriction until 3DS remediation is verified."
    )

    st.markdown("---")

    # ---------------------------------------------------------
    # 7. Follow-up and Ongoing Monitoring
    # ---------------------------------------------------------
    st.header("7. Follow-up and Ongoing Monitoring")
    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        monitoring_freq = st.selectbox("Monitoring Frequency", ["Daily", "Weekly", "Monthly"], index=0)
    with f_col2:
        followup_date = st.date_input("Follow-up Review Date", datetime.today())
    with f_col3:
        further_investigation = st.selectbox("Further Investigation Required", ["Yes", "No"], index=0)

    st.markdown("---")

    # ---------------------------------------------------------
    # 8. Investigation Approval
    # ---------------------------------------------------------
    st.header("8. Investigation Approval")
    a_col1, a_col2 = st.columns(2)
    with a_col1:
        prepared_by = st.text_input("Prepared by (Name)", value="Mohsen Hassan, CFE")
        reviewed_by = st.text_input("Reviewed by (Name)", value="Risk Manager")
    with a_col2:
        approved_by = st.text_input("Approved by (Name)", value="Head of Risk & Compliance")

    st.markdown("---")

    # ---------------------------------------------------------
    # 9. Supporting Documentation
    # ---------------------------------------------------------
    st.header("9. Supporting Documentation")
    docs_notes = st.text_area("Attached Evidence / Reports Reference:", value="Transaction logs, alert history records, merchant communications.")

    # Submit Button
    submitted = st.form_submit_button("💾 Save & Generate Report")

if submitted:
    st.success("✅ Investigation Report successfully processed and secured by Mohsen Hassan, CFE!")
