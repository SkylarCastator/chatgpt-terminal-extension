from langchain.llms import OpenAI
from langchain import PromptTemplate

template = """Quesitn: {question}

Answer: """

prompt = PromptTemplate(
    template=template,
    input_variables=['question'])

davinci = OpenAI(model_name="text-davinici-003")

#llm_chain = LLMChain(
#    promp=prompt,
#    llm=davinci
#)

#print(llm_chain.run(quesiton="What is your name?"))

#)

