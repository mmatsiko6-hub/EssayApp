from database import get_connection

def create_essay(essay):
    connection = get_connection()
    cursor = connection.cursor()

    essay_id_variable = cursor.var(int)

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