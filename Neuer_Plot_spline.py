#import packages

import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import Subplot
from run_simulation import *

#Import Solutions
datafile = open('solution.txt','r')
data = json.loads( datafile.read() )
datafile.close()

datanom.pop(0)

# change json datatype to dictionary
keys = [] #names of the variables
for i in range(0, len(data)):
	keys.append(data[i][0])
data_dic = {} #dict with all variables and values
for i in range(0, len(data)):
	temp_dic = {keys[i] : data[i][1] }
	data_dic.update(temp_dic)
    
solutionlist = np.ndarray.tolist(np.transpose(solution))
solnomlist = np.ndarray.tolist(np.transpose(solnom))
datanomlist = np.ndarray.tolist(np.transpose(datanom)) 

for i in range(0, solution.shape[1]):
   temp_dic = {'x' + str(i+1) + 'obs' : solutionlist[i] }
   data_dic.update(temp_dic)
   
for i in range(0, len(wtrue(time))):
   temp_dic = {'w' + str(i+1) + 'true' : wtrue(time)[i] }
   data_dic.update(temp_dic)

for i in range(0, solnom.shape[1]):
   temp_dic = {'x' + str(i+1) + 'nom' : solnomlist[i] }
   data_dic.update(temp_dic)
   keys.append('x' + str(i+1) + 'nom')
   
for i in range(0, len(datanom[0])):
   temp_dic = {'y' + str(i+1) + 'nom' : datanomlist[i] }
   data_dic.update(temp_dic)
   keys.append('y' + str(i+1) + 'nom')

xi = [] #Liste aller xi
for i in range(0, len(keys)):
    if (str('xi') + str(i) in keys):
        xi.append(str('xi') + str(i))

y = [] #Liste aller y
for i in range(0, len(keys)):
    if (str('y') + str(i) in keys):
        y.append(str('y') + str(i))

yobs = []
for i in range(1, len(y)+1):
    yobs.append(str('y') + str(i) + str('obs'))

x = [] #Liste aller w
for i in range(0, len(keys)):
    if (str('x') + str(i) in keys):
        x.append(str('x') + str(i))

xt = data_dic['time']
fig = plt.figure()
quad = np.ceil(np.sqrt(len(y))) #quadratischer Plot
for i in range(1,len(y)+1):
    ax = plt.subplot(quad,quad,i)
    ax.scatter(xt,data_dic['y' + str(i) + 'obs'],c='k',s=1.5)
    ax.errorbar(xt,data_dic['y' + str(i) + 'obs'],yerr = noisesd, marker = 'o',markersize=1,c='black',linestyle='none',ecolor='black',elinewidth = 1, capthick = 0.5, capsize = 1, label = 'y' + str(i) + 'obs')
    ax.plot(xt,data_dic['y' + str(i)],c='r',label = 'y' + str(i))
    ax.plot(xt,data_dic['y' + str(i) + 'nom'],c='b',label = 'y' + str(i) + 'nom')
    ax.legend()

fig.tight_layout()
pdfdirectory = 'plot_y.pdf'
pgfdirectory = 'plot_y.pgf'
fig.savefig(pdfdirectory)
plt.savefig(pgfdirectory)

fig2 = plt.figure()
quad = np.ceil(np.sqrt(len(x))) #solution beinhaltet die xobs
for i in range(1,len(x)+1):
    ax = plt.subplot(quad,quad,i)
    ax.scatter(xt,data_dic['x' + str(i) + 'obs'],c='k',label = 'x' + str(i) + 'obs',s = 1.5)
    ax.plot(xt,data_dic['x' + str(i)],c='r',label = 'x' + str(i))
    ax.plot(xt,data_dic['x' + str(i) + 'nom'],c='b',label = 'x' + str(i) + 'nom')
    ax.legend()

fig2.tight_layout()
pdfdirectory = 'plot_x.pdf'
pgfdirectory = 'plot_x.pgf'
fig2.savefig(pdfdirectory)
plt.savefig(pgfdirectory)

fig3 = plt.figure() #mit Abfrage, wann die jeweiligen xis 0 sind. wobs = xiobs
quad = np.ceil(np.sqrt(len(wtrue(time))))
for i in range(1,len(wtrue(time))+1):
    ax = plt.subplot(quad,quad,i)
    if isinstance(data_dic['w' + str(i) + 'true'],int) == False:
        ax.plot(xt,data_dic['w' + str(i) + 'true'],c='b',label = 'xi' + str(i) + 'true')
    else:
        ax.plot(xt,np.repeat(0,len(xt)),c='b',label = 'xi' + str(i) + 'true')
    if 'xi' + str(i) in xi:
        ax.plot(xt,data_dic['xi' + str(i)],c='r',label = 'xi' + str(i))
    else:
        ax.plot(xt,np.repeat(0,len(xt)),c='r',label = 'xi' + str(i))
    ax.legend()

fig3.tight_layout()
pdfdirectory = 'plot_xi.pdf'
pgfdirectory = 'plot_xi.pgf'
fig3.savefig(pdfdirectory)
plt.savefig(pgfdirectory)

#with open('data_dic.txt', 'w') as fp:
#    json.dump(data_dic, fp)

class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
            np.int16, np.int32, np.int64, np.uint8,
            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32, 
            np.float64)):
            return float(obj)
        elif isinstance(obj,(np.ndarray,)): #### This is the fix
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

dumped = json.dumps(data_dic, cls=NumpyEncoder)

with open('data_dic.txt', 'w') as f:
    json.dump(dumped, f)

import pandas as pd
data = pd.read_json(dumped)
data.to_csv('complete_solution.csv', sep = ',', encoding='utf-8')

#
#with different colors
#color=iter(plt.cm.rainbow(np.linspace(0,1,str(len(x)))))
#xt = data_dic['time']
#quad = np.ceil(np.sqrt(len(x)))
#for i in range(1,len(x)+1):
#    c=next(color)
#    ax = plt.subplot(quad,quad,i)
#    ax.plot(xt,data_dic['x' + str(i)],c=c)
#    ax.legend('x' + str(i))
    

#plotvar = w+y+x
#
#
## Start with one
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(xt,data_dic['x1'],color='k')
#
#for i in range(2, len(x)+1):
#    # Now later you get a new subplot; change the geometry of the existing
#    n = len(fig.axes)    
#    for j in range(n):
#        if i % 2 == 0:
#            fig.axes[j].change_geometry(n+1, n, j+1)
#            # Add the new
#            ax = fig.add_subplot(n+1, n, n+1)
#            ax.plot(xt,data_dic[str('x' + str(i) + '')])
#        else:
#            fig.axes[j].change_geometry(n, n+1, j+1)
#            # Add the new
#            ax = fig.add_subplot(n, n+1, n+1)
#            ax.plot(xt,data_dic[str('x' + str(i) + '')])
#    
#plt.show()zz
#
#fig2 = plt.figure()
#ax = fig2.add_subplot(111)
#ax.plot(xt,data_dic['x1'],color='k')
