from util import *
from investigations import *
from sklearn.neural_network import MLPClassifier

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import *
from sklearn.metrics import confusion_matrix

import seaborn as sns

def plot_seattle_vs_boston_listing_specs():
    """
    Plot the nature of the properties in Seattle vs Boston
    """

    # seattle_boston_compare('People Accommodated')
    # seattle_boston_compare('Number of Bathrooms')
    # seattle_boston_compare('Number of Beds')

    listings = read_csv('data/listings_joined.csv')
    listings = listings.dropna()

    # Plot the room types in a bar chart
    seattle_num_home = row_count(listings[(listings['Type of Room'] == 'Entire home/apt') & (listings['City'] == 'Seattle')])
    seattle_num_room = row_count(listings[(listings['Type of Room'] == 'Private room') & (listings['City'] == 'Seattle')])
    seattle_num_shared_room = row_count(listings[(listings['Type of Room'] == 'Shared room') & (listings['City'] == 'Seattle')])

    boston_num_home = row_count(listings[(listings['Type of Room'] == 'Entire home/apt') & (listings['City'] == 'Boston')])
    boston_num_room = row_count(listings[(listings['Type of Room'] == 'Private room') & (listings['City'] == 'Boston')])
    boston_num_shared_room = row_count(listings[(listings['Type of Room'] == 'Shared room') & (listings['City'] == 'Boston')])

    # indices = ['Entire home/apt', 'Private room', 'Shared room']

    N = 3

    # Specify the values of blue bars (height)
    blue_bar = (seattle_num_home, seattle_num_room, seattle_num_shared_room)
    # Specify the values of orange bars (height)
    orange_bar = (boston_num_home, boston_num_room, boston_num_shared_room)

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10, 5))

    # Width of a bar
    width = 0.3

    # Plotting
    plt.bar(ind, blue_bar, width, label='Seattle')
    plt.bar(ind + width, orange_bar, width, label='Boston')

    plt.ylabel('Number of Properties')
    plt.title('Type of Properties in Seattle vs Boston')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Entire home/apt', 'Private room', 'Shared room'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    plt.show()

def join_seattle_boston_apt_data(price_bucket_size):
    """
    Join the data for Seattle and Boston into a single csv file
    :param price_bucket_size: The size of the buckets for the price column
    """

    listings_seattle = read_csv('data/listings.csv')
    listings_boston = read_csv('data/boston/listings.csv')

    seattle_data = pd.DataFrame()
    seattle_data['Type of Room'] = listings_seattle['room_type']
    seattle_data['People Accommodated'] = listings_seattle['accommodates']
    seattle_data['Number of Bathrooms'] = listings_seattle['bathrooms']
    seattle_data['Number of Bedrooms'] = listings_seattle['bedrooms']
    seattle_data['Number of Beds'] = listings_seattle['beds']
    seattle_data['Price'] = listings_seattle['price'].apply(lambda x: int(parse_price(x)/price_bucket_size))
    seattle_data['City'] = 'Seattle'

    boston_data = pd.DataFrame()
    boston_data['Type of Room'] = listings_boston['room_type']
    boston_data['People Accommodated'] = listings_boston['accommodates']
    boston_data['Number of Bathrooms'] = listings_boston['bathrooms']
    boston_data['Number of Bedrooms'] = listings_boston['bedrooms']
    boston_data['Number of Beds'] = listings_boston['beds']
    boston_data['Price'] = listings_boston['price'].apply(parse_price).apply(lambda x: int(x/price_bucket_size))
    boston_data['City'] = 'Boston'

    seattle_data.append(boston_data).to_csv('data/listings_joined.csv', index=False)


def pricing_mode_rf():
    """
    Train a Random Forest classifier on the data
    """

    model_df = read_csv('data/pricing_model_train.csv')
    model_df = model_df.dropna()
    model_df['price'] = model_df['price'] * 10

    X = model_df[['accommodates', 'bathrooms', 'bedrooms', 'beds', 'guests_included']]
    Y = model_df['price']

    classifier = RandomForestClassifier(n_estimators=100)

    pipeline = Pipeline(
        [
            ('predict', classifier)
        ])

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=27)

    pipeline.fit(x_train, y_train)

    y_pred = pipeline.predict_proba(x_test)[:, 1]
    y_pred = y_pred >= 0.1

    matrix = confusion_matrix(y_test, y_pred)
    print(matrix)

def train_pricing_model(x, price_multiple):
    """
    Train a model based on the normalized data
    :param x: The input axis
    :param price_multiple: The price multiple is necessary to convert the price into an integer for classification
    """

    model_df = read_csv('data/pricing_model_train.csv')
    model_df = model_df.dropna()

    model_df['price'] = model_df['price'].apply(lambda x: int(x * price_multiple))

    print(model_df.head())

    X = [
        list(model_df[x])
    ]
    X = np.array(X).T.tolist()

    Y = list(model_df['price'])

    clf = MLPClassifier(solver='sgd', activation='relu', alpha=1e-7, hidden_layer_sizes=(9, 7), random_state=15, max_iter=1000000)

    ##############################

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

    clf.fit(x_train, y_train)

    pred = clf.predict([[0.4]])

    print(pred)

    y_pred = clf.predict(x_test)

    matrix = confusion_matrix(y_test, y_pred)

    pd.DataFrame(matrix).to_csv('data/confusion_matrix.csv',index=False)

    print(matrix)

    sns.heatmap(pd.DataFrame(matrix).pipe(normalize_confusion_matrix))

    plt.show()

    # clf.fit(X, Y)
    #
    # pred = clf.predict([[0.9, 0.9, 0.9, 0.9, 0.9]])
    #
    # print(pred)

def generate_pricing_model_data(price_bucket_size):
    """
    Puts price values into buckets and normalizes 5 input and the price columns
    :param price_bucket_size: The price bucket size
    """

    listings = read_csv('data/listings.csv')
    listings['price'] = listings['price'].apply(parse_price)

    model_df = pd.DataFrame()
    model_df['accommodates'] = listings['accommodates']
    model_df['bathrooms'] = listings['bathrooms']
    model_df['bedrooms'] = listings['bedrooms']
    model_df['beds'] = listings['beds']
    model_df['guests_included'] = listings['guests_included']
    model_df['price'] = listings['price']
    model_df = model_df.dropna()

    model_df['accommodates'] = model_df['accommodates'] / max(model_df['accommodates'])
    model_df['bathrooms'] = model_df['bathrooms'] / max(model_df['bathrooms'])
    model_df['bedrooms'] = model_df['bedrooms'] / max(model_df['bedrooms'])
    model_df['beds'] = model_df['beds'] / max(model_df['beds'])
    model_df['guests_included'] = model_df['guests_included'] / max(model_df['guests_included'])
    model_df['price'] = model_df['price'].apply(lambda x: int(x/price_bucket_size))
    model_df['price'] = model_df['price'] / max(model_df['price'])

    model_df.to_csv('data/pricing_model_train.csv', index=False)

def say_hello():

    print('hello world')