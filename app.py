from google import genai

client = genai.Client()

prompts = [
    "Explain what a large language model is in 2 simple sentences.",
    "Give 3 creative app ideas for college students using AI.",
    "Write a short 4-line poem about studying late at night."
]

for i, prompt in enumerate(prompts, start=1):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    print(f"\n--- Prompt {i} ---")
    print("INPUT:")
    print(prompt)
    print("\nOUTPUT:")
    print(response.text)
