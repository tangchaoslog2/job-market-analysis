def clean_salary(df):
    df["is_monthly"] = df["low"] < 20000
    df.loc[df["is_monthly"], "salary_clean"] = df["salary_clean"] * 12
    return df
