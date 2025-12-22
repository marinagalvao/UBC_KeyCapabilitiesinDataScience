"""
Created on Thurs March 13 15:17:42 2025

@author: Marina Galvao

This function creates helper data to test the group_and_sum function 
created on script script1.py for the Final Assignment for the 
Programming in Python for Data Science course

"""

from script1 import group_and_sum
import pandas as pd

def test_group_and_sum():
    
        # Create helper data 
        
        vinyl_sales = {'vinyl_artist': ['Taylor Swift', 'Ed Sheeran', 'Bruno Mars', 
                                'Britney Spears', 'Ed Sheeran', 'Britney Spears', 
                                'Ed Sheeran', 'Taylor Swift', 'Taylor Swift', 
                                'Childish Gambino'], 
                    
                'album_title': ['Reputation','Autumn Variations', 'Doo-Wops & Hooligans',
                                'Circus', '5','Blackout', 'Loose Change', 'Lovers','1989', 'Camp'],
                
                'album_price': [40, 33, 39.99, 34.99, 35, 39.99, 40, 45, 50.99, 37]}
        
        # Convert the dictionary to a dataframe which we can use for testing
        
        helper_data1 = pd.DataFrame.from_dict(vinyl_sales)
        
        # Call the group_and_sum function
        # In this case the group_and_sum function will give us the amount profitted from each artist 
        
        test1 = group_and_sum(helper_data1, 'vinyl_artist', 'album_price')
        
        # Create unit tests for the group and sum function
        
        assert test1.loc['Taylor Swift', 'album_price'] == 135.99, 'Sum for Taylor Swift is incorrect'
        assert test1.loc['Ed Sheeran', 'album_price'] == 108, 'Sum for Ed Sheeran is incorrect'
        assert test1.loc['Childish Gambino', 'album_price'] == 37, 'Sum for Childish Gambino is incorrect'
        
        
        
"""
Created on Fri March 14 07:22:01 2025

@author: Marina Galvao

This function creates helper data to test the group_and_sum function 
created on script script1.py for the Final Assignment for the 
Programming in Python for Data Science course

"""

from script1 import group_and_sum
import pandas as pd

def test_group_and_sum2():
    
        # Create helper data 
        
        store_bag_sales = {'sold_by': ['Amy B.', 'John L.', 'Katie G.', 
                                       'John L.', 'Rebeca M.', 'John L.', 
                                       'Amy B.', 'Hector C.', 'Hector C.', 
                                       'Donald W.'], 
                    
                'item': ['bag_491','bag_184', 'bag_141','bag_491', 'bag_943',
                         'bag_254', 'bag_141', 'bag_424', 'bag_324', 'bag_943'],
                
                'bag_price': [140, 100, 90, 135, 100, 200, 150, 135, 140, 100]}
        
        # Convert the dictionary to a dataframe which we can use for testing
        
        helper_data2 = pd.DataFrame.from_dict(store_bag_sales)

        # Call the group_and_sum function
        # In this case, the group_and_sum function will give us the total sold by each store employee, 
        # which can be used for instance, to calculate comission
        
        test2 = group_and_sum(helper_data2, 'sold_by', 'bag_price')
        
        # Create unit tests for the group and sum function
        
        assert test2.loc['Donald W.', 'bag_price'] == 100, 'Sum for Donald W. is incorrect'
        assert test2.loc['Amy B.', 'bag_price'] == 290, 'Sum for Amy B. is incorrect'
        assert test2.loc['John L.', 'bag_price'] == 435, 'Sum for John L. is incorrect'