from sqlalchemy.orm import sessionmaker
from db_manager import engine
from models import Student

Session = sessionmaker()
local_session = Session(bind=engine)


def option_selector():
    print("Here you can [C]reate, [U]pdate, [R]ead, or [D]elete users.")
    print()
    option = input("Type in the initial letter of they option you want: ").upper()
    validator = True

    while validator:
        print()

        if option == "C":
            name = input("Name of the student: ")
            email = input("Email of the student: ")
            phone = input("Phone of the student: ")

            student = Student(name=name, email=email, phone=phone)

            local_session.add(student)
            local_session.commit()

            print()
            print(f"Student {student.name} created.")
            print()

            continue_validation = input("Do you wanna do another operation? ('Yes'/'No'): ")
            if continue_validation == "No":
                validator = False
            
        elif option == "R":
            name = input("Name of the student to search: ")

            student = local_session.query(Student).filter(Student.name == name).first()

            print(f"Name: {student.name}, Email: {student.email}, Phone: {student.phone}")

            continue_validation = input("Do you wanna do another operation? ('Yes'/'No'): ")
            if continue_validation == "No":
                validator = False

        elif option == "U":
            name = input("Name of the student to update: ")
            student = local_session.query(Student).filter(Student.name == name).first()
            print()

            new_name = input("New name: ")
            print()
            student.name = new_name
            new_email = input("New email: ")
            print()
            student.email = new_email
            new_phone = int(input("New phone: "))
            print()
            student.phone = new_phone

            local_session.commit()

            continue_validation = input("Do you wanna do another operation? ('Yes'/'No'): ")
            if continue_validation == "No":
                validator = False

        elif option == "D":
            name = input("Name of the student to delete: ")
            student = local_session.query(Student).filter(Student.name == name).first()
            
            local_session.delete(student)
            
            continue_validation = input("Do you wanna do another operation? ('Yes'/'No'): ")
            if continue_validation == "No":
                validator = False

        else:
            print("That wasn't a valid option.")

option_selector()
