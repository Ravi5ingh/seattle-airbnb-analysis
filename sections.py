from util import *
from sklearn.neural_network import MLPClassifier

# from sklearn.pipeline import Pipeline
# from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import *
from sklearn.metrics import confusion_matrix

import seaborn as sns

def pricing_mode_rf():

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

def plot_training_data(x):

    model_df = read_csv('data/pricing_model_train.csv')
    model_df = model_df.dropna()

    plot_scatter(model_df, x=x, y='price')


def train_pricing_model(x, price_multiple):
    """

    :param x:
    :param price_multiple:
    :return:
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