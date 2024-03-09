from openai import OpenAI

# API Key fetched from environment variable "OPENAI_API_KEY"
client = OpenAI()

def askGpt(prompt, model="gpt-3.5-turbo", max_tokens=100):

    try:
        completion = client.chat.completions.create(
            max_tokens=max_tokens,
            model=model,
            messages=[
                {"role": "system", "content": f"You are a helpful assistant that gives short and concise answers which are less or equal to {max_tokens} tokens."},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        return str(e)
