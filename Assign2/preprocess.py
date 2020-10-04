from ttp import ttp
import pprint
import pandas as pd
data = open('./samples.csv', 'r').read()

template="""{{station}};{{date}};{{time}};{{Depth}};{{ParameterCode}};{{AnalysisMethodCode}};;{{Value}};{{Unit}};{{quality}}"""

parser = ttp(data, template)
parser.parse()
lis = parser.result()[0][0]
lis=sorted(lis, key=lambda k: k['station']+k['date']+k['ParameterCode'])

before = None
new_dic = {}
new_lis = []
for i in range(len(lis)):
    dic = lis[i]
    if dic["station"]+dic["date"]==before:
        new_dic[dic['ParameterCode']] = dic['Value']
    else:
        new_lis.append(new_dic)
        new_dic={}
        before = dic["station"]+dic["date"]
        new_dic["Station"] = dic["station"]
        new_dic["Sample Date"] = dic["date"]
        new_dic["Sample Time"] = dic["time"]
        new_dic[dic['ParameterCode']] = dic['Value']
new_lis = new_lis[1:]
col = ['Station', 'Sample Date', 'Sample Time', 'TEMP', 'Cl-Dis', 'TDS', 'pH',
       'O2-Dis', 'COD', 'EC', 'BOD', 'TURB', 'Alk-Tot', 'H-T', 'Ca-Dis']
# pd.DataFrame(new_lis)[col]
new_pd=pd.DataFrame(new_lis)[col]
for name in col[3:]:
    new_pd[name]=new_pd[name].astype(float)
new_pd.to_csv("Tarcleaned_samples.csv")
print(new_pd.shape)