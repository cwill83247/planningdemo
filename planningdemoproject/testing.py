import os
import openai
openai.api_key = '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'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)