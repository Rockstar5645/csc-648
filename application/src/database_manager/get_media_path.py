


def get_digital_media_path_by_id(id, db):
    db.query("SELECT file_path FROM digital_media WHERE media_id = %s", [id,])
    path = db.fetchall()
    db.commit()
    return path[0][0]

def get_digital_media_thumbnail_path_by_id(id, db):
    db.query("SELECT thumbnail_path FROM digital_media WHERE media_id = %s", [id,])
    path = db.fetchall()
    db.commit()
    return path[0][0]


