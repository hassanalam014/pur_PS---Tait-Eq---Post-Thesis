import os,sys,math,csv,numpy as npy
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

#======================================================
#Critical Point and Molecular Weight
#======================================================

Pc0 = 0.001
Tc0 = 265.0
Rc0 = 0.0001

Data1=False
Data2=False
Data3=False
Data4=True			#Grassia

#======================================================
#Loading Isotherm Data 1
#======================================================
if Data1==True:	
	with open('Data/Data 1 Kier Zoller Approximate M1/402K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_402K = range(0,numpts)
				T0_402K = range(0,numpts)
				R0_402K = range(0,numpts)
				M0_402K = range(0,numpts)
				I0_402K = range(0,numpts)
			if index1 >= 6:
				P0_402K[index2] = float(row[0])
				T0_402K[index2] = float(row[1])
				R0_402K[index2] = float(row[2])
				M0_402K[index2] = float(row[3])
				I0_402K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_402K
	T0 = T0_402K
	R0 = R0_402K
	M0 = M0_402K
	I0 = I0_402K

	with open('Data/Data 1 Kier Zoller Approximate M1/412K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_412K = range(0,numpts)
				T0_412K = range(0,numpts)
				R0_412K = range(0,numpts)
				M0_412K = range(0,numpts)
				I0_412K = range(0,numpts)
			if index1 >= 6:
				P0_412K[index2] = float(row[0])
				T0_412K[index2] = float(row[1])
				R0_412K[index2] = float(row[2])
				M0_412K[index2] = float(row[3])
				I0_412K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_412K),axis=0)
	T0 = npy.concatenate((T0,T0_412K),axis=0)
	R0 = npy.concatenate((R0,R0_412K),axis=0)
	M0 = npy.concatenate((M0,M0_412K),axis=0)
	I0 = npy.concatenate((I0,I0_412K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/422K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_422K = range(0,numpts)
				T0_422K = range(0,numpts)
				R0_422K = range(0,numpts)
				M0_422K = range(0,numpts)
				I0_422K = range(0,numpts)
			if index1 >= 6:
				P0_422K[index2] = float(row[0])
				T0_422K[index2] = float(row[1])
				R0_422K[index2] = float(row[2])
				M0_422K[index2] = float(row[3])
				I0_422K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_422K),axis=0)
	T0 = npy.concatenate((T0,T0_422K),axis=0)
	R0 = npy.concatenate((R0,R0_422K),axis=0)
	M0 = npy.concatenate((M0,M0_422K),axis=0)
	I0 = npy.concatenate((I0,I0_422K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/432K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_432K = range(0,numpts)
				T0_432K = range(0,numpts)
				R0_432K = range(0,numpts)
				M0_432K = range(0,numpts)
				I0_432K = range(0,numpts)
			if index1 >= 6:
				P0_432K[index2] = float(row[0])
				T0_432K[index2] = float(row[1])
				R0_432K[index2] = float(row[2])
				M0_432K[index2] = float(row[3])
				I0_432K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_432K),axis=0)
	T0 = npy.concatenate((T0,T0_432K),axis=0)
	R0 = npy.concatenate((R0,R0_432K),axis=0)
	M0 = npy.concatenate((M0,M0_432K),axis=0)
	I0 = npy.concatenate((I0,I0_432K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/442K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_442K = range(0,numpts)
				T0_442K = range(0,numpts)
				R0_442K = range(0,numpts)
				M0_442K = range(0,numpts)
				I0_442K = range(0,numpts)
			if index1 >= 6:
				P0_442K[index2] = float(row[0])
				T0_442K[index2] = float(row[1])
				R0_442K[index2] = float(row[2])
				M0_442K[index2] = float(row[3])
				I0_442K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_442K),axis=0)
	T0 = npy.concatenate((T0,T0_442K),axis=0)
	R0 = npy.concatenate((R0,R0_442K),axis=0)
	M0 = npy.concatenate((M0,M0_442K),axis=0)
	I0 = npy.concatenate((I0,I0_442K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/452K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_452K = range(0,numpts)
				T0_452K = range(0,numpts)
				R0_452K = range(0,numpts)
				M0_452K = range(0,numpts)
				I0_452K = range(0,numpts)
			if index1 >= 6:
				P0_452K[index2] = float(row[0])
				T0_452K[index2] = float(row[1])
				R0_452K[index2] = float(row[2])
				M0_452K[index2] = float(row[3])
				I0_452K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_452K),axis=0)
	T0 = npy.concatenate((T0,T0_452K),axis=0)
	R0 = npy.concatenate((R0,R0_452K),axis=0)
	M0 = npy.concatenate((M0,M0_452K),axis=0)
	I0 = npy.concatenate((I0,I0_452K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/463K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_463K = range(0,numpts)
				T0_463K = range(0,numpts)
				R0_463K = range(0,numpts)
				M0_463K = range(0,numpts)
				I0_463K = range(0,numpts)
			if index1 >= 6:
				P0_463K[index2] = float(row[0])
				T0_463K[index2] = float(row[1])
				R0_463K[index2] = float(row[2])
				M0_463K[index2] = float(row[3])
				I0_463K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_463K),axis=0)
	T0 = npy.concatenate((T0,T0_463K),axis=0)
	R0 = npy.concatenate((R0,R0_463K),axis=0)
	M0 = npy.concatenate((M0,M0_463K),axis=0)
	I0 = npy.concatenate((I0,I0_463K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/473K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_473K = range(0,numpts)
				T0_473K = range(0,numpts)
				R0_473K = range(0,numpts)
				M0_473K = range(0,numpts)
				I0_473K = range(0,numpts)
			if index1 >= 6:
				P0_473K[index2] = float(row[0])
				T0_473K[index2] = float(row[1])
				R0_473K[index2] = float(row[2])
				M0_473K[index2] = float(row[3])
				I0_473K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_473K),axis=0)
	T0 = npy.concatenate((T0,T0_473K),axis=0)
	R0 = npy.concatenate((R0,R0_473K),axis=0)
	M0 = npy.concatenate((M0,M0_473K),axis=0)
	I0 = npy.concatenate((I0,I0_473K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/482K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_482K = range(0,numpts)
				T0_482K = range(0,numpts)
				R0_482K = range(0,numpts)
				M0_482K = range(0,numpts)
				I0_482K = range(0,numpts)
			if index1 >= 6:
				P0_482K[index2] = float(row[0])
				T0_482K[index2] = float(row[1])
				R0_482K[index2] = float(row[2])
				M0_482K[index2] = float(row[3])
				I0_482K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_482K),axis=0)
	T0 = npy.concatenate((T0,T0_482K),axis=0)
	R0 = npy.concatenate((R0,R0_482K),axis=0)
	M0 = npy.concatenate((M0,M0_482K),axis=0)
	I0 = npy.concatenate((I0,I0_482K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/492K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_492K = range(0,numpts)
				T0_492K = range(0,numpts)
				R0_492K = range(0,numpts)
				M0_492K = range(0,numpts)
				I0_492K = range(0,numpts)
			if index1 >= 6:
				P0_492K[index2] = float(row[0])
				T0_492K[index2] = float(row[1])
				R0_492K[index2] = float(row[2])
				M0_492K[index2] = float(row[3])
				I0_492K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_492K),axis=0)
	T0 = npy.concatenate((T0,T0_492K),axis=0)
	R0 = npy.concatenate((R0,R0_492K),axis=0)
	M0 = npy.concatenate((M0,M0_492K),axis=0)
	I0 = npy.concatenate((I0,I0_492K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/503K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_503K = range(0,numpts)
				T0_503K = range(0,numpts)
				R0_503K = range(0,numpts)
				M0_503K = range(0,numpts)
				I0_503K = range(0,numpts)
			if index1 >= 6:
				P0_503K[index2] = float(row[0])
				T0_503K[index2] = float(row[1])
				R0_503K[index2] = float(row[2])
				M0_503K[index2] = float(row[3])
				I0_503K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_503K),axis=0)
	T0 = npy.concatenate((T0,T0_503K),axis=0)
	R0 = npy.concatenate((R0,R0_503K),axis=0)
	M0 = npy.concatenate((M0,M0_503K),axis=0)
	I0 = npy.concatenate((I0,I0_503K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/513K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_513K = range(0,numpts)
				T0_513K = range(0,numpts)
				R0_513K = range(0,numpts)
				M0_513K = range(0,numpts)
				I0_513K = range(0,numpts)
			if index1 >= 6:
				P0_513K[index2] = float(row[0])
				T0_513K[index2] = float(row[1])
				R0_513K[index2] = float(row[2])
				M0_513K[index2] = float(row[3])
				I0_513K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_513K),axis=0)
	T0 = npy.concatenate((T0,T0_513K),axis=0)
	R0 = npy.concatenate((R0,R0_513K),axis=0)
	M0 = npy.concatenate((M0,M0_513K),axis=0)
	I0 = npy.concatenate((I0,I0_513K),axis=0)

	with open('Data/Data 1 Kier Zoller Approximate M1/524K_PS_11E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_524K = range(0,numpts)
				T0_524K = range(0,numpts)
				R0_524K = range(0,numpts)
				M0_524K = range(0,numpts)
				I0_524K = range(0,numpts)
			if index1 >= 6:
				P0_524K[index2] = float(row[0])
				T0_524K[index2] = float(row[1])
				R0_524K[index2] = float(row[2])
				M0_524K[index2] = float(row[3])
				I0_524K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_524K),axis=0)
	T0 = npy.concatenate((T0,T0_524K),axis=0)
	R0 = npy.concatenate((R0,R0_524K),axis=0)
	M0 = npy.concatenate((M0,M0_524K),axis=0)
	I0 = npy.concatenate((I0,I0_524K),axis=0)

