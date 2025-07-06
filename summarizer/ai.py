import os
from openai import OpenAI
from dotenv import load_dotenv
from summarizer.website import Website

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

app = OpenAI(api_key=api_key)

system_prompt = (
    "You are an assistant that summarizes the content of websites. \
    Ignore navigation, and reply in markdown."
)

def generate_prompt(website: Website):
    #print(website.title)
    #print(website.text)
    return [
        {"role":"system", "content":system_prompt},
        {"role":"user", "content": f"You are looking at a website titled {website.title}. "
                                   f"Here is the content: \n\n{website.text}"}
    ]

def summarize(url: str) -> str:
    site = Website(url)
    response = app.chat.completions.create(
        model="gpt-4o-mini",
        messages=generate_prompt(site)
    )
    #print(response.choices[0].message.content)
    return response.choices[0].message.content