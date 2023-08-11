import psycopg2
from tests import database_methods, methods
from pytest_bdd import scenario, given, when, then, parsers
import os

current_script_path = os.path.abspath(__file__)
root_dir = os.path.dirname(current_script_path)
path1 = os.path.join(os.path.dirname(os.path.dirname(root_dir)), "tests")


@scenario('../features/db-testing.feature', 'Testing the DB')
def test_db():
    pass


creation = path1 + '/Database_queries/creation.sql'
insertion = path1 + '/Database_queries/insertion.sql'
retrieval = path1 + '/Database_queries/retrieval.sql'
DB_credentials = path1 + '/testData/DBcredentials.properties'


@given(parsers.parse('User tests DB'))
def db_connection():
    dbname = methods.get_data(DB_credentials, 'details', 'dbname')
    user = methods.get_data(DB_credentials, 'details', 'user')
    password = methods.get_data(DB_credentials, 'details', 'password')
    host = methods.get_data(DB_credentials, 'details', 'host')
    port = methods.get_data(DB_credentials, 'details', 'port')
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    yield conn
    conn.close()


@then(parsers.parse('User verifies DB operations with "{input_value}"'))
def insert_and_fetch(input_value, db_connection):
    database_methods.creation_table(db_connection, creation)
    database_methods.insert_value(db_connection, insertion)
    fetched_value = database_methods.fetch_value(db_connection, retrieval)
    assert (fetched_value == input_value), f"Expected {input_value}, but got {fetched_value}"
