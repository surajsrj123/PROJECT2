

class Employee:
    class_variable = "suraj patil"

    def inst_m(self):
        print(f"this is instance method:{self.class_variable}")


    @classmethod
    def class_m(cls):
        print (f"any value:{cls.class_variable}")

    @staticmethod
    def stat_m():
        print("this is static method")

object = Employee()
object.stat_m()
# Employee.stat_m()











