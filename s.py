import os
import requests
import pandas as pd


token = os.getenv("api_key")
if token == "1234":
    response=requests.get("https://jsonplaceholder.typicode.com/comments")
    data=response.json()
    print(data)
    df=pd.DataFrame(data)
    print(df[["id","email"]])

else:
    print("You do not have the correct token.")
    print(token)