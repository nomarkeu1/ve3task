from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import os
import time

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pprint



def index(request):
    form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        print(os.getcwd())
            
        
        print(uploaded_file_url)
        
        #time.sleep(1)

        df = pd.read_csv('media/data_P3Ed9OP.csv')

        df= df.dropna(axis=0, how='any') #drop rows containing NA values

        with open('out.txt', 'w') as f:
            #print('Filename:', filename, file=f) 

            #print(df.head(3),'\n',stream=out) 
            pprint.pprint(df.head(3),stream=f) 
            print("\n",file=f)
    
            titles = list(df.columns.values)
            for title in titles:
                mean=df[title].mean()
                median=df[title].median()
                standard_deviation=df[title].std()
                print(title+': Mean Value -  '+str(mean),', Median -  '+str(median),', SD -  '+str(standard_deviation),file=f)

        labels = ['Duration', 'Pulse', 'Maxpulse','Calories']
        #ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
        plt.hist(df, label=labels)
        plt.legend()
        #plt.show()
        plt.savefig('task/static/histogram.png')
        
        #read out.txt file
        file1 = open(r'out.txt',"r+",encoding='UTF-8')
        d = file1.read()
        print(d) #prints on cmd in the same formatting as in text file

        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url, 'dat':d
        })

        
    form = UploadFileForm()
    return render(request, "upload.html", {"form": form})

