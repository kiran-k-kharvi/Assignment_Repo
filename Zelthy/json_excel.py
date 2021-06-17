import requests
import pandas
x =requests.get("https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog")
res = pandas.DataFrame(x.json())
res.to_excel("my_exl.xlsx",index=False)