# pip install --upgrade google-genai
# gcloud auth application-default login


from google import genai
from google.genai import types
import base64

def generate():
  client = genai.Client(
      vertexai=True,
      project="massive-tensor-452009-d2",
      location="us-central1",
  )


  model = "gemini-2.0-flash-001"
  contents = [
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""list all genai topics without description""")
      ]
    ),
  ]
  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 8192,
    response_modalities = ["TEXT"],
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate()