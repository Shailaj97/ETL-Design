import psycopg2

def connect():
    return psycopg2.connect(host= "localhost", database= "e-commerce", user= "postgres",password= "apple_ball",port= 5432)

def ecommerce_extract():
    source_conn = connect()
    dest_conn = connect()

    source_cursor = source_conn.cursor()
    dest_cursor = source_conn.cursor()

    source_conn.close()
    dest_conn.close()

    select_query = """
    SELECT users.id AS user_id, users.username AS user_name, products.id AS product_id, products.name AS product_name,
    categories.id AS catogory_id, categories.name as category, products.price as product_price, sales.price AS sales_price,
    sales.quantity AS sales_quantity, (product.quantity-sales.quantity) AS remaining_product 
    FROM sales
    INNER JOIN users ON  users.id = sales.user_id 
    INNER JOIN products ON products.id = sales.product_id
    INNER JOIN categories ON categories.id = products.category_id
    """

    source_cursor.execute(select_query)
    result=source_cursor.fetchall()
    sql='''
    INSERT INTO raw_sales(user_id, username, product_id, product_name, category_id, category_name, current_price, sold_price, sold_quantity, remaining_quantity, sales_date)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    for row in result:
        dest_cursor.execute(sql,row)
        dest_connect.commit()

    
    
    source_con.close()
    dest_con.close()

if __name__ == "__main__" :
    ecommerce_extract()