import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Input name of city to analyze:').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Please enter Chicago, New York City, or Washington as your city of choice:')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Input name of the month to filter by, or all to apply no month filter:').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Input name of the day of week to filter by, or all to apply no day filter:').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    ## find the most popular month
    popular_month = df['month'].mode()[0]
    
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    
    ## find the most popular day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    
    print('Most Popular Day of Week:', popular_day_of_week)

    # TO DO: display the most common start hour

    ## extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    ## find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station

    popular_end_station = df['End Station'].mode()[0]
    
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    # Create a column of the trip (concatenate start and end stations into 1 column)
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
              
    popular_trip = df['Trip'].mode()[0]
    
    print('Most frequent combination of start station and end station:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_time = df['Trip Duration'].sum()
              
    print('Total Trip Duration (in seconds):', total_time)

    # TO DO: display mean travel time
    
    avg_time = df['Trip Duration'].mean()
              
    print('Average Trip Duration:', avg_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if city != 'washington':
    
        # TO DO: Display counts of user types

        user_types = df['User Type'].value_counts()
              
        print('Counts of User Types:\n', user_types)

        # TO DO: Display counts of gender

        # Getting rid of null values
        df['Gender'].fillna('Not Provided', inplace = True)
              
        gender_types = df['Gender'].value_counts()
              
        print('Counts of Gender:\n', gender_types)

        # TO DO: Display earliest, most recent, and most common year of birth

        # Getting rid of null values
        df['Birth Year'].fillna('Not Provided')
              
        # Earliest year of birth
        earliest_year = df['Birth Year'].min()
              
        print('Earliest Year of Birth:', earliest_year)
              
        # Most recent year of birth
        most_recent_year = df['Birth Year'].max()
              
        print('Most Recent Year of Birth:', most_recent_year)
              
        # Most common year of birth
        most_common_year = df['Birth Year'].mode()[0]
              
        print('Most Common Year of Birth:', most_common_year)
        
    else:
        # TO DO: Display counts of user types

        user_types = df['User Type'].value_counts()
              
        print('Counts of User Types:\n', user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    display = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    n = 5
    while display.lower() == 'yes':
        print(df.head(n))
        n += 5
        display = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n')
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)   

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
