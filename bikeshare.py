import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all']
months=['january', 'february', 'march', 'april', 'may','june','all']
cities=['chicago','new york city','washington']


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
    
    month ,day='all','all'
    
    city=input('Would you like to see data for chicago , new york city or washington ').lower()

    while city not in cities:
        print('An error appeared in typing the city please re-enter it again \n')
        city=input('Would you like to see data for chicago , new york city or washington ').lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    filter_date=input('Would you like to filter the data per month, day, all ?').lower()
    filtering=['month','day','all']
    
    while filter_date not in filtering:
        print('An error appeared in typing  please re-enter it again \n')
        filter_date=input('Would you like to filter the data per month, day, all ?  ').lower()
        
    
    
    if (filter_date=='month') or (filter_date=='all') :
        month=input('Which month - January, February, March, April, May,June or all? ').lower()
        while month not in months:
            print('An error appeared in typing the month please re-enter it again \n')
            month=input('Which month - January, February, March, April, May,June or all? ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if (filter_date== 'day') or (filter_date == 'all'):
        day= input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday or all ? ').lower()
        while day not in days:
            print('An error appeared in typing the day  please re-enter it again \n')
            day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday or all ? ').lower()

    
             

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    
    if(month!='all') :
       
        month=months.index(month)+1
        df=df[df['month']==month]

    if(day!='all'):
        df=df[df['day_of_week']==day.title()]
        
    print('the inputs are City :{}, Month : {} , Day : {} '.format(city,month,day) )
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('the most popular Month is : ' , popular_month)
    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print('the most popular Day of the Week is : ',popular_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('the most popular Hour is :' ,  popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()
    print('The most popular start station is : ', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()
    print('The most popular end station is : ', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['start & end_station']=df['Start Station']+'  '+ df['End Station']
    most_frequent_combination= df['start & end_station'].mode()
    print('The most frequent combination of start station and end station trip is : ', most_frequent_combination)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is : ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time is : ',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type=df['User Type'].value_counts()
    print('The counts of user types are ', count_user_type )

    # TO DO: Display counts of gender
    
    if city!='washington':
        gender_count=df['Gender'].value_counts()
        print('The count of gender are : ', gender_count )
    else:
        print('Sorry!!! no gender applied in this city ')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city!='washington' :
        earliest_year=df['Birth Year'].max()
        print('The most earliest year is :  ', earliest_year)
        most_recent_year=df['Birth Year'].min()
        print('The most recent year is :  ', most_recent_year)
        most_common_year=df['Birth Year'].mode()
        print('The most common year of birth is :  ', most_common_year)
    else:
        print('Sorry!!! no birth year applied in this city ')

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_row_data(df):
    
    ''' ask customer if he need to see the row data and show 5 rows and cst can ask for more '''
    
    response=input('Would you like to see 5 rows of data   ,please type yes or no '  ).lower()
    #default value for the counter that will multiplied in no. of rows if cst need more than five rows
    count=1

    while response == 'yes':
        #no_of_rows=5*count
        data=df.head(5*count)
        print('the five rows of data are  \n ',data)
        response=input('Would you like to see 5 rows of data   ,please type yes or no '  ).lower()
        if response == 'yes':
            count+=1

        else:
            break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_row_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
