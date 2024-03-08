# -*- coding: utf-8 -*-
"""
Created on Thu May 12 23:46:53 2022

@author: Nelson.Chung
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 03:59:37 2022

@author: Owner

"""
import tabula as tb
from PyPDF2 import PdfFileReader
import io, requests
import os

os.chdir('c:/Sabr/soccer/')



# def soc_pdf(year):
#     file='https://byucougars.com/sites/default/files/season-stats/stats-w-soccer-'+str(year)+'_0.pdf'
#     pdf=requests.get(file)
#     pdf_file = io.BytesIO(pdf.content) # response being a requests Response object
#     pdf_reader = PdfFileReader(pdf_file)
#     num_pages = pdf_reader.numPages
#     for k in range(1,num_pages+1):
#         wsoc = tb.read_pdf(file,pages=k)[0]
#         wsoc.to_excel('soccer_'+str(year)+'_'+str(k)+'.xlsx')

# for i in range(2002,2011):
#     soc_pdf(i)

pdf3=tb.read_pdf('https://byucougars.com/sites/default/files/season-stats/stats-w-soccer-2008_0.pdf', pages=1)
