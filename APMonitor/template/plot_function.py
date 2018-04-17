# import packages
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import Subplot

hfont = {'fontname':'Helvetica'}


# simple plot function
def plot2d(data, variables ,filename):

    # default vales
    logscale_x = False
    logscale_y = False
    logable = True
    
    grid_bool = False
    
    axistop_bool = False
    axisright_bool = False
    axisbottom_bool = True
    axisleft_bool = True
    
    legend_outside = True
    
    colors = {}
    for i in range(0,len(variables)):
        colors[variables[i]] = ['w','b','g','r','c','m','y','k'][i]
    # intern parameters
    plot_range = 1./8  # means of two data series differ by this factor, 
                        # the scalng is defined ill
    
    # prepare data --->
   
    # check for appropriate format of input
    if (isinstance( variables, list)):
        for i in variables:
            if (not isinstance(i,str)):
                print('second argument must be a list of str')
                return None
    else: 
        print('second argument must be a list')
                
    if (not isinstance(filename, str)):
        print('third argument must be of type str')
        return None
    if (not isinstance(data, list)): 
        print('first argument must be of type list')
        return None
    for j in data[0]:
        if (not isinstance(j,float) and not isinstance(j,int) ):
            print('data must be passed as a list of int or float')
            return None
    for i in data[1:]:
        for j in i:
            if (not isinstance(j,float) and not isinstance(j,int) ):
                print('data must be passed as list of int or float')
                return None
            elif j <= 0 and logable:
                print('logscale impossible')
                logable = False # to avoid using logscale
                

    
    #get number of rows and colums of data
    ncols = len(data)
    nrows = len(data[0])
    
    
    #check wether all rows have the same size and create df
    df = {} # initialize empty dictionary similar to dataframe
    for i in range(0,ncols):
        if not len(data[i]) == nrows:
            print('missing values in data set')
            return None
        else:
            df[ variables[i] ] = data[i]
    
    # <--- prepare data
    
    # ---> analyse data
    
    # get lower and upper bounds of each variable
    bounds = {}
 
    for i in variables:
        [bounds['lower',i] , bounds['upper',i] ] = [min(df[i]) , max(df[i])]
    
    # check whether magnitudes are approximately equal and use logscale if not
    means = [0] * (ncols-1)
    for i in range(1,ncols): # compute means of the columns
        means[i-1] = np.mean( df[ variables[i] ] )
    if min(means)/max(means) < plot_range and logable:  # if variables have different magnitudes set 
        print('ill scaling - use logscale')             # logscale
        logscale_y = True
	
    for i in range(1,ncols): # if one variable changes magnitude drastically set logscale
        if ( (max(df[variables[i]])-min(df[variables[i]])) != 0 ):
            temp = means[i-1]/(max(df[variables[i]])-min(df[variables[i]]))
            if temp < plot_range and logable and not logscale_y:
                print('very ill scaling - use logscale')
                logscale_y = True 
    
    # <--- analyse data
    

    # plot --->
    fig = plt.figure(1)
    ax = Subplot(fig,111)
    fig.add_subplot(ax)
    
    for i in variables[1:]:
        ax.scatter( df[variables[0]] , df[i] , label = '$' + i + '$' ,
                   color = colors[i])
    # font
    
    # labels and legend
    ax.legend(loc = 'best')
    plt.xlabel(variables[0], **hfont)
    if legend_outside:
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # logscale
    if logscale_y:
        plt.yscale('log')
    if logscale_x:
        plt.xscale('log')
    # grid
    plt.grid(grid_bool)

    # visible axis
    ax.axis["right"].set_visible(axisright_bool)
    ax.axis["top"].set_visible(axistop_bool)
    ax.axis["bottom"].set_visible(axisbottom_bool)
    ax.axis["left"].set_visible(axisleft_bool)
    
    # <--- plot
    
    # save plot --->
    pdfdirectory = filename + '.pdf'
    pgfdirectory = filename + '.pgf'
    fig.savefig(pdfdirectory)
    plt.savefig(pgfdirectory)
    # <--- save plot 
    
    
    print('run successful')
    return None    
