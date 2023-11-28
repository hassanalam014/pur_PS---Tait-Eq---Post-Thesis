import os,sys,math,numpy as npy,matplotlib.pyplot as plt
from math import *
from loadExperimentalData import *
from lmfit import minimize, Parameters, report_fit
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from isListOrNpyArray import *
# from calculateSimpleResidual import calculatePureResidual

def TaitVolume(P,T,V_0,alpha,B0,B1):
	# T=T-273.15
	# P = 100*P
	# print P,T,V_0,alpha,B0,B1
	C = 0.0894			#Universal Constant
	# print B1*T
	B_T = B0*math.exp(-B1*T)	#B(T): Tait Parameter
	V_0_T = V_0*math.exp(alpha*T)		#Zero Pressure Volume V(0,T), alpha: Thermal Expansion Coefficient
	V = V_0_T*(1-(C*math.log(1+(P/B_T))))
	# print P,T,V
	return V

def calculateTaitVolume(P0,T0,V_0,alpha,B0,B1):
    
  if not isListOrNpyArray(P0) and not isListOrNpyArray(T0):
      V = TaitVolume(P0,T0,V_0,alpha,B0,B1)
      result = V
    
  elif not isListOrNpyArray(P0):
      result = [[range(0,len(T0))] for x in range(2)]
      V = range(0,len(T0))
      for i in range(0,len(T0)):
          V[i] = TaitVolume(P0,T0[i],V_0,alpha,B0,B1)
      result[0] = V
      result[1] = T0
    
  elif not isListOrNpyArray(T0):
      result = [[range(0,len(P0))] for x in range(2)]
      V = range(0,len(P0))
      for i in range(0,len(P0)):
          V[i] = TaitVolume(P0[i],T0,V_0,alpha,B0,B1)
      result[0] = V
      result[1] = P0

  elif isListOrNpyArray(P0) and isListOrNpyArray(T0):
      result = [[range(0,len(P0))] for x in range(2)]
      V = range(0,len(P0))
      for i in range(0,len(P0)):
          V[i] = TaitVolume(P0[i],T0[i],V_0,alpha,B0,B1)
      result[0] = V
      result[1] = P0

  return result

def calculateResidual(params,P0,T0,R0):

	V_0 = params['V_0'].value
	alpha = params['alpha'].value
	B0 = params['B0'].value
	B1 = params['B1'].value
	
	# print V_0,alpha,B0,B1
	V0 = npy.zeros(len(R0))
	for i in range(0,len(R0)):
		V0[i] = 1.0/R0[i]

	residual = npy.zeros(len(P0))

	for j in range(0,len(P0)):
		# print j, len(P0), P0[j],T0[j],R0[j],V0[j]

		V = calculateTaitVolume(P0[j],T0[j],V_0,alpha,B0,B1)

		residual[j] = (V0[j]-V)/V0[j]
		# print V,V0[j]
		# print residual
	
	return residual

N = len(P0)
deltaP = max(P0)-min(P0)
deltaT = max(T0)-min(T0)
print('Performing fit with {} datapoints over a temperature range of {}-{}K and a pressure range of {}-{}MPa.'.format(N,min(T0),max(T0),round(min(P0),2),max(P0)))

#Initializing the parameters.
params = Parameters()
#The following code sets up the model's parameters. It includes both fitting parameters and parameters that will remain fixed
#for the fitting. The values given are the inital guesses of fitting parameters and values of fixed parameters.
#				(Name,		Value,		Vary?,		Min,		Max,		Expr)
params.add_many(('V_0',		0.6,		True,		0,			None,		None),
				('alpha',	0.0003,		True,		0,			None,		None),
				('B0',		16000,		True,		0,			None,		None),
				('B1',		0.005,		True,		0,			None,		None))

#Running the Levenberg-Marquart algorithm on the residuals in order to do least squares fitting. This will return the fitted value of the RESIDUALS.
#These need to be added to the experimental datapints to find the fitted pressures.
fit = minimize(calculateResidual,params,args=(P0,T0,R0))

#Reporting the values of the parameters. NEED TO FIGURE OUT HOW TO PRINT THIS TO FILE.
report_fit(fit.params)

V_0 = fit.params['V_0'].value
alpha = fit.params['alpha'].value
B0 = fit.params['B0'].value
B1 = fit.params['B1'].value

##########################################################
##########################################################

isotherms = True
isobars = False

# V_0:    0.78163187 +/- 0.00178507 (0.23%) (init = 0.6)
# alpha:  5.8637e-04 +/- 5.6814e-06 (0.97%) (init = 0.0003)
# B0:     462.943089 +/- 29.0677854 (6.28%) (init = 16000)
# B1:     0.00300811 +/- 1.5205e-04 (5.05%) (init = 0.005)

