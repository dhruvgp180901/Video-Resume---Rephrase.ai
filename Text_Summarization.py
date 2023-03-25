import openai
import re

# Set up OpenAI API key
openai.api_key = "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"

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