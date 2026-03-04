import matplotlib.pyplot as plt


def plot_salary_distribution(df):
    plt.hist(df["salary_clean"], bins=30)
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.savefig("output/salary_plot.png")
    plt.close()