P_exp_min = min(P0)
P_exp_max = max(P0)
T_exp_min = min(T0)
T_exp_max = max(T0)
R_exp_min = min(R0)
R_exp_max = max(R0)
V_exp_max = 1.0/R_exp_min
V_exp_min = 1.0/R_exp_max

Pmin = min(P0)
Pmax = max(P0)
Tmin = min(T0)
Tmax = max(T0)

print('The pressure range is {}-{}MPa and the temperature range is {}-{}K.'.format(Pmin,Pmax,Tmin,Tmax))

if isobars:
	V0_22MPA = 1/npy.array(R0_22MPA)
	V0_40MPA = 1/npy.array(R0_40MPA)
	V0_60MPA = 1/npy.array(R0_60MPA)

	T = npy.linspace(Tmin,Tmax,num=10)

	V_22MPA = npy.zeros(len(T))
	V_40MPA = npy.zeros(len(T))
	V_60MPA = npy.zeros(len(T))

	result = calculateTaitVolume(P0_22MPA[0],T,V_0,alpha,B0,B1)
	V_22MPA = result[0]
	result = calculateTaitVolume(P0_40MPA[0],T,V_0,alpha,B0,B1)
	V_40MPA = result[0]
	result = calculateTaitVolume(P0_60MPA[0],T,V_0,alpha,B0,B1)
	V_60MPA = result[0]

if isotherms:
	V0_378K = 1/npy.array(R0_378K)
	V0_383K = 1/npy.array(R0_383K)
	V0_388K = 1/npy.array(R0_388K)
	V0_393K = 1/npy.array(R0_393K)
	V0_398K = 1/npy.array(R0_398K)
	V0_403K = 1/npy.array(R0_403K)
	V0_408K = 1/npy.array(R0_408K)
	V0_413K = 1/npy.array(R0_413K)
	V0_418K = 1/npy.array(R0_418K)
	V0_423K = 1/npy.array(R0_423K)
	V0_428K = 1/npy.array(R0_428K)
	V0_433K = 1/npy.array(R0_433K)
	V0_438K = 1/npy.array(R0_438K)
	V0_443K = 1/npy.array(R0_443K)
	V0_448K = 1/npy.array(R0_448K)
	V0_453K = 1/npy.array(R0_453K)


	P = npy.linspace(Pmin,Pmax,num=10)


	result = calculateTaitVolume(P,T0_378K[0],V_0,alpha,B0,B1)
	V_378K = result[0]
	result = calculateTaitVolume(P,T0_383K[0],V_0,alpha,B0,B1)
	V_383K = result[0]
	result = calculateTaitVolume(P,T0_388K[0],V_0,alpha,B0,B1)
	V_388K = result[0]
	result = calculateTaitVolume(P,T0_393K[0],V_0,alpha,B0,B1)
	V_393K = result[0]
	result = calculateTaitVolume(P,T0_398K[0],V_0,alpha,B0,B1)
	V_398K = result[0]
	result = calculateTaitVolume(P,T0_403K[0],V_0,alpha,B0,B1)
	V_403K = result[0]
	result = calculateTaitVolume(P,T0_408K[0],V_0,alpha,B0,B1)
	V_408K = result[0]
	result = calculateTaitVolume(P,T0_413K[0],V_0,alpha,B0,B1)
	V_413K = result[0]
	result = calculateTaitVolume(P,T0_418K[0],V_0,alpha,B0,B1)
	V_418K = result[0]
	result = calculateTaitVolume(P,T0_423K[0],V_0,alpha,B0,B1)
	V_423K = result[0]
	result = calculateTaitVolume(P,T0_428K[0],V_0,alpha,B0,B1)
	V_428K = result[0]
	result = calculateTaitVolume(P,T0_433K[0],V_0,alpha,B0,B1)
	V_433K = result[0]
	result = calculateTaitVolume(P,T0_438K[0],V_0,alpha,B0,B1)
	V_438K = result[0]
	result = calculateTaitVolume(P,T0_443K[0],V_0,alpha,B0,B1)
	V_443K = result[0]
	result = calculateTaitVolume(P,T0_448K[0],V_0,alpha,B0,B1)
	V_448K = result[0]
	result = calculateTaitVolume(P,T0_453K[0],V_0,alpha,B0,B1)
	V_453K = result[0]

#Setting font size
axis_size = 20
title_size = 20
size = 10
label_size = 10
plt.rcParams['xtick.labelsize'] = label_size
plt.rcParams['ytick.labelsize'] = label_size

#Setting saved image properties
img_extension = '.png'
img_dpi = None
output_folder = 'plot_density'

#Checking for existence of output directory. If such a directory doesn't exist, one is created.
if not os.path.exists('./'+output_folder):
    os.makedirs('./'+output_folder)

