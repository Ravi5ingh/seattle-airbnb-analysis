from investigations import *
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

listings = read_csv('data/listings.csv')
listings['price'] = listings['price'].apply(parse_price)

plot_box(listings, 'accommodates', 'price', 'Number of People Accommodated', 'Price')

plot_box(listings, 'bedrooms', 'price', 'Number of Bedrooms', 'Price')

plot_box(listings, 'beds', 'price', 'Number of Beds', 'Price')

plot_box(listings, 'bathrooms', 'price', 'Number of Bathrooms', 'Price')

plot_box(listings, 'guests_included', 'price', 'Number of Guests Included', 'Price')