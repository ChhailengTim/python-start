def convert_emoji(message):
    words = message.split()
    emoji = {
        ":)": "😁",
        ":(": "😪"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "

    print(output)


messages = input("> ")
print(convert_emoji(messages))
