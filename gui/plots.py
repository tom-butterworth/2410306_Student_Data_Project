import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns #package I'll use for graph styling, has its own graphing functionality as well but I won't use this
sns.set_style("darkgrid") #set style for plots

def clearplots():
    plt.clf() #clears all plots from the current figure. This means new plots appear in the same window, rather than opening a new window

#Correlation between grade and attendance
def plot_grade_vs_attendance(df):
    clearplots()
    plt.scatter(df["attendance"], df["grade"]) #scatter graph of all attendance vs grade points

    #calculate line of best fit
    coefficients = np.polyfit(df["attendance"], df["grade"], 1) #returns array of [slope, intercept] of a linear (hence degree 1) line of best fit
    polynomial = np.poly1d(coefficients)
    plt.plot(df["attendance"], polynomial(df["attendance"]), linestyle="--")

    plt.title("Grade vs Attendance")
    plt.show()

#Bar chart of average grade per country
def plot_average_grade_by_country(df):
    clearplots()
    avg_grades = df.groupby("country")["grade"].mean() #group by country and calculate average grade for each country
    avg_grades.sort_values(ascending=False, inplace=True) #need inplace=True to directly change the avg_grades dataframe, otherwise it returns a modified df for later instead of using it
    plt.bar(avg_grades.index, avg_grades.values)
    plt.xticks(rotation=90) #rotate x axis labels vertically, so country names are more legible
    plt.title("Average Grade by Country")
    plt.show()

#Boxplot of grade distribution by country
def plot_boxplot_grades_by_country(df):
    clearplots()
    """
    df.loc[df["country"] == country, "grade"].values selects the grade where country is the current country. Every country then...
    ... has an array of grades
    for country in df["country"].unique() loops through every distinct country name in the data.
    grades_by_country is therefore a list of arrays, where each array contains all the grades of a certain country.
    """
    grades_by_country = [df.loc[df["country"] == country, "grade"].values for country in df["country"].unique()]
    plt.boxplot(grades_by_country, labels=df["country"].unique(), vert=True)
    plt.xticks(rotation=90)
    plt.ylabel("Grades")
    plt.title("Grade Distribution by Country")
    plt.show()

#Histogram of grade distribution
def plot_histogram_grade_distribution(df):
    clearplots()
    plt.hist(df["grade"], bins=50, edgecolor="black") #bins changes how many boxes/intervals the graph is split into
    plt.xlabel("Grades")
    plt.ylabel("Count")
    plt.title("Grade Distribution")
    plt.show()