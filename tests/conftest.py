"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name

import pytest
from app import create_app, User
from app.db import db


@pytest.fixture()
def application():
    """This makes the app"""
    application = create_app()
    application.config.update(
        #will save to the database file you can view
        ENV='development',
        #will save to memory / you can't see but runs fast
        #ENV='testing',

    )
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        #drops the database tables after the test runs
        db.drop_all()


@pytest.fixture()
def add_user(application):
    """ Adding a user to the application's database """
    with application.app_context():
        #new record
        user = User('keith@webizly.com', 'testtest', 0)
        db.session.add(user)
        db.session.commit()


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()
