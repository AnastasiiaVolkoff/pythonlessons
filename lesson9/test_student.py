from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:millsqueen@localhost/QA"
db = create_engine(db_connection_string)


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['subject_id'] == 1
    assert row1['subject_title'] == "English"


def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("insert into subject(\"subject_title\") values (:new_title)")
    new_id = connection.execute(sql, {"new_title": 'Предмет для тестирования'})
    assert new_id is not None

    result = connection.execute(
        text("SELECT * FROM subject WHERE subject_title = :title"),
        {"title": "Предмет для тестирования"}
    )
    rows = result.mappings().all()
    assert len(rows) == 1

    sql = text("DELETE FROM subject WHERE subject_title = :title")
    connection.execute(sql, {"title": 'Предмет для тестирования'})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("insert into subject(\"subject_title\") values (:new_title)")
    new_id = connection.execute(sql, {"new_title": 'Новый предмет'})
    assert new_id is not None

    sql = text(
        "UPDATE subject "
        "SET subject_title = 'updated' "
        "WHERE subject_title = :title"
    )
    connection.execute(sql, {"title": 'Новый предмет'})
    result = connection.execute(
        text("SELECT * FROM subject WHERE subject_title = :title"),
        {"title": "updated"}
    )
    rows = result.mappings().all()
    assert len(rows) == 1
    sql = text("DELETE FROM subject WHERE subject_title = :title")
    connection.execute(sql, {"title": 'updated'})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("insert into subject(\"subject_title\") values (:new_title)")
    new_id = connection.execute(sql, {"new_title": 'Предмет для удаления'})
    assert new_id is not None

    result = connection.execute(
        text("SELECT * FROM subject WHERE subject_title = :title"),
        {"title": "Предмет для удаления"}
    )
    rows = result.mappings().all()
    assert len(rows) == 1
    sql = text("DELETE FROM subject WHERE subject_title = :title")
    connection.execute(sql, {"title": 'Предмет для удаления'})

    transaction.commit()
    connection.close()
