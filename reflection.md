# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? We were given a terrible hint, and when the game was over, the new game button doesn't work at all.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The range for the number is static and doesn't change even after changing the difficulty. Whenever we insert a guess, we keep getting an incorrect hint that doesn't help in figuring out the number.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude to find and fix these bugs.
Claude recommended keeping the “string secret glitch” behavior (sometimes converting secret to a string) and handling it with try/except TypeError + string comparisons.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI pointed out that the hint logic in check_guess() was reversed (it said “Go HIGHER” when the guess was already too high). I fixed the messages and verified it by testing guesses above and below the secret number to confirm the hints were confirm the hints were correct.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI suggested handling comparisons by converting the secret number to a string and comparing strings. This was misleading because string comparisons don’t follow numeric order (e.g., "9" > "10"). I verified the issue by testing guesses and noticing incorrect “Too High/Too Low” results, so I removed the string conversion and kept everything as integers.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I checked by running the streamlit app and then looking if the bug was fixed. For example, I checked to see if the new game button was working properly after getting a correct guess which in this case I reviewed and asserted that was the case.
- Describe at least one test you ran (manual or using pytest) I used pytest to check if the new game was properly working and also to check if the number of guess changed as the level of difficulty changed. 
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app. This was because of streamlit because every time the user interacts with the app by clicking a butotn, the entire python script reruns from top to button.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? May use an example like a word document that deletese its content after typing a character, or a videogame that deletes all game progress each time they complete a quest, and a session state is like chest where we can store loot and he gets to keep even after all his progress is deleted.
- What change did you make that finally gave the game a stable secret number? The fix was moving the secret number into st.session_state in that way we get to keep our secret number even after streamlit reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? Always test the core logic functions with pytest before trusting the UI. 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task? Ask the AI to explain why before applying its suggestion, so in that way I can better understand the code and avoid making a new bug instead of fixing the previous one.
- In one or two sentences, describe how this project changed the way you think about AI generated code. AI-generated code looks correct at a glance but can have subtle logical errors that only show up at runtime. So it's always good to check for this bugs and understand the code that AI generated.
