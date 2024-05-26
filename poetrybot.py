import streamlit as st
import openai

OPENAI_API_KEY = "your-openai-api-key"

openai.api_key = OPENAI_API_KEY

# Streamlit app
st.title('Short Poetry Creator')

st.write('This app uses the OpenAI API to generate short poems based on your input.')

# Select poem type
poem_type = st.selectbox('Select Poem Type:', ['Haiku', 'Tanka'])

# Input text from the user
user_input = st.text_area('Enter your prompt:', 'Nature')

# Generate Poem button
if st.button(f'Generate {poem_type}'):
    if user_input:
        # Construct prompt for generating the selected type of poem
        if poem_type == 'Haiku':
            prompt = f"Write a haiku about {user_input}."
            max_tokens = 30
        elif poem_type == 'Tanka':
            prompt = f"Write a tanka about {user_input}."
            max_tokens = 50

        # Call OpenAI API to generate the poem
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7
        )
        generated_text = response.choices[0].text.strip()

        # Display the generated poem
        st.subheader(f'Generated {poem_type}:')
        st.write(generated_text)

        # Ask the user to generate another poem
        another_poem = st.checkbox(f'Generate Another {poem_type}')
        if another_poem:
            user_input = st.text_area('Enter another prompt:', '')
            if user_input:
                # Add the user's input to the prompt and generate another poem
                if poem_type == 'Haiku':
                    prompt = f"Write a haiku about {user_input}."
                    max_tokens = 30
                elif poem_type == 'Tanka':
                    prompt = f"Write a tanka about {user_input}."
                    max_tokens = 50

                response = openai.Completion.create(
                    engine='text-davinci-003',
                    prompt=prompt,
                    max_tokens=max_tokens,
                    n=1,
                    stop=None,
                    temperature=0.7
                )
                generated_text = response.choices[0].text.strip()
                st.subheader(f'Another {poem_type}:')
                st.write(generated_text)
            else:
                st.warning(f'Please enter a prompt to generate another {poem_type}.')

    else:
        st.warning(f'Please enter a prompt to generate a {poem_type}.')

# Display API usage instructions
st.sidebar.header('Instructions')
st.sidebar.write('1. Select a poem type from the dropdown menu.')
st.sidebar.write('2. Enter your prompt in the text area.')
st.sidebar.write(f'3. Click the "Generate {poem_type}" button to get a poem from the OpenAI API.')
st.sidebar.write(f'4. If you want to generate another poem, check the "Generate Another {poem_type}" checkbox and enter a new prompt.')
