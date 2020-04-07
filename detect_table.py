#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xlrd
import pandas as pd
import sys

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    def detectTable():             
        wb=xlrd.open_workbook(input_file)                                       
        names = []; data = []
        for name in wb.sheet_names():
            sheet = wb.sheet_by_name(name)
            counter = 0
            for i in range(sheet.nrows):                                     
                for j in range(sheet.ncols):
                    if sheet.cell_value(i,j)!= '' and (i-1<0 or sheet.cell_value(i-1,j) == '') and (j-1<0 or sheet.cell_value(i,j-1) == ''): 
                        counter +=1
            names.append(name); data.append(counter)
            df = pd.DataFrame(data = data, index = names, columns = ['number of tables'])
            output = df.to_csv(output_file)
        return output
    detectTable()


# In[ ]:




