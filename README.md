# Analysis of Seattle's Airbnb Data
Analysis of Airbnb data for Seattle. Source: (https://www.kaggle.com/airbnb/seattle/data)

## Calendar Data
The first thing that strikes me is that there is a lot of missing data in the price column so I decided
to see how much data was missing. To visualize this, I plotted how populated the price data is for each
listing id. The following histogram is what I got:

![Airbnb](./viz/PriceDataAvailabilityHistogram.png)

The x-axis is 50 buckets of price data availability percentages and the y-axis is the number
of listings in that bucket. (eg. The last bucket is 98-100% and the y-value is >1000) This means
that more than a 1000 listings have price data available for 98-100% of the days for which they were listed.