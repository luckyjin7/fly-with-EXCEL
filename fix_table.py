#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import xlrd
import xlwt

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    rb=xlrd.open_workbook(input_file)
    wb = xlwt.Workbook()

    for name in rb.sheet_names():
        r_sheet = rb.sheet_by_name(name) 
        w_sheet = wb.add_sheet(name)    
        for i in range(r_sheet.nrows):                                     
            for j in range(r_sheet.ncols):
                if r_sheet.cell_value(i,j) == '' and (i-1>=0 and r_sheet.cell_value(i-1,j)!='') and (j-1>=0 and r_sheet.cell_value(i,j-1)!=''):
                    r_sheet.put_cell(i,j,1,'null',0)
                w_sheet.write(i,j, r_sheet.cell_value(i,j))     
    wb.save(output_file)


# In[ ]:




