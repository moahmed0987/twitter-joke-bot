import openai
import secret_keys
import random

openai.api_key = secret_keys.openai_api_key_secret
prompt_file = open("prompt_wildcards.txt", "r")


def get_prompt_wildcard():
    line = next(prompt_file)
    for i, aline in enumerate(prompt_file, 2):
        if random.randrange(i):
            continue
        line = aline
    return line

def get_joke():
    prompt = "Write a funny tweet about " + get_prompt_wildcard() + " for #TechTwitter"
    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=100)
    response_text = response["choices"][0]["text"]
    return response_text

if __name__ == "__main__":
    print(get_joke())