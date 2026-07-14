import pytest
from yougile_api import YougileAPI


@pytest.fixture
def api():
    return YougileAPI()


@pytest.fixture
def created_project(api):
    title = "Test Project"
    response = api.create_project(title)
    project_id = response.get("id")
    yield project_id
    if project_id:
        try:
            api.delete_project(project_id)
        except Exception:
            pass
