# 📊 GlobalTech – Sales Dashboard
Analyzing product and category profitability while identifying under-performing areas to help leadership gain a quick, unified view of sales data and business performance.  
Built using **SQL, Power BI, and Python**.

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Tools & Technologies](#tools--technologies)
- [The Problem ⛔](#the-problem-)
- [Solution I Used ✅](#solution-i-used-)
- [Work Impact 🚀](#work-impact-)
- [Dashboard](#dashboard)
- [Author & Contact](#author--contact)

---

## About the Project
A leading UK-based retail company, operating across multiple cities, wanted to centralize and track its sales data to gain deeper insights into performance, growth, and profitability.

---

## Dataset
- **Fact Tables**: Stored in **3 Excel files**, each containing multiple monthly tabs (Sales, Vendors, Inventory).  
- **Product Dimension Table**: Stored in **PostgreSQL database**.  
- **Manufacturer Data**: Images and references maintained in **Google Sheets**.  
- All Excel monthly tabs were converted into individual CSV files using Python to make them Power BI-friendly.  

---

## Tools & Technologies
- **SQL**: Used for querying, joins, filtering, and advanced analysis.  
- **Python**: Automated conversion of Excel monthly tabs into individual CSVs for seamless integration with Power BI.  
- **Power BI**: Built interactive dashboards to visualize sales KPIs and provide actionable insights.  
- **GitHub**: For hosting project files, documentation, and version control.  

---

## The Problem ⛔
1. **Inconsistent Data Structures Across Files**  
   - (*The business was honestly fed up with their data entry staff, who seemed to have a personal hobby of “creatively” renaming columns in every file.*)  
   - Sales data was scattered across multiple Excel files spanning three years, with each month stored in a separate tab.  
   - Column names were inconsistent (e.g., *“Date”* vs. *“Datee”*, *“TotalCost”* vs. *“Cost”*, *“ProductKey”* vs. *“P-Key”*).  
   - This inconsistency made it extremely difficult to append and clean the data without heavy manual effort, slowing down reporting cycles.

2. **Consolidating Data From Multiple Sources**  
   - Sales files lived in local folders, product information was stored in PostgreSQL, and manufacturer images were tucked away in Google Sheets.  
   - With data spread across different platforms and formats, consolidating everything into one reliable source became a significant hurdle.

3. **No Bird’s-Eye View of Products**  
   - The business lacked a clear picture of which products were top performers versus which contributed minimally to revenue.  
   - Without this visibility, optimizing inventory and marketing spend was a shot in the dark.

4. **Unclear Time-Series Evaluation**  
   - While the business wanted to explore time-series trends, they lacked structured visibility into seasonality, growth patterns, or sales cycles.

5. **Lack of a Unified Dashboard for Insights**  
   - Instead of one consolidated view, insights were scattered across different files and reports, making it hard for the business to track product performance, seasonal patterns, profitability, and growth in a single place.

---

## Solution I Used ✅
1. **Fixing Data Inconsistencies**  
   - A robust M script was developed to automatically clean and standardize inconsistent column names across files.  
   - This eliminated manual corrections and ensured future-proof consistency in sales data preparation.

2. **Seamless Data Consolidation**  
   - Power Query was implemented to integrate data from multiple sources (Excel files, PostgreSQL, Google Sheets).  
   - This enabled a single, reliable source of truth for analysis and reporting.

3. **Clear Product-Level Insights**  
   - A dedicated view was created to track product performance with Year-over-Year sales comparisons.  
   - Helped the business quickly identify top-performing and underperforming products.

4. **Time-Series Analysis**  
   - A specialized tab was built to provide visibility into monthly and quarterly sales trends.  
   - Comparisons against moving averages highlighted seasonal patterns and growth.

5. **Comprehensive Business Dashboard**  
   - A structured dashboard was developed with separate tabs addressing each key business question — from profitability and category contribution to seasonal trends.  
   - Leadership now has a complete and actionable view of performance.

---

## Work Impact 🚀
- **Massive Time Savings –** Automated data cleaning and consolidation eliminated countless manual hours spent fixing column names and merging files.  
- **Error-Free Reporting –** By standardizing structures and using Power Query, the business no longer suffers from inconsistent naming or manual entry mistakes.  
- **Crystal-Clear Product Insights –** Leadership now has instant visibility into top-performing and underperforming products with YoY comparisons.  
- **Smarter Forecasting & Planning –** Time-series analysis with moving averages revealed seasonal trends and growth patterns, empowering proactive planning.  
- **One Unified Dashboard –** Instead of scattered reports, the business now has a complete 360° view to act fast and strategically.

---

## Dashboard
👉 [Click here to explore the interactive Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZGY2NjRmYTYtODg0My00ZjA1LThjOTYtYzMyOGJhYTgxZjU0IiwidCI6IjYyZWE2YjA3LWY5YzUtNDk2My1hYWFhLWJjYmQ2YjhkNjFlZSJ9)  
 

---

## Author & Contact
👨‍💻 **Chirag Sharma** – Data Analyst  
📧 Email: ChiragSh146@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/chirag-sharma-cc1/)  
🔗 [Portfolio](https://www.linkedin.com/in/chirag-sharma-cc1/)  

---



