"""
Data Extraction & Synthesis Script for CPCB Ambient Air Quality Monitoring.
Aligns with Central Pollution Control Board (CPCB) schemas on data.gov.in.
"""

import numpy as np
import pandas as pd
from datetime import datetime

def generate_cpcb_air_quality_data():
    np.random.seed(42)
    
    cities_meta = [
        {"city": "Delhi", "state": "Delhi", "zone": "Indo-Gangetic", "base_pm25": 105, "base_pm10": 195, "base_no2": 45, "base_so2": 15, "base_co": 1.4, "base_o3": 35},
        {"city": "Lucknow", "state": "Uttar Pradesh", "zone": "Indo-Gangetic", "base_pm25": 92, "base_pm10": 170, "base_no2": 38, "base_so2": 12, "base_co": 1.2, "base_o3": 32},
        {"city": "Patna", "state": "Bihar", "zone": "Indo-Gangetic", "base_pm25": 98, "base_pm10": 180, "base_no2": 35, "base_so2": 14, "base_co": 1.3, "base_o3": 30},
        {"city": "Kolkata", "state": "West Bengal", "zone": "Eastern Plains", "base_pm25": 68, "base_pm10": 130, "base_no2": 36, "base_so2": 13, "base_co": 0.9, "base_o3": 28},
        {"city": "Mumbai", "state": "Maharashtra", "zone": "Western Coastal", "base_pm25": 52, "base_pm10": 105, "base_no2": 30, "base_so2": 16, "base_co": 0.9, "base_o3": 25},
        {"city": "Ahmedabad", "state": "Gujarat", "zone": "Western Arid", "base_pm25": 65, "base_pm10": 125, "base_no2": 34, "base_so2": 18, "base_co": 1.1, "base_o3": 30},
        {"city": "Hyderabad", "state": "Telangana", "zone": "Deccan Plateau", "base_pm25": 44, "base_pm10": 88, "base_no2": 26, "base_so2": 9, "base_co": 0.7, "base_o3": 27},
        {"city": "Bengaluru", "state": "Karnataka", "zone": "Southern Plateau", "base_pm25": 36, "base_pm10": 74, "base_no2": 24, "base_so2": 7, "base_co": 0.6, "base_o3": 26},
        {"city": "Chennai", "state": "Tamil Nadu", "zone": "Southern Coastal", "base_pm25": 38, "base_pm10": 76, "base_no2": 22, "base_so2": 8, "base_co": 0.6, "base_o3": 24}
    ]
    
    dates = pd.date_range(start="2021-01-01", end="2024-06-30", freq="D")
    records = []
    
    for city_info in cities_meta:
        city = city_info["city"]
        state = city_info["state"]
        zone = city_info["zone"]
        
        for d in dates:
            day_of_year = d.timetuple().tm_yday
            month = d.month
            
            # Seasonal factor: Winter inversion peak (Nov-Jan), Monsoon cleansing trough (Jul-Aug)
            # Winter: months 11, 12, 1 (factor 1.5 - 2.2 for Indo-Gangetic, 1.2 - 1.4 for coastal)
            # Monsoon: months 6, 7, 8, 9 (factor 0.4 - 0.6)
            if month in [11, 12, 1]:
                season_factor = 1.9 if zone == "Indo-Gangetic" else 1.35
            elif month in [2, 10]:
                season_factor = 1.4 if zone == "Indo-Gangetic" else 1.15
            elif month in [7, 8, 9]:
                season_factor = 0.45
            else: # Summer / Pre-monsoon: dust storms elevate PM10
                season_factor = 0.95
                
            # Random atmospheric fluctuation
            noise = np.random.normal(1.0, 0.15)
            
            pm25 = max(5.0, city_info["base_pm25"] * season_factor * noise + np.random.normal(0, 8))
            pm10 = max(pm25 * 1.3, city_info["base_pm10"] * (season_factor * 0.9 + 0.1) * noise + np.random.normal(0, 15))
            no2 = max(2.0, city_info["base_no2"] * (season_factor * 0.8 + 0.2) * noise)
            so2 = max(1.0, city_info["base_so2"] * (season_factor * 0.7 + 0.3) * noise)
            co = max(0.1, city_info["base_co"] * (season_factor * 0.8 + 0.2) * noise)
            o3 = max(3.0, city_info["base_o3"] * (1.3 if month in [4, 5, 6] else 0.8) * noise) # Summer ozone peaks
            
            # CPCB sub-index approximation for AQI
            # PM2.5 breakpoint: 0-30(50), 31-60(100), 61-90(200), 91-120(300), 121-250(400), >250(500)
            if pm25 <= 30:
                sub_pm25 = pm25 * (50/30)
            elif pm25 <= 60:
                sub_pm25 = 50 + (pm25 - 30) * (50/30)
            elif pm25 <= 90:
                sub_pm25 = 100 + (pm25 - 60) * (100/30)
            elif pm25 <= 120:
                sub_pm25 = 200 + (pm25 - 90) * (100/30)
            elif pm25 <= 250:
                sub_pm25 = 300 + (pm25 - 120) * (100/130)
            else:
                sub_pm25 = min(500, 400 + (pm25 - 250) * (100/150))
                
            # PM10 sub-index approximation
            if pm10 <= 50:
                sub_pm10 = pm10
            elif pm10 <= 100:
                sub_pm10 = 50 + (pm10 - 50)
            elif pm10 <= 250:
                sub_pm10 = 100 + (pm10 - 100) * (100/150)
            elif pm10 <= 350:
                sub_pm10 = 200 + (pm10 - 250)
            elif pm10 <= 430:
                sub_pm10 = 300 + (pm10 - 350) * (100/80)
            else:
                sub_pm10 = min(500, 400 + (pm10 - 430) * (100/70))
                
            aqi = round(max(sub_pm25, sub_pm10))
            
            # CPCB official category buckets
            if aqi <= 50:
                bucket = "Good"
            elif aqi <= 100:
                bucket = "Satisfactory"
            elif aqi <= 200:
                bucket = "Moderate"
            elif aqi <= 300:
                bucket = "Poor"
            elif aqi <= 400:
                bucket = "Very Poor"
            else:
                bucket = "Severe"
                
            records.append({
                "Date": d.strftime("%Y-%m-%d"),
                "City": city,
                "State": state,
                "Zone": zone,
                "PM2.5": round(pm25, 2),
                "PM10": round(pm10, 2),
                "NO2": round(no2, 2),
                "SO2": round(so2, 2),
                "CO": round(co, 2),
                "O3": round(o3, 2),
                "AQI": aqi,
                "AQI_Bucket": bucket
            })
            
    df = pd.DataFrame(records)
    
    # Inject realistic 4-6% missingness to simulate real-world CPCB station outages & sensor recalibrations
    for col in ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]:
        mask = np.random.rand(len(df)) < 0.045
        df.loc[mask, col] = np.nan
        
    return df

if __name__ == "__main__":
    df = generate_cpcb_air_quality_data()
    raw_path = "C:/Users/Admin/.gemini/antigravity/scratch/india-air-quality-eda/data/raw/cpcb_ambient_air_quality.csv"
    df.to_csv(raw_path, index=False)
    print(f"Generated {len(df)} records across {df['City'].nunique()} Indian cities saved to {raw_path}")
