import requests
from bs4 import BeautifulSoup
import pandas as pd

product_name=[]
description=[]
Review=[]

for i in range(1,5):
    url="https://www.flipkart.com/6bo/b5g/~cs-vyc2x9xrdg/pr?sid=6bo%2Cb5g&collection-tab-name=Core+i5+Laptops&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkNvcmUgaTUgTGFwdG9wcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=3.productCard.PMU_V2_3&page="+str(i)
    r=requests.get(url)
    #`print(r)

    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")

    names=box.find_all("div",class_="_4rR01T")
    #print(name)

    for i in names:
        name=i.text
        product_name.append(name)
    #print(product_name)

    desc=box.find_all("div",class_="fMghEO")

    for i in desc:
        d=i.text
        description.append(d)
    #print(description)

    reviews=box.find_all("div",class_="_3LWZlK")

    for i in reviews:
        r=i.text
        Review.append(r)
    #print(Review)

df=pd.DataFrame({"Product Name":product_name,"Description":description,"Review":Review})
print(df)

df.to_csv("Flipkart_multiple_pages_webscrapping.csv")