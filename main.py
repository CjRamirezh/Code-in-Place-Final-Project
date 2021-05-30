"""
This program will analyze a whatsapp chat from your choice, all you have to do is export a chat from
Whatsapp and save the .txt file in the same folder as the main.py archive, then run the program and
choose from the different options.
"""

def main():
    file_name = introduction()
    while True:
        selected_option = option_selection()
        if selected_option == "":
            break
        elif selected_option == "1":
            who_sent_more_whatsapps(file_name)
        elif selected_option == "2":
            who_sent_more_voice(file_name)
        else:
            print("Enter a valid number or press enter to exit\n")

def who_sent_more_voice(file_name):
    dict = {}
    with open(file_name) as f:
        next(f)
        for line in f:
            line = line.strip()
            if not line.startswith("[") and not line.startswith("\u200e"): continue
            person = line.split("]")
            person = person[1]
            person = person.split(":")
            person = person[0]
            person = person.strip()
            text = line.split("]")
            text = text[1]
            text = text.split(":")
            try:
                text = text[1]
                text = text.strip()
            except:
                continue
            if text.find("audio") != -1 and text.startswith("\u200e"):
                if person not in dict:
                    dict[person] = 1
                else:
                    dict[person] += 1
    sent_more = None
    voice_messages = []
    for per in dict:
        print(per, "has sent", dict[per], "voice message")
        voice_messages.append(dict[per])
        if sent_more is None or dict[sent_more] < dict[per]:
            sent_more = per
    if len(voice_messages) == 2:
        print(sent_more, "has sent more voice messages,", max(voice_messages) - min(voice_messages), "more exactly")
    else:
        print(sent_more, "has sent more voice messages")
    print(""
          "")


def who_sent_more_whatsapps(file_name):
    dict = {}
    with open(file_name) as f:
        next(f)
        for line in f:
            line = line.strip()
            if not line.startswith("[") and not line.startswith("\u200e"): continue
            person = line.split("]")
            person = person[1]
            person = person.split(":")
            person = person[0]
            person = person.strip()

            if person not in dict:
                dict[person] = 1
            else:
                dict[person] += 1

    sent_more = None
    chats = []
    for per in dict:
        print(per, "has sent", dict[per], "Whatsapps")
        chats.append(dict[per])
        if sent_more is None or dict[sent_more] < dict[per]:
            sent_more = per
    if len(chats) == 2:
        print(sent_more, "has sent more Whatsapps,", max(chats) - min(chats), "more exactly")
    else:
        print(sent_more, "has sent more Whatsapps")
    print(""
          "")


def option_selection():
    """
    Ask the user for an option
    :return: selected_option
    """
    selected_option = input("Enter the number of the option you want:\n"
                            "1. Who sent more Whatsapps\n"
                            "2. Who sent more voice messages\n\n"
                            "leave blank to exit\n")
    return selected_option

def introduction():
    """
    This function introduces the user to the program and ask for a chat text file
    :return: file_name
    """
    print("""
     _____________________________________________________
    |      ¡WELCOME TO THE WHATSAPP CHAT ANALYZER!        |
    | ENTER THE NAME OF THE CHAT FILE YOU WANT TO ANALYZE |
    |          THEN SELECT THE OPTION YOU WANT            |
    |_____________________________________________________|
    """)

    file_name = input("(press enter to default name)\n"
                      "Enter the name of the chat file to analyze: ")

    if file_name == "":
        file_name = "_chat.txt"

    print("Analizing", file_name, "...")
    print("")
    return file_name

if __name__ == '__main__':
    main()