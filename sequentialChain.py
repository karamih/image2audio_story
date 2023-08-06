from langchain.chains import SimpleSequentialChain
from text2story import story_chain
from translatedStory import translation_chain


chain = SimpleSequentialChain(chains=[story_chain, translation_chain])