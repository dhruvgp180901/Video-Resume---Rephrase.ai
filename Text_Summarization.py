import openai
import re
import os

from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API key
openai.api_key = os.environ["OPEN_API_KEY"]

def summarize_resume(resume_text):
    resume_text = re.sub('\n', ' ', resume_text)
    resume_text = re.sub('\W+', ' ', resume_text)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following resume:\n{resume_text}\nSummary:",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].text.strip()
    print("Resume Summarized!")
    return summary