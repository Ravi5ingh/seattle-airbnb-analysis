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

I made a mistake here. I didn't do the last part *(**ie.** verifying)* properly. As a result, I got the wrong answer to the right question but I will explain this after I've described what I did.

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
