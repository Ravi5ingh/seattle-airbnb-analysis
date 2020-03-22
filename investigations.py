import pandas as pd

from util import *

def plot_listings_vs_booking():
    """
    Every day from first to last day of data, plot how many properties were listed and how many properties
    were booked each day
    """

    # This is what we want to populate and plot
    listing_data = pd.DataFrame(columns=['date', 'total', 'booked'])

    calendar = pd.read_csv('./data/calendar.csv', parse_dates=['date']).pipe(reduce_mem_usage)

    # These are the min and max dates in calendar (worked out earlier)
    current_date = min(calendar['date'])
    end_date = max(calendar['date'])

    while current_date <= end_date:

        todays_listings = calendar[calendar['date'] == current_date]

        total = row_count(todays_listings)
        booked = row_count(todays_listings[todays_listings['available'] == 'f'])

        listing_data = listing_data.append({'date': current_date, 'total': total, 'booked': booked}, ignore_index=True)

        if (current_date.day == 1):
            print('Data collected for ' + str(current_date))

        current_date = current_date + timedelta(days=1)

    standardize_plot_fonts()

    plot = listing_data.plot(x='date')
    plot.set_xlabel('Date')
    plot.set_ylabel('Number of rooms booked')
    plot.set_title('Bookings over the year')

    plt.show()

def plot_price_data_availability_histogram():
    """
    Plots a histogram representing what the price data availabilities in the raw calendar data
    The availability for any listing id is the percentage of days for which there is price data
    """

    calendar = read_csv('data/calendar.csv')

    unique_listing_ids = calendar['listing_id'].unique()

    print(str(unique_listing_ids.size) + ' unique Ids')

    listing_price_data_availability = pd.DataFrame(columns=['Listing Id', 'Availability'])

    rows_done = 0
    for listing_id in unique_listing_ids:

        listings = calendar[calendar['listing_id'] == listing_id]
        total = len(listings.index)
        num_nans = len(listings[is_nan(listings['price'])].index)
        num_vals = total - num_nans

        listing_price_data_availability = listing_price_data_availability.append({'Listing Id': listing_id, 'Availability': num_vals / total * 100}, ignore_index=True)

        if(rows_done%1000==0):
            print(str(rows_done) + ' ids done')

        rows_done += 1

    listing_price_data_availability.to_csv('data/listing_availabilities.csv', index=False)

    listing_price_data_availability = listing_price_data_availability.sort_values(by='Availability', ascending=False)

    standardize_plot_fonts()

    histogram = listing_price_data_availability.hist(column='Availability', bins=50)

    describe_hist(histogram,
                  title='Number of Listings for each Price Data Availability bucket',
                  x_label='Data Availability Percentage',
                  y_label='Number of listings')

    plt.show()


