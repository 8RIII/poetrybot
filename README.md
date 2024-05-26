# Poetry Maker

This project aims to create an interactive web application using Streamlit and the OpenAI API. The app will generate short poems, specifically Haikus and Tankas, based on user prompts. The goal is to provide an engaging tool for users to explore and appreciate the art of short poetry.

## Features:

User Prompt Input: Users can enter a prompt or theme for their poem. 
<br />
Poem Type Selection: Users can choose between generating a Haiku or a Tanka. 
<br />
Poem Generation: Using the OpenAI API, the app generates a poem based on the user's input.
<br />
Interactive UI: A user-friendly interface built with Streamlit, allowing easy interaction and immediate results.
<br />
Regenerate Option: Users can generate another poem with the same or a new prompt.
<br />

## Technology Stack:

Streamlit: For building the web application interface.
<br />
OpenAI API: For generating the content of the poems.
<br />
Python: The programming language used to integrate Streamlit with the OpenAI API.
<br />
streamlit-js-eval: For handling JavaScript evaluations in Streamlit.
<br />
python-dotenv: For loading environment variables securely.
<br />

## Installation and Setup

### Clone the repository:
git clone https://github.com/your-username/short-poetry-creator.git
cd short-poetry-creator

### Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install dependencies:
pip install -r requirements.txt

### Set up environment variables:
#### Create a .env file in the project directory and add your OpenAI API key:

OPENAI_API_KEY=your-openai-api-key

## Run the app:
streamlit run app.py