#======================================================
#Loading Isotherm Data 2
#======================================================

if Data2==True:	
	with open('Data/Data 2 Just Overlap M1/383K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_383K = range(0,numpts)
				T0_383K = range(0,numpts)
				R0_383K = range(0,numpts)
				M0_383K = range(0,numpts)
				I0_383K = range(0,numpts)
			if index1 >= 6:
				P0_383K[index2] = float(row[0])
				T0_383K[index2] = float(row[1])
				R0_383K[index2] = float(row[2])
				M0_383K[index2] = float(row[3])
				I0_383K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_383K
	T0 = T0_383K
	R0 = R0_383K
	M0 = M0_383K
	I0 = I0_383K

	with open('Data/Data 2 Just Overlap M1/393K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_393K = range(0,numpts)
				T0_393K = range(0,numpts)
				R0_393K = range(0,numpts)
				M0_393K = range(0,numpts)
				I0_393K = range(0,numpts)
			if index1 >= 6:
				P0_393K[index2] = float(row[0])
				T0_393K[index2] = float(row[1])
				R0_393K[index2] = float(row[2])
				M0_393K[index2] = float(row[3])
				I0_393K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_393K),axis=0)
	T0 = npy.concatenate((T0,T0_393K),axis=0)
	R0 = npy.concatenate((R0,R0_393K),axis=0)
	M0 = npy.concatenate((M0,M0_393K),axis=0)
	I0 = npy.concatenate((I0,I0_393K),axis=0)

	with open('Data/Data 2 Just Overlap M1/403K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_403K = range(0,numpts)
				T0_403K = range(0,numpts)
				R0_403K = range(0,numpts)
				M0_403K = range(0,numpts)
				I0_403K = range(0,numpts)
			if index1 >= 6:
				P0_403K[index2] = float(row[0])
				T0_403K[index2] = float(row[1])
				R0_403K[index2] = float(row[2])
				M0_403K[index2] = float(row[3])
				I0_403K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_403K),axis=0)
	T0 = npy.concatenate((T0,T0_403K),axis=0)
	R0 = npy.concatenate((R0,R0_403K),axis=0)
	M0 = npy.concatenate((M0,M0_403K),axis=0)
	I0 = npy.concatenate((I0,I0_403K),axis=0)

	with open('Data/Data 2 Just Overlap M1/413K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_413K = range(0,numpts)
				T0_413K = range(0,numpts)
				R0_413K = range(0,numpts)
				M0_413K = range(0,numpts)
				I0_413K = range(0,numpts)
			if index1 >= 6:
				P0_413K[index2] = float(row[0])
				T0_413K[index2] = float(row[1])
				R0_413K[index2] = float(row[2])
				M0_413K[index2] = float(row[3])
				I0_413K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_413K),axis=0)
	T0 = npy.concatenate((T0,T0_413K),axis=0)
	R0 = npy.concatenate((R0,R0_413K),axis=0)
	M0 = npy.concatenate((M0,M0_413K),axis=0)
	I0 = npy.concatenate((I0,I0_413K),axis=0)

	with open('Data/Data 2 Just Overlap M1/423K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_423K = range(0,numpts)
				T0_423K = range(0,numpts)
				R0_423K = range(0,numpts)
				M0_423K = range(0,numpts)
				I0_423K = range(0,numpts)
			if index1 >= 6:
				P0_423K[index2] = float(row[0])
				T0_423K[index2] = float(row[1])
				R0_423K[index2] = float(row[2])
				M0_423K[index2] = float(row[3])
				I0_423K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_423K),axis=0)
	T0 = npy.concatenate((T0,T0_423K),axis=0)
	R0 = npy.concatenate((R0,R0_423K),axis=0)
	M0 = npy.concatenate((M0,M0_423K),axis=0)
	I0 = npy.concatenate((I0,I0_423K),axis=0)

	with open('Data/Data 2 Just Overlap M1/433K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_433K = range(0,numpts)
				T0_433K = range(0,numpts)
				R0_433K = range(0,numpts)
				M0_433K = range(0,numpts)
				I0_433K = range(0,numpts)
			if index1 >= 6:
				P0_433K[index2] = float(row[0])
				T0_433K[index2] = float(row[1])
				R0_433K[index2] = float(row[2])
				M0_433K[index2] = float(row[3])
				I0_433K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_433K),axis=0)
	T0 = npy.concatenate((T0,T0_433K),axis=0)
	R0 = npy.concatenate((R0,R0_433K),axis=0)
	M0 = npy.concatenate((M0,M0_433K),axis=0)
	I0 = npy.concatenate((I0,I0_433K),axis=0)

	with open('Data/Data 2 Just Overlap M1/443K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_443K = range(0,numpts)
				T0_443K = range(0,numpts)
				R0_443K = range(0,numpts)
				M0_443K = range(0,numpts)
				I0_443K = range(0,numpts)
			if index1 >= 6:
				P0_443K[index2] = float(row[0])
				T0_443K[index2] = float(row[1])
				R0_443K[index2] = float(row[2])
				M0_443K[index2] = float(row[3])
				I0_443K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_443K),axis=0)
	T0 = npy.concatenate((T0,T0_443K),axis=0)
	R0 = npy.concatenate((R0,R0_443K),axis=0)
	M0 = npy.concatenate((M0,M0_443K),axis=0)
	I0 = npy.concatenate((I0,I0_443K),axis=0)

	with open('Data/Data 2 Just Overlap M1/453K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_453K = range(0,numpts)
				T0_453K = range(0,numpts)
				R0_453K = range(0,numpts)
				M0_453K = range(0,numpts)
				I0_453K = range(0,numpts)
			if index1 >= 6:
				P0_453K[index2] = float(row[0])
				T0_453K[index2] = float(row[1])
				R0_453K[index2] = float(row[2])
				M0_453K[index2] = float(row[3])
				I0_453K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_453K),axis=0)
	T0 = npy.concatenate((T0,T0_453K),axis=0)
	R0 = npy.concatenate((R0,R0_453K),axis=0)
	M0 = npy.concatenate((M0,M0_453K),axis=0)
	I0 = npy.concatenate((I0,I0_453K),axis=0)

	with open('Data/Data 2 Just Overlap M1/463K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_463K = range(0,numpts)
				T0_463K = range(0,numpts)
				R0_463K = range(0,numpts)
				M0_463K = range(0,numpts)
				I0_463K = range(0,numpts)
			if index1 >= 6:
				P0_463K[index2] = float(row[0])
				T0_463K[index2] = float(row[1])
				R0_463K[index2] = float(row[2])
				M0_463K[index2] = float(row[3])
				I0_463K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_463K),axis=0)
	T0 = npy.concatenate((T0,T0_463K),axis=0)
	R0 = npy.concatenate((R0,R0_463K),axis=0)
	M0 = npy.concatenate((M0,M0_463K),axis=0)
	I0 = npy.concatenate((I0,I0_463K),axis=0)

	with open('Data/Data 2 Just Overlap M1/473K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_473K = range(0,numpts)
				T0_473K = range(0,numpts)
				R0_473K = range(0,numpts)
				M0_473K = range(0,numpts)
				I0_473K = range(0,numpts)
			if index1 >= 6:
				P0_473K[index2] = float(row[0])
				T0_473K[index2] = float(row[1])
				R0_473K[index2] = float(row[2])
				M0_473K[index2] = float(row[3])
				I0_473K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_473K),axis=0)
	T0 = npy.concatenate((T0,T0_473K),axis=0)
	R0 = npy.concatenate((R0,R0_473K),axis=0)
	M0 = npy.concatenate((M0,M0_473K),axis=0)
	I0 = npy.concatenate((I0,I0_473K),axis=0)

	with open('Data/Data 2 Just Overlap M1/483K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_483K = range(0,numpts)
				T0_483K = range(0,numpts)
				R0_483K = range(0,numpts)
				M0_483K = range(0,numpts)
				I0_483K = range(0,numpts)
			if index1 >= 6:
				P0_483K[index2] = float(row[0])
				T0_483K[index2] = float(row[1])
				R0_483K[index2] = float(row[2])
				M0_483K[index2] = float(row[3])
				I0_483K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_483K),axis=0)
	T0 = npy.concatenate((T0,T0_483K),axis=0)
	R0 = npy.concatenate((R0,R0_483K),axis=0)
	M0 = npy.concatenate((M0,M0_483K),axis=0)
	I0 = npy.concatenate((I0,I0_483K),axis=0)

	with open('Data/Data 2 Just Overlap M1/493K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_493K = range(0,numpts)
				T0_493K = range(0,numpts)
				R0_493K = range(0,numpts)
				M0_493K = range(0,numpts)
				I0_493K = range(0,numpts)
			if index1 >= 6:
				P0_493K[index2] = float(row[0])
				T0_493K[index2] = float(row[1])
				R0_493K[index2] = float(row[2])
				M0_493K[index2] = float(row[3])
				I0_493K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_493K),axis=0)
	T0 = npy.concatenate((T0,T0_493K),axis=0)
	R0 = npy.concatenate((R0,R0_493K),axis=0)
	M0 = npy.concatenate((M0,M0_493K),axis=0)
	I0 = npy.concatenate((I0,I0_493K),axis=0)

	with open('Data/Data 2 Just Overlap M1/503K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_503K = range(0,numpts)
				T0_503K = range(0,numpts)
				R0_503K = range(0,numpts)
				M0_503K = range(0,numpts)
				I0_503K = range(0,numpts)
			if index1 >= 6:
				P0_503K[index2] = float(row[0])
				T0_503K[index2] = float(row[1])
				R0_503K[index2] = float(row[2])
				M0_503K[index2] = float(row[3])
				I0_503K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_503K),axis=0)
	T0 = npy.concatenate((T0,T0_503K),axis=0)
	R0 = npy.concatenate((R0,R0_503K),axis=0)
	M0 = npy.concatenate((M0,M0_503K),axis=0)
	I0 = npy.concatenate((I0,I0_503K),axis=0)

	with open('Data/Data 2 Just Overlap M1/513K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_513K = range(0,numpts)
				T0_513K = range(0,numpts)
				R0_513K = range(0,numpts)
				M0_513K = range(0,numpts)
				I0_513K = range(0,numpts)
			if index1 >= 6:
				P0_513K[index2] = float(row[0])
				T0_513K[index2] = float(row[1])
				R0_513K[index2] = float(row[2])
				M0_513K[index2] = float(row[3])
				I0_513K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_513K),axis=0)
	T0 = npy.concatenate((T0,T0_513K),axis=0)
	R0 = npy.concatenate((R0,R0_513K),axis=0)
	M0 = npy.concatenate((M0,M0_513K),axis=0)
	I0 = npy.concatenate((I0,I0_513K),axis=0)

	with open('Data/Data 2 Just Overlap M1/523K_PS_25E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_523K = range(0,numpts)
				T0_523K = range(0,numpts)
				R0_523K = range(0,numpts)
				M0_523K = range(0,numpts)
				I0_523K = range(0,numpts)
			if index1 >= 6:
				P0_523K[index2] = float(row[0])
				T0_523K[index2] = float(row[1])
				R0_523K[index2] = float(row[2])
				M0_523K[index2] = float(row[3])
				I0_523K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_523K),axis=0)
	T0 = npy.concatenate((T0,T0_523K),axis=0)
	R0 = npy.concatenate((R0,R0_523K),axis=0)
	M0 = npy.concatenate((M0,M0_523K),axis=0)
	I0 = npy.concatenate((I0,I0_523K),axis=0)

