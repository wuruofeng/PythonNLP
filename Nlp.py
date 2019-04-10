from aip import AipNlp
import time
APP_ID = 'ur_id'
API_KEY = 'ur_key'
SECRET_KEY = 'ur_s_key'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

#DB

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="ur_password", # 数据库密码
    database="python"
)

mycursor = mydb.cursor()

sql_str = "SELECT itemTextP FROM weibodate "
sql = "UPDATE weibodate SET selfJudgement = %s WHERE id_num = %s "
mycursor.execute(sql_str)
myresult = mycursor.fetchall()  # myresult为text数组
for num in range(0,1000):
    text = myresult[num][0]
    p = client.sentimentClassify(text)
    sentiment = p["items"][0]["sentiment"]  # 情感级别 0是负向  1是中性  2是正向
    s = sentiment-1
    s1 = num
    temp = str(s)
    temp1 = str(s1)
    val = (temp, temp1,)
    mycursor.execute(sql, val)
    time.sleep(0.6)
    mydb.commit()
    time.sleep(0.6)
    print(mycursor.rowcount, " 条当前记录被修改,  共计修改了",num,"条")






# text = "以后吧，这一家人派一个代表治病就行了大大节约医疗资源啊。根据量子纠缠原理，实际上，都不用来医院，我国已经实现2000公里距离的量子纠缠通讯，足不出户就可以享受北京名医诊治。哇，北京中医药大学，牛啊脑洞开得够大够清奇但是，有人提出万一家里有一个娃其实是隔壁老王家的，咋办量 全文"
# 调用

# confidence = p["items"][0]["confidence"]  #置信度
# positive_prob = p["items"][0]["positive_prob"]  #积极类别的概率
# negative_prob = p["items"][0]["negative_prob"]  #消极类别的概率
# #print(text)
# print(sentiment)
# print(confidence)
# print(positive_prob)
# print(negative_prob)
