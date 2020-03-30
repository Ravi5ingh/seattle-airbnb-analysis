from util import *

import pandas as pd
import seaborn as sns
import xml.dom.minidom

def generate_distance_data_for(df, center_longitude, center_latitude):
    """
    Generate a csv that adds a column to quantify the straight-line distance between the property and the
    provided map point
    :param df: The data frame with the listings 
    :param center_longitude: The longitude of the point to which distance for each listing must be calculated
    :param center_latitude: The latitude of the point to which distance for each listing must be calculated
    """

    x = 4

def generate_kml_for(df, output_file_name):
    """
    Generate a KML file based on the coordinate data in the data frame provided
    :param df: The data frame with coordinate data
    :return:
    """

    # This constructs the KML document from the CSV file.
    kmlDoc = xml.dom.minidom.Document()

    kmlElement = kmlDoc.createElementNS('http://earth.google.com/kml/2.2', 'kml')
    kmlElement.setAttribute('xmlns', 'http://earth.google.com/kml/2.2')
    kmlElement = kmlDoc.appendChild(kmlElement)
    documentElement = kmlDoc.createElement('Document')
    documentElement = kmlElement.appendChild(documentElement)

    for index, row in df.iterrows():
        # KML, in its' infinite retardation, expects 'longitude, latitude'
        coordinates = row['longitude'] + ',' + row['latitude']
        placemarkElement = append_coordinate_to(kmlDoc, coordinates)
        documentElement.appendChild(placemarkElement)
    kmlFile = open(output_file_name, 'wb')
    kmlFile.write(kmlDoc.toprettyxml('  ', newl='\n', encoding='utf-8'))


def append_coordinate_to(kml_doc, coordinates):
    """
    Given an XML document, and coordinates, append the coordinates to the XML doc in KML format
    :param kml_doc: The XML document which is actually a KML document being built
    :param coordinates: The coordinates in the format 'longitude, latitude'
    :return: Return the created XML element
    """
    placemarkElement = kml_doc.createElement('Placemark')

    pointElement = kml_doc.createElement('Point')
    placemarkElement.appendChild(pointElement)
    coorElement = kml_doc.createElement('coordinates')
    coorElement.appendChild(kml_doc.createTextNode(coordinates))
    pointElement.appendChild(coorElement)
    return placemarkElement

def seattle_boston_compare(y):
    """
    Compare the given feature of listings in Seattle vs Boston
    :param y: The feature we want to compare
    """

    listings = read_csv('data/listings_joined.csv')
    listings = listings.dropna()

    # Create a redundant column to facilitate the creation of a violin plot
    listings[''] = 0

    # Create a violin plot
    plot = sns.violinplot(x='', y=y, hue='City', split=True, data=listings)
    plot.set_xticklabels([''])

    plt.show()

def seattle_boston_compare_price_of(x, yticklabels):
    """
    Compare Seattle vs. Boston prices of the given feature
    :param x: The feature of which we want to compare the price
    :param yticklabels: The labels for the x-axis
    """

    listings = read_csv('data/listings_joined.csv')
    listings = listings.dropna()
    listings = listings[listings['Price'] <= 20]

    print(max(listings['Price']))

    # Create a violin plot
    plot = sns.violinplot(x=x, y='Price', hue='City', split=True, data=listings)
    plot.set_yticklabels(yticklabels)

    plt.show()

def plot_box(data_frame, x, y, x_label, y_label):
    """
    Given a data frame, plot a box plot where the x values are discreet
    :param data_frame: The data frame to use
    :param x: The x-axis dataframe column (discreet)
    :param y: The y-axis dataframe column
    :param x_label: The x-axis label
    :param y_label: The y-axis label
    """

    inter_df = pd.DataFrame()
    inter_df[x] = data_frame[x]
    inter_df[y] = data_frame[y]

    inter_df.dropna()

    plot_df = pd.DataFrame()

    num_rows = row_count(inter_df)

    from_val = int(min(inter_df[x]))
    to_val = int(max(inter_df[x]))
    for i in range(from_val, to_val + 1):
        plot_df[str(i)] = pad(inter_df[inter_df[x] == i][y], num_rows)

    standardize_plot_fonts()

    plot_to_show = plot_df.plot.box()

    plot_to_show.set_title(y_label + ' vs ' + x_label)
    plot_to_show.set_xlabel(x_label)
    plot_to_show.set_ylabel(y_label)

    plt.show()


