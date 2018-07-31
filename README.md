# 2018 / 7 / 31
# Mongodb基本指令 : 
```
show dbs                #看所有資料庫名稱
show collections        #看所有集合名稱
db.[ ].find().pretty()  #看集合的所有資料
db.[ ].find()           #看集合的資料
```
```
db.dropDatabase()       #刪除資料庫
db.[ ].drop()           #刪除集合
db.collection.remove()  #刪除(欲刪除文檔)
```
```
use [db]                #使用資料庫
db.[ ].insert()         #創建集合並在()中給資料
db.collection.update()  #更新(欲更新文檔)
```
# pymongo基本語法
# http://www.runoob.com/python3/python-mongodb.html

# 學習github基本操作並上傳作業
```
git clone
git add .
git status
git commit -m ""
git push
```