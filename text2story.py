from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from prompts import story_prompt

load_dotenv(find_dotenv())

llm = ChatOpenAI(model_name='gpt-3.5-turbo',
                 temperature=1)

story_chain = LLMChain(llm=llm,
                       prompt=story_prompt)