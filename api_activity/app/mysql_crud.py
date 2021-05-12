import pymysql.cursors

connection = pymysql.connect(host='10.20.19.205',
                             user='devmysql',
                             password='mY$Ql@d3v2o21!!',
                             database='seo',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = """
            CREATE TABLE `users` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `email` varchar(255) COLLATE utf8_bin NOT NULL,
                `password` varchar(255) COLLATE utf8_bin NOT NULL,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
            AUTO_INCREMENT=1 ;
        """
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
