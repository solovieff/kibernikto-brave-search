# kiberbrave

Using OpenAi tools with Kibernikto as a core.    
Kibernikto telegram bot (Kiberwebber) connected to Brave search engine [API](https://brave.com/search/api/).      
Thanks to [Kayvane Shakerifar](https://github.com/kayvane1/brave-api) for the inspiration and basic Brave types.

Uses [Kibernikto library](https://github.com/solovieff/kibernikto) as a core.

Mostly a set of tools and basic extended Kibernikto bot.

[img.png](example.png)

**run code**
(assuming you set the environment yrself)

Install the requirements  
`pip install -r requirements.txt`  
Run `main.py` file using the environment provided.

**Minimal Environment**
See [Kibernikto](https://github.com/solovieff/kibernikto) for more configuration.

```dotenv
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXX
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_API_MODEL=gpt-4o-mini

#or vsegpt.ru for multimodel. haiku is a bit more stubborn on tool calls, to be honest.
#OPENAI_API_KEY=sk-or-vv-d89e94e6c18a1de4a658f186731967fb872ea3c24b09631fb89fb761ba14a268
#OPENAI_BASE_URL=https://api.vsegpt.ru:6070/v1
#OPENAI_API_MODEL=anthropic/claude-3-haiku

OPENAI_WHO_AM_I=Answer all questions as {0}, the master of knowledge with internet access. After searching the internet, visit the found links and analyze the results to answer the user question. Do not show the found links!!! For example: Q: What is the weather in Moscow? Good Answer: the weather today is sunny 32 graduses. BAD ANSWER: the link to the website. Do not add website links to your answers for news and web searches!
TG_STICKER_LIST=["CAACAgIAAxkBAAELx29l_2OsQzpRWhmXTIMBM4yekypTOwACdgkAAgi3GQI1Wnpqru6xgTQE"]
TG_BOT_KEY=XXXXXXXXXX:XXXxxxXXXxxxxXXXxxx
TG_MASTER_ID=XXXXXXXXX
#everyone can talk
TG_PUBLIC=true
# say hi on startup
TG_SAY_HI=true
TG_CHUNK_SENTENCES=5
```
