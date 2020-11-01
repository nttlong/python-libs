
import obj_sql





@obj_sql.table("hr_emps")
class employees:
    @obj_sql.field("Code")
    def code(self): pass
    @obj_sql.field("FirstName")
    def name(self): pass
    @obj_sql.field("LastName")
    def last_name(self):pass

sql = obj_sql.query(employees.code,employees.name+" "+employees.last_name)
m = employees.code -" "+employees.code
print(m)
