#import pandas as pd 
"""data = pd.read_csv("C:\Users\Sunsh\Downloads\load_data_peak6.csv") 
                   #Preview the first 5 lines of the loaded data """
#data.head()

import csv

#data = open(r"C:/Users/Sunsh/Downloads/load_data_peak6.csv")
#data = csv.reader(data)  
#print(data)


 # white = pd.read_csv(r"C:\\Users\\Sunsh\ßDownloads\\load_data_peak6.csv", encoding="utf-8")
  #print(white)
  
  #g = codecs.open("r"C:\Users\Sunsh\ßDownloads\load_data_peak6.csv", "r", encoding="utf-8")
                 # print (g)
                  
                  
#self.path = r'C:/Users/Sunsh/Downloads/load_data_peak6.csv'
a = csv.reader(open(r'C:\Users\Sunsh\Downloads\load_data_peak6.csv', newline='', encoding='utf-8'))
print (a)

import pandas
df = pandas.read_csv(r'C:\Users\Sunsh\Downloads\load_data_peak6.csv')
print(df)



