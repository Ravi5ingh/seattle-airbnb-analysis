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

price_bucket_size = 50
column_to_use = 'accommodates'
model_df = read_csv('data/pricing_model_train.csv')
model_df = model_df.dropna()


generate_pricing_model_data(price_bucket_size)
#
# model_df[column_to_use] = model_df[column_to_use].apply(lambda x: int(x * 10))
# model_df['price'] = model_df['price'].apply(lambda x: x * 1000)
# plot_box(model_df, column_to_use, 'price', column_to_use, 'Price')

train_pricing_model(column_to_use, 1000 / price_bucket_size)


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




