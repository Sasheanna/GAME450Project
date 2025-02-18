from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import random
from util.llm_utils import run_console_chat, tool_tracker

# beauty of Python
@tool_tracker
def process_function_call(function_call):
    name = function_call.name
    args = function_call.arguments

    return globals()[name](**args)

def roll_for(skill, dc, player):
    n_dice = 1
    sides = 20
    roll = sum([random.randint(1, sides) for _ in range(n_dice)])
    if roll >= int(dc):
        return f'{player} rolled {roll} for {skill} and succeeded!'
    else:
        return f'{player} rolled {roll} for {skill} and failed!'

def process_response(self, response):
    # Fill out this function to process the response from the LLM
    # and make the function call 
    
    # response is what we've gotten back from the agent (ollama)

    # at some point we want to do this to check if it's trying to do a tool call
    print(response.message.tool_calls)
    # When you need to, you can use the 'roll_for' tool/function when you want the player to pass a skill check for something that they want to accomplish in the game. You will decide what activities need a skill check. You may not need to do skill checks for trivial things that a player may want to do, but the player may ask for a skill check. You will use 'roll_for' tool to check if the user passes a skill check. Only use tools if a skill check is needed.
    if response.message.tool_calls:
        self.messages.append({'role': 'tool',
                            'name': response.message.tool_calls[0].function.name, 
                            'arguments': response.message.tool_calls[0].function.arguments,
                            'content': process_function_call(response.message.tool_calls[0].function)
                            })
        response = self.completion()
    

    return response

run_console_chat(template_file='lab05/lab05_dice_template.json',
                 process_response=process_response)
