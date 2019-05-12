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
    while True:
        try:
            city = str(input('Would you like to see data for Chicago, New York, or Washington?\n'))
            break
        except:
            print('\nPlease input Chicago, New York, or Washington\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            both = str(input('Would you like to filter the data by month, day, or not at all?\n'))
            break
        except:
            print('\nPlease input month, day or not\n')  
    if both == 'month':
        while True:
            try:
                month = str(input('Which month - January, February, March, April, May, or June?\n'))
                break
            except:
                print('\nPlease input a valid month\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            try:
                day = str(input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n'))
                break
            except:
                print('\nPlease input a valid day\n')

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
    city = city.lower()
    month = month.lower()
    day = day.lower()
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    popular_month = df['Start Time'].dt.month.mode()[0]
    print('Most popular Month:' , popular_month)

    # TO DO: display the most common day of week
    popular_day = df['Start Time'].dt.weekday_name.mode()[0]
    print('Most popular day:' , popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most popular hour:' , popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most popular used start station:' , start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most popular used end station:' , end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start end station'] = df['Start Station'].map(str) + df['End Station']
    start_end_station = df['start end station'].mode()[0]
    print('Most popular combination of start station and end station trip:' , start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum = df['Trip Duration'].sum()
    print("total travel time is" , sum)

    # TO DO: display mean travel time
    mean = sum / len(df)
    print("mean travel time is" , mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    a = len(df['User Type'].unique())
    print('counts of user types', a)

    # TO DO: Display counts of gender
    b = len(df['Gender'].unique())
    print('counts of gender', b)

    # TO DO: Display earliest, most recent, and most common year of birth
    max = df['Birth Year'].max()
    min = df['Birth Year'].min()
    common = df['Birth Year'].mode()[0]
    print('earliest of birth is %s, most recent of birth is %s, and most common year of birth is %s' % (min, max, common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
