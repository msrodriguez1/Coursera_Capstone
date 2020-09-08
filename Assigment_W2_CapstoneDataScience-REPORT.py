#!/usr/bin/env python
# coding: utf-8

# # Planning new cosmopolitan cities

# **Introduction**

# What differences has an attractive and cosmopolitan city, such as New York, Paris, London, or Rome, from other cities of the world?. Besides the extravagant arquichecture of the buildings and the avant-garde that takes place in those cities, a factor that makes them very attractive is how well they are organized. 
# City organization and planning is important to improve life quality of the neighbours, ensure succes of the stores and rise of the neighbourhood price. The question that arises is: How can plan the not yet consolidated cities to improve them and make them more easy to live and attractive?
# 

# **Problem**

# Particulary in this report the target city to be planed it Santiago de Chile. Santiago de Chile is a huge city with  5.2 million inhabitants , that is the third part of the total population of Chile. This city is the capital of the country. Different types of neighbourhoods exists in Santiago, some of them are very rich and others very poor, but what they have in common is that were not planned. That explains why people have to travel from neighbourhood to neihbourhood to find a store, bank o go to school or job. That reduce life quality of the inhabitants and make it more expensive. 

# **Interest**

# The municipalities that govern the neighbourhood may be interested in improve the neighbourhoods by planning them, this to ensure that every inhabitant has access to the basic places such as stores, gym, schools, banks, pharmacy and health attention. A good planning of the cities may result in an increase of the neighbourhood value. 

# **Data adquisition and processing methodology**

# To build a system that recomends the optimal planning of a neighbourhood based on what is actually available in the place is necesary to caracterize a model neighbourhood. To do that a model with be built to caracterize the neighbourhood of cosmopolitan cities. The model wil be train with the data of New York, Toronto, Paris, Sydney, Melbourne and London. This caracterization of the neighbourhoods of the cities will be usefull to have a reference of how are they planned according to the population, accesses, and location. 

# The model will take as input the location, population and distance from center of a particular neighbourhood of Santiago de Chile. Then, the model will retrieve the most similar neighbourhoods (from Toronto, Paris New York, Sydney, etc...). After that, those neighbourhoods will be analyzed to determine what have in common (how many stores, what kind of stores, etc...). Finally the model will suggest what to add to the chilean neighbourhood to make it more like a first world city neighbourhood. 

# To train the model the data will be obtain by API in Foursquare. 

# In[ ]:




