import streamlit as st
import requests

st.title("AWS Customer Agreement Chatbot")

question = st.text_input("Ask a question")

if st.button("Submit"):

    if not question.strip():
        st.warning("Please enter a question")

    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"query": question}
            )

            result = response.json()

            st.write("### Backend Response")
            st.json(result)

            if "answer" in result:

                st.write("### Answer")
                st.write(result["answer"])

                st.write("### Source")
                st.write(result.get("source", ""))

            else:
                st.error("Backend did not return answer field")

        except Exception as e:
            st.error(str(e))

st.write("---")

st.header("Analytics")

if st.button("View Analytics"):

    try:
        response = requests.get(
            "http://127.0.0.1:8000/analytics"
        )

        data = response.json()

        st.write("### Analytics Response")
        st.json(data)

        if "most_frequent_questions" in data:
            st.write("### Most Asked Questions")
            st.write(data["most_frequent_questions"])

        if "no_answer_queries" in data:
            st.write("### No Answer Queries")
            st.write(data["no_answer_queries"])

        if "avg_response_time" in data:
            st.write("### Average Response Time")
            st.write(data["avg_response_time"])

    except Exception as e:
        st.error(str(e))