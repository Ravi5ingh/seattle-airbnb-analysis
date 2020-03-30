# Analysis of Seattle's Airbnb Data
This blog post is about my attempt to mine Airbnb's data for the city of Seattle. It details what I thought, how I approached problems, and what I did to answer some questions I raised. The blog post is intended for the general audience and so does not assume any technical background.

## CRISP-DM
Data mining is the process of diving into data to look for patterns. With the explosion of big data in recent years, it has become instrumental for business intelligence and planning.

Data Mining is a somewhat abstract term that can be interpreted and executed in different ways. CRISP-DM *(Cross-industry standard process for data mining)* is a system that gives concrete structure this process. It was conceived in 1996 at DaimlerChrysler.

This is what it looks like:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/CRISP-DM.png?raw=true)

At a high level, CRISP-DM is a cyclical process that tells you how to systematically process your data to derive value. One cycle is basically one data processing pipeline that begins with a question and ends with an answer. There is also an optional step for deployment where that makes sense. If you want a detailed explanation, you can read all about this [here](ftp://ftp.software.ibm.com/software/analytics/spss/support/Modeler/Documentation/14/UserManual/CRISP-DM.pdf).

## Question 1
What I've done here is to run through the cycle three times in order to answer three questions I
posed about the data. As I am new to this, I decided to start off with a very simple question which
would allow me to get familiar with CRISP-DM. I decided to look into how busy the Airbnb scene
in Seattle is based on the available data.

### Business Understanding
In CRISP-DM, there is a lot of importance placed on correctly posing the question. This makes sense because the whole point of the process is to gain and use insight based on the data. You can't do this if you don't know what you want to know. Another consequence of not performing this step properly is that you may spend a great deal of effort finding the right answer to the wrong question. 


For this reason I should make this question more specific. So a better question is: Based on the available date range, how many properties are listed, and how many of them are booked on any given day?

### Data Understanding
Now that we know exactly what we'd like to know, the next step is to get our hands on the data that we will need to investigate to get our answers. According to CRISP-DM, understanding the data involves collecting, describing, exploring, and verifying the data.

I made a mistake here. I didn't do the last part *(**ie.** verifying)* properly. As a result, my inference was wrong but I will explain this after I've described what I did.

In our case, Airbnb's Seattle data set consists of 3 files:
* calendar.csv
* listings.csv
* reviews.csv

The file that I thought I needed to answer this question was calendar.csv. The following is a preview of the data within it:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/calendar.png?raw=true)

There are four columns in here and this is what I thought they meant:

* listing_id: This is a reference number that uniquely identifies one Airbnb propety in Seattle.
* date: This is the date which 1 row of data is for
* available: This tells you if the property is available or not on this day *(**ie.** 't' for yes and 'f' for no)* 
* price: This tells you the daily rent for this property

In theory, based on this data, one should be able to work out how many properties were listed on any given day and how many of them were booked so I did this.

### Data Preparation
It is virtually never the case that the data is in the format we want it to be to create our models or to answer our questions. CRISP-DM lays out a method for selecting, cleaning, constructing, and integrating our data to prepare it for modelling.

To do this, I've written some code to get a date-wise list showing how many properties were listed and booked on any given day. The code for this is available in the jupyter notebook [here](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/jupyter/main.ipynb).

### Modelling
The modelling steps usually involves selecting a model and a way to assess it, building the model, and then assessing it. My model is simply a line chart so this step is small.

Once I prepared the data, the following is what I got:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/BookingsOverYear.png?raw=true)

### Evaluation
The chart above looks interesting but it is not what I expected. There are three remarkable traits. The first is that the total properties listed never changes. There are always 3818 properties listed on any given day. The second is that the chart indicates that business has been steadily declining as the number of rooms booked has been coming down. The third is that there are spikes at April start and July start.
 
