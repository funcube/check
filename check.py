

from datetime import datetime

bank1 = [] # 一銀文
bank2 = [] # 台企公司
bank3 = [] # 臺企榮和
bank4 = [] # 臺企鑫
bank5 = [] # 聯邦茹

from datetime import datetime
X =datetime.today()
cusy = X.year
cusm = X.month
cusd = X.day
idname = str(cusy)+'-'+str(cusm)+'-'+str(cusd)

name1= idname +'-'+'一銀文.csv'
name2= idname +'-'+'臺企公司.csv'
name3= idname +'-'+'臺企榮和.csv'
name4= idname +'-'+'臺企鑫.csv'
name5= idname +'-'+'聯邦茹.csv'

# 5 臺企茹代收轉檔
bank5 = []

with open('代收-聯邦茹.csv', 'r') as f5:
	for line5 in f5:
		for line5 in f5:
		 B1,B2,B3,B4,B5,B6,B7 = line5.strip().split(',')
		 bank5.append([B1,B2,B3,B4,B5,B6,B7])
		 
with open(name5,'w') as f5:
		for b5 in bank5:
			pis = b5[6]
			
			f5.write('聯邦茹'+ ','+b5[1]+ ','+ b5[4]+ ','+ pis[3:10]+ '\n' )
			
print('5 聯邦茹轉檔成功！')


# 4 臺企旭鑫代收轉檔
with open('代收-臺企鑫.csv', 'r') as f4:
	for line4 in f4:
		for line4 in f4:
		 #if '異動日' in line:
			#continue
		 N1,N2,N3,N4,N5,N6,N7,N8,N9 = line4.strip().split(',')
		 bank4.append([N1,N2,N3,N4,N5,N6,N7,N8,N9])
		# print(bank) for check file 

#for b4 in bank4:
#	print('臺企旭鑫的代收資料 :', b4[0], b4[3], b4[4])


with open(name4,'w') as f4:
		for b4 in bank4:
		 f4.write('臺企旭鑫'+ ','+b4[0]+ ','+ b4[3]+ ','+ b4[5]+ '\n' )

print('4旭鑫代收轉檔成功 !!!!')

# 3 臺企榮和代收轉檔 
with open('代收-臺企榮和.csv', 'r') as f3:
	for line3 in f3:
		for line3 in f3:
		 R0,R1,R2,R3,R4,R5,R6,R7,R8 = line3.strip().split(',')
		 bank3.append([R0,R1,R2,R3,R4,R5,R6,R7,R8])
    
with open(name3,'w') as f3:
		for b3 in bank3:
		 f3.write('臺企榮和'+ ','+b3[0]+ ','+ b3[3]+ ','+ b3[5]+ '\n' )

print('3臺企榮和轉檔成功 !!!!')

# 2 臺企公司代收轉檔 
with open('代收-臺企公司.csv', 'r') as f2:
	for line2 in f2:
		for line2 in f2:
		 C0,C1,C2,C3,C4,C5,C6,C7,C8 = line2.strip().split(',')
		 bank2.append([C0,C1,C2,C3,C4,C5,C6,C7,C8])
    
	
with open(name2,'w') as f2:
		for b2 in bank2:
		 f2.write('臺企公司'+ ','+b2[0]+ ','+ b2[3]+ ','+ b2[5]+ '\n' )

print('2臺企公司轉檔成功 !!!!')

# 1 臺企一銀文代收轉檔 
with open('代收-一銀文.csv', 'r') as f1:
	for line1 in f1:
		for line1 in f1:
		 W0,W1,W2,W3,W4,W5,W6,W7 = line1.strip().split(',')
		 bank1.append([W0,W1,W2,W3,W4,W5,W6,W7])
    
	
with open(name1,'w') as f1:
		for b1 in bank1:
		 f1.write('一銀文'+ ','+b1[0]+ ','+ b1[3]+ ','+ b1[6]+ '\n' )

print('1一銀文轉檔成功 !!!!')

