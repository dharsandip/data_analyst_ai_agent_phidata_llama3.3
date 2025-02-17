In this project, a Streamlit Application with AI Agent for Data Analysis has been built in Python with Phidata, 
DuckDbAgent and Llama3.3 model (Open Source LLM). A "DuckDb Agent" in Phidata is a specialized agent that allows users to 
analyze data using the DuckDB database engine within the Phidata platform, essentially enabling direct SQL queries and 
data manipulation on datasets through the powerful analytical capabilities of DuckDB.

After launching the Streamlit App, user needs to upload a csv file containing data. Then, they can type any question for analyzing 
or getting some insight from the data and click on "Analyze" button and our Data Analyst Agent (created with phidata) with the help 
of duckdb and LLM, will answer the question. 


Steps to setup:

1. Please install all the required python libraries (pip install -r requirements.txt)

2. Please check the .env_sample file and you will need to get those API keys on your own (please signup on those websites and get free API keys)
   and then create .env file with your API keys and keep in in the working directory

3. Now, you should be able to run the python script

