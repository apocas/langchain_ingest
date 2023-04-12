from langchain.chat_models import ChatOpenAI
from brain import Brain


def index(path, data):
    brain = Brain(path)
    brain.clear()
    brain.loadFolder(data)
    brain.index()
    brain.save()


def demo(path="./learning/dbs/finaldb/"):
    brain = Brain(path)

    brain.clear()

    brain.loadFileTXT("./learning/data/state_of_the_union.txt")
    brain.index()

    brain.wakeup()

    # print(brain.queryChain("Who are you?", 4))

    print(brain.ask("Who are you?") + "\n")  # I am the fing president

    print(brain.ask("What did the president say about Ketanji Brown Jackson") + "\n")
    print(brain.ask("Which president?") + "\n")

    print(brain.ask("Who is xiripiticompany?") + "\n")  # No idea...
    brain.loadFileTXT("./learning/data/xiripiti.txt")
    brain.index()
    print(brain.ask("Who is xiripiticompany?") + "\n")  # Enlightened


def play(path):
    brain = Brain(path=path, llm=ChatOpenAI(temperature=0))
    brain.wakeup()
    while True:
        print("AI: " + brain.ask(input("User: ")) + "\n")

def test(path):
    brain = Brain(path=path, llm=ChatOpenAI(temperature=0))
    brain.wakeup()
    print(brain.queryChain("write me some code in python to list all files in a folder?"))

index("./learning/dbs/testdb/", "./learning/data/")
#play("./learning/dbs/testdb/")
#test("./learning/dbs/testdb/")
