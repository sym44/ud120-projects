#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data.keys()))
print(enron_data)

i = 0
for key in enron_data:
    if enron_data[key]['poi'] == True :
        i += 1

print(i)

print(enron_data['PRENTICE JAMES']['total_stock_value'])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print(enron_data['LAY KENNETH L']['total_payments'], enron_data['SKILLING JEFFREY K']['total_payments'], enron_data['FASTOW ANDREW S']['total_payments'])

ii = 0
iii = 0
for key in enron_data:
    if enron_data[key]['salary'] != 'NaN':
        ii += 1
    if enron_data[key]['email_address'] != 'NaN':
        iii += 1

print(ii, iii)

index = 0
for key in enron_data:
    if enron_data[key]['total_payments'] == 'NaN':
        index += 1
print(index, index/146.0)

index2 = 0
for key in enron_data:
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True:
        index2 += 1
print(index2, index2/18.0)