import os 
import json 
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat 
import random
from util.llm_utils import run_console_chat, tool_tracker, pretty_stringify_chat, ollama_seed as seed

# tool calls
from tool_calls.access_data import access_world_info
from tool_calls.dice_tool import roll_for
#from tool_calls.purchase import # UNIMPLEMENTED

#from RAG_operations import 

@tool_tracker

def process_response(self, response):
    # Fill out this function to process the response from the LLM
    # and make the function call 
    
    # response is what we've gotten back from the agent (ollama)

    # at some point we want to do this to check if it's trying to do a tool call
    if response.message.tool_calls:
        self.messages.append({'role': 'tool',
                            'name': response.message.tool_calls[0].function.name, 
                            'arguments': response.message.tool_calls[0].function.arguments,
                            #'content': process_function_call(response.message.tool_calls[0].function)
                            })
        response = self.completion()
    

    return response


run_console_chat(template_file='project/DM2_template.json',
                 process_response=process_response,
                 end_regex=r'END SESSION')

#Player sheet created on first session
sign_your_name = 'Team something'
player_name = sign_your_name.replace(" ", "_").lower()
player_data = {
    "name": sign_your_name,
    "class":"Bard",
    "level":1,
    "stats": {
        "strength":8,
        "dextrity":14,
        "intelligence":16,
        "charisma":18
    }
}

#save in the file
player_folder = Path ('project/players')
player_folder.mkdir(parents=True, exist_ok=True)
player_file = player_folder / f"{player_name}.json"

#save it only one time
if not player_file.exists():
    with open(player_file, "w") as f:
        json.dump(player_data, f, indent=2)
    os.chmod(player_file,0o444) #file is read only 
    print(f"Player sheet created and saved for {sign_your_name}")
else:
    print(f"Player sheet already exist for {sign_your_name}")
#model 
model = 'llama3.2'
options = {'temperature': 0.5, 'max_tokens': 100}
options |= {'seed': seed(sign_your_name)}
messages = [{'role':'system', 'content': 'Youn should have emotions like a human being and be able to convey those emotions in your responses'},]
#chat loop
# while True:
#     response = chat(model=model, messages=messages, stream=False, options=options)
#     print(f'DM: {response.message.content}')
#     messages.append({'role':'assistant', 'content':response.message.content})
#     message = {'role':'user', 'content': input('You: ')}
#     if message ['content'].strip().lower() == '/exit':
#         break
#     messages.append(message)

# save the chat 
with open(Path('project/playerInfo.txt'),'a') as f:
    file_string = ''
    file_string += '--------------------------NEW ATTEMPT----------------------\n\n\n'
    file_string += f'Model: {model}\n'
    file_string += f'Options: {options}\n'
    file_string += pretty_stringify_chat(messages)
    file_string += '--------------------------END OF ATTEMPT--------------------\n\n\n'
    f.write(file_string)


