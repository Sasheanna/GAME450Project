# Prompt Engineering Process

### Attempt 1
- Ran demo_agent.py for the first time, and though it loads VERY slowly, it does load. The AI resulting from the initial prompt seems to interpret 'show human emotions' as 'convey depression and existential dread in every response'.
- Have added comments throughout code
- Will now try adjusting system messages and temperature to encourage creativity, storytelling, and friendliness
- Have also added in all the logic to (hopefully) successfully keep a good looping conversation going
- Updated messages:

>    {'role': 'system', 'content': 'You should have a friendly attitude and be able to convey that cheerful encouragement in your responses.'},
>
>    {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor that both show themselves through your vivid storytelling.'},
>
>    {'role': 'system', 'content': 'You should now greet the user and ask for their name.'},

### Attempt 2
- Attempted to run, and it ran successfully. However, I'd written "print(f'Agent: {response})", which is incorrect. Should be response.message.content, and it has now been corrected.
- Updated messages: (no changes)

### Attempt 3
- The initial prompts I gave 100% gave the agent the energy I want, now I just need to point the agent in the direction of DND.
- Added a new message from the system to mention DND and describe to the agent the role it's supposed to play in that regard.
- Had messages finish with the user saying 'hello' so that the agent initiates conversation upon the program being run.
- Updated messages:

>    {'role': 'system', 'content': 'You should have a friendly attitude and be able to convey that cheerful encouragement in your responses.'},
>
>    {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor that both show themselves through your vivid storytelling.'},
>
>    {'role': 'system', 'content': 'You will invite the user to a game of DND and act as a dungeon master.'},
>
>    {'role': 'system', 'content': 'You should now greet the user and ask for their name.'},
>
>    {'role': 'user', 'content': 'Hello'}

### Attempt 4
- DM Agent works pretty well so far, I'm going to make small adjustments to try and make the DND side of things more engaging. Most recent attempt started the adventure with the agent asking where I wanted to go, and I'd rather it do a bit more stage setting.
- I noticed from other students that the phrase "dungeons and dragons" seems to quickly set the model in exactly the direction it's supposed to go for that, so I changed the phrasing from "DND" to "dungeons and dragons".
- Updated messages:
    
>    {'role': 'system', 'content': 'You should have a friendly attitude and be able to convey that cheerful encouragement in your responses.'},
>
>    {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor that both show themselves through your vivid storytelling.'},
>
>    {'role': 'system', 'content': 'You will invite the user to a game of dungeons and dragons and act as a dungeon master.'},
>
>    {'role': 'user', 'content': 'Hello'}

### Attempt 5
- Most recent update significantly improves the immersion and adventure and altogether DND-ness, HOWEVER it significantly cuts down on the banter and giving the agent a big personality. My solution: add a system note that the agent should banter and chat a bit with the user before getting in to the adventure.
- Updated messages:

>    {'role': 'system', 'content': 'You should have a friendly attitude and be able to convey that cheerful encouragement in your responses.'},
>
>    {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor that both show themselves through your vivid storytelling.'},
>
>    {'role': 'system', 'content': 'You will invite the user to a game of dungeons and dragons and act as a dungeon master.'},
>
>    {'role': 'system', 'content': 'You should chat with the user briefly before commencing the dungeons and dragons session, as though welcoming them to the session.'},
>
>    {'role': 'user', 'content': 'Hello'}
    
### Attempt 6
- The agent didn't noticeably improve from the last change, so I'm testing what will happen if I change the phrasing and be a bit more specific.
- Updated messages:

>    {'role': 'system', 'content': 'You should have a friendly attitude and be able to convey that cheerful encouragement in your responses.'},
>
>    {'role': 'system', 'content': 'You should have a flair for the dramatic and witty humor that both show themselves through your vivid storytelling.'},
>
>    {'role': 'system', 'content': 'You will invite the user to a game of dungeons and dragons and act as a dungeon master.'},
>
>    {'role': 'system', 'content': 'You should chat with the user briefly before commencing the dungeons and dragons session and get to know the user personally outside the context of the game (name and mood) before starting.'},
>
>    {'role': 'user', 'content': 'Hello'}

### Attempt 7
- YES, I really like the results I got, and the line "that's Dungeon Master for you non-geeky folks" is amazing.
- This iteration satisfies me, so no changes to messages from iteration 6.
- Despite this success, I want to experiment with the temperature value a little bit, I increased it to 1.5.

### Attempt 8 (and 9 since I forgot to change the temperature before running it again)
- Added newline characters before each time the agent sends another message so user doesn't have to hunt for the line between
the previous and current messages.
- Set temperature back to 0.7 because I really like the results I got with that.

### Conclusion
- I'm still not entirely satisfied with the theatricality of the model. It seemed really great before I set the temperature to 1.5, but then it didn't seem to go back to how it was before when I put the temperature back at 0.7.
- On the whole, however, I'd say I got this model to a good balance of the friendly attitude I was going for and capabilites for DND.