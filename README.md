# Web UI Chatbot
Hello everyone, this is my a new chatbot with some major changes:
1. used python totally as an API.
2. Build fronted from scratch, using HTML, CSS and JS.
3. Used flask to host the server locally
## here's the step-by-step guide for setup and run this chatbot locally:
Step 1:
Clone this Repo into your local device
or
paste this into your terminal:
 ```bash
 git clone https://github.com/sarvdny/web-ui-chatbot
 ```
Step 2:
Open the folder `web-ui-chatbot`.
or
paste this into your terminal:
```bash
cd web-ui-chatbot
```
Step 3:
Create a `.env` file
Step 4:
Paste this into your `.env` file:
```code
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
OPENAI_MODEL="YOUR_PREFERRED_OPENAI_MODEL"
OPENAI_BASE_URL="YOUR_OPENAI_BASE_URL"
```
Step 5:
type this into your terminal:
```bash
uv sync
uv run main.py
```
And you are done! your chatbot is online.
### Things to keep in mind:
- This bot doesn't use memory. Means the chatbot doesn't remember the previous chats after giving a prompt.
- If you facing any problrm related to `uv`, please check the official uv docs [Here](https://docs.astral.sh/uv/).
---
be free to give some suggestions to this bot. Thankyou! 

Happy Coding
