import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Fraud Investigation Report", layout="wide")

# Main Title & Header
st.title("🛡️ FRAUD AND LOSS CONTROL INVESTIGATION REPORT")
st.caption("Report Classification: Confidential – Internal Use Only")
st.markdown("---")

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
        investigator = st.text_input("Responsible Investigator", value="Risk Analyst Team")
        inv_status = st.selectbox("Investigation Status", ["Open", "Under Review", "Closed"])

    st.markdown("---")

    # ---------------------------------------------------------
    # 2. Reason for Investigation
    # ---------------------------------------------------------
    st.header("2. Reason for Investigation")
    reason = st.text_area(
        "Describe the event or monitoring alert that triggered the investigation:",
        value="Monthly fraud rate exceeded the Acquirer's established threshold and notification of a compliance violation was received."
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

    st.info(f"📊 **Calculated Metrics Preview:** Fraud Rate (Count) = **{fraud_rate_count:.2f}%** | Fraud Rate (Value) = **{fraud_rate_val:.2f}%** | Chargeback Rate = **{cb_rate_count:.2f}%**")

    analysis_notes = st.text_area(
        "Findings, Monitoring Alerts, Root Cause & Evidence Reviewed:",
        value="Spike in e-commerce transactions originating from high-risk BINs. Lack of 3DS authentication implementation."
    )

    st.markdown("---")

    # ---------------------------------------------------------
    # 4. Investigation Findings
    # ---------------------------------------------------------
    st.header("4. Investigation Findings")
    col_f1, col_f2 = st.columns([3, 1])
    
    with col_f1:
        identified_issues = st.text_area("Identified Issue(s)", value="Excessive fraudulent transactions and lack of proper velocity checks.")
        root_cause = st.text_input("Root Cause", value="Compromised payment gateway security / missing 3DS.")
        impact = st.text_area("Impact on Merchant or Acquirer", value="Potential financial loss and exposure to scheme fines.")
        mastercard_standards = st.text_input("Mastercard Standards or Program Requirements Involved", value="Mastercard SDP / Excessive Chargeback Program (ECP)")
    
    with col_f2:
        risk_assessment = st.radio("Risk Assessment", ["Low", "Medium", "High"], index=2)

    st.markdown("---")

    # ---------------------------------------------------------
    # 5. Corrective Actions
    # ---------------------------------------------------------
    st.header("5. Corrective Actions")
    st.write("Actions required or implemented to address the findings:")
    
    action_1 = st.text_input("Action 1", value="Implement mandatory 3DS authentication")
    status_1 = st.selectbox("Status 1", ["Pending", "Completed"], index=0, key="s1")
    
    action_2 = st.text_input("Action 2", value="Adjustment of fraud monitoring thresholds")
    status_2 = st.selectbox("Status 2", ["Pending", "Completed"], index=1, key="s2")

    st.markdown("---")

    # ---------------------------------------------------------
    # 6. Investigation Conclusion
    # ---------------------------------------------------------
    st.header("6. Investigation Conclusion")
    conclusion = st.text_area(
        "Conclusion Summary:",
        value="Investigation is ongoing. Merchant is currently under temporary restriction pending 3DS integration."
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
        prepared_by = st.text_input("Prepared by (Name)", value="Risk Analyst")
        reviewed_by = st.text_input("Reviewed by (Name)", value="Risk Manager")
    with a_col2:
        approved_by = st.text_input("Approved by (Name)", value="Head of Risk & Compliance")

    st.markdown("---")

    # ---------------------------------------------------------
    # 9. Supporting Documentation
    # ---------------------------------------------------------
    st.header("9. Supporting Documentation")
    docs_notes = st.text_area("Attached Evidence / Reports Reference:", value="Transaction monitoring logs, Acquirer alert history, Merchant communication records.")

    # Submit Button
    submitted = st.form_submit_button("💾 Save & Generate Report")

if submitted:
    st.success("✅ The Fraud Investigation Report has been successfully saved and processed!")
