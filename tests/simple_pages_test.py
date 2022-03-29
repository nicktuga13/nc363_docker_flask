"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""

    response = client.get("/")
    assert response.status_code == 200
    assert b'<a href="/about" class="nav-link">About</a>' in response.data
    assert b'<a href="/page1" class="nav-link">Git</a>' in response.data
    assert b'<a href="/page2" class="nav-link">Docker</a>' in response.data
    assert b'<a href="/page3" class="nav-link">Python/Flask</a>' in response.data
    assert b'<a href="/page4" class="nav-link">Continuous Integration</a>' in response.data
    assert b'<a href="/page5" class="nav-link">OOP</a>' in response.data
    assert b'<a href="/page6" class="nav-link">AAA</a>' in response.data
    assert b'<a href="/page7" class="nav-link">Calculator Principles</a>' in response.data
    assert b'<a href="/page8" class="nav-link">Calculator Design</a>' in response.data
    assert b'<a href="/page9" class="nav-link">Pylint</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200


def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200


def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200


def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200


def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200


def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 200


def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/page6")
    assert response.status_code == 200


def test_request_page7(client):
    """This makes the index page"""
    response = client.get("/page7")
    assert response.status_code == 200


def test_request_page8(client):
    """This makes the index page"""
    response = client.get("/page8")
    assert response.status_code == 200


def test_request_page9(client):
    """This makes the index page"""
    response = client.get("/page9")
    assert response.status_code == 200


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page10")
    assert response.status_code == 404
