# GENERATIVE-TEXT-MODEL

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: ANSHU VEERAMALLA

**INTERN ID**: CODF269

**DOMAIN**: AIML(ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE)

**DURATION**: 1 MONTH

**MENTOR**: NEELA SANTOSH

## DESCRIPTION

# Text Generation with GPT-2

This project implements a **Text Generation App** built using **Streamlit** and **OpenAI's GPT-2 model**. The app allows users to input prompts from predefined questions, and it generates informative and coherent paragraphs based on the selected prompt. It leverages the power of **transformer-based models** for **Natural Language Processing (NLP)** to generate text that mimics human-like writing.

### **Overview**

The core functionality of the app revolves around using **GPT-2** (a powerful language model developed by OpenAI) to generate text based on an input prompt. The app is built using **Streamlit**, which provides a simple and interactive interface for users to input a question, and get a generated response. The GPT-2 model is pre-trained on a large dataset and is capable of generating coherent and contextually relevant text, making it a perfect choice for text generation tasks.

### **Key Features**

- **Predefined Questions**: The app includes a set of predefined questions on topics like **Artificial Intelligence**, **Machine Learning**, **Natural Language Processing**, and **Deep Learning**. Users can select a question to generate a detailed response.
  
- **Text Generation with GPT-2**: The app uses the **GPT-2** model, a transformer-based architecture, to generate text based on the input prompt. This model has been fine-tuned to produce high-quality text with a variety of parameters to control the creativity and coherence of the output.

- **Adjustable Parameters**: The text generation parameters, such as **temperature**, **top-p**, **top-k**, and **max length**, are configured to optimize text quality and creativity. Users can experiment with these settings to fine-tune the output as needed.

- **Streamlit Interface**: Built with **Streamlit**, the app provides a user-friendly interface that is easy to use and doesn't require any programming knowledge. Users simply select a question from the dropdown menu, click a button to generate the text, and see the result instantly.

### **How It Works**

1. **Model Loading**: The app loads the **GPT-2** model and its tokenizer from the Hugging Face **Transformers** library. The model is set to evaluation mode to prevent unnecessary training updates.

2. **Text Generation**: Once the user selects a question and clicks the **Generate Text** button, the app encodes the input prompt using the **GPT-2 tokenizer** and generates text using the **GPT-2 model**. The text is then decoded back into readable format.

3. **Output Display**: The generated text is displayed below the button in the Streamlit interface, where users can read and analyze the response. The app is designed to generate text with coherence and relevance to the selected prompt.

4. **Settings**: The text generation is controlled by several parameters:
   - **Max Length**: The maximum length of the generated text.
   - **Temperature**: Controls the randomness of the generation. A higher temperature increases randomness.
   - **Top-p (nucleus sampling)** and **Top-k sampling**: These methods control the diversity and quality of the generated text.

### **Technologies Used**

- **Streamlit**: A Python framework for building interactive web applications with minimal code.
- **Hugging Face Transformers**: The library that provides access to pre-trained transformer models, including **GPT-2**.
- **GPT-2**: A large-scale language model developed by OpenAI for natural language generation tasks.
- **PyTorch**: The deep learning framework used to run the GPT-2 model.
- **Python**: The programming language used to develop the app and integrate the GPT-2 model.

### **How to Run the Application**

#### **1. Install Required Libraries**

Before running the app, ensure you have the required libraries installed. Run the following command:

```bash
pip install streamlit transformers torch
```

This will install **Streamlit**, **Transformers** from Hugging Face, and **PyTorch** for running the GPT-2 model.

#### **2. Download or Clone the Repository**

Clone the repository or download the project files to your local machine.

#### **3. Run the Streamlit App**

Once you've installed the dependencies and have the project files, run the following command to start the app:

```bash
streamlit run generative_text.py
```

This command will launch the app in your default web browser.

#### **4. Use the Application**

- **Select a question** from the dropdown list.
- **Click "Generate Text"** to see the model's response to the selected question.
- The generated text will be displayed below, and you can analyze it for relevance and coherence.

### **Conclusion**

The **Text Generation App** is a simple yet powerful tool that demonstrates the capabilities of **GPT-2** for **natural language generation** tasks. Built with **Streamlit**, it offers an intuitive interface to interact with the model and explore text generation in real-time. Whether you're exploring AI-related topics or simply curious about language models, this app provides an engaging experience.

## OUTPUT

