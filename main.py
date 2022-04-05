# Easy mode

number_in_seconds = int(input("Enter the number of seconds to be converted: "))
seconds_in_a_year = 31536000
seconds_in_a_day = 86400
seconds_in_an_hour = 3600
seconds_in_a_minute = 60

years = number_in_seconds // seconds_in_a_year
first_remainder = number_in_seconds % seconds_in_a_year
days = first_remainder // seconds_in_a_day
second_remainder = first_remainder % seconds_in_a_day
hours = second_remainder // seconds_in_an_hour
third_remainder = second_remainder % seconds_in_an_hour
minutes = third_remainder // seconds_in_a_minute
fourth_remainder = third_remainder % seconds_in_a_minute
seconds = fourth_remainder

print(f"The time you entered is {years}:{days}:{hours}:{minutes}:{seconds}")

