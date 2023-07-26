text = "Python is a versatile programming language that has gained immense popularity in the field of data analysis and machine learning. Its simplicity, readability, and vast array of libraries make it an ideal choice for handling complex data tasks. One such powerful application is RFM analysis, a technique used in marketing to segment customers based on their purchasing behavior. In this tutorial, we will guide you through the process of implementing RFM analysis using Python. We will start by explaining the concept of RFM analysis and its significance in marketing. Then, we will dive into the practical aspects of conducting RFM analysis using Python, step by step. In the next section of the article, we will demonstrate how to calculate RFM scores for each customer using Python, considering different approaches for assigning scores to recency, frequency, and monetary value."

import re
text = re.sub("[^A-Za-z0-9 ]", "", text).lower()
arr = text.split(" ")
temp = {}

for item in arr:
    if item in temp:
        temp[item] += 1
    else:
        temp[item] = 1


ff = sorted(temp.items(), key=lambda x: x[1], reverse=True)

i = 0
result = {}
while i < 10 and i < len(ff):
    temp = ff[i]
    result[temp[0]] = temp[1]
    i = i + 1

print(result)