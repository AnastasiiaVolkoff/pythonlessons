from sqlalchemy import create_engine, text


class SubjectTable:
    __scripts = {
        "select": text("SELECT * FROM subject"),
        "insert_new": text(
            "INSERT INTO subject(\"subject_title\") "
            "VALUES(:new_title)"
        ),
        "update": text(
            "UPDATE subject "
            "SET subject_title = :new_title "
            "WHERE subject_title = :title"
        ),
        "delete": text("DELETE FROM subject WHERE subject_title = :title")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def add_subject(self, title):
        connection = self.__db.connect()
        transaction = connection.begin()
        result = connection.execute(
            self.__scripts["insert_new"],
            {"new_title": title}
        )
        transaction.commit()
        connection.close()
        return result

    def update(self, title, new_title):
        connection = self.__db.connect()
        transaction = connection.begin()
        connection.execute(
            self.__scripts["update"],
            {"title": title, "new_title": new_title}
        )
        transaction.commit()
        connection.close()

    def delete(self, title):
        connection = self.__db.connect()
        transaction = connection.begin()
        connection.execute(
            self.__scripts["delete"],
            {"title": title}
        )
        transaction.commit()
        connection.close()
