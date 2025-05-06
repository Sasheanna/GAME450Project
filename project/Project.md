**1.0 Base System Functionality**
This system acts as a Dungeons and Dragons Dungeon Master. The system is able to handle to following scenarios:
>1.1 Social encounters with NPC characters 
>1.2 Interactions with a trader NPC
>1.3 Dice rolling 
>1.4 Storing the player information within a character sheet
>1.5 Allows players to purchase items from traders
>1.6  

**2.0 Prompt Engineering and Model Parameter choices**

**3.0 Tools Usages**

**4.0 Planning and reasoning** 
**5.0 RAG Implementation**
RAG was implemented to allow the DM agent to access world lore information and story progress information stored in the form of text files in the 'data' folder.  This ability for the DM agent was implemented as a tool call, so that RAG operations would not be performed every time the agent's turn in the chat occurred.  This implementation proved to be difficult to test, and to be fully useful and fully testable would require a significantly larger amount of information stored than was used for initial testing purposes.  Additionally, this further testing could reveal that the DM agent needs to be adjusted so that it gives useful and relevant input to the RAG tool call, as initial tests showed it had a tendency to be overly specific, resulting in an empty response from the RAG call. However, a separate file (called 'RAG_operations') was used to confirm that the RAG operations worked separate from the tool call.  Thus, although the combination of RAG operations and tool calls was difficult to test and confirm effectiveness, the separate components were confirmed to work and the problems almost certainly result from a lack of lore data to test on. 
**6.0 Additional Tools/Innovations** 
**7.0 Code Quality & Modular Design**
The code quality of this project has prioritized reducing time-costly operations (such as RAG), and clarity through commenting.  Additionally, a module design has been accomplished by splitting the key functionalities into separate files.  For example, the main program runs in the file main.py, but RAG functionality is written in the RAG_operations, and each tool call has a separate file in the tool_calls folder.  Additionally, each model (both the DM and the trader) has a separate file for their initial prompts. This modularity not only allows for easy scalability, where new features can be added cleanly and easily, but also reduces merge conflicts when a team is working on this proejct together.