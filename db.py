#import postgresql
#db = postgresql.open('pq://user:password@host:port/database')
#db.execute("CREATE TABLE emp (emp_first_name text, emp_last_name text, emp_salary numeric)")
#make_emp = db.prepare("INSERT INTO emp VALUES ($1, $2, $3)")
#make_emp("John", "Doe", "75,322")
#with db.xact():
#    make_emp("Jane", "Doe", "75,322")
#    make_emp("Edward", "Johnson", "82,744")