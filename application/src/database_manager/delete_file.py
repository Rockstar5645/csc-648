


def delete_file(media_id, db):
    base_sql = "DELETE FROM digital_media WHERE media_id = %s"
    db.query(base_sql, (media_id,))
    db.commit()
