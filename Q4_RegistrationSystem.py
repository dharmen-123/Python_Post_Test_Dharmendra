# Q4. Create a Student Registration System: (5 Marks)
# • Create your own exception: InvalidAgeError
# • Create your own exception: InvalidMarksError
# • Ask user to enter: name, age, marks
# • If age < 15 or age > 30 fi raise InvalidAgeError
# • If marks < 0 or marks > 100 fi raise InvalidMarksError
# • If valid fi print 'Student registered successfully!'

class InvalidAgeError:
    pass

class InvalidMarksError:
    pass

class Registration:
    def user(self,name, age , marks):
        try:
            if age<15 or age>30:
                raise InvalidAgeError("Age is not valid")
            elif marks<0 or marks>100:
                raise InvalidMarksError("Marks are Not valid")
            else:
                print("Details are Valid")

        except InvalidAgeError as e:
            print(f"Invalid Age {e}")
        except InvalidMarksError as e:
            print(f"Invalid marks {e}")
        finally:
            print("Registration Successfull")

R=Registration()
R.user("Ravi",17, 67)
        
