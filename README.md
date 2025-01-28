# **AskMyData**  
An AI-powered chatbot built using Streamlit and GROQ's API, designed to answer user queries based on an uploaded dataset. The chatbot supports multiple file formats for datasets, including `.txt`, `.json`, `.csv`, and `.xlsx`, and dynamically processes them to provide relevant responses.  

## **Features**  
- **Multi-File Format Support**: Accepts `.txt`, `.json`, `.csv`, and `.xlsx` datasets.  
- **Dynamic Dataset Processing**: Automatically processes datasets for preview and use as context.  
- **Real-Time Chat**: Users can interact with the chatbot in a conversational manner.  
- **Session Persistence**: Maintains chat history during a session.  
- **Smart Request Handling**: Summarizes large datasets and trims chat history to meet GROQ's API limits.  

---

## **Tech Stack**  
- **Frontend**: Streamlit for interactive UI.  
- **Backend**: Python, GROQ API for AI chat completions.  
- **Libraries**:  
  - `streamlit`: For creating the web app.  
  - `pandas`: For handling `.csv` and `.xlsx` files.  
  - `openpyxl`: For processing `.xlsx` files.  
  - `groq`: Python client for GROQ's API.  

---

## **Getting Started**  

### **Prerequisites**  
Ensure you have the following installed:  
- Python 3.8+  
- pip  

### **Installation**  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/jaisw07/AskMyData.git
   cd AskMyData
   ```

2. **Set Up a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up GROQ API Key**  
   - Obtain your GROQ API key from the [GROQ Console](https://console.groq.com/).  
   - Create a `.env` file in the root directory:  
     ```env
     GROQ_API_KEY=your_groq_api_key
     ```  

5. **Run the Application**  
   ```bash
   streamlit run app.py
   ```  

---

## **How to Use**  

1. **Upload a Dataset**  
   - Supported formats: `.txt`, `.json`, `.csv`, `.xlsx`.  
   - The dataset is processed and displayed for preview.  

2. **Ask Questions**  
   - Type your question in the input box and press "Enter" or click "Submit".  
   - The chatbot uses the uploaded dataset as context to generate responses.  

3. **Chat History**  
   - View your chat history on the interface.  

---

## **Project Structure**  
```
ai-chatbot-with-groq/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (GROQ API key)
├── README.md             # Project documentation
└── data/                 # Example datasets (optional)
```

---

## **Example Datasets**  

- **Text File (`.txt`)**: Plain text containing the dataset.  
- **JSON File (`.json`)**: Structured data in JSON format.  
- **CSV File (`.csv`)**: Tabular data in CSV format.  
- **Excel File (`.xlsx`)**: Tabular data in Excel format.  

---

## **Handling Large Datasets**  
- If the dataset is too large for the GROQ API limits, the app will:  
  - Summarize the dataset (e.g., show only headers and a few rows for tabular data).  
  - Trim the chat history to fit within the API's character limit.  

---

## **Known Issues**  
- **API Rate Limits**: Ensure that the request size (dataset + query) stays within GROQ's API limits.  
- **Large Datasets**: Very large files may be truncated. Consider summarizing the data manually if needed.  

---

## **Contributing**  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Description of changes"
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```  
5. Create a pull request.  

---

## **License**  
This project is licensed under the [MIT License](LICENSE).  

---

## **Acknowledgements**  
- [Streamlit](https://streamlit.io/) for providing an easy-to-use UI framework.  
- [GROQ](https://groq.com/) for the AI API services.  
- [Pandas](https://pandas.pydata.org/) for data processing.  
