def read_query_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def creation_table(db_connection, filename):
    query = read_query_from_file(filename)
    with db_connection.cursor() as cur:
        cur.execute(query)
        db_connection.commit()


def insert_value(db_connection, filename):
    query = read_query_from_file(filename)
    with db_connection.cursor() as cur:
        cur.execute(query)
        db_connection.commit()


def fetch_value(db_connection, filename):
    query = read_query_from_file(filename)
    with db_connection.cursor() as cur:
        cur.execute(query)
        result = cur.fetchone()
        return result[0] if result else None
