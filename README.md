# Analysis of Seattle's Airbnb Data
The purpose of this project is to demo a data mining project for Udacity. This has to be done in accordance with the 
CRISP-DM methodology. To start off, here is a visualization of CRISP-DM:

<p align="center">
  <img src="/viz/CRISP-DM.png" width="400" height="400">
</p>
Source: (https://blog.magrathealabs.com/crisp-dm-and-what-i-did-wrong-70c4e7e8656)

## Structure
The structure of this project is as follows:
* ./data/ - This is the directory with all the data
* ./jupyter/ - This contains the jupyter notebooks for this project
* ./viz/ - This contains all the visualizations of the project

This is actually a pycharm project with a sub-section for the jupyter notebooks.

## Choosing a Dataset
For this exercise, I decided to use Airbnb's Seattle data set for two reasons. Firstly the data set looks interesting
and it is one whose context I can fully grasp. Secondly, this was suggested by Udacity and I thought I may find 
more support in case I run into issues. The data set is available here: (https://www.kaggle.com/airbnb/seattle/data)

## The first question
In order to try and understand how CRISP-DM works, I decided to try the cycle with a simple task. The first thing I
wanted to do was to understand how busy the Airbnb scene in Seattle is based on the available data.

### Business Understanding
The first step in this process is the business understanding. In order to gain understanding, it is crucial
to ask the right question and to pose the problem correctly. In our case, we want to understand how busy Airbnb
is in Seattle. The most logical question to ask then is:

Based on the data, what does room listing and availability over time in Seattle look like?

The objective of this cycle is to find out how many rooms are listed and how many are booked/available at any given time.
The way to assess success is pretty straightforward. If we can visualize the data, we succeeded.

### Data Understanding
The purpose of the data understanding step is to collect, describe, explore, and verify the data sources necessary
to answer the business question. The data set consists of the following 3 files:
* calendar.csv
* listings.csv
* reviews.csv

The data we want is in the calendar.csv. To preview this I loaded it up in the jupyter notebook at 
jupyter/main.ipynb. But first I installed the ability to import util.ipynb from main.ipynb like this :
 ```python
 # This installs the ability to import jupyter notebooks
import sys

!{sys.executable} -m pip install import_ipynb
 ```
 
 I then loaded the data:
 ```python
 # Read a CSV
import import_ipynb
from util import *

calendar = read_csv('../data/calendar.csv')

calendar.head()
 ```
Notice I imported util which contains a special read_csv function which extends pandas.read_csv to make it more
memory efficient. This is what we see:

![](viz/jupyter/calendar.png)

So we see that 1 record in calendar is 1 day's availability for 1 listing and its price. It looks like there are 
missing values in price but what we care about the following columns:
* listing_id
* data
* available

Let's see if any of them have missing values (They don't):
![](viz/jupyter/calendar_null_check.png)

### Data Preparation & Modelling
The next step is to prepare the data for modelling. For this one needs to  select, clean, construct, and format
the data. In our case we just need to select, and construct the data. What we want to know is : 
For every day, how many rooms were listed and how many were booked.

The way we do this is by iterating through the whole date range and plotting how many properties were listed
on that day and how many properties were booked that day. The following is the code to do this

```python
import import_ipynb
from util import *
from datetime import timedelta

# This is what we want to populate and plot
listing_data = pd.DataFrame(columns=['date', 'total', 'booked'])

calendar = pd.read_csv('../data/calendar.csv', parse_dates=['date']).pipe(reduce_mem_usage)

# These are the min and max dates in calendar
current_date = min(calendar['date'])
end_date = max(calendar['date'])

while current_date <= end_date:

    todays_listings = calendar[calendar['date'] == current_date]

    total = row_count(todays_listings)
    booked = row_count(todays_listings[todays_listings['available'] == 'f'])

    listing_data = listing_data.append({'date': current_date, 'total': total, 'booked': booked}, ignore_index = True)

    if(current_date.day == 1):
        print('Data collected for ' + str(current_date))

    current_date = current_date + timedelta(days=1)

standardize_plot_fonts()

plot = listing_data.plot(x='date')
plot.set_xlabel('Date')
plot.set_ylabel('Number of rooms booked')
plot.set_title('Bookings over the year')

plt.show()
```
The following is the resulting plot:

![](viz/BookingsOverYear.png)

In this case, the modelling step is very small because all we're doing is generating a plot which you can see above

### Evaluation
Now to answer the question that we asked. Based on the data we have (Jan. 2016 to Jan. 2017), it looks like the number
of rooms booked has been steadily declining however there have been 2 spikes. Once at April start and the second
at Jul start.

We don't know whether nor not these spikes are cyclical as we don't have multiple years' data. The other remarkable
trait is that the total number of listings at any given time never deviates from 3818. This was not initially obvious.
This seems to indicate that there must be a business rule limiting the number of properties that can be listed in
Seattle.

## The Second Question
For the next cycle, I decided to dig a little deeper into the data set. Now I've decided I want to understand
how the properties in Seattle are priced on Airbnb. This is an abstract requirement so we have to ask a concrete
question.

### Business Understanding
The question should be:

What are the primary factors in the property specifications that affect the price and how do they correlate?

The objective here is to find those factors (if any) that correlate most strongly with the listed price of a property
and understand the nature of that correlation. 

The assessment would be: If we are able to find at-least 1 correlating factor and determine how the price correlates
whit the factor, we will have succeeded.

## Data Understanding
The data that we need is pricing data. A quick look at the csv files reveals a problem. Both the calendar.csv
and the listings.csv files have a 'price' column. The latter file has 2 more columns called 'weekly_price'
and 'monthly_price'. This looks to me like the 'price' column in listings.csv must the default daily price for the
property that the prospective landlord sets up initially and the 'price' column in calendar.csv must be set at
the time of listing (to override default value). To verify this, I decided to cross-check the 'price' column values
in the 2 files.

This can be a bit tricky because the 'price' values in the 2 might be slightly off but that doesn't necessarily
mean they don't match. To solve this problem, I decided to visualize instead what the price differences actually look like.
I joined the calendar.csv and listings.csv tables on listing id and generated a list of price diff values. I then
plotted the price diff values in a histogram to get their profile. This is what I got:
![](viz/PriceDeviationFrequency.png)

This figure visualized the frequency of diff values and it is pretty much what I expected to see. In the vast majority
of cases, the difference between the calendar price and the listing price is 0 as the histogram shows. What this tells
us is that both these columns are the daily price of the property which means we can use the 'price' column in 
listsings.csv. 

To explore the data further, I picked a few magnitude columns in listings.csv that could correlate with price
(I'm ignoring the categorical variables for now) and plotted a correlation matrix. This is what I got:
![](viz/PriceCorrMatrix.png)

This indicates that there is a practically usable correlation between the price and some of the other columns.
The next logical thing is to plot the following columns against price as they show promise:

* accommodates (65%)
* bedrooms (63%)
* beds (59%)
* bathrooms (52%)
* guests_included (39%)

The following are these plots:

| | | 
|:-------------------------:|:-------------------------:|
![](viz/PriceVsAccommodates.png)|![](viz/PriceVsBedrooms.png)
![](viz/PriceVsBeds.png)|![](viz/PriceVsBathrooms.png)
![](viz/PriceVsGuests.png) |

