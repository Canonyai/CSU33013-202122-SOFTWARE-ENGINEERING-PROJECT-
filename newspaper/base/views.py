from django.shortcuts import render
# Create your views here.
import pandas as pd
import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.Headlines

hG = pd.DataFrame(db.general.find())

general=[]
count=1
for (i,j) in zip(hG.title,hG.urlToImage):
    general=general+[
    {"id":count,"name":i,"image":j},
    ]
    count=count+1

hG = pd.DataFrame(db.entertainment.find())

Entertainment=[]
count=1
for (i,j) in zip(hG.title,hG.urlToImage):
    Entertainment=Entertainment+[
    {"id":count,"name":i,"image":j},
    ]
    
    count=count+1


hG = pd.DataFrame(db.business.find())

business=[]
count=1
for (i,j) in zip(hG.title,hG.urlToImage):
    business=business+[
    {"id":count,"name":i,"image":j},
    ]
    
    count=count+1



hG = pd.DataFrame(db.health.find())
health=[]
count=1
for (i,j) in zip(hG.title,hG.urlToImage):
    health=health+[
    {"id":count,"name":i,"image":j},
    ]
    
    count=count+1

hG = pd.DataFrame(db.science.find())
science=[]
count=1
for (i,j) in zip(hG.title,hG.urlToImage):
    science=science+[
    {"id":count,"name":i,"image":j},
    ]
    
    count=count+1


hG = pd.DataFrame(db.sports.find())
sports=[]
count=1
for (i,j) in zip(hG.title,hG.urlToImage):
    sports=sports+[
    {"id":count,"name":i,"image":j},
    ]
    
    count=count+1


hG = pd.DataFrame(db.technology.find())
technology=[]
count=1
for (i,j) in zip(hG.title,hG.urlToImage):
    technology=technology+[
    {"id":count,"name":i,"image":j},
    ]
    
    count=count+1


def home(request):
    return render(request,'home.html',{'general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})
def summarize(request,pk):
    return render(request,'summarize.html')
