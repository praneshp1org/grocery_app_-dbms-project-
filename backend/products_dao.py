# import mysql.connector
# from sql_connection import get_sql_connection
from sql_connection import get_sql_connection
# def get_all_products(connection):
        
#     cursor = connection.cursor()

#     query = "SELECT products.products_id, products.price_per_unit, products.name, products.uom_id, uom.uom_name FROM grocery_store.products inner join grocery_store.uom on products.uom_id=uom.uom_id"
#     cursor.execute(query)
#     response = []
#     for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
#         # print(product_id,name, price_per_unit, uom_name)
#         response.append(
#             {
#                 'product_id': product_id,
#                 'name': name,
#                 'uom_id': uom_id,
#                 'price_per_unit':price_per_unit,
#                 'uom_name': uom_name
#             }
#         )
#     return response
#     print(response)
def get_all_products(connection):
    cursor = connection.cursor()

    query = "SELECT products.products_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM grocery_store.products INNER JOIN grocery_store.uom ON products.uom_id = uom.uom_id"
    cursor.execute(query)
    
    response = []
    
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    
    return response



def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = ("INSERT INTO products "
    "(name, uom_id, price_per_unit)"
    "VALUES (%s, %s, %s)")

    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, products_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where products_id=" + str(products_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__=='__main__':
    connection = get_sql_connection()
    get_all_products(connection)
    # print(insert_new_product(connection, {
    #     'product_name': 'onion',
    #     'uom_id': 2, 
    #     'price_per_unit': '70'
    # }))
    # print(delete_product(connection, 5))