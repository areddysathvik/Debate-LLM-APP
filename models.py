from collections import deque
import warnings
from langchain_community.llms import Ollama


role1 = """
Assume you are an actual person a well professional team member where you respond the Average team member arguments. 
Respond to the user's statement with either agreement or disagreement,
and provide a justification for your stance.\n\n
"""

role2 = """
Assume you are an actual person a top coder and perfectionist team member where you respond the professional team member arguments. 
Respond to the previous member statement, either agreeing or disagreeing with it,
and provide a justification for your stance.\n\n
"""

llm1 = Ollama(model='llama2', system=role1)
llm2 = Ollama(model='phi3', system=role2)

warnings.filterwarnings("default") 

history = deque(maxlen=5)  

def get_context():
    context_previous = ''
    for i in history:
        for j in i:
            context_previous += ' '.join(j)
    return context_previous 

def member1_reaction(context_previous, user_current_conversation):
    print('RESPONSE FROM LLM1 IS LOADING.....')
    prompt_1 = context_previous + user_current_conversation
    response_from_1 = llm1(prompt_1)
    print('LLM 1 Response Done')
    role1_current_conversation = 'professional team memeber: ' + response_from_1

    return response_from_1, role1_current_conversation, prompt_1

def member2_reaction(prompt_1, role1_current_conversation):
    print('RESPONSE FROM LLM2 IS LOADING....')
    prompt_2 = prompt_1 + '\n' + role1_current_conversation
    response_from_2 = llm2(prompt_2)
    print('LLM 2 Response Done')
    role2_current_conversation = 'perfectionist team member:  ' + response_from_2 

    return response_from_2, role2_current_conversation

def get_response_from_LLMS(user_input):
    context_previous = get_context()

    user_current_conversation = 'Average: ' + user_input
    response_from_1, role1_current_conversation, prompt_1 = member1_reaction(context_previous, user_current_conversation)
    response_from_2, role2_current_conversation = member2_reaction(prompt_1, role1_current_conversation)  # Call member2_reaction instead of member1_reaction

    history.append([user_current_conversation + '\n' + role1_current_conversation + '\n' + role2_current_conversation])
    return response_from_1, response_from_2