# **AI Code Reviewer**

## **Overview**
The **AI Code Reviewer** is a Streamlit-based web application that leverages Google Generative AI's Gemini 1.5 model to analyze Python code for errors, suggest corrections, and provide constructive feedback. Designed for developers and learners, this app improves coding practices and debugging efficiency.

---

## **Features**
- **Raw Code Input**: Paste or type Python code directly into the text area for review.
- **File Upload**: Upload Python scripts (`.py` files) for comprehensive analysis.
- **Error Categorization**: Highlights issues in the code, categorizing them as syntax, runtime, or logical errors.
- **Corrected Code**: Provides corrected versions of the submitted code with detailed comments.
- **Suggestions**: Offers tips to improve coding practices.
- **Sample Code Examples**: Includes predefined code snippets for testing the application.
- **Download Option**: Download the corrected code as a `.py` file.
- **User-Friendly Interface**: Designed with a responsive layout for seamless desktop and mobile usage.

---

## **Tech Stack**
- **Frontend**: [Streamlit](https://streamlit.io/) - For building the user interface.
- **Backend**: [Google Generative AI Gemini 1.5](https://ai.google/) - For natural language processing and code analysis.
- **Language**: Python 3.10
- **Deployment**: Local or cloud-based deployment using Streamlit.

---

## **Installation**
Follow these steps to run the application locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Rohitjakkam/AI-Code-Reviewer.git
   cd ai-code-reviewer
   ```

2. **Set Up the Environment**
   Install the required Python dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the API Key**
   - Place your Google Generative AI API key in a text file located at `Keys/GeminiDemo1.txt`.

4. **Run the Application**
   Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**
   Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## **Usage**
### **Raw Code Input**
1. Select the `Raw Code` tab.
2. Enter or paste your Python code in the text area.
3. Click `Submit` to analyze your code.
4. Review the output, including bugs, corrected code, and suggestions.

### **File Upload**
1. Select the `Code File` tab.
2. Upload a `.py` file.
3. Click `Submit` to analyze the file.
4. Download the corrected file if needed.

### **Predefined Examples**
1. Open the sidebar menu.
2. Choose a sample code snippet.
3. Analyze the code as you would with the `Raw Code` input.
   
---

## **Future Enhancements**
- **Multi-Language Support**: Extend support to other programming languages.
- **Advanced Analytics**: Provide in-depth analysis like code optimization suggestions and performance metrics.
- **Integration with IDEs**: Directly use the app within IDEs like VS Code or PyCharm.
- **Collaborative Review**: Allow team members to review and comment on code collaboratively.

---

## **Contributing**
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git commit -m "Add new feature"
   git push origin feature-name
   ```
4. Open a pull request.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Contact**
For questions or feedback, please contact:
- **Author**: Rohit Jakkam
- **GitHub**: [Rohit Jakkam](https://github.com/Rohitjakkam)
- **LinkedIn**: [Rohit Jakkam](https://www.linkedin.com/in/rohitjakkam/)
