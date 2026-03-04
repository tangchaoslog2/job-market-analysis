import sqlite3


def run_sql_analysis(df):
    conn = sqlite3.connect(":memory:")
    df.to_sql("jobs", conn, index=False)

    query = """
    SELECT location, AVG(salary_clean) as avg_salary
    FROM jobs
    GROUP BY location
    ORDER BY avg_salary DESC
    LIMIT 10
    """

    result = conn.execute(query).fetchall()
    conn.close()
    return result
