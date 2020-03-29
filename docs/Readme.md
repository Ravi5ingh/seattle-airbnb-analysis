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


For this reason we should make this question more specific. So a better question is: Based on the available date range, how many properties are listed, and how many of them are booked on any given day?

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

### Modeling
The modeling steps usually involves selecting a model and a way to assess it, building the model, and then assessing it. My model is simply a line chart so this step is small.

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

