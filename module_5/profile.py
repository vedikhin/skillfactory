from pandas_profiling import ProfileReport
import pandas as pd

df = pd.read_csv('train.csv')
prof = ProfileReport(df)
prof.to_file(output_file='output.html')