Pesa Pulse: Customer Data Analytics

This is a project I am working on to practise Python and data analysis.I used the JSONPlaceholder API to retrieve customer information and explore the data.

Tools Used

*Python
* Requests
* Pandas
* Matplotlib
* pathlib

What I Have Done So Far

1. Getting Customer Data

I used the Requests library to connect to the API and retrieve customer data. I created a function called get_customers() to fetch the information. I also added a timeout and error handling in case the connection fails.

2. Exploring the Data

I created an explore() function to help me understand how the customer data is organised. I used loops and recursion to go through dictionaries and lists and print the keys and their data types.

3. Extracting Customer Information

I created an extract_attributes() function to pick out the information I needed from each customer. This included names, emails, phone numbers, addresses, company details, latitude and longitude.

4. Finding Customer Cities

I created a unique_cities() function to find all the different cities in the data. I also created a city_counts() function to count how many customers came from each city.

5. Counting Email Domains

I created an email_domain_counts() function to count the different email endings used by customers. I used loops, dictionaries and the split() method to do this.

6. Working with Pandas

I created a to_dataframe() function to convert the extracted customer information into a Pandas DataFrame so I could view it in a table.

7. Creating Charts

I used Matplotlib to create two bar charts:

A chart showing the number of customers in each city.

A chart showing the number of customers for each email domain.

I saved the charts inside a folder called visuals.

"What I Found"

I retrieved 10 customer records from the API.

There were 10 different cities.

Each city had one customer.

The .biz email ending appeared 3 times.

The other email endings were .tv, .net, .org, .ca, .info, .me and .io.

"What I Have Learned"

* Through this project, I have practised:

* Connecting to an API using Python.

* Handling errors when retrieving data.

* Working with dictionaries and lists.

* Understanding nested data.

* Writing functions and using loops.

* Using Pandas to organise data.

* Creating charts using Matplotlib.

------------------Conclusion------------------------------

This project has helped me understand how to retrieve data from an API, work with it using Python and present it in a way that is easier to understand. I am still learning, and I will continue improving the project as I go.