#======================================================
#Loading Isotherm Data 3
#======================================================

if Data3==True:	
	with open('Data/Data 3 Approximate M1/453K_PS_238E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_453K = range(0,numpts)
				T0_453K = range(0,numpts)
				R0_453K = range(0,numpts)
				M0_453K = range(0,numpts)
				I0_453K = range(0,numpts)
			if index1 >= 6:
				P0_453K[index2] = float(row[0])
				T0_453K[index2] = float(row[1])
				R0_453K[index2] = float(row[2])
				M0_453K[index2] = float(row[3])
				I0_453K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_453K
	T0 = T0_453K
	R0 = R0_453K
	M0 = M0_453K
	I0 = I0_453K

	with open('Data/Data 3 Approximate M1/473K_PS_238E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_473K = range(0,numpts)
				T0_473K = range(0,numpts)
				R0_473K = range(0,numpts)
				M0_473K = range(0,numpts)
				I0_473K = range(0,numpts)
			if index1 >= 6:
				P0_473K[index2] = float(row[0])
				T0_473K[index2] = float(row[1])
				R0_473K[index2] = float(row[2])
				M0_473K[index2] = float(row[3])
				I0_473K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_473K),axis=0)
	T0 = npy.concatenate((T0,T0_473K),axis=0)
	R0 = npy.concatenate((R0,R0_473K),axis=0)
	M0 = npy.concatenate((M0,M0_473K),axis=0)
	I0 = npy.concatenate((I0,I0_473K),axis=0)

	with open('Data/Data 3 Approximate M1/493K_PS_238E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_493K = range(0,numpts)
				T0_493K = range(0,numpts)
				R0_493K = range(0,numpts)
				M0_493K = range(0,numpts)
				I0_493K = range(0,numpts)
			if index1 >= 6:
				P0_493K[index2] = float(row[0])
				T0_493K[index2] = float(row[1])
				R0_493K[index2] = float(row[2])
				M0_493K[index2] = float(row[3])
				I0_493K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_493K),axis=0)
	T0 = npy.concatenate((T0,T0_493K),axis=0)
	R0 = npy.concatenate((R0,R0_493K),axis=0)
	M0 = npy.concatenate((M0,M0_493K),axis=0)
	I0 = npy.concatenate((I0,I0_493K),axis=0)

