from textnode import TextNode, TextType

def main():
    tt = TextType.TEXT
    tn = TextNode("Hello World", tt, "google.com")
    print(tn)


main()
