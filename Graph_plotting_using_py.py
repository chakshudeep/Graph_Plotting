import numpy as np
from matplotlib import pyplot as plt

def check_zero(x):
    if(x<=0):
        return False
    else:
        return True

def simple_plot():
    
    plt.style.use('ggplot')
    title_name=str(input('Enter the title of Graph:'))
    
    x=[]
    m=int(input('Enter the number of lines(greater than 0):'))
    if(check_zero(m)==0):
        print('ERROR, TRY AGAIN!!!')
        return
    
    n=int(input('Enter the number of points(greater than 0):'))
    if(check_zero(n)==0):
        print('ERROR, TRY AGAIN!!!')
        return

    x_label=str(input('Enter label for X-axis:'))
    y_label=str(input('Enter label for y-axis:'))


    print('Enter the elements on x-axis:')
    for i in range(0,n):
        x_ele=float(input('x-axis:'))
        x.append(x_ele)

    for i in range(1,m+1):
        y=[]
        label_name=str(input('Enter the label name for line-'+str(i)+':'))

        print('Enter the elements of y-axis for line-'+str(i)+':')
        for j in range(0,n):
            y_ele=float(input('y-axis:'))
            y.append(y_ele)
        plt.plot(x,y, label=label_name,marker='.')

    plt.title(title_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()

def bar_chart():

    plt.style.use('fivethirtyeight')
    title_name=str(input('Enter the title of Bar Graph:'))

    x=[]

    m=int(input('Enter the number of Bar data i.e. type of bars(greater than 0):'))
    if(check_zero(m)==0):
        print('ERROR, TRY AGAIN!!!')
        return

    n=int(input('Enter the number of points(greater than 0):'))
    if(check_zero(n)==0):
        print('ERROR, TRY AGAIN!!!')
        return

    x_label=str(input('Enter label for X-axis:'))
    y_label=str(input('Enter label for y-axis:'))

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    print('Enter the elements on x-axis:')
    for i in range(0,n):
        x_ele=str(input('x-axis:'))
        x.append(x_ele)

    width=0.25
    x_indexes=np.arange(len(x))

    for i in range(1,m+1):
        y=[]
        label_name=str(input('Enter the label name for bar type-'+str(i)+':'))

        print('Enter the elements of y-axis for line-'+str(i)+':')
        for j in range(0,n):
            y_ele=float(input('y-axis:'))
            y.append(y_ele)

        bar1=x_indexes+((i-(m-1))*width)
        plt.bar(bar1,y,width=width,label=label_name)

    plt.xticks(ticks=x_indexes,labels=x)
    plt.legend()
    plt.title(title_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()
    plt.show()

def histogram():
    
    plt.style.use('seaborn')

    data=[]
    bin_=[]
    title=str(input('Enter the title of Histogram:'))
    m=int(input('Enter the number of elements in the data(greater than 0):'))

    if(check_zero(m)==0):
        print('ERROR, TRY AGAIN!!!')
        return

    x_label=str(input('Enter the label for X-axis:'))
    y_label=str(input('Enter the label for Y-axis:'))
    label_=str(input('Enter the label to be put in legend:'))

    bin_start=int(input('Enter the starting bin value:'))
    bin_interval=int(input('Enter the bin interval:'))
    

    for i in range(0,m):
        ele=int(input('Enter the element-'+str(i+1)+':'))
        data.append(ele)
        bin_.append(bin_start)
        bin_start=bin_start+bin_interval
    
    plt.hist(data,bins=bin_,edgecolor='black',color='#fc4f30',label=label_)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.tight_layout()
    plt.show()

def pie_charts():
    plt.style.use('fivethirtyeight')
    pie=[]
    label_name=[]
    explode=[]
    title_name=str(input('Enter the title of the Pie Chart:'))
    
    m=int(input('Enter the number of elements(greater than 0):'))

    if(check_zero(m)==0):
        print('ERROR, TRY AGAIN!!!')
        return
    
    for i in range(0,m):
        pie_label=str(input('Enter the label for element-'+str(i+1)+':'))
        pie_val=int(input('Enter the value of  element-'+str(i+1)+':'))
        pie.append(pie_val)
        label_name.append(pie_label)
        explode.append(0)
    
    explode[i]=0.2
    
    plt.pie(pie,labels=label_name,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',
    wedgeprops={'edgecolor':'black'})

    plt.title(title_name)
    plt.tight_layout()
    plt.show()

def scatter_plot():
    plt.style.use('ggplot')
    x=[]
    title=str(input('Enter the title of the scatter plot:'))
    m=int(input('Enter the number of scatter plot(greater than 0):'))
    if(check_zero(m)==0):
        print('ERROR, TRY AGAIN!!!')
        return

    n=int(input('Enter the number of points(greater than 0):'))
    if(check_zero(n)==0):
        print('ERROR, TRY AGAIN!!!')
        return

    x_label=str(input('Enter label for X-axis:'))
    y_label=str(input('Enter label for y-axis:'))

    print('Enter the elements on x-axis:')
    for i in range(0,n):
        x_ele=float(input('x-axis:'))
        x.append(x_ele)

    for i in range(1,m+1):
        y=[]
        label_name=str(input('Enter the label name for scatter plot data-'+str(i)+':'))

        print('Enter the elements of y-axis for scatter plot data-'+str(i)+':')
        for j in range(0,n):
            y_ele=float(input('y-axis:'))
            y.append(y_ele)
        plt.scatter(x, y,s=100,edgecolors='black',alpha=0.75,linewidths=1,label=label_name)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()


# MAIN FUNCTION 
print("""*****************************************************************************
    Hello User! , Welcome to our Graph Plotting Application.
    Now,Choose the options from the 'Menu' according to graph you want to plot
    **********************************************************************************
    ^^^^^^^^^^^^^^^^^^MENU^^^^^^^^^^^^^^^^^^
    1->SIMPLE LINE GRAPH
    2->BAR GRAPH
    3->PIE CHART
    4->HISTOGRAM
    5->SCATTER PLOT
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")

choice=int(input('Enter your choice:'))

if(choice==1):
    simple_plot()
elif(choice==2):
    bar_chart()
elif(choice==3):
    pie_charts()
elif(choice==4):
    histogram()
elif(choice==5):
    scatter_plot()

print("******THANK YOU FOR USING OUR SERVICE******")