from hello_app.db_init import Student, db

student_john = Student(firstname='john', 
							lastname='doe',
                            email='jd@example.com', 
							age=23,
							active=True,
                            bio='Biology student')

sammy = Student(firstname='Sammy',
			lastname='Shark',
			email='sammyshark@example.com',
			active=True,
			age=20,
			bio='Marine biology student')

carl = Student(firstname='Carl',
			lastname='White',
			email='carlwhite@example.com', 
			active=True,
			age=22,
			bio='Marine geology student')

db.session.add(sammy)
db.session.add(carl)
db.session.add(student_john)
db.session.commit()