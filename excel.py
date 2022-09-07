import pandas as pd
import pymongo
myclent = pymongo.MongoClient("mongodb+srv://shahab:arkan@cluster0.vgwfj5h.mongodb.net/?retryWrites=true&w=majority")
mydb = myclent["platin"]
mycol = mydb["user"]

mydoc = mycol.find({}).limit(500)
xx = []
for x in mydoc:
    xx.append(x['name'])



list1 = xx
list2 = xx
col1 = "names"
col2 = "Y"
data = pd.DataFrame({col1:list1,col2:list2})
data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)