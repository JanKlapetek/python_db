import psycopg2
import _datetime

def main():
    while True:
        print("\nOptions:")
        print("1. Add an item to cart")
        print("2. Delete an item from the cart")
        print("3. Edit an item in the cart")
        print("4. Clear the cart")
        print("5. Search in the cart")
        print("6. View the cart contents")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            get_all_products()
            
        elif choice == '2':
            type = input("Enter product type (Boty or Shoes or Fitness or Sports): ")
            get_products_by_type(type)
            
        elif choice == '3':
            product = input('Enter product by manufacturer to check (example Nike): ')
            check_product_by_manufacturer(product)
            
        elif choice == '4':
            get_top_customers()
            
        elif choice == '5':
            get_favorite_manufacturer()
            
        elif choice == '6':
            print('Delete customers after date 2024-05-01 !')
            delete_customers_after_date("2024-05-01")
            
        elif choice == '7':
            print("Exiting...Program END")
            break
        else:
            print("Invalid choice, please try again")
        
    

def get_all_products():
    conn = psycopg2.connect(database="sportsstore", user="koyeb-adm", password="RmiEvoMz7a3s", host="ep-white-band-a2h03cgc.eu-central-1.pg.koyeb.app", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sportsstore;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    
def get_products_by_type(product_type):
    conn = psycopg2.connect(database="sportsstore", user="koyeb-adm", password="RmiEvoMz7a3s", host="ep-white-band-a2h03cgc.eu-central-1.pg.koyeb.app", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sportsstore WHERE product_type = %s;", (product_type,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    
def check_product_by_manufacturer(manufacturer_name):
    conn = psycopg2.connect(database="sportsstore", user="koyeb-adm", password="RmiEvoMz7a3s", host="ep-white-band-a2h03cgc.eu-central-1.pg.koyeb.app", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM sportsstore WHERE manufacturer = %s;", (manufacturer_name,))
    count = cur.fetchone()[0]
    if count > 0:
        print("Yes, the product from the {} retailer is in stock.".format(manufacturer_name))
    else:
        print("The product from the {} seller is out of stock.".format(manufacturer_name))
    conn.close()
    
def get_top_customers():
    conn = psycopg2.connect(database="sportsstore", user="koyeb-adm", password="RmiEvoMz7a3s", host="ep-white-band-a2h03cgc.eu-central-1.pg.koyeb.app", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT customer_name FROM customers ORDER BY registration_date LIMIT 3;")
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
    conn.close()

def get_favorite_manufacturer():
    conn = psycopg2.connect(database="sportsstore", user="koyeb-adm", password="RmiEvoMz7a3s", host="ep-white-band-a2h03cgc.eu-central-1.pg.koyeb.app", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT manufacturer FROM sportsstore GROUP BY manufacturer ORDER BY SUM(total_sales) DESC LIMIT 1;")
    row = cur.fetchone()
    print(row[0])
    conn.close()
    
def delete_customers_after_date(delete_date):
    conn = psycopg2.connect(database="sportsstore", user="koyeb-adm", password="RmiEvoMz7a3s", host="ep-white-band-a2h03cgc.eu-central-1.pg.koyeb.app", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM customers WHERE registration_date > %s;", (delete_date,))
    deleted_count = cur.rowcount
    conn.commit()
    conn.close()
    print("Number of deleted customers: {}".format(deleted_count))





if __name__ == "__main__":
    main()