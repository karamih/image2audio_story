from langchain import PromptTemplate

pt_story = """
You are a story teller.
get the scenario and then create a creative and interesting story.
story should be under 20 words.
INPUT: {scenario}
STORY:
"""

story_prompt = PromptTemplate(input_variables=['scenario'],
                             template=pt_story)


translation_pt = """
You are a translator.
get the context and then translate it to Persian.
CONTEXT: {context}
TRANSLATED:
"""

translation_prompt = PromptTemplate(input_variables=['context'],
                                    template=translation_pt)