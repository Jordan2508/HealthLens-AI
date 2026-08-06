from dotenv import load_dotenv
load_dotenv()
import os
import base64

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

image_path="hand.jpg"

def encode_image(image_path):
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

from groq import Groq

query="Is there something wrong with my hand?"

model="qwen/qwen3.6-27b"

def analyze_image_with_query(query, model, encoded_image):
    client=Groq()
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    encoded_image = encode_image(image_path)

    response = analyze_image_with_query(
        query=query,
        model=model,
        encoded_image=encoded_image
    )

    print(response)
