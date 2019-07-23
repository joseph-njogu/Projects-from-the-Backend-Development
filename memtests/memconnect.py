import sys, psycopg2, cache
 
def car_by_country(country):
 
        # Define Query
        sql = "SELECT company FROM models WHERE country = '%s'" % country
 
        cached = cache.get_result(sql)
 
        if not cached:
                # Init DB
                db = psycopg2.connect("dbname=cars user=monstrado host=db-server")
                cursor = db.cursor()
 
 
                cursor.execute(sql)
 
                cars = cursor.fetchall()
 
                print_cars(cars)
                cache.set_result(sql, cars)
        else:
                print("Cached Results")
                print_cars(cached)
 
def print_cars(cars):
        print("Company")
        print("-" * 15)
        for car in cars:
                print(car[0])
 
 
country = sys.argv[len(sys.argv)-1]
car_by_country(country)