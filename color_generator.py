import requests
import pandas as pd
import random
import os
import openai
import main as m 

openai.api_key = os.environ.get('openai_api')
openai.Model.list()

input_text = m.body("inputU2")

inputPersonalityType = m.model_result_type(input_text)

df = pd.read_csv("PersonalityColorHex.csv")
listPersonalities = []
for i in df['Personality']: #Creating a list for personality-type headers
    listPersonalities.append(i)

def personalityText(inputPersonalityType): #Using this function to get text.
    if(inputPersonalityType):
        text = ""
        index = listPersonalities.index(inputPersonalityType)
        result = df.loc[index]
        listSen = []
        for i in result:
            listSen.append(i)
        text = "Colors in pattern "  + listSen[random.choice([1,3,5])] + " with " + listSen[7] + " and " +listSen[random.randint(8,9)] + " with " + listSen[10] + "."
        return text
    else:
        return ""


prompt_ = "Sweater with "+ personalityText(inputPersonalityType)

objectImage = openai.Image.create(
  prompt=prompt_,
  n=2,
  size="1024x1024"
)

urls=[]
for items in objectImage["data"]:
    urls.append(items["url"])

