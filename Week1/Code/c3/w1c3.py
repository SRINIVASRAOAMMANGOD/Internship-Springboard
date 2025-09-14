import os
print("path:", os.getcwd())

import pandas as pd

# Option 1: Use raw string (recommended for Windows paths)
df = pd.read_csv(r'C:\Users\HP\Desktop\Internship-Springboard\Week1\dataset\tweet csv\chatGPT.csv', encoding='utf-8')
# Load the CSV file from the current directory
#df = pd.read_csv("tweets.csv", encoding="utf-8") # code looks in root directory
# Option 2: Use forward slashes
# df = pd.read_csv('C:/Users/HP/Desktop/Internship-Springboard/Week1/dataset/tweet csv/chatGPT.csv', encoding='utf-8')

print(df.head())
print(df.count())
