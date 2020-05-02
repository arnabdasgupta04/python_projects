# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:46:14 2020

@author: SONY
"""

from translate import Translator
while True:
   try: 
       b=input("Enter the code for language to be converted : ")
       t= Translator(to_lang=b)
       a=input("Enter the text in english to be converted : ")
       t1=t.translate(a)
       print()
       print(t1)
       break

   except RuntimeError:
       print()
       print("Please enter code for any other language")
    
    
    
    
       '''with open(f'C:/Users/SONY/Desktop/translate_to_{b}.txt',mode ='w') as file:
          file.write(t1)'''