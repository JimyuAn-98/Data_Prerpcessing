import sys
import numpy
import pandas as pd

def save_in_xlsx(a,name):
    data = pd.DataFrame(a)
    writer = pd.ExcelWriter(r'%s.xlsx'%(name))
    data.to_excel(writer,'page_1',float_format='%.6f')
    writer.save()
    writer.close()

