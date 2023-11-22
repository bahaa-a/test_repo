from openai import OpenAI
import streamlit as st



def generate_image(prompt, key):
  
  client = OpenAI(api_key = key)

  response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

  image_url = response.data[0].url
  return image_url



with st.form("Generate_Image_Form"):
  api_key = st.text_input(label='API KEY')
  image_prompt = st.text_input(label="PROMPT")
  form_submit = st.form_submit_button("Generate Image")

if form_submit:
  image_url = generate_image(prompt=image_prompt, key=api_key)
  st.write(image_url)



