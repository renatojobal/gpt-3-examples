
import os
import openai
import setup
import logging

logging.basicConfig(level=logging.WARNING)

openai.api_key = os.getenv("OPENAI_API_KEY")


# GPT-3 Engine parameters
bot_name = "Don Piguave"
human_name = "You"



salute = f"""
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
You can exit typing ^C. (Command + C), (Ctrl + C)

{bot_name}: Hi! How can I help you today?
"""

print(salute, end="")


nex_input = input(human_name+": ")
actual_promt = salute + human_name + ": " + nex_input + "\n" + bot_name + ":"
print(bot_name + ":", end="")



response = openai.Completion.create(
            engine="davinci",
            temperature=0.9,
            max_tokens=190,
            top_p=1,
            prompt = actual_promt,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", "Human:", "AI:"]
        )


ai_response = response.choices[0].text
print(ai_response)

# Update promt
actual_promt += ai_response

print("Actual promt")
print(actual_promt)