The second conclusion is wrong and it is the result of a mistake I made in the data understanding section. I later found out that the calendar.csv data is not past booking data but future booking data. This completely changes the meaning. This chart does not show steadily declining business. It shows how booked the properties are 365 days into the future so it makes sense that properties are less booked further into the future. The spikes still mean the same thing *(**ie.** People must be booking for dates in April for an event or holiday like Easter)*

What this shows us is the value of being systematic with the data mining process. What I've done here is found the right answer to the wrong question.

## Question 2
For the next cycle, I decided to look at pricing. I wanted to understand how properties in Seattle are priced for Airbnb.

### Business & Data Understanding
The right question in this case is:

What are the primary factors in the property specifications that affect the price and how do they correlate?

The first thing I did was to get a hold of the pricing data but this seems to exist in both the calendar.csv file and the listings.csv file. The technical details of how I resolved this are in the Readme and the jupyter notebook. The conclusion is that I used the data in the listings.csv.

The aim here is to find out what affects property values in Seattle. So logically, I examined the relationship between the key features of the properties in Seattle. I picked the following features:
* accommodates - Number of people that a property can accommodate
* bathrooms - Number of bathrooms in a property
* bedrooms - Number of bedrooms in a property
* beds - Number of beds in a property
* guests_included - The number guests you can have in a property
* minimum_nights - The minimum booking period in nights
* maximum_nights - The maximum booking period in nights
* number_of_reviews - The number reviews a property has
* price - The price of a property

The following is what the correlation matrix for these features looks like:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/PriceCorrMatrix.png?raw=true)

The chart above shows the relationship between any 2 features from the list above. The relationship is a number between 0 and 1 which indicates how possible it is to infer 1 value from the other.

The most important thing here is that price is relatively strongly and positively correlated with the following features:
* accommodates
* bathrooms
* bedrooms
* beds
* guests_included

This makes a lot of sense. The above are all proxies of the size of the property and how expensive a property is has a lot to do with how big it is.

The next step is to examine more closely, the nature of these correlations. To do this, I plotted box plots for these correlations *(Because price is a continuous value whereas the property features are discrete values)*

The following are the box plots:

| | | 
|:-------------------------:|:-------------------------:|
![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/PriceVsAccommodates.png?raw=true)|![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/PriceVsBedrooms.png?raw=true)
![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/PriceVsBeds.png?raw=true)|![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/PriceVsBathrooms.png?raw=true)
![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/PriceVsGuests.png?raw=true) |

All the features are positively correlated with price which means, as their value goes up, so does price.

### Data Preparation
Following this insight, I did what appeared logic to me. I tried to fit a simple model to this data so I could predict a property's price based on the 5 columns in the previous section.

Data preparation in this case is straightforward. The first thing I did is put the price values into buckets. This makes sense given that the data clearly has a many-to-one relationship *(**eg.** multiple property prices for 3 bedrooms)*. I experimented with different bucket sizes before settling on 50. The next step is to pick out the columns and normalize them. I did this and created a new csv called 'pricing_model_train.csv'

### Modelling
I used machine learning to model the relationship between the inputs and output. In this case I chose a standard classifier based on neural networks. I trained this classifier on the data in pricing_model_train.csv and the following are the results I got:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/confusion_matrix_labelled.png?raw=true)

The confusion matrix above is a way to quantify the merit of a model. It basically shows how many times the trained model predicted the price correctly vs. incorrectly. For eg. the value at the third row and third column is 90. This means that, there are 90 instances where the model correctly predicted that a property is between $150-$200. The value at the fifth row and third column is 15. This means that in 15 instances the model predicted a price of $150-$200 but it was actually $250-$300. 

This confusion matrix is not as good as I was expecting it to be but it was the best I could get despite spending some time tinkering with the training parameters. Upon further research, I came across why this was.

