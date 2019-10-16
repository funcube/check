# 這個是check.py 的改寫

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

from datetime import datetime

import time

#（1）讀取excell 資料的函數

def fileread(name,i,j,k):

	X =datetime.today() # 再檔案名稱加入當天日期
	cusy = X.year
	cusm = X.month
	cusd = X.day
	idname = str(cusy)+'-'+str(cusm)+str(cusd)

	wb = load_workbook(filename = name +'.xlsx')
	ws = wb.active
	#print(ws) # 這個是我檢查讀取是否正確的第一步
	# （3） 將檔案存入【】中 
	bank = []
	rows =ws.rows
	columns =ws.columns

	for row in rows:
		line = [col.value for col in row]
		# print(line)
		bank.append(line)
	for b in bank: # 確認存入是否正確
			print(str(b[i]),b[j],b[k])
	#存入資料
	wbr = Workbook()
	dest_filename = name+idname+'.xlsx'
	ws2 = wbr.create_sheet(title=name)

	for b in bank: 
		ws2.append(b)

	wbr.save(filename = dest_filename)


	

fileread('代收-一銀文',0,3,6)


