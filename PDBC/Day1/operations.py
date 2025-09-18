from db import get_connection
connectionTODB=get_connection()
cur=connectionTODB.cursor()
def add_Employee():
    emp_name=input("enter emp name :-- ")
    emp_sal=float(input("enter emp sal :-- "))
    emp_deptttttt=input("enter emp dept :-- ")
    emp_loc=input("enter emp loc :-- ")

     # object which helps you to comunicate in better way with db from py file
    cur.execute("insert into employees (emp_name,emp_sal,emp_dept,emp_loc) values (%s,%s,%s,%s) ",(emp_name,emp_sal,emp_deptttttt,emp_loc))

    connectionTODB.commit()
    connectionTODB.close()
    # print(emp_name)
    print(f"{emp_name}   added employee successfully...")


def view_Employee():
    cur.execute("select * from employees")
    data=cur.fetchall()
    for i in data:
        print(i[1])
    connectionTODB.close()
    print(f" employee data fetched successfully...")

def delete_Employee():
    emp_id=int(input("enetr emp_id "))
    cur.execute("delete from employees where emp_id = %s",(emp_id,))
    connectionTODB.commit()
    connectionTODB.close()


