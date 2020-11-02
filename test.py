import obj_sql


@obj_sql.table("hr_emps")
class employees:
    """Danh sach nhan vien"""
    @obj_sql.field("Code")
    def code(self):
        """Ma nhan vien"""
        pass

    @obj_sql.field("FirstName")
    def name(self): pass

    @obj_sql.field("LastName")
    def last_name(self): pass

emps= employees
sql = obj_sql.select(employees.code, employees.name + " " + employees.last_name)

m = emps.code + " " + emps.code
print(m)
