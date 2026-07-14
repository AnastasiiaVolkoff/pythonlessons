from yougile_api import YougileAPI


# ---------- ПОЗИТИВНЫЕ ТЕСТЫ ----------

def test_create_project_positive(api):
    """Позитивный тест POST /projects – создание проекта."""
    title = "Новый проект"
    create_response = api.create_project(title)
    project_id = create_response.get("id")
    assert project_id is not None, "Не удалось создать проект"

    get_response = api.get_project(project_id)
    assert get_response.get("title") == title, (
        f"Название не совпадает. Ожидалось: {title}, "
        f"получено: {get_response.get('title')}"
    )


def test_get_project_positive(api, created_project):
    """Позитивный тест GET /projects/{id} – получение проекта."""
    project_id = created_project
    response = api.get_project(project_id)
    assert response.get("id") == project_id, "ID проекта не совпадает"
    assert response.get("title") is not None, "Название проекта отсутствует"


def test_update_project_positive(api, created_project):
    """Позитивный тест PUT /projects/{id} – обновление названия."""
    project_id = created_project
    new_title = "Обновлённое название"
    update_response = api.update_project(project_id, {"title": new_title})
    assert update_response.get("id") == project_id, "ID не совпадает после обновления"

    get_response = api.get_project(project_id)
    assert get_response.get("title") == new_title, (
        f"Название не обновилось. Ожидалось: {new_title}, "
        f"получено: {get_response.get('title')}"
    )


# ---------- НЕГАТИВНЫЕ ТЕСТЫ ----------

def test_create_project_negative_empty_title(api):
    """Негативный тест POST: создание проекта с пустым названием."""
    response = api.create_project("")
    assert response.get("statusCode") == 400, "Ожидался статус 400"
    assert "title should not be empty" in str(response.get("message", "")), (
        "Сообщение об ошибке не соответствует ожидаемому"
    )


def test_get_project_negative_invalid_id(api):
    """Негативный тест GET: несуществующий ID."""
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(invalid_id)
    assert response.get("statusCode") == 404, "Ожидался статус 404"
    assert "проект не найден" in str(response.get("message", "")).lower(), (
        "Сообщение об ошибке не соответствует ожидаемому"
    )


def test_update_project_negative_invalid_id(api):
    """Негативный тест PUT: обновление несуществующего проекта."""
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(invalid_id, {"title": "Новое имя"})
    assert response.get("statusCode") == 404, "Ожидался статус 404"
    assert "проект не найден" in str(response.get("message", "")).lower(), (
        "Сообщение об ошибке не соответствует ожидаемому"
    )


def test_update_project_negative_empty_title(api, created_project):
    """Негативный тест PUT: обновление с пустым названием."""
    project_id = created_project
    response = api.update_project(project_id, {"title": ""})
    assert response.get("statusCode") in (400, 422), (
        f"Ожидался статус 400 или 422, получен {response.get('statusCode')}"
    )
