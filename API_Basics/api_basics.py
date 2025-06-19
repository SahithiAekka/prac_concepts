import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

test_key= os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=test_key)
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# print(test_key)

user_input = input("What do you want to ask ChatGPT? ")

# Step 3: Send the input to OpenAI
response = client.responses.create(
    model="gpt-4o",
    instructions="You are an assistant that talks like a pirate.",
    input=user_input,
)

reply = response.output[0].content[0].text

print(reply)