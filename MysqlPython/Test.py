from MysqlPython.PlayerSearch import DB_Queries

query = DB_Queries()
str = query.makeQuery("미정", "미정", "필라델피아", "150", "이상", "70", "이상")
print(str)

