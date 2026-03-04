from load_data import load_data
from clean_data import clean_salary
from sql_analysis import run_sql_analysis
from visualize import plot_salary_distribution


def main():
    df = load_data("data/jobs-usa.csv")
    df = clean_salary(df)
    plot_salary_distribution(df)
    result = run_sql_analysis(df)
    print(result)


if __name__ == "__main__":
    main()
