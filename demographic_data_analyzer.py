import pandas as pd
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')  # Replace with your actual data path
    
    # Race count
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)  # Round to 1 decimal place

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)  # Round to 1 decimal place

    # Higher and lower education categories
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage with salary >50K (higher education)
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)  # Round to 1 decimal place
    # Percentage with salary >50K (lower education)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)  # Round to 1 decimal place

    # Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # Percentage of people who work the minimum hours per week and earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)  # Round to 1 decimal place

    # Country with the highest percentage of people earning >50K
    country_salary = df.groupby('native-country').apply(lambda x: (x['salary'] == '>50K').mean() * 100)
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max(), 1)  # Round to 1 decimal place

    # Most popular occupation in India for those earning >50K
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