def plot_price_box_vs(column_name, readable_column_name):
    """
    Plot property price vs the number of people it accomodates
    :param column_name: The name of the dataframe column to use as the x-axis
    :param readable_column_name: The name to put on the plot labels
    """

    listings = read_csv('data/listings.csv')

    plot_df = pd.DataFrame()
    plot_df[column_name] = listings[column_name]
    num_rows = row_count(listings)

    from_val = min(plot_df[column_name])
    to_val = max(plot_df[column_name])
    for i in range(from_val, to_val + 1):
        plot_df[str(i)] = pad(listings[listings[column_name] == i]['price'].apply(lambda x: float(x.replace('$', '').replace(',',''))), num_rows)

    standardize_plot_fonts()

    plot_to_show = plot_df.plot.box()

    plot_to_show.set_title('Price vs ' + readable_column_name)
    plot_to_show.set_xlabel(readable_column_name)
    plot_to_show.set_ylabel('Price')

    plt.show()

def show_price_correlation_matrix():
    """
    Plot a correlation matrix that shows how price correlates with other columns
    """

    listings = read_csv('./data/listings.csv')

    correlation_df = pd.DataFrame()
    correlation_df['accommodates'] = listings['accommodates']
    correlation_df['bathrooms'] = listings['bathrooms']
    correlation_df['bedrooms'] = listings['bedrooms']
    correlation_df['beds'] = listings['beds']
    correlation_df['guests_included'] = listings['guests_included']
    correlation_df['minimum_nights'] = listings['minimum_nights']
    correlation_df['maximum_nights'] = listings['maximum_nights']
    correlation_df['number_of_reviews'] = listings['number_of_reviews']
    correlation_df['price'] = listings['price'].replace('$', '').replace(',', '').apply(lambda x: float(x.replace('$', '').replace(',', '')))


    corr_matrix = correlation_df.corr()

    standardize_plot_fonts()

    sns.heatmap(corr_matrix, xticklabels=corr_matrix.columns, yticklabels=corr_matrix.columns, annot=True)

    plt.title('Correlation Matrix for price column')

    plt.show()

def plot_listing_price_diffs():
    """
    Plot a histogram of price diffs between calendar.csv and listings.csv
    """

    listings = read_csv('./data/listings.csv')

    # Remove listings in calendar that don't have price data
    calendar = read_csv('./data/calendar.csv')
    calendar = calendar.dropna()
    unique_listing_ids = calendar['listing_id'].unique()

    # Build up the listing id prices in calendar
    listing_id_2_price = {}
    i = 0
    for listing_id in unique_listing_ids:
        listing_for_id = calendar[calendar['listing_id'] == listing_id]
        price = listing_for_id['price'].iloc[0].replace('$', '').replace(',', '')
        listing_id_2_price[listing_id] = price

        if i%500==0:
            print(str(i) + ' listing ids processed')
        i += 1

    # Build up a map of listing id price diffs
    listing_price_diffs = {}
    for listing_id in listing_id_2_price.keys():

        price_in_listings = listings[listings['id'] == listing_id]['price'].iloc[0].replace('$', '').replace(',', '')

        listing_price_diffs[listing_id] = float(listing_id_2_price[listing_id]) - float(price_in_listings)

    standardize_plot_fonts()

    # Plot a histogram of the diff values
    plt.hist(listing_price_diffs.values(), bins=100)
    plt.title('Instances of price deviation')
    plt.xlabel('Price deviation')
    plt.ylabel('Number of listings')

    plt.show()



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


