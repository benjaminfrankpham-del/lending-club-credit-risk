import pandas as pd

RAW_PATH = "data/archive/accepted_2007_to_2018q4.csv/accepted_2007_to_2018Q4.csv"  # adjust to your filename
OUT_PATH = "data/loans_2013_2015.csv"

# Only columns known at the time of application (avoids data leakage)
cols = [
    "id", "loan_amnt", "term", "int_rate", "installment", "grade", "sub_grade",
    "emp_length", "home_ownership", "annual_inc", "verification_status",
    "issue_d", "loan_status", "purpose", "addr_state", "dti", "delinq_2yrs",
    "earliest_cr_line", "fico_range_low", "fico_range_high", "open_acc",
    "pub_rec", "revol_bal", "revol_util", "total_acc", "application_type",
]

keep_status = ["Fully Paid", "Charged Off", "Default"]
chunks = []

for chunk in pd.read_csv(RAW_PATH, usecols=cols, chunksize=100_000, low_memory=False):
    chunk = chunk[chunk["loan_status"].isin(keep_status)]
    chunk["issue_date"] = pd.to_datetime(chunk["issue_d"], format="%b-%Y", errors="coerce")
    chunk = chunk[(chunk["issue_date"] >= "2013-01-01") & (chunk["issue_date"] <= "2015-12-31")]
    chunks.append(chunk)

df = pd.concat(chunks, ignore_index=True)
df["default"] = df["loan_status"].isin(["Charged Off", "Default"]).astype(int)

print(df.shape)
print(df["default"].value_counts(normalize=True))

df.to_csv(OUT_PATH, index=False)