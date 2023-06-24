import mysql.connector

cnx = mysql.connector.connect(user='root', password='password@',
                              host='127.0.0.1',
                              database='grocery_store')
cursor = cnx.cursor()
query = "SELECT products.products_id, products.price_per_unit, products.name, products.uom_id, uom.uom_name FROM grocery_store.products inner join grocery_store.uom on products.uom_id=uom.uom_id"
cursor.execute(query)
for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
    print(product_id,name, price_per_unit, uom_name)
cnx.close()