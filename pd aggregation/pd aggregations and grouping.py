import pandas as pd

# Load the booking data from a CSV file into a Pandas DataFrame
Hotel_Reservations = pd.read_csv('Hotel Reservations.csv')

# Group the booking data by booking status
booking_status_groups = Hotel_Reservations.groupby('booking_status')

# Compute the count of bookings and average number of adults for each booking status
bookings_by_status = booking_status_groups.agg({
    'Booking_ID': 'count',    # Compute the count of bookings for each group
    'no_of_adults': 'mean'    # Compute the average number of adults for each group
})

# Rename the columns for better readability
bookings_by_status.columns = ['Num_Bookings', 'Avg_Adults']

# Print the result
print('Booking Data Grouped by Status:')
print(bookings_by_status)
print('\n')

# Group the booking data by arrival year, month, and date
arrival_date_groups = Hotel_Reservations.groupby(['arrival_year', 'arrival_month', 'arrival_date'])

# Compute the count of bookings and total number of guests (adults and children) for each arrival date
bookings_by_arrival_date = arrival_date_groups.agg({
    'Booking_ID': 'count',           # Compute the count of bookings for each group
    'no_of_adults': 'sum',           # Compute the total number of adults for each group
    'no_of_children': 'sum'          # Compute the total number of children for each group
})

# Compute the total number of guests (adults and children) for each arrival date
bookings_by_arrival_date['Total_Guests'] = bookings_by_arrival_date['no_of_adults'] + bookings_by_arrival_date['no_of_children']

# Sort the result by arrival date
bookings_by_arrival_date = bookings_by_arrival_date.sort_index()

# Print the result
print('Booking Data Grouped by Arrival Date:')
print(bookings_by_arrival_date)
print('\n')

# Group the booking data by lead time and booking status
lead_time_groups = Hotel_Reservations.groupby(['lead_time', 'booking_status'])

# Compute the count of bookings for each lead time and booking status
bookings_by_lead_time = lead_time_groups.agg({
    'Booking_ID': 'count'            # Compute the count of bookings for each group
})

# Reshape the data so that booking status becomes columns and lead time becomes rows
bookings_by_lead_time = bookings_by_lead_time.unstack('booking_status')

# Fill in missing values with 0 (for lead times with no bookings)
bookings_by_lead_time = bookings_by_lead_time.fillna(0)

# Print the result
print('Booking Data Grouped by Lead Time and Booking Status:')
print(bookings_by_lead_time)