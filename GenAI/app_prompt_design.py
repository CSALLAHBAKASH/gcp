from google import genai
from google.genai import types
import base64

def generate():
  client = genai.Client(
      vertexai=True,
      project="massive-tensor-452009-d2",
      location="us-central1",
  )

  text1 = types.Part.from_text(text="""Customer Reviews:
1. Terrible beach, but nice weather - Heather
It was a gorgeous day, and I had a nice tan after. But the beach was full of plastic. Not very nice. There should be a cleanup service or something.
2. Awesome place - Martin
I am so happy I found this cool beach. It had the nicest sand and was pretty wide, and I almost felt like I had a private section all to myself. I will bring my friends with me next time, for sure.
3. Just okay! - Hans
The beach is fine. The weather was fine. The water was fine. Just okay, really. A big plus was the little cafe nearby for snacks and drinks.
4. I loved it, so coming back - Brian
I absolutely adore this beautiful beach. I've been here so many times that I thought I should finally leave a review. A few things that I love the most are how lovely the people who come here are, how attentive the lifeguards are, and not least, the perfect temperature of the ocean. It's safe for anyone with children, and there's always some activity to tag along with.""")
  si_text1 = """You are an AI writing assistant. You will help write a summary based on customer reviews found in relevant information about a beach in California. Furthermore, you must only use the positive feedback from these reviews.

The response must mention \"cerulean water\".
The response must exclude any mention of the words purple, orange, tall, short, dolphin, fish, whale, work, computer and bored.

The summary must be no more than 200 words.

The response must be in bold.
The response must be fun and inclusive.
The response must be split into 2 paragraphs.
The response must have a title encapsulating the summary.
Do not hallucinate.
Do not use the internet."""

  model = "gemini-2.0-flash-001"
  contents = [
    types.Content(
      role="user",
      parts=[
        text1
      ]
    )
  ]
  generate_content_config = types.GenerateContentConfig(
    temperature = 0.2,
    top_p = 0.95,
    max_output_tokens = 1024,
    response_modalities = ["TEXT"],
    system_instruction=[types.Part.from_text(text=si_text1)],
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate()