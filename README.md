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
 ```
 # This installs the ability to import jupyter notebooks
import sys

!{sys.executable} -m pip install import_ipynb
 ```
 
I then loaded the data:
 ```
 # Read a CSV
import import_ipynb
from util import *

calendar = read_csv('../data/calendar.csv')

calendar.head()
 ```
 Notice I imported util which contains a special read_csv function which extends pandas.read_csv to make it more
 memory efficient.







<!--
## Calendar Data
The first thing that strikes me is that there is a lot of missing data in the price column so I decided
to see how much data was missing. To visualize this, I plotted how populated the price data is for each
listing id. The following histogram is what I got:

![Airbnb](./viz/PriceDataAvailabilityHistogram.png)

The x-axis is 50 buckets of price data availability percentages and the y-axis is the number
of listings in that bucket. (eg. The last bucket is 98-100% and the y-value is >1000) This means
that more than a 1000 listings have price data available for 98-100% of the days for which they were listed.
-->