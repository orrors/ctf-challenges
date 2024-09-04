from application.database import query_db

class shop(object):

    @staticmethod
    def select_by_id(product_id):
        res = query_db(f"SELECT data FROM products WHERE id='{product_id}'", one=True)
        print(res)
        return res

    @staticmethod
    def all_products():
        return query_db('SELECT * FROM products')    
