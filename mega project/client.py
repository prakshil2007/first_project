from openai import OpenAI 

# client = OpenAI() 
# defaults to getting the key using os.environ.get("OPENAI_API_KEY") 
# # if you saved the key under a different environment variable name,
#  you can do something like: 
client = OpenAI( 
  api_key="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",
)

completion = client.chat.completions.create( 
    model="gpt-5-nano", 
    messages=[
    {"role": "system", "content": "You are a virtual assistant named Friday skilled in general tasks like alexa and google asssistant."}, 
    {"role": "user", "content": "what is coding"}
    ]
)

print(completion. choices[0].message.content)