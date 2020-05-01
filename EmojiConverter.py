# Emoji Converter
while True:
    message=input("> ")
    words=message.split(" ")
    emojis={
        ":)":"🙂",
        ":(":"🙁",
        "B)":"😎",
        ":D":"😃",
        ":p":"😋",
        ":|":"😐",
        ":*":"😘",
        ":o":"😮"
        }
    output=""
    for word in words:
      output+=emojis.get(word,word)+" "
      
      print(output)
