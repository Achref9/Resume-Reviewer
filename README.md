# 📃 PDF Critique Summarizer

This is a Streamlit web application that allows you to upload a PDF (such as a resume or a written document) and receive a constructive critique summary tailored to a job role you specify.

---

## ✨ Features

- Upload PDF files.
- Enter a job role to contextualize recommendations.
- Extracts all text content from the PDF.
- Generates a critique covering:
  - Content Clarity
  - Experience Description
  - Content Quality
  - Content Originality
  - Suggested improvements relevant to your job role
- Interactive and easy-to-use web interface.

---

## 🏗️ Project Structure

- `streamlit` - Builds the user interface.
- `PyPDF2` - Extracts text from uploaded PDFs.
- `openai` - Calls the OpenAI API for summarization.
- `dotenv` - Loads environment variables securely.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-critique-summarizer.git
cd pdf-critique-summarizer
```
2. Create and activate a virtual environment (optional)
bash
```
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate
```
3. Install the requirements
bash
```
pip install -r requirements.txt
```
Make sure you have your API Key ready from:<br/>
https://platform.openai.com/api-keys <br/>
Make a .env file and put it under this variable <br/>
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
