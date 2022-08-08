user_queries = {
    'create_user': 'INSERT INTO user (username, password) VALUES (%s, %s)',
    'get_user': 'SELECT * FROM user WHERE username = %s;',
    'get_user_by_id': 'SELECT * FROM user WHERE id = %s;',
    'get_user_by_name': 'SELECT * FROM user WHERE username = %s;',
    'get_user_by_name_and_pwd': 'SELECT * FROM user WHERE username = %s AND password = %s;',
    'edit_user_name': 'UPDATE user SET username = %s, WHERE id = %s;',
    'edit_user_password': 'UPDATE user SET password = %s, WHERE id = %s;',
    'delete_user': 'DELETE FROM user WHERE id = %s;',
}
