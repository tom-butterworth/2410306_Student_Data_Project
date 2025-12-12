import matplotlib.pyplot as plt

#Correlation between grade and attendance
def plot_grade_vs_attendance(df):
    plt.scatter(df["attendance"], df["grade"])
    plt.show()

#Bar chart of average grade per country
def plot_average_grade_by_country(df):
    avg_grades = df.groupby("country")["grade"].mean() #group by country and calculate average grade for each country
    avg_grades.sort_values(ascending=False, inplace=True) #need inplace=True to directly change the avg_grades dataframe, otherwise it returns a modified df for later instead of using it
    plt.bar(avg_grades.index, avg_grades.values)
    plt.xticks(rotation=90) #rotate x axis labels vertically, so country names are more legible
    plt.show()