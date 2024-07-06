class Database:

    def __init__(self):

        try:

            import mysql.connector

            self.conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'password', database = 'indigo')

            self.mycursor = self.conn.cursor()

        except:

            print('error connecting to the database')

    def get_cities(self):

        cities = []

        self.mycursor.execute("""
        select distinct Source from flights_cleaned
        union 
        select Destination Source from flights_cleaned
        """)

        data = self.mycursor.fetchall()

        cities = [j[0] for j in data]

        return cities

    def get_flight_data(self, source, destination):

        self.mycursor.execute("""
        select Airline, Route, Dep_Time, Duration, Price from flights_cleaned where Source = '{}' and Destination = '{}'
        """.format(source, destination))

        data = self.mycursor.fetchall()

        return data

    def get_flight_frequency(self):

        cities = []
        frequency = []

        self.mycursor.execute("""
        select Airline, count(*) from flights_cleaned
        group by Airline
        """)

        data = self.mycursor.fetchall()

        for j in data:

            cities.append(j[0])
            frequency.append(j[1])

        return cities, frequency

    def get_busiest_airports(self):

        cities = []
        frequency = []

        self.mycursor.execute("""
        with temp as (select Source from flights_cleaned
        union all
        select Destination from flights_cleaned)
        
        select Source, count(*) from temp
        group by Source
        order by count(*) desc
        """)

        data = self.mycursor.fetchall()

        for j in data:

            cities.append(j[0])
            frequency.append(j[1])

        return cities, frequency

    def daily_flights(self):

        date = []
        frequency = []

        self.mycursor.execute("""
        select Date_of_Journey, count(*) from flights_cleaned group by Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for j in data:

            date.append(j[0])
            frequency.append(j[1])

        return date, frequency