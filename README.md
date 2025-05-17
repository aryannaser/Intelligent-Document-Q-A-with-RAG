# Intelligent Document Q&A with RAG

A simple web application that allows users to upload PDF documents and ask questions about their content using Google's Gemini AI models.

## Features

- PDF document upload and text extraction
- Question answering based on document content
- Support for both Gemini 1.5 Pro and Gemini 1.0 Pro models
- Debug mode for troubleshooting
- Text preview for extracted content

## Requirements

- Python 3.8+
- Streamlit
- PyPDF2
- Google Gemini API key

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Intelligent-Document-Q-A-with-RAG.git
   cd Intelligent-Document-Q-A-with-RAG
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory with your Google Gemini API key:
   ```
   GOOGLE_API_KEY="your_api_key_here"
   ```

   Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

4. Add ~/.local/bin to your PATH if you use zsh (so you can run Streamlit and other Python tools):
   ```sh
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

5. Run the application:
   ```
   streamlit run app.py
   ```

## Usage

1. Upload a PDF document
2. Click "Extract Text from PDF"
3. Ask questions about the document content
4. Toggle "Debug Mode" if you need more details about the process

## Stopping the Application

To stop the Streamlit app or any running process in your terminal:

- If running in the foreground, press <kbd>Ctrl</kbd> + <kbd>C</kbd>.
- If you started the app in the background (with & or using nohup), find the process and kill it:
  ```zsh
  # Find the Streamlit process
  ps aux | grep streamlit
  # Kill the process by PID (replace <PID> with the actual number)
  kill <PID>
  # Or force kill if needed
  kill -9 <PID>
  ```

## Future Improvements

- Implement true RAG (Retrieval Augmented Generation) with vector stores
- Add support for more document formats (DOCX, TXT, etc.)
- Improve document chunking for better context handling
- Add document summarization features

## License

MIT License - See LICENSE file for details