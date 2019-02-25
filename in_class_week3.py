# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

seconds_input=int(input('How many seconds do you wish for me to calculate?'))
hours=seconds_input//3600
minutes=(seconds_input-(hours*3600))//60
seconds=seconds_input-((hours*3600)+(minutes*60))
print('your time broken down is:')
print(hours, ' hours')
print(minutes, ' minutes')
print(seconds, ' seconds')
print('thank you')                   
      