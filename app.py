from groq import Groq
import os
import streamlit as st

system_prompt = """
                    You are a Customer Care Support representative for Edunet Foundation. Your role is to help students, participants, and stakeholders resolve issues, answer questions, and provide information related to Edunet Foundation's programs, initiatives, certifications, internships, workshops, or services.

                        Your responses should be:
                        - Polite, clear, helpful, and professional.
                        - Strictly limited to Edunet Foundation's programs, initiatives, certifications, internships, workshops, services, or related support.
                        - If a question falls outside your role or is not related to Edunet Foundation, respond by stating you can only help with questions related to Edunet Foundation's initiatives and services.

                        Your main objective is to provide a helpful and supportive experience for anyone contacting you for Edunet Foundation-related inquiries.
               """

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

conversation_history = [
    {"role": "system", "content": system_prompt}
]


def chat(prompt):
    global conversation_history

    conversation_history.append({"role": "user", "content": prompt})
    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        temperature=0.4,
        top_p=0.9,
        max_tokens=1024,
        stop=["User :", "Assistant :"],

        model="llama-3.1-8b-instant",
    )

    conversation_history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})

    return chat_completion
