def searchContent(strl, query):
    '''Function to get search result from given array of string'''
    strlist = strl.split(" ")
    querylist = query.split(" ")
    score = 0
    for word1 in strlist:
        for word2 in querylist:
            if word1.lower() == word2.lower():
                score += 1

    return score


if __name__ == "__main__":
    # Assigining string list and taking query as user input
    strlist = ["hello python", "Python data science in python",
               "Py hub", "welcome to python world"]
    query = input("Enter your search query: ")

    # Putting scores returned by function for each sentence in a list
    scores = [searchContent(itm, query) for itm in strlist]

    # Putting scores along with sentence in list
    sItmList = [scoredItm for scoredItm in sorted(zip(scores, strlist), reverse=True) if scoredItm[0] != 0]

    # Printing results in the console
    print(f"\n{len(sItmList)} item found")
    for itm in sItmList:
        print(f"\"{itm[1]} \" -  {(itm[0] / sItmList[0][0])*100}% related with your search")
