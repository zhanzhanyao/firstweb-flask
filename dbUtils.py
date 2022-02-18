class dbUtils:
    def __init__(self, dbName):
        import sqlite3

        self.conn = sqlite3.connect(dbName)

    def db_action(self, sql, actionType=0):
        """进行相关业务操作"""
        try:
            res = self.conn.execute(sql)
            if actionType == 1:
                # 查询业务，返回查询列表
                return res.fetchall()
            else:
                # 代表新增、删除、更新业务，返回逻辑值
                return True
        except ValueError as e:
            print(e)

    def close(self):
        self.conn.commit()
        self.conn.close()


# 创建数据库
db = dbUtils("firstweb_flask.db")
# 创建新闻表
sql = "create table news (newsid int, content text, author text)"
if db.db_action(sql, 0) == True:
    print("创建新闻表成功")
else:
    print("新闻表创建失败")
sql = "insert into news value(1, 'This weekend, there's no more need to practice your accio manuscript spells', 'Yao')"
if db.db_action(sql, 0) == True:
    print("新增新闻表成功")
db.close()
