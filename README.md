# kiberbrave

Demonstrates how easy it is to use OpenAi tools with Kibernikto as a core.  
Basic telegram AI planner. Can use voice messages.  
Can be updated to retrieve plans etc, just a demo functionality for now.
Reminds of planned messages.
Uses [Kibernikto library](https://github.com/solovieff/kibernikto) as a core and is mostly here to show it's
capabilities.

**All you need to use functions with Kibernikto is:**

- Create you functions in 'tools' package and import them as in `main.py` file.
  See [tools/plan_event.py](https://github.com/solovieff/kibernikto-planner/blob/main/planner/tools/plan_event.py) for
  details. Pay attention to namings!
- Optionally: create Kibernikto child class to extend the functionality.  
  See [_kiberplanner bot](https://github.com/solovieff/kibernikto-planner/blob/main/planner/bots/tooler/_kiberplanner.py)
  it adds current time to default system message.
- Use your bot when running a dispatcher like `await comprehensive_dispatcher.async_start(Kiberplanner, tools_to_use)`
  in `main.py`

Mostly a set of tools and extended Kibernikto bots.

<img width="526" alt="image" src="https://github.com/solovieff/kibernikto-planner/assets/5033247/c3801b89-fa7f-4840-963b-db1a1c439214">


**run code**
(assuming you set the environment yrself)

Install the requirements  
`pip install -r requirements.txt`  
Run `main.py` file using the environment provided.

**Minimal Environment**

```dotenv
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXX
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_API_MODEL=gpt-4o
OPENAI_MAX_TOKENS=550
OPENAI_MAX_MESSAGES=5
OPENAI_TEMPERATURE=0.1

VOICE_PROCESSOR=openai
VOICE_FILE_LOCATION=/tmp
VOICE_OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXX
VOICE_OPENAI_API_MODEL=whisper-1
VOICE_OPENAI_API_BASE_URL=https://api.openai.com/v1

TG_REACTION_CALLS=["hi","hola", "plan", "schedule"]
TG_STICKER_LIST=["CAACAgIAAxkBAAELx29l_2OsQzpRWhmXTIMBM4yekypTOwACdgkAAgi3GQI1Wnpqru6xgTQE"]
TG_BOT_KEY=XXXXXXXXXX:XXXxxxXXXxxxxXXXxxx
TG_MASTER_ID=XXXXXXXXX
#everyone can talk
TG_PUBLIC=true
# say hi on startup
TG_SAY_HI=true
TG_CHUNK_SENTENCES=5

```
