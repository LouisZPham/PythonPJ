import openai

# Set up OpenAI API key
import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# Set OpenAI API key
openai.api_key = secrets["sk-zK**************9zyboTPhO1kc"]

# Generate text
prompt = "The quick brown fox"
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=50
)
text = response.choices[0].text
print(text)
This code will generate 50 additional tokens of text following the prompt "The quick brown fox". You can customize the prompt and the number of tokens generated according to your needs. Note that this code uses the "davinci" engine, which is the most advanced and expensive engine offered by OpenAI. If you want to use a cheaper engine, you can replace "davinci" with one of the other engine options (e.g., "curie", "babbage", etc.).





