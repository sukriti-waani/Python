from openai import OpenAI

client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "What is coding"}
  ]
)

print(completion.choices[0].message.content)
