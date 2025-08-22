# This is Python code file to create data.

import os
import pandas as pd
import numpy as np

data = {
    "Name": ["M", "N", "O"],
    "Age": [23, 34, 12],
    "City": ["Pune", "Mumbai", "Surat"]
}

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample.csv')

df = pd.DataFrame(data, index=False)
df.to_csv(file_path)

print('File Created and Saved Successfully at', file_path)

