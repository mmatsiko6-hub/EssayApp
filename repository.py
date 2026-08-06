from database import get_connection

def create_essay(essay):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
    INSERT INTO essays (title,author_name, body, status)
    VALUES (:1, :2, :3, :4)
    """

    cursor.execute(
        sql,
        (
            essay.title,
            essay.author_name,
            essay.body,
            essay.status,
        )
    )
    connection.commit()

    cursor.close()
    connection.close()

    return {
        "title": essay.title,
        "author_name": essay.author_name,
        "body": essay.body,
        "status": essay.status
    }

def get_essay_by_id(essay_id):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
    SELECT essay_id, title, author_name, body, status
    from essays
    WHERE essay_id = :1
    """
    cursor.execute(sql, (essay_id,))
    row = cursor.fetchone()

   
    if row is None:
        return None

    essay = {
        "essay_id": row[0],
        "title": row[1],
        "author_name": row[2],
        "body": row[3].read(),
        "status": row[4]
    }

    cursor.close()
    connection.close()

    return essay

def update_essay(essay_id, essay):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
    update essays
    set title = :1,
        author_name = :2,
        body = :3,
        status = :4
    where essay_id = :5
    """

    cursor.execute(
        sql,
        (
            essay.title,
            essay.author_name,
            essay.body,
            essay.status,
            essay_id
        )
    )

    connection.commit()

    rows_updated = cursor.rowcount

    cursor.close()
    connection.close()

    return rows_updated
    