from investigations import *
from sections import *
import math
from scipy import stats

# plot_listings_vs_booking()

# plot_listing_price_diffs()

# show_price_correlation_matrix()

# plot_price_box_vs('accommodates', 'Number of People Accomodated')

# plot_price_box_vs('guests_included', 'Number of Guests Allowed')

# listings = read_csv('data/listings.csv')
# listings['price'] = listings['price'].apply(parse_price)
#
# standardize_plot_fonts()
#
# plot = listings.plot.scatter(x='bedrooms', y='price')
# # plot.set_xlabel('Monthly Debt')
# # plot.set_ylabel('Salary')
# # plot.set_title('Salary vs Monthly Debt')
#
# plt.show()

# plot_price_box_vs('bedrooms', '')

# listings = read_csv('data/listings.csv')
# listings['price'] = listings['price'].apply(parse_price)

# plot_box(listings, 'accommodates', 'price', 'Number of People Accommodated', 'Price')
#
# plot_box(listings, 'bedrooms', 'price', 'Number of Bedrooms', 'Price')
#
# plot_box(listings, 'beds', 'price', 'Number of Beds', 'Price')
#
# plot_box(listings, 'bathrooms', 'price', 'Number of Bathrooms', 'Price')
#
# plot_box(listings, 'guests_included', 'price', 'Number of Guests Included', 'Price')

# say_hello()

# accommodates
# bathrooms
# bedrooms
# beds
# guests_included

# price_bucket_size = 50
# column_to_use = 'accommodates'
# model_df = read_csv('data/pricing_model_train.csv')
# model_df = model_df.dropna()
#

# generate_pricing_model_data(price_bucket_size)
#
# model_df[column_to_use] = model_df[column_to_use].apply(lambda x: int(x * 10))
# model_df['price'] = model_df['price'].apply(lambda x: x * 1000)
# plot_box(model_df, column_to_use, 'price', column_to_use, 'Price')

# train_pricing_model(column_to_use, 1000 / price_bucket_size)


# x = np.array(model_df[column_to_use].apply(lambda x: np.float64(x)))
# y = np.array(model_df['price'].apply(lambda x: np.float64(x)))
#
# plt.plot(x, y, 'o')
#
# m, b = np.polyfit(x, y, deg=1)

# print(m)
# print(b)

# plt.plot(x, m * x + b)
#
# plt.show()


# Join the data from the two cities
# join_seattle_boston_apt_data(price_bucket_size=50)

# listings = read_csv('data/listings_joined.csv')
# listings = listings.dropna()
# listings = listings[listings['Price'] <= 20]
# listings[''] = 0 # Create a redundant column to facilitate the creation of a violin plot
#
# # Create a violin plot
# plot = sns.violinplot(x='', y='Price', hue='City', split=True, data=listings)
# plot.set_xticklabels([''])
# plot.set_yticklabels(['', '$0', '$250', '$500', '$750', '$1,000'])
#
# plt.show()3


# seattle_data = pd.DataFrame()
# 'Type of Room'] = listings_seattle['room_type']
# 'People Accommodated'] = listings_seattle['accommodates']
# 'Number of Bathrooms'] = listings_seattle['bathrooms']
# 'Number of Bedrooms'] = listings_seattle['bedrooms']
# 'Number of Beds'] = listings_seattle['beds']
# 'Price'] = listings_seattle['price'].apply(lambda x: int(parse_price(x) / price_bucket_size))
# 'City'] = 'Seattle'

# seattle_boston_compare_price_of('Type of Room', ['', '$0', '$250', '$500', '$750', '$1,000'])
# seattle_boston_compare_price_of('People Accommodated', ['', '$0', '$142', '$286', '$429', '$571', '$714', '$857', '$1,000'])
# seattle_boston_compare_price_of('Number of Bathrooms', ['', '$0', '$250', '$500', '$750', '$1,000'])
# seattle_boston_compare_price_of('Number of Bedrooms', ['', '$0', '$250', '$500', '$750', '$1,000'])
# seattle_boston_compare_price_of('Number of Beds', ['', '$0', '$167', '$333', '$500', '$667', '$833', '$1,000'])



# seattle_boston_compare('People Accommodated')
# seattle_boston_compare('Number of Bathrooms')
# seattle_boston_compare('Number of Bedrooms')
# seattle_boston_compare('Number of Beds')

# plot_seattle_vs_boston_listing_specs()

# show_seattle_value_for_money()
# show_boston_value_for_money()

show_seattle_average_property_specs()
show_boston_average_property_specs()

# listings = pd.read_csv('data/listings.csv', dtype={'longitude': str, 'latitude': str})
#
# generate_kml_for(listings, 'data/listings_viz_meta.kml')