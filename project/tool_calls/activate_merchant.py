
from util.llm_utils import run_console_chat
from main import process_response

def activate_merchant(player_money, items):

    run_console_chat(template_file='project/DM_template.json',
                 process_response=process_response,
                 items=items,
                 end_regex=r'TRADE COMPLETED (.*)')