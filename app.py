import streamlit as st 
from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("./personnelportfolio")
tokenizer = T5Tokenizer.from_pretrained("./personnelportfolio")

st.title("Personnel portfolio chatbot app in pytorch")
st.write("This is a simple app that tells about me.")
st.write("You have to ask him a question about me and it will reply")
text_input = st.text_input("Enter a prompt:", placeholder="Age,Hobby,Experience etc")
submit_button = st.button("Generate")

messages = []

if submit_button:
    inputs = tokenizer.encode(text_input, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, num_beams=5, early_stopping=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.write("Generated prompt:")
    st.write(response)
