def search(strList, query):
    resultList = []
    for list in strList:
        if query.lower()  in list.lower():
            resultList.append(list)
    
    return resultList

if __name__ == "__main__":
    strList = ["this is python", "Hello python", "Python is Python"]
    print(search(strList, "python"))