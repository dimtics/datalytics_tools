# -*- coding: utf-8 -*-
"""
@author: Oladimeji Salau

Purpose: A python code to download data from a given url into a specified destination directory. The downloaded data will be decompressed if it is zipped from the source. 
The script can be run more than once without fear of data being over-written.

How to use it
==============
* Specify the url from which data is to be downloaded as FILE_URL.
* Specify the destination directory as TARGETDIR.
* Run the script.

Requirements
============
Ensure relevant python modules as noted below are installed on your system.

"""

import os
import requests
import tarfile
import zipfile


FILE_URL = "https://xxxx/yyyy/data.tgz" 
TARGETDIR = '/Users/xxxx/yyyy/zzzz/target' # target folder to save the downloaded data 

def fetch_data(url=FILE_URL, dest=TARGETDIR):
    '''script to download small or large data file from a given url'''
    try:       
        if not os.path.isdir(dest):
            #if there is no such folder already, create one and download the file in there...
            os.makedirs(dest)
            filext = url.split('/')[-1]
            target_file = os.path.join(dest, filext)
            r = requests.get(url, stream=True)
            with open(target_file, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024): 
                    if chunk: 
                        f.write(chunk)
            
            for i in os.listdir(dest):    
                k = os.path.join(dest, i)
                
                #extract the file if it is zipped with tgz, gzip, bz2 and lzma compression
                if tarfile.is_tarfile(k):
                    compfile = tarfile.open(k)
                    compfile.extractall(path=dest)
                    compfile.close()
                    
                #extract the file if it is zipped with zip compression
                if zipfile.is_zipfile(k):
                    with zipfile.ZipFile(k,"r") as compfile:
                        compfile.extractall(path=dest)
                      
        else:
            #if the data is already downloaded, do nothing...
            if len(os.listdir(dest)):
                pass
    
    #capture and print error
    except Exception as err: 
        print(err)
          
