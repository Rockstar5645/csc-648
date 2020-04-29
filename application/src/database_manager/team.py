def get_team(conn, name=None):
    if name == None: # if no param : return whole team table
        conn.query("SELECT * FROM team_about")
    else: # get team_member
        conn.query("SELECT * FROM team_about WHERE `name` LIKE %s", ("%" + name + "%",))
    data = conn.fetchall()
    conn.commit()
    return data