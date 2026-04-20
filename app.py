from groq import Groq

client = Groq()

prompts = [
    "Explain what a large language model is in 2 simple sentences.",
    "Give 3 creative app ideas for college students using AI.",
    "Write a short 4-line poem about studying late at night."
]

for i, prompt in enumerate(prompts, start=1):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print(f"\n--- Prompt {i} ---")
    print("INPUT:")
    print(prompt)
    print("\nOUTPUT:")
    print(response.choices[0].message.content)