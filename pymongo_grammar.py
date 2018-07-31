import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
x = mycol.insert_one(mydict) #插入單一

mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
x = mycol.insert_many(mylist) #插入多個
 
myquery = { "name": "Taobao" } 
mycol.delete_one(myquery) #刪除
mydoc = mycol.find().sort("alexa") #排序

myquery = { "alexa": "10000" }
newvalues = { "$set": { "alexa": "12345" } }
mycol.update_one(myquery, newvalues) #更新

for x in mycol.find():#查詢
  print(x)
for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1 }):#查詢指定文檔
  print(x)