class Telephone:
    rental = 300
    def call(self):
        print("Calling")

    def receive(self):
        print("Receiving")

class Mobile(Telephone):
    rental = 400
    def chat(self):
        print("Chatting")

nokia = Mobile()
nokia.chat()
nokia.call()
nokia.receive()
print(nokia.rental)
