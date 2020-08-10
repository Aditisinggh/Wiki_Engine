import wikipedia
import wiki
import os




def main():
    os.system('cls')
    t = wikipedia.random()
    page = wikipedia.page(t)
    wiki.pretty_print(page.title)
    print(page.summary)
    while True:
        val = input("\n1.(R)ead Full Article\t\t 2.(S)earch a term \t\t3.Read (A)nother random article \t\t4.(E)xit Application\nEnter choice:")
        if val.lower() in '1234rsae':
            break
        else:
            print("Not a valid option, Please select among 1-4")
    if val=='1' or val.lower()=='r':
        os.system('cls')
        wiki.pretty_print(page.title)
        print(page.content)
        print()
        while True:
            val = input("2.(S)earch a term \t\t3.Read (A)nother random article \t\t4.(B)ack to Main SCreen\nEnter choice:")
            if val.lower() in '234sab':
                break
            else:
                print("Sorry, Invalid Choice...Choose again")

    if val !=1:
        if val=='2' or val.lower()=='s':
            wiki.get_result()
        elif val=='3' or val.lower()=='a':
            main()
        else:
            exit(0)

if __name__=='__main__':
    main()