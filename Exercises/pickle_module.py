import pickle
import requests

# getting and formating data
url = f"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = requests.get(url).text
dataRow = list(data.split("\n"))
rowList = [itm.split(',') for itm in dataRow]


# writing pkl file with data here data is 'rowList'
fileObj = open("irisData.pkl", "wb")  # File Object
pickle.dump(rowList, fileObj)
fileObj.close()


# Reading .pkl file using pkl
pklFile = "irisData.pkl"
fileobj = open(pklFile, "rb")
pklFileData = pickle.load(fileobj)
print(pklFileData[0:5])
