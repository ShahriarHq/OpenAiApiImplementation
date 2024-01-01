from openai import OpenAI
api_key = "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"

client = OpenAI(api_key=api_key)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url