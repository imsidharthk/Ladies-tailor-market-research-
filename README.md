🛡️ 📢 Disclaimer
Due to privacy concerns, the original dataset containing shop names, phone numbers, and addresses cannot be shared publicly. The data was collected for internal analysis and strategic decision-making by S.L. Tailor. Any shared version (if applicable) will be anonymized or sample-only to protect the identities of the businesses involved.

# 🧵 Market Research & Data Analytics for S.L. Tailor – Ranchi

This project aimed to help **S.L. Tailor** understand the local market landscape of ladies tailor shops in **Ranchi, India**. The focus was on collecting, cleaning, and analyzing competitor data to support **area-wise marketing, pricing, and business decisions**.

---

## 🔧 Tools & Technologies Used

- **Python**, **Selenium** – Web scraping from Google Maps  
- **Excel (Advanced Functions)** – Data cleaning  
- **Power Query** – Handling data inconsistencies and transformations  
- **Google Sheets** – Data automation and syncing  
- **Google Looker Studio**, **Power BI** – Interactive dashboard creation

---

## 🎯 Project Goals

- Identify competitors in the ladies tailoring business across Ranchi  
- Analyze their ratings, locations, and distribution  
- Suggest areas for targeted advertising and pricing strategy  
- Build interactive dashboards for easy business decision-making

---

## 🧠 Challenges & Solutions

### 1. **Web Scraping Detection**
**Problem:** Google Maps detects automated behavior and blocks bots.  
**Solution:** Used `WebDriverWait` and added time delays to mimic human behavior and avoid automation detection.

### 2. **Dirty and Inconsistent Address/Phone Data**
**Problem:** Address and phone number fields contained garbage characters (like special symbols).  
**Solution:** Replaced garbage characters with spaces, then applied `.strip()` to clean the values.

### 3. **Extracting Pincode, Area, State from Address**
**Problem:** The address column had inconsistent comma-separated values (sometimes 5, sometimes 6 commas), making normal split-to-column unreliable.  
**Solution:** Used **Power Query** in Excel to dynamically split and clean the data based on pattern recognition.

---

## 📊 Insights & Outcomes

- A complete dataset of over **100+ tailor shops** with Name, Address, GMap link, Ratings, and Area info.  
- **Interactive dashboards** created in Google Looker Studio and Power BI for:
  - Area-wise shop density
  - Competition levels
  - Pricing trends
  - Marketing zone recommendations

---

## 📎 Deliverables
 
- Google Looker Studio Dashboard  
- Power BI Dashboard  
- Web scraping Python script 1st run app.py then run scrapper2.py

---

## 🚀 Impact

Enabled the client to launch **targeted ad campaigns**, optimize pricing, and choose **profitable locations** based on data-driven insights.

---


