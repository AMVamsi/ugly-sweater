import streamlit as st 

# st.set_page_config(page_title="Sweater Personality",
#                    page_icon="🎄")

from PIL import Image
import re 
import color_generator as c 
import joblib
import cohere
import os
from dotenv import load_dotenv
load_dotenv()


st.markdown('<h1 style="color:rgb(255,75,75);">Huggszzy</h1>', unsafe_allow_html=True)
header = Image.open("images/header.png")
image = st.image(header)

personality = {
    'ISTJ' : 'The Inspector- reserved and practical, they tend to be loyal, orderly, and traditional.', 
    'ISTP' : 'The Crafter- highly independent, they enjoy new experiences that provide first-hand learning.', 
    'ISFJ' : 'The Protector- Warm-hearted and dedicated, they are always ready to protect the people they care about.', 
    'ISFP' : 'The Artist- Easy-going and flexible, they tend to be reserved and artistic.', 
    'INFJ' : 'The Advocate- Creative and analytical, they are considered one of the rarest Myers-Briggs types.', 
    'INFP' : 'The Medicator- Idealistic with high values, they strive to make the world a better place.', 
    'INTJ' : 'The Architect- High logical, they are both very creative and analytical', 
    'INTP' : 'The Thinker- Quiet and introverted, they are known for having a rich inner world.', 
    'ESTP' : 'The Persuader- out-going and dramatic, they enjoy spending time with others and focusing on the here-and-now.', 
    'ESTJ' : 'The Director- Assertive and rule-oriented, they have principles and a tendency to take charge.', 
    'ESFP' : 'The Performer- Outgoing and spontaneous, they enjoy taking center stage.', 
    'ESFJ' : 'The Caregiver- Soft-hearted and outgoing, they tend to believe the best about other people.', 
    'ENFP' : 'The Champion- Charismatic and energetic, they enjoy situations where they can put their creativity to work.', 
    'ENFJ' : 'The Giver- Loyal and sensitive, they are known for being understanding and generous.', 
    'ENTP' : 'The Debater- Highly inventive, they love being surrounded by ideas and tend to start many projects (but may struggle to finish them).',
    'ENTJ' : 'The Commander- Outspoken and confident, they are great at making plans and organizing projects.'
}
personality_list=['ISTJ', 'ISTP', 'ISFJ','ISFP','INFJ','INFP','INTJ','INTP','ESTP','ESTJ','ESFP','ESFJ','ENFP','ENFJ', 
    'ENTP','ENTJ' ]


def questions(): 
    st.subheader("Create Your Christmas Sweater")
    st.markdown("<b>How would you describe yourself?</b>",
              unsafe_allow_html=True)

def body():
    input = st.text_input("Enter or paste any text that best describes you",
                        key="input")
    #Check if input is a string 
    if isinstance(input, str): 
        if  re.findall(r'(https?://\S+)',input): 
          st.warning("Please enter text only!")
    return input
        
def personalityType(input): 
    if input:   
        st.write(input)
        st.success("You are about to find your personality")
        expander = st.expander("Click here")
        model_result= model_result_type(input) #change this 
        expander.write(personality[model_result]) #change to model_result_type 

def generateSweater(): 
    if st.button("Generate My Sweater"): 
        img_file = c.urls[random.choice([0,1])]
        st.image(img_file) 
        st.snow()

def model_result_type(input):
    if(input):
        
        api_key = os.environ.get('cohere_api')

        # Create and retrieve a Cohere API key from os.cohere.ai
        co = cohere.Client(api_key)
        filename = "trained_model.pkl"
        loaded_model = joblib.load(filename)
        response = co.embed(input.split())

        type = loaded_model.predict(response.embeddings)

        return personality_list[type[0]]
    else:
        return ""
    

def main(): 
    questions()
    input = body()
    personalityType(input)
    generateSweater()

if __name__ == "__main__":
  main()
