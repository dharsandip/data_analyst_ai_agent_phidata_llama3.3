
import json
#from phi.model.openai import OpenAIChat
from phi.agent.duckdb import DuckDbAgent
from phi.agent import Agent
#from phi.tools.firecrawl import FirecrawlTools
from phi.model.groq import Groq
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def analyze_data(query):

    data_analyst_agent = DuckDbAgent(
        model=Groq(id="llama-3.3-70b-versatile"),
        semantic_model=json.dumps(
            {
                "tables": [
                    {
                        "name": "Bank_Transaction_Fraud_Detection",
                        "description": "Contains Banking Transactions data for Fraud Detection",
                        "path": "./data.csv",
                    }
                ]
            }
        ),
        structured_outputs=True,
    )
    
    
    output = data_analyst_agent.run(
    #    "Please go through the data and tell me how many total Transactions are there. In your response, please only mention the answer and nothing else. ",
        query + ". In your response, please only mention the answer and nothing else",
        # "Show me a histogram of ratings. "
        # "Choose an appropriate bucket size but share how you chose it. "
        # "Show me the result as a pretty ascii diagram",
        stream=True,
    )

    answer = ''.join(chunk.content for chunk in output)

    return answer



def main():

    html_temp = """
    <div style="background-color:violet;padding:8px">
    <h2 style="color:black;text-align:center;">Data Analysis by AI Agent</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)    
    
    st.image("logo.jpg", width=500)

    csv_file = st.file_uploader("**Upload CSV File**", type=["csv"])
    
    if ((csv_file is not None) and ('csv' in str(csv_file))):
        bytes_data = csv_file.read()
        
        with open("data.csv", 'wb') as f: 
            f.write(bytes_data)
            f.close()
   
    query = st.text_input("**Question**","")
    
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #DD3300;
        color:#eeffee;
    }
    </style>""", unsafe_allow_html=True)

    if st.button("Analyze"):
        answer = analyze_data(query)
        st.success('Answer: {}'.format(answer))
    

if __name__=='__main__':
    main()

