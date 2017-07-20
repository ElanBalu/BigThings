import pandas as pd
from pymongo import MongoClient

class WinError(Exception):
	""" MongoDB Connection error Will be print Here"""
	pass

fileLocation = "C:\Elan\StudyMeterial\Python Bible\File\Titanic.csv"

fileContent = pd.read_csv(fileLocation,header = 0,index_col=0)
mongoClient = MongoClient('localhost',27017)

db = mongoClient.pythonIns

collection = db.pythonCol

data_array = fileContent.iloc[:,[0,4]]

for key,val in data_array.iterrows():
	try:
		collection.insert_one({"name":val["Name"],"survived":val["Survived"]})
		print(val["Name"] + "====" + val["Survived"])
	#print(val)
	#	print(val[:])
	except Exception as e:
		print(e)
		break
	except:
		print("error Occured")
		break
	

