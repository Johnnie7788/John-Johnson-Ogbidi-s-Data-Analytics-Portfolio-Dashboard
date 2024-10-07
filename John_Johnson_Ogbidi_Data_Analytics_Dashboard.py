#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page background image (URL or local image path)
page_bg_img = '''
<style>
body {
    background-image: url("https://your-image-url-here.com/background.jpg");
    background-size: cover;
    color: white;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Work Experience Data with Tooltip
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

# Skills Data
skills_data = pd.DataFrame({
    "Role": ["Data Analyst (Research)", "Data Analyst (Research)", "Data Analyst (Research)", "Data Analyst (Research)", "Data Analyst (Research)", "Data Analyst (Research)", "Data Analyst (Research)", "Data Analyst (Research)", "Data Analyst (Research)",
             "Data Analyst & Director of Operations", "Data Analyst & Director of Operations", "Data Analyst & Director of Operations", "Data Analyst & Director of Operations", "Data Analyst & Director of Operations", "Data Analyst & Director of Operations", "Data Analyst & Director of Operations", "Data Analyst & Director of Operations", "Data Analyst & Director of Operations"],
    "Skill": ["Python", "SQL", "Power BI", "Tableau", "Machine Learning", "Azure", "R", "KNIME", "Office 365", 
              "Python", "SQL", "Power BI", "Tableau", "Machine Learning", "Azure", "R", "KNIME", "Office 365"],
    "Skill Level (%)": [90, 85, 70, 0, 80, 75, 60, 30, 95, 
                        80, 75, 60, 90, 65, 50, 50, 40, 85]
})

# Project Data with Tooltip and Labels
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

# GitHub Scripts
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

# Overall Technical Skills with SAP and SAS included
overall_skills = {
    "Skill": [
        "Python", "SQL", "Power BI", "Tableau", "Machine Learning",
        "Azure", "R", "KNIME", "Office 365", "SAS", "SAP"
    ],
    "Proficiency": [90, 80, 65, 45, 75, 60, 55, 35, 90, 70, 60]
}

df_overall_skills = pd.DataFrame(overall_skills)

# Streamlit Layout of the dashboard with section backgrounds
st.title("John Johnson Ogbidi's Data Analytics Portfolio Dashboard")

# Work Experience Timeline with Tooltip
st.markdown('''<style>div[role="heading"]{background-color:#3b5998;padding:10px;border-radius:10px;}</style>''', unsafe_allow_html=True)
st.header("Work Experience Timeline")
fig_work_exp = px.bar(
    df_work_exp,
    x='Role',
    y='Duration (Years)',
    color='Company',
    text='Key Achievement',
    hover_data={'Key Achievement': True},
    title="Duration and Key Achievements of Roles",
    labels={"Duration (Years)": "Years in Role"}
)
st.plotly_chart(fig_work_exp)

# Skills Breakdown per Role with Labels
st.markdown('''<style>div[role="heading"]{background-color:#4CAF50;padding:10px;border-radius:10px;}</style>''', unsafe_allow_html=True)
st.header("Technical Skills Applied in Roles")
fig_skills_by_role = px.bar(
    skills_data,
    x='Role',
    y='Skill Level (%)',
    color='Skill',
    barmode='group',
    title="Technical Skills by Role",
    text_auto=True
)
st.plotly_chart(fig_skills_by_role)

# Project Impact with Tooltips and Labels
st.markdown('''<style>div[role="heading"]{background-color:#ff9800;padding:10px;border-radius:10px;}</style>''', unsafe_allow_html=True)
st.header("Project Impact")
fig_projects = px.bar(
    df_projects,
    x='Project',
    y='Impact (%)',
    text='Key Detail',
    title="Impact of Key Projects (in %)",
    hover_data={'Key Detail': True},
    labels={"Impact (%)": "Impact (%)"}
)
st.plotly_chart(fig_projects)

# Overall Technical Skills Breakdown
st.markdown('''<style>div[role="heading"]{background-color:#9C27B0;padding:10px;border-radius:10px;}</style>''', unsafe_allow_html=True)
st.header("Overall Technical Skills Breakdown")
fig_overall_skills = px.pie(
    df_overall_skills,
    names='Skill',
    values='Proficiency',
    title="Overall Technical Skills Breakdown"
)
st.plotly_chart(fig_overall_skills)

# GitHub Scripts represented in alphabetical order
st.markdown('''<style>div[role="heading"]{background-color:#00BCD4;padding:10px;border-radius:10px;}</style>''', unsafe_allow_html=True)
st.header("GitHub Scripts (Alphabetical Order)")
fig_scripts = go.Figure(data=[
    go.Bar(
        x=scripts_data['Script'],
        y=[1]*len(scripts_data),
        marker_color=px.colors.qualitative.Prism,
        text=scripts_data['Script'],
        hoverinfo='text',
        name="Scripts"
    )
]).update_traces(marker_line_width=2).update_layout(
    title="GitHub Scripts",
    xaxis_title="Script",
    yaxis_title="Count"
)
st.plotly_chart(fig_scripts)

# Education Section
st.markdown('''<style>div[role="heading"]{background-color:#FFC107;padding:10px;border-radius:10px;}</style>''', unsafe_allow_html=True)
st.header("Education")
st.markdown("""
- **MSc Data Analytics, University of Central Lancashire, England (2023)**
- **MSc Geophysics, Delta State University, Nigeria (2014)**
- **BSc Physics, Delta State University, Nigeria (2007)**
""")

# Certifications Section
st.markdown('''<style>div[role="heading"]{background-color:#f44336;padding:10px;border-radius:10px;}</style>''', unsafe_allow_html=True)
st.header("Certifications")
st.markdown("""
- **SAS Certified: Business Intelligence and Data Mining**
""")

# Contact Information
st.markdown('''<style>div[role="heading"]{background-color:#607D8B;padding:10px;border-radius:10px;}</style>''', unsafe_allow_html=True)
st.header("Contact Information")
st.markdown("""
- **Email**: johnjohnsonogbidi@gmail.com  
- **Phone**: +49 162 5839423  
- **GitHub**: [https://github.com/Johnnie7788/Business-Intelligence-Analytics-Scripts](https://github.com/Johnnie7788/Business-Intelligence-Analytics-Scripts)
""")

