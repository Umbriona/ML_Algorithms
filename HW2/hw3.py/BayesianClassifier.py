from urllib import request
import numpy as np

url_data = "http://www.cse.chalmers.se/research/lab/mlcourse/dataset2.txt"
def GetData(url_data):
    response = request.urlopen(url_data)
    data = response.read()
    data_str = str(data)
    data_str = data_str.replace("b'", '')
    print(data_str)
    data_list=data_str.split(r'\r\n')

    for item in data_list:
        print(item)

GetData(url_data)