import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", 100)
file_path = "../data/jobs-usa.csv"
df = pd.read_csv(file_path)
print("数据前五行：")
print(df.head())
print("\n数据基本信息:")
print(df.info())
print(df["description"].iloc[0])
skills_list = [
    "Python",
    "SQL",
    "Tableau",
    "Hadoop",
    "Java",
    "Linux",
    "Excel",
    "Power BI",
    "Machine Learning",
    "R",
    "C++",
]
# 5️⃣ 定义技能对应正则表达式（用于字符串匹配）
skill_patterns = {
    "Python": r"\bpython\b",
    "SQL": r"\bsql\b",
    "Tableau": r"\btableau\b",
    "Hadoop": r"\bhadoop\b",
    "Java": r"\bjava\b",
    "Linux": r"\blinux\b",
    "Excel": r"\bexcel\b",
    "Power BI": r"\bpower[\s\-_]?bi\b",
    "Machine Learning": r"\bmachine[\s\-_]?learning\b",
    "R": r"\br\b",
    "C++": r"\bc\+\+\b",
}
for skill, pattern in skill_patterns.items():
    df[skill] = df["description"].str.contains(pattern, case=False, na=False)
# 7️⃣ 定义技能组（分组）
skill_groups = {
    "Programming": ["Python", "Java", "R", "C++", "SQL"],
    "BI & Analytics": ["Tableau", "Power BI", "Excel", "Machine Learning"],
}
for group, cols in skill_groups.items():
    df[group] = df[cols].any(axis=1)
    # 9️⃣ 输出技能出现次数（统计频率）
print("\n每个技能出现次数:")
print(df[skills_list].sum())

print("\n每个技能组出现次数:")
print(df[list(skill_groups.keys())].sum())

