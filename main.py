import streamlit as st 
from PIL import Image
import re 
import color_generator as c 
import joblib as jb
import cohere

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

st.set_page_config(page_title="Sweater Personality",
                   page_icon="🎄")
st.markdown('<h1 style="color:rgb(255,75,75);">Huggszzy</h1>', unsafe_allow_html=True)
header = Image.open("images/header.png")
image = st.image(header)

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
        model_result= personality_list[model_result_type(input)] #change this 
        expander.write(personality[model_result]) #change to model_result_type 

def generateSweater(): 
    if st.button("Generate My Sweater"): 
        img_file = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-oEWvZa5qHHviMa2ac3EVFclF/user-cNFvk4UTWEilNBYeXNMgPukP/img-as7m9Xm0Pu93ztwQ8lx84l3g.png?st=2022-12-04T17%3A13%3A19Z&se=2022-12-04T19%3A13%3A19Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-04T12%3A05%3A13Z&ske=2022-12-05T12%3A05%3A13Z&sks=b&skv=2021-08-06&sig=4LRaQTt%2BocOE8RvtWkky6imrP%2BrgrGliMXItI0B3O78%3D"
        st.image(img_file) 
        st.snow()

def model_result_type(input):
    # ADD YOUR API KEY HERE
    api_key = "7mHjN9V4dW4djta6LdGoXFXlpMwScsIuPdYK6URf"

    # Create and retrieve a Cohere API key from os.cohere.ai
    co = cohere.Client(api_key)
    filename = "Completed_model.joblib"
    loaded_model = jb.load(filename)
    response = co.embed(input)
    type = loaded_model.predict(response.embeddings)
    return type
    

def main(): 
    questions()
    input = body()
    personalityType(input)
    generateSweater()
    model_result_type(input)

if __name__ == "__main__":
  main()