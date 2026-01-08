from sqlalchemy import create_engine, text

engine = create_engine(
    f"mysql+pymysql://user:user@127.0.1.29:3306/restourant?charset=utf8mb4"
)

def get_all_not_checked():
    sql_get_all = text("""
    SELECT * FROM app_booktable WHERE tg_check = False
    """)
    with engine.connect() as conn:
        result = conn.execute(sql_get_all)
        return result
def change_tg_check(id):
    sql_change = text("""
    UPDATE app_booktable SET tg_check = TRUE WHERE id = :id
    """)
    with engine.connect() as conn:
        conn.execute(sql_change, {"id": id})
        conn.commit()
    
def get_admin(user_id):
    sql_get = text("""
    SELECT * FROM app_admin WHERE user_id = :user_id
    """)
    with engine.connect() as conn:
        result = conn.execute(sql_get, {"user_id": user_id}).fetchone()
        if result is None:
            return None
        return result
def get_admins():
    sql_get = text("""
    SELECT * FROM app_admin WHERE bot_connect = TRUE
    """)
    with engine.connect() as conn:
        result = conn.execute(sql_get).fetchall()
        if result is None:
            return None
        return result
def change_tg_active(user_id):
    sql_change = text("""
    UPDATE app_admin SET bot_connect = TRUE WHERE user_id = :user_id
    """)
    with engine.connect() as conn:
        conn.execute(sql_change, {"user_id": user_id})
        conn.commit()
