**1.0 Base System Functionality**
This system acts as a Dungeons and Dragons Dungeon Master. The system is able to handle to following scenarios:
>1.1 Social encounters with NPC characters 
>1.2 Interactions with a trader NPC
>1.3 Dice rolling 
>1.4 Storing the player information within a character sheet
>1.5 Allows players to purchase items from traders 

**2.0 Prompt Engineering and Model Parameter choices**
1.  DnD Trader Scenario
2.  Model: llama: 3.2
3.  Temperature: 1.2
4.  Max Tokens: Not set
5.  Rationale:
The trader is designed to act as a lively and entertaining character, offering players a fun and dynamic interaction. A high temperature (1.2) was chosen to allow the model to be creative, surprising, and engaging—essential for portraying a vibrant DnD shopkeeper.
6.  Prompt Techniques:
    -   Role-based prompting: The model is instructed to act as a DnD merchant with a specific behavior.
    -   Structured output: Strict instructions enforce the output format (TRADE COMPLETED [...]), using examples to eliminate ambiguity.
    -   Contextual guidance: Clear rules ensure the model doesn’t alter the item list or add commentary.

2.  Dungeon Master Scenario
3.  Model: llama: 3.2
4.  Temperature: 0.7
5.  Max Tokens: Not set
6.  Tool Used: roll_for
7.  Rationale:
The Dungeon Master needs to tell a compelling and imaginative story while still maintaining coherence and player engagement. A moderate temperature (0.7) provides a balanced output—creative yet focused.
8.  Prompt Techniques:
    -   Multiple system-level prompts are used to define personality (dramatic, witty), behavior (cheerful and friendly), and role (Dungeon Master).
    -   Conversational setup is included to simulate natural dialogue before starting the game.
    -   Tool-use instructions (roll_for) are embedded to simulate DnD mechanics with clear guidance on when and how to use it.
    -   The model is instructed to lead and respond in-character consistently, guiding the user through a personalized adventure.


**3.0 Tools Usages**
The system has three primary tool calls:
 - Dice rolls
 - Trading
 - Accessing the player sheet 
 
The dice roll tool call rolls dice for the player. The tool call rools two dice and adds them together. 

The trading tool call checks the traders inventory, checks the player amount of money, and the amount of items the player wants. The tool call compares the amount of items the player wants to ensure that the trader has that amount of items in their inventory. In addition the tool call compares the amount of currency the player has to the cost of items the player wants. This is all in an effort to limit errors made by the LLM. 

The final tool call is a tool call that access the player sheet. The player sheet is stored in a JSON format that is not able to be modified by the LLM. The LLM is able to use the tool call to access information off of the player sheet, such as the player level and abilities.

**4.0 Planning and reasoning** 
The LLM uses chain-of-thought prompting when utalizing the trading tool call. This again is in an effort to help prevent errors made by the LLM in the amount of items delivered to the player, as well as the amount of items removed from the traders inventory. 

**5.0 RAG Implementation**
RAG was implemented to allow the DM agent to access world lore information and story progress information stored in the form of text files in the 'data' folder.  This ability for the DM agent was implemented as a tool call, so that RAG operations would not be performed every time the agent's turn in the chat occurred.  This implementation proved to be difficult to test, and to be fully useful and fully testable would require a significantly larger amount of information stored than was used for initial testing purposes.  Additionally, this further testing could reveal that the DM agent needs to be adjusted so that it gives useful and relevant input to the RAG tool call, as initial tests showed it had a tendency to be overly specific, resulting in an empty response from the RAG call. However, a separate file (called 'RAG_operations') was used to confirm that the RAG operations worked separate from the tool call.  Thus, although the combination of RAG operations and tool calls was difficult to test and confirm effectiveness, the separate components were confirmed to work and the problems almost certainly result from a lack of lore data to test on. 

**6.0 Additional Tools/Innovations** 
There were no additional tools added into the system. 

**7.0 Code Quality & Modular Design**
The code quality of this project has prioritized reducing time-costly operations (such as RAG), and clarity through commenting.  Additionally, a module design has been accomplished by splitting the key functionalities into separate files.  For example, the main program runs in the file main.py, but RAG functionality is written in the RAG_operations, and each tool call has a separate file in the tool_calls folder.  Additionally, each model (both the DM and the trader) has a separate file for their initial prompts. This modularity not only allows for easy scalability, where new features can be added cleanly and easily, but also reduces merge conflicts when a team is working on this proejct together.