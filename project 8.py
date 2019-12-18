#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
        temp = input("Enter the average tempurature per day separated by commas: ")
        temp = temp.split(",")
        coolDays = 0
        heatDays = 0

        for x in temp:
            if float(x) > 80 or float(x) < 60:
                if int(x) > 80:
                    coolDays += float(x) - 80
                else:
                    heatDays += 60 - float(x)

        print("There are", coolDays, "cooling degrees days and there are", heatDays, "heating degrees days.")
        
main()


# In[ ]:




