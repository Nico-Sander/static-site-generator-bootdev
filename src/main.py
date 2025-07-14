from textnode import TextNode, TextType

def main():
    tt = TextType("plain")
    tn = TextNode("Hello World", tt, "google.com")
    print(tn)


main()