#Defining linetype
line_style = ['-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':']
dot_style= ['ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk']

#General line properties.
linewidth = 2
markersize = 4

arrow_ls = 'dashdot'
show_arrows = True

#==================================================================================
#P versus R plots.
figPUREPMMA=plt.figure(num=None, figsize=(12, 10), dpi=img_dpi, facecolor='w', edgecolor='k')
ax = plt.axes()

if isobars:
	# plt.plot(T,V_22MPA,'r',lw=linewidth,ls='-',label='22MPA theory')
	# plt.plot(T,V_40MPA,'b',lw=linewidth,ls='-',label='40MPA theory')
	# plt.plot(T,V_60MPA,'g',lw=linewidth,ls='-',label='60MPA theory')

	# plt.plot(T0_22MPA,V0_22MPA,'^k',ms=markersize,label='22MPA experiment')
	# plt.plot(T0_40MPA,V0_40MPA,'sk',ms=markersize,label='40MPA experiment')
	# plt.plot(T0_60MPA,V0_60MPA,'sk',ms=markersize,label='60MPA experiment')

	plt.xlabel('Temperature T (K)',fontsize=axis_size)
	plt.ylabel(r'Specific Volume $v$ ($cm^3/g$)',fontsize=axis_size)
	# plt.axis([0.90*T_exp_min,1.15*T_exp_max,0.98*V_exp_min,1.02*V_exp_max])
	plt.legend(loc=4,fontsize=size,numpoints=1)

if isotherms:


	plt.plot(P,V_378K,'r',lw=linewidth,ls='-',label='378K theory')
	plt.plot(P,V_383K,'b',lw=linewidth,ls='-',label='383K theory')
	plt.plot(P,V_388K,'b',lw=linewidth,ls='-',label='388K theory')
	plt.plot(P,V_393K,'g',lw=linewidth,ls='-',label='393K theory')
	plt.plot(P,V_398K,'y',lw=linewidth,ls='-',label='398K theory')
	plt.plot(P,V_403K,'y',lw=linewidth,ls='-',label='403K theory')
	plt.plot(P,V_408K,'m',lw=linewidth,ls='-',label='408K theory')
	plt.plot(P,V_413K,'g',lw=linewidth,ls='-',label='413K theory')
	plt.plot(P,V_418K,'g',lw=linewidth,ls='-',label='418K theory')
	plt.plot(P,V_423K,'r',lw=linewidth,ls='-',label='423K theory')
	plt.plot(P,V_428K,'b',lw=linewidth,ls='-',label='428K theory')
	plt.plot(P,V_433K,'b',lw=linewidth,ls='-',label='433K theory')
	plt.plot(P,V_438K,'g',lw=linewidth,ls='-',label='438K theory')
	plt.plot(P,V_443K,'b',lw=linewidth,ls='-',label='443K theory')
	plt.plot(P,V_448K,'b',lw=linewidth,ls='-',label='448K theory')
	plt.plot(P,V_453K,'g',lw=linewidth,ls='-',label='453K theory')


	plt.plot(P0_378K,V0_378K,'^k',ms=markersize,label='378K experiment')
	plt.plot(P0_383K,V0_383K,'sk',ms=markersize,label='383K experiment')
	plt.plot(P0_388K,V0_388K,'sk',ms=markersize,label='388K experiment')
	plt.plot(P0_393K,V0_393K,'sk',ms=markersize,label='393K experiment')
	plt.plot(P0_398K,V0_398K,'sk',ms=markersize,label='398K experiment')
	plt.plot(P0_403K,V0_403K,'^k',ms=markersize,label='403K experiment')
	plt.plot(P0_408K,V0_408K,'^k',ms=markersize,label='408K experiment')
	plt.plot(P0_413K,V0_413K,'sk',ms=markersize,label='413K experiment')
	plt.plot(P0_418K,V0_418K,'sk',ms=markersize,label='418K experiment')
	plt.plot(P0_423K,V0_423K,'sk',ms=markersize,label='423K experiment')
	plt.plot(P0_428K,V0_428K,'^k',ms=markersize,label='428K experiment')
	plt.plot(P0_433K,V0_433K,'sk',ms=markersize,label='433K experiment')
	plt.plot(P0_438K,V0_438K,'sk',ms=markersize,label='438K experiment')
	plt.plot(P0_443K,V0_443K,'^k',ms=markersize,label='443K experiment')
	plt.plot(P0_448K,V0_448K,'sk',ms=markersize,label='448K experiment')
	plt.plot(P0_453K,V0_453K,'sk',ms=markersize,label='453K experiment')


	plt.xlabel('Pressure P (MPA)',fontsize=axis_size)
	plt.ylabel(r'Specific Volume $v$ ($cm^3/g$)',fontsize=axis_size)
	# plt.axis([0.90*T_exp_min,1.15*T_exp_max,0.98*V_exp_min,1.02*V_exp_max])
	plt.legend(loc=4,fontsize=size,numpoints=1)

# figPUREPMMA.savefig('./'+output_folder+r'\pure_PMMA_density'+img_extension,dpi=img_dpi)

plt.show()
