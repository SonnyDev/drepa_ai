# DrepaAI: The AI Companion for Sickle Cell Disease Patients and Doctors

## Overview

DrepaAI is an AI-driven companion designed to provide critical information and support to Sickle Cell Disease (SCD) patients and healthcare providers, particularly in low-resource settings. Utilizing advanced AI models and cloud infrastructure, DrepaAI offers a conversational interface, educational resources, and a symptom checker to bridge the information gap in SCD management.

## Inspiration

Sickle Cell Disease is the most common genetic disorder worldwide, affecting millions, especially in low-income countries. Many patients and doctors in these regions lack access to the information they need to manage the disease effectively. This project was inspired by the need to address this gap and improve healthcare outcomes for SCD patients globally.

## Features

- **Chatbot Functionality**: A conversational interface to answer questions about SCD, symptoms, treatments, and management strategies.


## Technology Stack

- **AI Model**: Mistral Model
- **Cloud Platform**: Groq Cloud for inference
- **User Interface**: Streamlit

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/SonnyDev/drepa_ai.git
    cd DrepaAI
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit Application**
    ```bash
    streamlit run main.py
    ```
You should have a .env file with a GROQ_API_KEY environment variable containing your GROP API KEY


## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please feel free to contact us at [sonnymupfuni01@gmail.com](mailto:sonnymupfuni01@gmail.com).
