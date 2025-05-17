import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from utils import extract_text_from_pdf

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize session state
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = ""
if 'debug_info' not in st.session_state:
    st.session_state.debug_info = ""

# App header
st.set_page_config(page_title="Document Q&A with Gemini", page_icon="📚")
st.title("Document Q&A with Gemini")
st.write("Upload a PDF document and ask questions about it")

# Debug mode toggle
debug_mode = st.sidebar.checkbox("Debug Mode")

# Display API key status
if not api_key:
    st.sidebar.error("❌ API key not found in .env file")
else:
    st.sidebar.success("✅ API key loaded")
    # Configure Gemini API
    genai.configure(api_key=api_key)

# Choose model
model_options = ["gemini-1.5-pro", "gemini-1.0-pro"]
selected_model = st.sidebar.selectbox("Select Gemini Model", model_options)

# File uploader for PDF
uploaded_file = st.file_uploader("Upload your PDF document", type="pdf")

# Process the uploaded file
if uploaded_file:
    # Display file info
    file_size_mb = uploaded_file.size / (1024 * 1024)
    st.write(f"📄 Uploaded: **{uploaded_file.name}** ({file_size_mb:.2f} MB)")
    
    # Extract text button
    if st.button("Extract Text from PDF"):
        with st.spinner("Extracting text from PDF..."):
            # Get file bytes
            pdf_bytes = uploaded_file.getvalue()
            
            # Extract text
            extracted_text = extract_text_from_pdf(pdf_bytes)
            
            # Store in session state
            st.session_state.extracted_text = extracted_text
            
            # Add debug info
            st.session_state.debug_info = f"Text extraction completed. Found {len(extracted_text)} characters."
            
            # Show success
            st.success("Text extracted successfully!")
    
    # Display debug info
    if debug_mode and st.session_state.debug_info:
        st.write("Debug Info:", st.session_state.debug_info)
    
    # Show text preview if extracted
    if st.session_state.extracted_text:
        with st.expander("Preview Extracted Text"):
            st.text_area("Document Text", st.session_state.extracted_text[:5000], height=250)
            st.write(f"Total text length: {len(st.session_state.extracted_text)} characters")
        
        # Ask questions
        st.subheader("Ask a Question")
        user_question = st.text_input("What would you like to know about this document?")
        
        if user_question and st.button("Get Answer"):
            if not st.session_state.extracted_text.strip():
                st.error("No text was extracted from the PDF. Please try another document.")
            else:
                with st.spinner(f"Generating answer using {selected_model}..."):
                    try:
                        # Create the Gemini model
                        model = genai.GenerativeModel(selected_model)
                        
                        # Create the prompt
                        prompt = f"""
                        I need you to answer a question based on the document text provided below.
                        
                        DOCUMENT TEXT:
                        {st.session_state.extracted_text[:10000]} 
                        
                        QUESTION: {user_question}
                        
                        Please answer the question based ONLY on the information from the document text.
                        If the document doesn't contain relevant information, please say so.
                        """
                        
                        if debug_mode:
                            st.write("Sending prompt to Gemini...")
                        
                        # Get the response
                        response = model.generate_content(prompt)
                        
                        # Display the answer
                        st.subheader("Answer")
                        st.write(response.text)
                        
                        if debug_mode:
                            st.write("Response received successfully.")
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                        if debug_mode:
                            st.write("Exception details:", str(e))
else:
    st.info("Please upload a PDF document to begin.")
    
# Show sidebar instructions
st.sidebar.markdown("## Instructions")
st.sidebar.markdown("""
1. Upload a PDF document
2. Click 'Extract Text from PDF'
3. Ask questions about the document
4. Toggle 'Debug Mode' to see detailed information
""")

# Show model selection info
st.sidebar.markdown(f"Using model: **{selected_model}**") 