# ===============================
# EXPERIMENT 4: DATA CLEANING + VISUALIZATION
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# -------------------------------
# STEP 1: LOAD DATASET
# -------------------------------

# Load your real-time dataset
df = pd.read_csv("realtime_urls.csv")

print("Dataset Loaded Successfully\n")
print(df.head())

# -------------------------------
# STEP 2: INSPECT DATA
# -------------------------------

print("\nDataset Info:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())

# -------------------------------
# STEP 3: DATA CLEANING
# -------------------------------

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna("", inplace=True)

# Convert URLs to lowercase
df['url'] = df['url'].str.lower()

print("\nAfter Cleaning:")
print(df.shape)

# -------------------------------
# STEP 4: FEATURE ENGINEERING
# -------------------------------

# URL Length
df['url_length'] = df['url'].apply(len)

# Count special characters
df['special_chars'] = df['url'].apply(lambda x: len(re.findall(r'[@_\-=?]', x)))

# Count digits
df['digit_count'] = df['url'].apply(lambda x: len(re.findall(r'\d', x)))

# Keyword flag (login, secure, verify)
df['keyword_flag'] = df['url'].apply(
    lambda x: 1 if any(word in x for word in ['login', 'secure', 'verify']) else 0
)

# IP-based URL detection
df['ip_flag'] = df['url'].apply(
    lambda x: 1 if re.search(r'\d+\.\d+\.\d+\.\d+', x) else 0
)

# Label encoding (malicious = 1)
df['label'] = 1

print("\nFeature Engineering Done\n")
print(df.head())

# -------------------------------
# STEP 5: DATA REDUCTION
# -------------------------------

# Keep only required columns
df_final = df[['url', 'url_length', 'special_chars', 'digit_count',
               'keyword_flag', 'ip_flag', 'label']]

print("\nFinal Dataset:\n")
print(df_final.head())

# -------------------------------
# STEP 6: SAVE CLEAN DATA
# -------------------------------

df_final.to_csv("cleaned_urls.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_urls.csv'")

# -------------------------------
# STEP 7: VISUALIZATION
# -------------------------------

# 1. URL Length Distribution
plt.figure()
plt.hist(df_final['url_length'], bins=30)
plt.title("URL Length Distribution")
plt.xlabel("URL Length")
plt.ylabel("Frequency")
plt.show()

# 2. Special Characters Distribution
plt.figure()
plt.hist(df_final['special_chars'], bins=20)
plt.title("Special Characters Distribution")
plt.xlabel("Count")
plt.ylabel("Frequency")
plt.show()

# 3. Digit Count Distribution
plt.figure()
plt.hist(df_final['digit_count'], bins=20)
plt.title("Digit Count Distribution")
plt.xlabel("Digits")
plt.ylabel("Frequency")
plt.show()

# 4. Keyword Flag Count
plt.figure()
df_final['keyword_flag'].value_counts().plot(kind='bar')
plt.title("Keyword Presence")
plt.xlabel("0 = No, 1 = Yes")
plt.ylabel("Count")
plt.show()

# 5. IP-based URL Count
plt.figure()
df_final['ip_flag'].value_counts().plot(kind='bar')
plt.title("IP-based URL Detection")
plt.xlabel("0 = No, 1 = Yes")
plt.ylabel("Count")
plt.show()