### Evaluation
This is a typical example of the multicollinearity problem detailed [here](https://en.wikipedia.org/wiki/Multicollinearity). Essentially the problem is that all the input features we chose are correlated with each other. The technical reason why this is a problem is that the model cannot indepenently gauge the effect of 1 input variable on the output. Intuitively the problem is that all the input features are saying the same thing. For eg. once you know how many people a property can accommodate, the other features like bedrooms, bathrooms etc. don't bring any new information that would allow us to infer the price as they are all a proxy for property size.

Based on this insight, I guessed that if I trained the model on the most strongly correlated input variable *(**ie.** accommodates)*, I should basically get the same result. This proved to be correct. The accuracy of the two models turned out to be :

* 5 input model precision: 55.4%
* 1 input model precision: 53.0%

### Deployment
Depending on the business context, if the number above are good enough, in theory this could be deployed on Airbnb's website to provide suggestions to prospective landlords with regards to how much they should price the propery for.

## Question 3
For the third CRISP-DM cycle, I decided I wanted to include an additional data set to do some comparative analysis. There is another data set of Airbnb listings and bookings for Boston available [here](https://www.kaggle.com/airbnb/boston/data) that is in the same format as this data set for Seattle. This is very convenient as it will make data understanding and preparation very simple. What I'd like to understand this time is how the apartments in Seattle compare with the ones in Boston

### Business & Data Understanding
The question in this case should be:

How do the key specs for the apartments in Seattle compare to the ones in Boston and how pricey are they?

The Boston data set is very convenient because it is almost identically organized as the Seattle data set. We have the same three files *(**ie.** calendar.csv, listings.csv and reviews.csv)*. I picked the following features for comparison between Seattle and Boston:
* room_type
* accommodates
* bathrooms
* bedrooms
* beds
* price

The listings.csv file in both data sets contains these features so I didn't have a problem.

### Data Preparation & Modelling
All I had to do to prepare the data was to join it. I created a new table with the chosen columns above plus one more for the city. This is what the joined data looks like:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/ListingsJoinedPreview.png?raw=true)

I then modelled the data using violin charts. To begin with I created a chart to visualize the price distribution in both cities. This is what I got:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_price_limited.png?raw=true)

This chart doesn't give a clear indication of the price difference in the two cities so I broke it down further into property types and this is what I got:

| | | 
|:-------------------------:|:-------------------------:|
![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_price_of_roomtypes.png?raw=true)|![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_price_of_peopleaccommodated.png?raw=true)
![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_price_of_bathrooms.png?raw=true)|![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_price_of_bedrooms.png?raw=true)
![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_price_of_beds.png?raw=true)|

A cursory glance at the above charts indicates that the properties in Boston are generally pricier than the equivalently spec'd apartments in Seattle. This is a statement about the price so I compared the distribution of property types in the two cities and this is what I got:

| | |
|:-------------------------:|:-------------------------:|
![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_peopleaccommodated.png?raw=true)|![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_bathrooms.png?raw=true)
![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_bedrooms.png?raw=true)|![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_beds.png?raw=true)|

*(**Note:** I created a redundant x-axis because seaborn doesn't like to plot violin charts without one)*

If one looks carefully at the charts above, it will become apparent that Boston generally has more properties at the smaller end and fewer at the larger end of the property size spectrum. The conclusion that I derive from that is that properties in Boston are generally smaller.

The following chart compares the explicitly classified property types in the two cities:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_roomtype.png?raw=true)

This chart further reinforces this conclusion. Seattle has more full houses and Boston has more private rooms. The shared room category is not big enough to be statistically significant.

After this, I decided to verify the results of our model so I wrote some code to display the average characteristics of the properties in Seattle vs Boston as well as the value for money. The following are the results of the former:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_average_property.png?raw=true)

The following summarizes the value for money for the two cities:

![](https://github.com/Ravi5ingh/seattle-airbnb-analysis/blob/master/viz/jupyter/seattle_vs_boston_value_for_money.png?raw=true)

The above summaries confirm what the models are telling us.

### Evaluation
To re-iterate the third question was :

How do the key specs for the apartments in Seattle compare to the ones in Boston and how pricey are they?

The answer to this question is: Based on the key specs we chose, it looks like the properties in Boston are generally smaller than the ones in Seattle. Also, properties in Boston are more expensive when compared to equally spec'd properties in Seattle.
