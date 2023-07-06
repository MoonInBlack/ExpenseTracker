from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()

    def create_conection(self):
        # подключение к SQlite3 и таблицы если ее нет

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        # драйвер бд

        db.setUserName('expense_db.db')
        # имя бд

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не удается открыть базу данных",
                                          "Нажмите Cancel для выхода.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        # создать query для выполнение запроса на создание таблицы expenses

        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Balance REAL, Responsible VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        # запрос на добавление, редактирование, удаление записей, подсчет сумм в бд

        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        query.exec()

    def add_new_transaction_query(self, date, balance, responsible):
        # запрос на добавление записей в таблицу бд

        sql_query = "INSERT INTO expenses (Date, Balance, Responsible) VALUES (?,?,?)"
        self.execute_query_with_params(sql_query, [date, balance, responsible])

    def update_transaction_query(self, date, balance, responsible):
        # запрос на редактирование записей в таблице бд

        sql_query = "UPDATE expenses SET Date=?, Balance=?, Responsible=?, WHERE ID=?"
        self.execute_query_with_params(sql_query,
                                       [date, balance, responsible, id])

    def delete_transaction_query(self, id):
        # запрос на удаление записей в таблице бд

        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        # общая функция для подсчета сумм для полей

        sql_query = f"SELECT SUM ({column}) FROM expenses"
        if filter is not None and value is not None:
            sql_query += f"WHERE {filter} = ?"

        query_values = []
        # список значений для подстановки запросов

        if value is not None:
           query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0)) + 'шт'

        return '0'

    # вызываем метод get_total передаем ему параметры фильтрации и получаем результат
    def total_balance(self):
        return self.get_total(column="Balance")

    def total_min(self):
        return self.get_total(column="Balance", filter="Responsible", )












        

