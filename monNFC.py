import pymongo
import serial
import time    


ser = serial.Serial("COM4",115200,timeout= 0.5) 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NFCdata"]

#dblist = myclient.database_names()
print (ser.name)
#print (dblist)
n=0
localtime = time.asctime( time.localtime(time.time()) )
id_dic={}
while True:
    value = ser.readline()
    ID = ''
    
    if (len(value)==13):
        ID=''
        value = str(value)
        for i in range(2,13):
            ID += value[i]

        if (ID in id_dic):
            mycol = mydb[id_dic[ID]]
            userData = { "ID" : ID, "time" : str(localtime)}
            insertData = mycol.insert_one(userData)
        else:
            n += 1
            user = 'user' + str(n)
            id_dic[ID] = user
            mycol = mydb[user]
            userData = { "ID" : ID, "time" : str(localtime)}
            insertData = mycol.insert_one(userData)
        print(id_dic)
        for data in mycol.find():
            print(data)

        
             
        #     user = 'user'+str(dic[show])
        #     mydict = { "ID" : show, "time" : str(localtime)}
        #     x = mycol.insert_one(mydict)
            

        # for i in collist:
        #     dic[]
        #     if (show in idlist):
                
        #     else:    
        #         mycol = mydb[i]
        #         z = mycol.find_one()
        #         idlist.append(z["ID"])

        # if (show in idlist):
        #     mycol = mydb[]
        #     mydict = { "ID" : show, "time" : str(localtime)}
        #     x = mycol.insert_one(mydict)
        # else:
        #     n += 1
        #     user = 'user'+str(n)
        #     mycol = mydb[user]
        #     mydict = { "ID" : show, "time" : str(localtime)}
        #     x = mycol.insert_one(mydict)
        
        # mycol = mybd[collist]
        # for x in mycol.find():
        #     print(x)


        # print (idlist)


        # print (show +" "+ str(localtime))
        # if (show in dic):
        #     print (dic)
        #     mycol = mydb[user+dic[show]]
        #     user = 'user'+str(dic[show])
        #     mydict = { "ID" : show, "time" : str(localtime)}
        #     x = mycol.insert_one(mydict)
        #     #fi = mycol.find()
        #     # for i in fi:
        #     #     print (i)
        #     n = int(dic[show])
        #     print (user + " " + show +" "+ str(localtime))
            
            
        # else:
        #     n+=1
        #     dic[show]=str(n)
        #     print (dic)
        #     user = 'user'+str(n)
        #     mycol = mydb[user]
        #     mydict = { "ID" : show, "time" : str(localtime)}
        #     x = mycol.insert_one(mydict)
        #     #fi = mycol.find()
        #     # for i in fi:
        #     #     #print (i)
        #     print (user + " " + show +" "+ str(localtime))