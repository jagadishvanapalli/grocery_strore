from sqlconnection import get_sql_connection
def get_all_products(connection):
    cursor = connection.cursor()
    query="SELECT products.product_id,products.p_name,products.unit_id,products.price_per_unit,uom.uom_name From grocery_store.products inner join uom on products.unit_id=uom.uom_id;"
    cursor.execute(query)
    response=[]
    for (product_id,p_name,unit_id,price_per_unit,uom_name) in cursor:
        response.append(
            {
                'product_id':product_id,
                'product_name':p_name,
                'unit_id':unit_id,
                'price_per_unit':price_per_unit,
                'uom_name':uom_name
            }
        )
    return response




def insert_new_product(connection,products):
    cursor = connection.cursor()
    query="insert into products(p_name,unit_id,price_per_unit) values (%s,%s,%s);"
    data=(products['product_name'],products['unit_id'],products['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid



def delete_product(connection,product_id):
    cursor = connection.cursor()
    query="delete from products where product_id="+ str(product_id)
    cursor.execute(query)
    connection.commit()
    cursor.close()



if __name__=='__main__':
    connection=get_sql_connection()
    print(delete_product(connection,1))