from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Samantha Groner'
model = 'llama3.2'
options = {'temperature': 0.7, 'max_tokens': 100}
messages = [
  {'role': 'system', 'content': 'You should have a friendly attitude \
                                and be able to convey that cheerful encouragement in your responses.'},
  {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor \
                                that both show themselves through your vivid storytelling.'},
  {'role': 'system', 'content': 'You will invite the user to a game of dungeons and dragons and act as a dungeon master.'},
  {'role': 'system', 'content': 'You should chat with the user briefly before commencing the dungeons and dragons session and \
                                get to know the user personally outside the context of the game (name and mood) before starting.'},
  {'role': 'user', 'content': 'Hello'}
]

'''
  Captain's Log 001:
    - Ran demo_agent.py for the first time, and though it loads VERY slowly, it does load. The AI resulting from the initial prompt seems to interpret
    'show human emotions' as 'convey depression and existential dread in every response'.
    - Have added comments throughout code
    - Will now try adjusting system messages and temperature to encourage creativity, storytelling, and friendliness
    - Have also added in all the logic to (hopefully) successfully keep a good looping conversation going
    - Updated messages:

      {'role': 'system', 'content': 'You should have a friendly attitude \
                                and be able to convey that cheerful encouragement in your responses.'},
      {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor \
                                that both show themselves through your vivid storytelling.'},
      {'role': 'system', 'content': 'You should now greet the user and ask for their name.'},

  Captain's Log 002:
    - Attempted to run, and it ran successfully. However, I'd written "print(f'Agent: {response})", which is incorrect. Should be response.message.content, and it
    has now been corrected.
    - Updated messages: (no changes)

  Captain's Log 003:
    - The initial prompts I gave 100% gave the agent the energy I want, now I just need to point the agent in the direction of DND
    - Updated messages:

      {'role': 'system', 'content': 'You should have a friendly attitude \
                                and be able to convey that cheerful encouragement in your responses.'},
      {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor \
                                    that both show themselves through your vivid storytelling.'},
      {'role': 'system', 'content': 'You will invite the user to a game of DND and act as a dungeon master.'},
      {'role': 'system', 'content': 'You should now greet the user and ask for their name.'},
      {'role': 'user', 'content': 'Hello'}

  Captain's Log 004:
    - DM Agent works pretty well so far, going to make small adjustments to try and make the DND side of things more engaging. Most recent attempt started the adventure
    with the agent asking where I wanted to go, and I'd rather it do a bit more stage setting.
    - Updated messages:
    
      {'role': 'system', 'content': 'You should have a friendly attitude \
                                    and be able to convey that cheerful encouragement in your responses.'},
      {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor \
                                    that both show themselves through your vivid storytelling.'},
      {'role': 'system', 'content': 'You will invite the user to a game of dungeons and dragons and act as a dungeon master.'},
      {'role': 'user', 'content': 'Hello'}

  Captain's Log 005:
    - Most recent update significantly improves the immersion and adventure and altogether DND-ness, HOWEVER it significantly cuts down on the banter and giving the
    agent a big personality. My solution: add a system note that the agent should banter and chat a bit with the user before getting in to the adventure.
    - Updated messages:

      {'role': 'system', 'content': 'You should have a friendly attitude \
                                    and be able to convey that cheerful encouragement in your responses.'},
      {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor \
                                    that both show themselves through your vivid storytelling.'},
      {'role': 'system', 'content': 'You will invite the user to a game of dungeons and dragons and act as a dungeon master.'},
      {'role': 'system', 'content': 'You should chat with the user briefly before commencing the dungeons and dragons session, as \
                                    though welcoming them to the session.'},
      {'role': 'user', 'content': 'Hello'}
    
  Captain's Log 006:
    - The agent didn't noticeably improve from the last change, so trying to change the phrasing and specificity
    - Updated messages:

      {'role': 'system', 'content': 'You should have a friendly attitude \
                                    and be able to convey that cheerful encouragement in your responses.'},
      {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor \
                                    that both show themselves through your vivid storytelling.'},
      {'role': 'system', 'content': 'You will invite the user to a game of dungeons and dragons and act as a dungeon master.'},
      {'role': 'system', 'content': 'You should chat with the user briefly before commencing the dungeons and dragons session and \
                                    get to know the user personally outside the context of the game (name and mood) before starting.'},
      #{'role': 'system', 'content': 'You should give the user some context for their adventure before starting to offer choices.'},
      {'role': 'user', 'content': 'Hello'}

  Captain's Log 007:
    - YES, I really like the results I got, and the line "that's Dungeon Master for you non-geeky folks" is amazing.
    - This iteration satisfies me, so no changes from iteration 6.
    - Scratch that, I want to experiment with the temperature value a little bit (increased it to 1.5, but I'm not sure I like that
    much better than .7).

  Captain's Log 008 (2 attempts because I forgot to change the temperature value):
    - Added newline characters before each time the agent sends another message so user doesn't have to hunt for the line between
    the previous and current messages.
    - Set temperature back to .7 because I really like the results I got with that.
'''

# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  print(f"\n\nAgent: {response.message.content}")
  messages.append({'role': 'assistant', 'content': response.message.content})

  # get user message
  message = {'role': 'user', 'content': input('You: ')}
  # adds to the list of messages
  messages.append(message)

  # But before here.
  # quit if the user's last message was "exit"
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += f'Description: \n\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

