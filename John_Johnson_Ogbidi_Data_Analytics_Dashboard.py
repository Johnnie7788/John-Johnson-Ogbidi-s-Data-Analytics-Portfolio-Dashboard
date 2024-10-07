#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Custom CSS to create 3D-like sections and backgrounds
st.markdown("""
    <style>
    .section {
        background-color: #f9f9f9;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .section-header {
        color: #fff;
        background-color: #007BFF;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.5em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .education-section {
        background-color: #007BFF;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .certifications-section {
        background-color: #28A745;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .contact-section {
        background-color: #6C757D;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit Layout of the dashboard
st.title("John Johnson Ogbidi's Data Analytics Portfolio Dashboard")

# Work Experience Timeline with Tooltip
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-header">Work Experience Timeline</div>', unsafe_allow_html=True)

df_work_exp = pd.DataFrame({
    "Role": ["Data Analyst (Research)", "Data Analyst & Director of Operations"],
    "Company": [
        "Institute of Geophysics and Meteorology, University of Cologne",
        "Alberg Services Nigeria Limited"
    ],
    "Duration (Years)": [1, 10],
    "Key Achievement": [
        "30% improvement in subsurface prediction accuracy, 20% risk reduction, 25% data visualization efficiency increase",
        "25% monitoring efficiency, 14% forecasting accuracy, 12% revenue forecasting improvement"
    ]
})
fig_work_exp = px.bar(
    df_work_exp,
    x='Role',
    y='Duration (Years)',
    color='Company',
    text='Key Achievement',
    hover_data={'Key Achievement': True},
    title="Duration and Key Achievements of Roles",
    labels={"Duration (Years)": "Years in Role"},
    color_discrete_sequence=["#007BFF", "#00BFFF"]
)
st.plotly_chart(fig_work_exp)
st.markdown('</div>', unsafe_allow_html=True)

# Skills Breakdown per Role with Labels
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-header">Technical Skills Applied in Roles</div>', unsafe_allow_html=True)

skills_by_role = {
    "Role": ["Data Analyst (Research)", "Data Analyst & Director of Operations"],
    "Python": [90, 80],
    "SQL": [85, 75],
    "Power BI": [70, 60],
    "Tableau": [0, 90],
    "Machine Learning": [80, 65],
    "Azure": [75, 50],
    "R": [60, 50],
    "KNIME": [30, 40],
    "Office 365": [95, 85]
}
df_skills_by_role = pd.DataFrame(skills_by_role)
fig_skills_by_role = px.bar(
    df_skills_by_role,
    x='Role',
    y=['Python', 'SQL', 'Power BI', 'Tableau', 'Machine Learning', 'Azure',
       'R', 'KNIME', 'Office 365 (Excel, Word, PowerPoint)'],
    title="Technical Skills by Role",
    labels={"value": "Skill Level (%)"},
    barmode='group',
    text_auto=True,
    color_discrete_sequence=px.colors.qualitative.Prism
)
st.plotly_chart(fig_skills_by_role)
st.markdown('</div>', unsafe_allow_html=True)

# Project Impact Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-header">Project Impact</div>', unsafe_allow_html=True)

df_projects = pd.DataFrame({
    "Project": [
        "Subsurface Prediction Accuracy",
        "Machine Learning Risk Reduction",
        "Power BI Visualization Efficiency",
        "AI-Powered Analytics Integration",
        "Revenue Forecasting Accuracy",
        "Customer Retention Improvement",
        "Pricing Accuracy & Profitability",
        "Energy Demand Forecasting",
        "Market Share Identification",
        "Operational Efficiency"
    ],
    "Impact (%)": [30, 20, 25, 13, 20, 20, 18, 16, 22, 15],
    "Key Detail": [
        "Improved accuracy by 30%",
        "Reduced risk by 20%",
        "Enhanced efficiency by 25%",
        "Integrated AI for 13% improvement",
        "Improved revenue forecasting by 20%",
        "Increased customer retention by 20%",
        "Improved pricing accuracy by 18%",
        "Enhanced demand forecasting by 16%",
        "Improved market share identification by 22%",
        "Enhanced operational efficiency by 15%"
    ]
})
fig_projects = px.bar(
    df_projects,
    x='Project',
    y='Impact (%)',
    text='Key Detail',
    title="Impact of Key Projects (in %)",
    hover_data={'Key Detail': True},
    color_discrete_sequence=["#FF7F0E"]
)
st.plotly_chart(fig_projects)
st.markdown('</div>', unsafe_allow_html=True)

# Overall Technical Skills Breakdown
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-header">Overall Technical Skills Breakdown</div>', unsafe_allow_html=True)

df_overall_skills = pd.DataFrame({
    "Skill": [
        "Python", "SQL", "Power BI", "Tableau", "Machine Learning",
        "Azure", "R", "KNIME", "Office 365", "SAS", "SAP"
    ],
    "Proficiency": [90, 80, 65, 45, 75, 60, 55, 35, 90, 70, 60]
})
fig_overall_skills = px.pie(
    df_overall_skills,
    names='Skill',
    values='Proficiency',
    title="Overall Technical Skills Breakdown"
)
st.plotly_chart(fig_overall_skills)
st.markdown('</div>', unsafe_allow_html=True)

# GitHub Scripts represented in alphabetical order
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-header">GitHub Scripts (Alphabetical Order)</div>', unsafe_allow_html=True)

scripts_data = pd.DataFrame({
    "Script": [
        "AI-Driven Data Governance & Business Insights Generation",
        "AI-Driven Sentiment Prediction and Customer Insights Platform",
        "AI-Powered Project Management Intelligence Suite (AIPMIS)",
        "Customer Behavior Analytics",
        "Energy Trend Forecasting and Analysis",
        "Financial Forecasting Analysis",
        "Healthcare Business Intelligence: Patient Readmission Analytics and Predictive Insights",
        "Market Positioning Analysis",
        "Market Trend Analysis",
        "Operational Efficiency Analysis",
        "Pricing Modeling",
        "Sales AI Optimizer",
        "SAP FinSales Intelligence",
        "SupplyChain AI Analyst"
    ]
})
fig_scripts = go.Figure(data=[
    go.Bar(
        x=scripts_data['Script'],
        y=[1]*len(scripts_data),
        marker_color=px.colors.qualitative.Vivid,
        text=scripts_data['Script'],
        hoverinfo='text',
        name="Scripts"
    )
])
fig_scripts.update_layout(
    title="GitHub Scripts",
    xaxis_title="Script",
    yaxis_title="Count"
)
st.plotly_chart(fig_scripts)
st.markdown('</div>', unsafe_allow_html=True)

# Education Section
st.markdown('<div class="education-section">', unsafe_allow_html=True)
st.markdown("""
- **MSc Data Analytics, University of Central Lancashire, England (2023)**  
- **MSc Geophysics, Delta State University, Nigeria (2014)**  
- **BSc Physics, Delta State University, Nigeria (2007)**  
""")
st.markdown('</div>', unsafe_allow_html=True)

# Certifications Section
st.markdown('<div class="certifications-section">', unsafe_allow_html=True)
st.markdown("""
- **SAS Certified: Business Intelligence and Data Mining**
""")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Information Section
st.markdown('<div class="contact-section">', unsafe_allow_html=True)
st.markdown("""
- **Email**: johnjohnsonogbidi@gmail.com  
- **Phone**: +49 162 5839423  
- **GitHub**: [https://github.com/Johnnie7788/Business-Intelligence-Analytics-Scripts](https://github.com/Johnnie7788/Business-Intelligence-Analytics-Scripts)
""")
st.markdown('</div>', unsafe_allow_html=True)

