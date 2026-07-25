from sqlalchemy import create_engine, text


DB_CONNECTION_STRING = (
    "postgresql://postgres:millsqueen@localhost/QA"
)
db = create_engine(DB_CONNECTION_STRING)


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['subject_id'] == 1
    assert row1['subject_title'] == "English"
    connection.close()


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "INSERT INTO subject(\"subject_title\") VALUES (:new_title)"
    )
    connection.execute(sql, {"new_title": 'Предмет для тестирования'})

    result = connection.execute(
        text("SELECT * FROM subject WHERE subject_title = :title"),
        {"title": "Предмет для тестирования"}
    )
    rows = result.mappings().all()
    assert len(rows) == 1

    sql_delete = text("DELETE FROM subject WHERE subject_title = :title")
    connection.execute(sql_delete, {"title": 'Предмет для тестирования'})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql_insert = text(
        "INSERT INTO subject(\"subject_title\") VALUES (:new_title)"
    )
    connection.execute(sql_insert, {"new_title": 'Новый предмет'})

    sql_update = text(
        "UPDATE subject "
        "SET subject_title = 'updated' "
        "WHERE subject_title = :title"
    )
    connection.execute(sql_update, {"title": 'Новый предмет'})

    result = connection.execute(
        text("SELECT * FROM subject WHERE subject_title = :title"),
        {"title": "updated"}
    )
    rows = result.mappings().all()
    assert len(rows) == 1

    sql_delete = text("DELETE FROM subject WHERE subject_title = :title")
    connection.execute(sql_delete, {"title": 'updated'})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql_insert = text(
        "INSERT INTO subject(\"subject_title\") VALUES (:new_title)"
    )
    connection.execute(sql_insert, {"new_title": 'Предмет для удаления'})

    result = connection.execute(
        text("SELECT * FROM subject WHERE subject_title = :title"),
        {"title": "Предмет для удаления"}
    )
    rows = result.mappings().all()
    assert len(rows) == 1

    sql_delete = text("DELETE FROM subject WHERE subject_title = :title")
    connection.execute(sql_delete, {"title": 'Предмет для удаления'})

    transaction.commit()
    connection.close()
