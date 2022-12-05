import requests
import pandas as pd
import random
import os
import openai
import main as m 
#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 - testKey
#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 - mainKey

openai.api_key = "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"
openai.Model.list()

inputPersonalityType = m.model_result_type()

df = pd.read_csv("PersonalityColorHex.csv")
listPersonalities = []
for i in df['Personality']: #Creating a list for personality-type headers
    listPersonalities.append(i)

def personalityText(inputPersonalityType): #Using this function to get text.
    text = ""
    index = listPersonalities.index(inputPersonalityType)
    result = df.loc[index]
    listSen = []
    for i in result:
        listSen.append(i)
    text = "Colors in pattern "  + listSen[random.choice([1,3,5])] + " with " + listSen[7] + " and " +listSen[random.randint(8,9)] + " with " + listSen[10] + "."
    return text


prompt_ = "Sweater with "+ personalityText(inputPersonalityType)
print(prompt_)
imageURL = openai.Image.create(
  prompt=prompt_,
  n=2,
  size="1024x1024"
)


