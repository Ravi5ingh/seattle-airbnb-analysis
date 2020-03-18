import pandas as pd

from util import *

def plot_price_data_availability_histogram():
    """
    Plots a histogram representing what the price data availabilities in the raw calendar data
    The availability for any listing id is the percentage of days for which there is price data
    """

    calendar = pd.read_csv('data/calendar.csv').pipe(reduce_mem_usage)

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


