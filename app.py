# Importing dependencies
import streamlit as st  # App development framework
import google.generativeai as genai  # LLM provider

# Accessing and configuring the API key
try:
    with open("Keys/gemini.txt") as f:
        key = f.read().strip()
    if not key:
        st.error("API key not found! Please provide a valid key.")
    else:
        genai.configure(api_key=key)
except FileNotFoundError:
    st.error("API key file not found! Ensure 'GeminiDemo1.txt' exists in the 'Keys' folder.")

# Setting up Streamlit page configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon=":robot_face:",
    layout="centered",
)

# Instruction to the model
sys_prompt = """You are an expert, helpful, and sensible AI Python Code Reviewer. 
User will give you the Python code written by them. 
You should analyze the code and identify all the bugs or errors. 
You will most probably receive any of the following 3 cases of inputs - incorrect code, correct code, or irrelevant out-of-scope request.
...
"""

# Configuring the model
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash", 
    system_instruction=sys_prompt
)

# Setting up the title
st.title(":green[:robot_face: AI Code Reviewer]")

# Tab layout for user inputs
tab_1, tab_2 = st.tabs([':orange[:memo:__Raw Code__]', ':orange[:page_facing_up:__Code File__]'])

# Tab 1: Raw Code Input
with tab_1:
    st.markdown('<p style="font-size: 20px; color: orange;"><b>Enter your Python code below:</b></p>', unsafe_allow_html=True)
    user_prompt = st.text_area("", placeholder="Type or paste your code here...")
    btn_click_1 = st.button("Submit", "tab_1")
    
    if btn_click_1:
        with st.spinner(':green[__Please wait :hourglass_flowing_sand: while I :robot_face: review your code ...__]'):
            try:
                response = model.generate_content(user_prompt)
                st.markdown(response.text, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Tab 2: File Upload
with tab_2:
    st.markdown('<p style="font-size: 20px; color: orange;"><b>Choose a .py file</b></p>', unsafe_allow_html=True)
    st.write(":warning:__Only 1 file shall be uploaded__")
    uploaded_file = st.file_uploader("Upload your .py file")
    if uploaded_file:
        st.write("filename:", uploaded_file.name)
        btn_click_2 = st.button("Submit", "tab_2")
        if btn_click_2:
            with st.spinner(':green[__Please wait :hourglass_flowing_sand: while I :robot_face: review your code file ...__]'):
                try:
                    if uploaded_file.name.endswith('.py'):
                        bytes_data = uploaded_file.getvalue().decode("utf-8")
                        response = model.generate_content(bytes_data)
                        st.markdown(response.text, unsafe_allow_html=True)
                        st.download_button(
                            label="Download Corrected Code",
                            data=response.text,
                            file_name="corrected_code.py",
                            mime="text/x-python",
                        )
                    else:
                        st.error("Please upload a valid .py file!")
                except Exception as e:
                    st.error(f"Error processing the file: {e}")

# Styling and additional features
st.markdown('<style>.stMarkdown { font-size: 18px; }</style>', unsafe_allow_html=True)
st.markdown('<p style="color: blue;">Enhancements implemented!</p>', unsafe_allow_html=True)

# Predefined Examples
st.sidebar.header("Try Example Codes:")
example_codes = {
    "Simple Function": "def hello_world():\n    print('Hello, world!')",
    "Error Example": "print(1 / 0)",
}
example = st.sidebar.selectbox("Choose a sample code:", options=example_codes.keys())
if example:
    user_prompt = example_codes[example]
    st.text_area("Code Example:", user_prompt, height=200)
