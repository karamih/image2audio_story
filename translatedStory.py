from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from dotenv import load_dotenv, find_dotenv
from prompts import translation_prompt


load_dotenv(find_dotenv())

llm = ChatOpenAI(model_name='gpt-3.5-turbo')

translation_chain = LLMChain(prompt=translation_prompt,
                             llm=llm)