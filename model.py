import mysql.connector

# --- Connection helper ---
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="bookmark_db"
    )

###############
def add_link(title, url, details=None, group="GLOBAL"):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO links (title, url, details, groupe)
    VALUES (%s, %s, %s, %s)
    """
    values = (title, url, details, group)

    cursor.execute(sql, values)
    conn.commit()

    new_id = cursor.lastrowid  # INSERT → use lastrowid

    cursor.close()
    conn.close()
    return new_id

###############
def get_link(id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # dictionary=True gives column names

    sql = "SELECT * FROM links WHERE id=%s"
    cursor.execute(sql, (id,))

    row = cursor.fetchone()  # SELECT one → fetchone()

    cursor.close()
    conn.close()
    return row

###############
def get_links():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM links"
    cursor.execute(sql)

    rows = cursor.fetchall()  # SELECT many → fetchall()

    cursor.close()
    conn.close()
    return rows

###############
def edit_link(id: int, title=None, url=None, details=None, group=None):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE links
    SET title=%s, url=%s, details=%s, groupe=%s
    WHERE id=%s
    """
    values = (title, url, details, group, id)

    cursor.execute(sql, values)
    conn.commit()

    updated = cursor.rowcount

    cursor.close()
    conn.close()
    return updated

###############
def delete_link(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "DELETE FROM links WHERE id=%s"
    cursor.execute(sql, (id,))
    conn.commit()

    deleted = cursor.rowcount

    cursor.close()
    conn.close()
    return deleted

###############
def search_by_title(title):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM links WHERE title LIKE %s"
    pattern = f"%{title}%"

    cursor.execute(sql, (pattern,))
    result = cursor.fetchall

    cursor.close()
    conn.close()
    return result

###############
def count_in_group(groupe_name):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT COUNT(*) FROM links WHERE groupe=%s"
    value = (groupe_name,)
    cursor.execute(sql, value)

    result = cursor.fetchone()[0]  # grab the count number

    cursor.close()
    conn.close()
    return result


###############
def list_groups():
    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT DISTINCT groupe FROM links"
    cursor.execute(sql)

    groups = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return groups

###############
def search_by_groupe(groupe_name):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM links WHERE title LIKE %s"
    pattern = f"%{groupe_name}%"

    cursor.execute(sql, (pattern,))
    result = cursor.fetchall

    cursor.close()
    conn.close()
    return result