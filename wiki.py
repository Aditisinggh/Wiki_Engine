import wikipedia as wiki
import os


__all__ = ['search','get_result']


def pretty_print(title):
    width = os.get_terminal_size()[0]
    print('='*width)
    print('{}'.format(title.center(width)))
    print('='*width)

def search():
    """
    Search a possible list of contents on Wikipedia page matching your query.
    In case of any disambiguation, it recursively provides a better, more clear alternative to your search term.
    """ 
    os.system('cls')
    topic = input("Enter your search query (Press X to Quit):")
    if topic.lower()=='x':
        exit(0)
    res = wiki.search(topic)
    if len(res)==1:
        return res[0]
        
    elif res == []:
        if wiki.suggest(topic) != None:
            print("You want to search for: {}?".format(wiki.suggest(topic)))
            ch = input("Enter Y(Yes) to continue or any other key to search other term:")
            if ch.lower()=='y' or ch.lower()=='yes':
                return wiki.suggest(topic)
        else:
            print("Sorry, no content matches your query.\nTry with another term.")
        return(search())
    else:
        print("\nSuggested topics are:")
        for i,r in enumerate(res,1):
            print('{}. {}'.format(i,r))
        ch = int(input("Press corresponding number to read about any term from the suggestions:"))
        if ch in range(1,len(res)+1):
            return res[ch-1]
        else:
            print("Sorry, your term is not in given suggestions\nCarrying on with the original query...")
            return res[0]


def get_result():
    while True:
        
        t = search()
        while True:
            try:
                print()
                print(wiki.summary(t,sentences=3))
            except wiki.DisambiguationError as e:
                print("You need to be a little more specific.\nChoose among the following:")
                for i,r in enumerate(e.options,1):
                    print( '{}. {}'.format(i,r))
                t = int(input("Your choice:"))
                t = e.options[t-1]
                continue
                
            break        
        while True:      
            val = input("\n1.(R)ead Full Article\t\t 2.(S)earch other term \t\t 3.(B)ack to Main Screen\t\t 4.(E)xit Application\nChoice:")
            if val.lower() in '1234rsbe':
                break
            else:
                print("Sorry, not a valid option.... Chhoose again")
        if val=='1' or val.lower()=='r':
            os.system('cls')
            pretty_print(wiki.page(t).title)
            print(wiki.page(t).content)
            print("\n\nTo look on Wikipedia, follow this link: {}".format(wiki.page(t).url))
            while True:
                val = input("\n 2.(S)earch other term \t\t 3.(B)ack to Main Screen\t\t\4.(E)xit Application\nChoice:")
                if  val.lower in '234sbe':
                    break
                else:
                    print("\nSorry Invalid choice, Choose again")
        if val=='2' or val.lower()=='s':
            continue
        elif val=='3' or val.lower()=='b':
            break
        else:
            exit(0)




if __name__=='__main__':
    get_result()
        
