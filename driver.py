import wikipedia
import wiki
import generate_random
import os
while True:
    os.system('cls')
    wiki.pretty_print("Hello Ma'am/Sir Welcome to the Wikipedia Search")
    print()
    print("Choose among the following:\n \
        1.(S)earch a term.\n \
        2.(R)ead Random Article.\n \
        3.(E)xit Application")

    x = input("Enter Choice:")
    if (x.lower() == "s" or x == "1"):
        wiki.get_result()

    elif(x.lower()=='r' or x=='2'):
        generate_random.main()
    
    elif(x.lower()=='e' or x=='3'):
        wiki.pretty_print('Thank You')
        exit(0)
    else:
        print("Sorry Invalid Choice\nPlease Enter Again...\n")