#======================================================
#Loading Isotherm Data 4
#======================================================

if Data4==True:	
	with open('Data/Data 4 Grassia Approximate M1/378K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_378K = range(0,numpts)
				T0_378K = range(0,numpts)
				R0_378K = range(0,numpts)
				M0_378K = range(0,numpts)
				I0_378K = range(0,numpts)
			if index1 >= 6:
				P0_378K[index2] = float(row[0])
				T0_378K[index2] = float(row[1])
				R0_378K[index2] = float(row[2])
				M0_378K[index2] = float(row[3])
				I0_378K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_378K
	T0 = T0_378K
	R0 = R0_378K
	M0 = M0_378K
	I0 = I0_378K

	with open('Data/Data 4 Grassia Approximate M1/383K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_383K = range(0,numpts)
				T0_383K = range(0,numpts)
				R0_383K = range(0,numpts)
				M0_383K = range(0,numpts)
				I0_383K = range(0,numpts)
			if index1 >= 6:
				P0_383K[index2] = float(row[0])
				T0_383K[index2] = float(row[1])
				R0_383K[index2] = float(row[2])
				M0_383K[index2] = float(row[3])
				I0_383K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_383K),axis=0)
	T0 = npy.concatenate((T0,T0_383K),axis=0)
	R0 = npy.concatenate((R0,R0_383K),axis=0)
	M0 = npy.concatenate((M0,M0_383K),axis=0)
	I0 = npy.concatenate((I0,I0_383K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/388K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_388K = range(0,numpts)
				T0_388K = range(0,numpts)
				R0_388K = range(0,numpts)
				M0_388K = range(0,numpts)
				I0_388K = range(0,numpts)
			if index1 >= 6:
				P0_388K[index2] = float(row[0])
				T0_388K[index2] = float(row[1])
				R0_388K[index2] = float(row[2])
				M0_388K[index2] = float(row[3])
				I0_388K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_388K),axis=0)
	T0 = npy.concatenate((T0,T0_388K),axis=0)
	R0 = npy.concatenate((R0,R0_388K),axis=0)
	M0 = npy.concatenate((M0,M0_388K),axis=0)
	I0 = npy.concatenate((I0,I0_388K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/393K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_393K = range(0,numpts)
				T0_393K = range(0,numpts)
				R0_393K = range(0,numpts)
				M0_393K = range(0,numpts)
				I0_393K = range(0,numpts)
			if index1 >= 6:
				P0_393K[index2] = float(row[0])
				T0_393K[index2] = float(row[1])
				R0_393K[index2] = float(row[2])
				M0_393K[index2] = float(row[3])
				I0_393K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_393K),axis=0)
	T0 = npy.concatenate((T0,T0_393K),axis=0)
	R0 = npy.concatenate((R0,R0_393K),axis=0)
	M0 = npy.concatenate((M0,M0_393K),axis=0)
	I0 = npy.concatenate((I0,I0_393K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/398K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_398K = range(0,numpts)
				T0_398K = range(0,numpts)
				R0_398K = range(0,numpts)
				M0_398K = range(0,numpts)
				I0_398K = range(0,numpts)
			if index1 >= 6:
				P0_398K[index2] = float(row[0])
				T0_398K[index2] = float(row[1])
				R0_398K[index2] = float(row[2])
				M0_398K[index2] = float(row[3])
				I0_398K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_398K),axis=0)
	T0 = npy.concatenate((T0,T0_398K),axis=0)
	R0 = npy.concatenate((R0,R0_398K),axis=0)
	M0 = npy.concatenate((M0,M0_398K),axis=0)
	I0 = npy.concatenate((I0,I0_398K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/403K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_403K = range(0,numpts)
				T0_403K = range(0,numpts)
				R0_403K = range(0,numpts)
				M0_403K = range(0,numpts)
				I0_403K = range(0,numpts)
			if index1 >= 6:
				P0_403K[index2] = float(row[0])
				T0_403K[index2] = float(row[1])
				R0_403K[index2] = float(row[2])
				M0_403K[index2] = float(row[3])
				I0_403K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_403K),axis=0)
	T0 = npy.concatenate((T0,T0_403K),axis=0)
	R0 = npy.concatenate((R0,R0_403K),axis=0)
	M0 = npy.concatenate((M0,M0_403K),axis=0)
	I0 = npy.concatenate((I0,I0_403K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/408K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_408K = range(0,numpts)
				T0_408K = range(0,numpts)
				R0_408K = range(0,numpts)
				M0_408K = range(0,numpts)
				I0_408K = range(0,numpts)
			if index1 >= 6:
				P0_408K[index2] = float(row[0])
				T0_408K[index2] = float(row[1])
				R0_408K[index2] = float(row[2])
				M0_408K[index2] = float(row[3])
				I0_408K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_408K),axis=0)
	T0 = npy.concatenate((T0,T0_408K),axis=0)
	R0 = npy.concatenate((R0,R0_408K),axis=0)
	M0 = npy.concatenate((M0,M0_408K),axis=0)
	I0 = npy.concatenate((I0,I0_408K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/413K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_413K = range(0,numpts)
				T0_413K = range(0,numpts)
				R0_413K = range(0,numpts)
				M0_413K = range(0,numpts)
				I0_413K = range(0,numpts)
			if index1 >= 6:
				P0_413K[index2] = float(row[0])
				T0_413K[index2] = float(row[1])
				R0_413K[index2] = float(row[2])
				M0_413K[index2] = float(row[3])
				I0_413K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_413K),axis=0)
	T0 = npy.concatenate((T0,T0_413K),axis=0)
	R0 = npy.concatenate((R0,R0_413K),axis=0)
	M0 = npy.concatenate((M0,M0_413K),axis=0)
	I0 = npy.concatenate((I0,I0_413K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/418K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_418K = range(0,numpts)
				T0_418K = range(0,numpts)
				R0_418K = range(0,numpts)
				M0_418K = range(0,numpts)
				I0_418K = range(0,numpts)
			if index1 >= 6:
				P0_418K[index2] = float(row[0])
				T0_418K[index2] = float(row[1])
				R0_418K[index2] = float(row[2])
				M0_418K[index2] = float(row[3])
				I0_418K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_418K),axis=0)
	T0 = npy.concatenate((T0,T0_418K),axis=0)
	R0 = npy.concatenate((R0,R0_418K),axis=0)
	M0 = npy.concatenate((M0,M0_418K),axis=0)
	I0 = npy.concatenate((I0,I0_418K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/423K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_423K = range(0,numpts)
				T0_423K = range(0,numpts)
				R0_423K = range(0,numpts)
				M0_423K = range(0,numpts)
				I0_423K = range(0,numpts)
			if index1 >= 6:
				P0_423K[index2] = float(row[0])
				T0_423K[index2] = float(row[1])
				R0_423K[index2] = float(row[2])
				M0_423K[index2] = float(row[3])
				I0_423K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_423K),axis=0)
	T0 = npy.concatenate((T0,T0_423K),axis=0)
	R0 = npy.concatenate((R0,R0_423K),axis=0)
	M0 = npy.concatenate((M0,M0_423K),axis=0)
	I0 = npy.concatenate((I0,I0_423K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/428K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_428K = range(0,numpts)
				T0_428K = range(0,numpts)
				R0_428K = range(0,numpts)
				M0_428K = range(0,numpts)
				I0_428K = range(0,numpts)
			if index1 >= 6:
				P0_428K[index2] = float(row[0])
				T0_428K[index2] = float(row[1])
				R0_428K[index2] = float(row[2])
				M0_428K[index2] = float(row[3])
				I0_428K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_428K),axis=0)
	T0 = npy.concatenate((T0,T0_428K),axis=0)
	R0 = npy.concatenate((R0,R0_428K),axis=0)
	M0 = npy.concatenate((M0,M0_428K),axis=0)
	I0 = npy.concatenate((I0,I0_428K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/433K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_433K = range(0,numpts)
				T0_433K = range(0,numpts)
				R0_433K = range(0,numpts)
				M0_433K = range(0,numpts)
				I0_433K = range(0,numpts)
			if index1 >= 6:
				P0_433K[index2] = float(row[0])
				T0_433K[index2] = float(row[1])
				R0_433K[index2] = float(row[2])
				M0_433K[index2] = float(row[3])
				I0_433K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_433K),axis=0)
	T0 = npy.concatenate((T0,T0_433K),axis=0)
	R0 = npy.concatenate((R0,R0_433K),axis=0)
	M0 = npy.concatenate((M0,M0_433K),axis=0)
	I0 = npy.concatenate((I0,I0_433K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/438K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_438K = range(0,numpts)
				T0_438K = range(0,numpts)
				R0_438K = range(0,numpts)
				M0_438K = range(0,numpts)
				I0_438K = range(0,numpts)
			if index1 >= 6:
				P0_438K[index2] = float(row[0])
				T0_438K[index2] = float(row[1])
				R0_438K[index2] = float(row[2])
				M0_438K[index2] = float(row[3])
				I0_438K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_438K),axis=0)
	T0 = npy.concatenate((T0,T0_438K),axis=0)
	R0 = npy.concatenate((R0,R0_438K),axis=0)
	M0 = npy.concatenate((M0,M0_438K),axis=0)
	I0 = npy.concatenate((I0,I0_438K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/443K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_443K = range(0,numpts)
				T0_443K = range(0,numpts)
				R0_443K = range(0,numpts)
				M0_443K = range(0,numpts)
				I0_443K = range(0,numpts)
			if index1 >= 6:
				P0_443K[index2] = float(row[0])
				T0_443K[index2] = float(row[1])
				R0_443K[index2] = float(row[2])
				M0_443K[index2] = float(row[3])
				I0_443K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_443K),axis=0)
	T0 = npy.concatenate((T0,T0_443K),axis=0)
	R0 = npy.concatenate((R0,R0_443K),axis=0)
	M0 = npy.concatenate((M0,M0_443K),axis=0)
	I0 = npy.concatenate((I0,I0_443K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/448K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_448K = range(0,numpts)
				T0_448K = range(0,numpts)
				R0_448K = range(0,numpts)
				M0_448K = range(0,numpts)
				I0_448K = range(0,numpts)
			if index1 >= 6:
				P0_448K[index2] = float(row[0])
				T0_448K[index2] = float(row[1])
				R0_448K[index2] = float(row[2])
				M0_448K[index2] = float(row[3])
				I0_448K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_448K),axis=0)
	T0 = npy.concatenate((T0,T0_448K),axis=0)
	R0 = npy.concatenate((R0,R0_448K),axis=0)
	M0 = npy.concatenate((M0,M0_448K),axis=0)
	I0 = npy.concatenate((I0,I0_448K),axis=0)

	with open('Data/Data 4 Grassia Approximate M1/453K_PS_29E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_453K = range(0,numpts)
				T0_453K = range(0,numpts)
				R0_453K = range(0,numpts)
				M0_453K = range(0,numpts)
				I0_453K = range(0,numpts)
			if index1 >= 6:
				P0_453K[index2] = float(row[0])
				T0_453K[index2] = float(row[1])
				R0_453K[index2] = float(row[2])
				M0_453K[index2] = float(row[3])
				I0_453K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_453K),axis=0)
	T0 = npy.concatenate((T0,T0_453K),axis=0)
	R0 = npy.concatenate((R0,R0_453K),axis=0)
	M0 = npy.concatenate((M0,M0_453K),axis=0)
	I0 = npy.concatenate((I0,I0_453K),axis=0)

#======================================================
#Isotherm PVT Data
#======================================================

#Including all experimental data.
#temp = ['303K','312K','321K','332K','343K','354K','364K','373K','383K','393K','402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']
#Only data 20K above the glass transition.
#temp = ['402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']
#All data excluding all data within 20K of the glass transition.
#temp = ['303K','312K','321K','332K','343K','402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']

#for i in range(0,len(temp)):
#	exec "P0_%s,T0_%s,R0_%s,M0_%s,I0_%s = loadExperimentalData('%s_PS_11E4_PVT','isotherm',True)" % (temp[i],temp[i],temp[i],temp[i],temp[i],temp[i])