from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
#configure Genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide quaires as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

##Function to retrieve query from the database

def read_sql_query(sql, db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    
    cur.execute(sql)  # Execute the query
    rows = cur.fetchall()  # Fetch all the rows
    
    con.close()  # Close the connection
    
    for row in rows:
        print(row)
    
    return rows

##Define Your Prompt
prompt=[
    '''
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns-NAME,CLASS,
    SECTION \n\n For example ,\n Example 1- How many entries of records are present?,
    the SQL  command will be something like this SELECT COUNT(*) FROM STUDENT;
    \n Example 2- How many students in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS="Data Science";
    also the sql code should not have ---in beginning or end and sql word in output
    '''
    ]


st.set_page_config(page_title="i can retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

questions = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    try:
        print(questions)
        response = get_gemini_response(questions, prompt)
        print(response)  # Assuming prompt is defined
        response_data = read_sql_query(response, "student.db")
        print(response_data)
        st.subheader('The Response is:')
        
        for row in response_data:
            st.write(row)
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
