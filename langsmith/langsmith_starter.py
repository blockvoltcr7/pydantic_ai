from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
llm.invoke("Hello, world!")
llm.generate("Hello, world!")

# print the output
print(llm.invoke("Hello, world!"))
# print(llm.generate("Hello, world!"))
