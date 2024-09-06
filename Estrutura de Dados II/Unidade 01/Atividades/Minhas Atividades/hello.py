import time
def slotword(words):
    for i, char in enumerate(words):
        for j in range(65, ord(char) + 1):
            print(words[:i] + chr(j))
            time.sleep(0.01)

word = "Saboia"
for i, char in enumerate(word):
    for j in range(65, ord(char) + 1):
        print(word[:i] + chr(j))
        time.sleep(0.001)