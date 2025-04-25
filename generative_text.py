import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model.eval()

# Text generation function
def generate_text(prompt, max_length=200):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=max_length,
            temperature=0.7,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            top_p=0.95,
            top_k=60,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit app
def main():
    st.markdown("<h1 style='text-align: center; color: #3366cc;'>CodTech Internship-Text Generator</h1>", unsafe_allow_html=True)
    st.write("Select a question below to generate a paragraph based on your prompt.")

    questions = [
        "What is AI?",
        "What is NLP?",
        "What is Machine Learning?",
        "What is Deep Learning?"
    ]

    selected_question = st.selectbox("Choose a question:", questions)

    if st.button("Generate Text"):
        generated = generate_text(selected_question)
        st.subheader("Generated Text:")
        st.write(generated)

if __name__ == "__main__":
    main()
