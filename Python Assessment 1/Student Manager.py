from tkinter import *

# Initialize the main window
root = Tk()
root.title("Student Manager")
root.geometry("700x500")
root.resizable(0, 0)  

var = StringVar(root)  # Variable to hold the selected student name
var.set("Select Student")  # Set default text for the dropdown

title_label = Label(root, text="Student Manager", font=("Arial", 24))
title_label.pack(pady=10)

# Create the dropdown menu for student selection
student_dropdown = OptionMenu(root, var, "")
student_dropdown.pack(side=TOP, pady=(5, 10))  # Pack dropdown on top with padding



def LoadData():# function to load the text file
    students = []#create a list to store data
    with open("marks.txt", "r") as filehandler:#open file
        # Read the first line to get the number of students (optional)
        num_students = int(filehandler.readline().strip())  # This line is optional. using just to read first till the end of line
        
        # Read the rest of the lines for student data
        for line in filehandler:
            parts = line.strip().split(",") #split the reading when it detects a comma
            student_code = parts[0]#get student code
            student_name = parts[1]#get student name
            marks = list(map(int, parts[2:]))  # Convert marks to a list of integers
            students.append((student_code, student_name, marks))
    
    return students  # Return only the student data


def viewAllRecord():  # Function to view all student records
    txtarea.delete("1.0", 'end')  # Clear the text area
    students = LoadData()  # Load the students data here
    
    for student in students: 
        student_code = student[0]  # Get Student code
        student_name = student[1]  # Get Student name
        coursework_marks = student[2]  # Get Marks
        exam_mark = coursework_marks.pop()  # Assuming the last mark is the exam mark
        total_coursework_marks = sum(coursework_marks)  # Sum of coursework marks
        total_marks = total_coursework_marks + exam_mark  # Total marks
        overall_percentage = (total_marks / 160) * 100  # Calculate overall percentage

        # Format to display on the text area
        record = (
            f"Student Name: {student_name}\n"
            f"Student Number: {student_code}\n"
            f"Total Coursework Mark: {total_coursework_marks}\n"
            f"Exam Mark: {exam_mark}\n"
            f"Overall Percentage: {overall_percentage:.2f}%\n"
            f"Student Grade: {'A' if overall_percentage >= 70 else 'B' if overall_percentage >= 60 else 'C' if overall_percentage >= 50 else 'D' if overall_percentage >= 40 else 'F'}\n"
            f"{'-'*40}\n"  # Separator between records
        )
        txtarea.insert(END, record)

def dropdown(students):  # Function for dropdown menu
    student_dropdown['menu'].delete(0, 'end')  # Clear the current options
    for student in students:
        student_name = student[1]  # Get student name
        student_dropdown['menu'].add_command(label=student_name, command=lambda value=student_name: var.set(value))  # call the variable to get students names

# Load data at the beginning and populate the dropdown
students = LoadData()  # Load the students data here
dropdown(students)  # Populate the dropdown with loaded students

def individualRecord():  # Function to view an individual student's record
    selected_student = var.get()  # Get the selected student name from the dropdown
    if selected_student == "Select Student":
        txtarea.delete("1.0", 'end')
        txtarea.insert(END, "Please select a student.")
        return

    students = LoadData()  # Reload student data

    # Find the selected student's data
    for student in students:
        if student[1] == selected_student:  # Compare names
            student_code = student[0]#Get student code
            coursework_marks = student[2] #Get marks
            exam_mark = coursework_marks.pop()  # Assuming the last mark is the exam mark
            total_coursework_marks = sum(coursework_marks)  # Sum of coursework marks
            total_marks = total_coursework_marks + exam_mark  # Total marks
            overall_percentage = (total_marks / 160) * 100  # Calculate overall percentage

            # Format of the output
            record = (
                f"Student Name: {student[1]}\n"
                f"Student Number: {student_code}\n"
                f"Total Coursework Mark: {total_coursework_marks}\n"
                f"Exam Mark: {exam_mark}\n"
                f"Overall Percentage: {overall_percentage:.2f}%\n"
                f"Student Grade: {'A' if overall_percentage >= 70 else 'B' if overall_percentage >= 60 else 'C' if overall_percentage >= 50 else 'D' if overall_percentage >= 40 else 'F'}\n"
            )
            txtarea.delete("1.0", 'end')  # Clear previous records
            txtarea.insert(END, record)
            break

def highestMark():#Function to get the highest mark
    students = LoadData()  # Load the students data here

    # Initialize variables to track the highest mark and student details
    highest_mark = 0
    top_student = None

    for student in students:
        student_code = student[0] #Get student code
        student_name = student[1] #Get student name
        coursework_marks = student[2] #Get marks
        exam_mark = coursework_marks.pop()  # Assuming last mark is the exam mark
        total_coursework_marks = sum(coursework_marks)  # Sum of coursework marks
        overall_percentage = (total_coursework_marks + exam_mark) / 160 * 100  # Calculate overall percentage

        # Check if this student has the highest mark 
        total_marks = total_coursework_marks + exam_mark
        if total_marks > highest_mark:
            highest_mark = total_marks
            top_student = (student_code, student_name, total_coursework_marks, exam_mark, overall_percentage)

    #Display the top student details
    if top_student:
        student_code, student_name, total_coursework_marks, exam_mark, overall_percentage = top_student
        record = (
            f"Student Name: {student_name}\n"
            f"Student Number: {student_code}\n"
            f"Total Coursework Mark: {total_coursework_marks}\n"
            f"Exam Mark: {exam_mark}\n"
            f"Overall Percentage: {overall_percentage:.2f}%\n"
            f"Student Grade: {'A' if overall_percentage >= 70 else 'B' if overall_percentage >= 60 else 'C' if overall_percentage >= 50 else 'D' if overall_percentage >= 40 else 'F'}\n"
        )
        txtarea.delete("1.0", 'end')  # Clear the text area before displaying
        txtarea.insert(END, record)
    else:
        txtarea.delete("1.0", 'end')
        txtarea.insert(END, "No students found.")#If theres none

def lowestMark():#Function to get the lowest mark. Just reverse everything
    students = LoadData()  # Load the students data here

    # Initialize variables to track the lowest mark and student details
    lowest_mark = float('inf')  # Set to a very high value initially
    least_student = None

    for student in students:
        student_code = student[0]#Get code
        student_name = student[1]#Get student name
        coursework_marks = student[2]#Get marks
        exam_mark = coursework_marks.pop()  # Assuming last mark is the exam mark
        total_coursework_marks = sum(coursework_marks)  # Sum of coursework marks
        overall_percentage = (total_coursework_marks + exam_mark) / 160 * 100  # Calculate overall percentage

        # Check if this student has the lowest mark so far
        total_marks = total_coursework_marks + exam_mark
        if total_marks < lowest_mark:
            lowest_mark = total_marks
            least_student = (student_code, student_name, total_coursework_marks, exam_mark, overall_percentage)

    #Display the least student's details
    if least_student:
        student_code, student_name, total_coursework_marks, exam_mark, overall_percentage = least_student
        record = (
            f"Student Name: {student_name}\n"
            f"Student Number: {student_code}\n"
            f"Total Coursework Mark: {total_coursework_marks}\n"
            f"Exam Mark: {exam_mark}\n"
            f"Overall Percentage: {overall_percentage:.2f}%\n"
            f"Student Grade: {'A' if overall_percentage >= 70 else 'B' if overall_percentage >= 60 else 'C' if overall_percentage >= 50 else 'D' if overall_percentage >= 40 else 'F'}\n"
        )
        txtarea.delete("1.0", 'end')  # Clear the text area before displaying
        txtarea.insert(END, record)
    else:
        txtarea.delete("1.0", 'end')
        txtarea.insert(END, "No students found.")#If there's none

def sort(order='ascending'):#function to sort students by name
    students = LoadData()  # Load the student data
    # A list for sorting
    studentSort = []#Create a list to store data

    for student in students:
        student_code = student[0] #Get student code
        student_name = student[1] #Get student name
        coursework_marks = student[2] #Get marks
        exam_mark = coursework_marks.pop()  # Assuming last mark is the exam mark
        total_coursework_marks = sum(coursework_marks)  # Sum of coursework marks
        total_marks = total_coursework_marks + exam_mark  # Total marks
        overall_percentage = (total_marks / 160) * 100  # Calculate overall percentage

        # Append student details to the sorting list
        studentSort.append((student_code, student_name, total_coursework_marks, exam_mark, total_marks, overall_percentage))

    # Sort the list based on the specified order
    if order == 'ascending':
        studentSort.sort(key=lambda x: x[5])  # Sort by overall percentage
    else:
        studentSort.sort(key=lambda x: x[5], reverse=True)  # Sort by overall percentage descending

    # Clear the text area before displaying sorted results
    txtarea.delete("1.0", 'end')

    # Display sorted student records
    for student in studentSort:
        student_code, student_name, total_coursework_marks, exam_mark, total_marks, overall_percentage = student
        record = (
            #Display the output
            f"Student Name: {student_name}\n"
            f"Student Number: {student_code}\n"
            f"Total Coursework Mark: {total_coursework_marks}\n"
            f"Exam Mark: {exam_mark}\n"
            f"Overall Percentage: {overall_percentage:.2f}%\n"
            f"Student Grade: {'A' if overall_percentage >= 70 else 'B' if overall_percentage >= 60 else 'C' if overall_percentage >= 50 else 'D' if overall_percentage >= 40 else 'F'}\n"
            f"{'-'*40}\n"  # Separator
        )
        txtarea.insert(END, record)

def addStudent():#Function to add student
    # Create a new window to get the student's information
    add_window = Toplevel(root)
    add_window.title("Add New Student")
    add_window.geometry("400x300")

    # Labels and Entries for student details
    Label(add_window, text="Student Code:").grid(row=0, column=0, padx=10, pady=10)
    student_code_entry = Entry(add_window)
    student_code_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(add_window, text="Student Name:").grid(row=1, column=0, padx=10, pady=10)
    student_name_entry = Entry(add_window)
    student_name_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(add_window, text="Marks (comma-separated):").grid(row=2, column=0, padx=10, pady=10)
    marks_entry = Entry(add_window)
    marks_entry.grid(row=2, column=1, padx=10, pady=10)

    # Function to save the new student record
    def save_student():
        student_code = student_code_entry.get()#Get code
        student_name = student_name_entry.get()#Get name
        marks_text = marks_entry.get()#Get marks
        
        # Convert marks input into a list of integers
        try:
            marks = list(map(int, marks_text.split(',')))
            if len(marks) < 5:  # Assuming you require a minimum of 5 marks
                txtarea.delete("1.0", 'end')
                txtarea.insert(END, "Please enter at least 5 marks.")
                return
        except ValueError:
            txtarea.delete("1.0", 'end')
            txtarea.insert(END, "Please enter valid marks (comma-separated integers).")
            return

        # Append the new student record to the file
        with open("marks.txt", "a") as filehandler:
            filehandler.write(f"{student_code},{student_name},{','.join(map(str, marks))}\n")

        txtarea.delete("1.0", 'end')
        txtarea.insert(END, f"Added new student: {student_name} (Code: {student_code})")

        add_window.destroy()  # Close the add student window

        students = LoadData()  # Reload the data to include the newly added student
        dropdown(students)  # Refresh the dropdown menu with updated data

    # Button to save the student
    Button(add_window, text="Save", command=save_student).grid(row=3, column=0, columnspan=2, pady=20)

def deleteStudent():#Function to delete student
    #new window
    delete_window = Toplevel(root)
    delete_window.title("Delete Student")
    delete_window.geometry("300x200")

    # Label for selecting a student
    Label(delete_window, text="Select Student to Delete:").pack(pady=10)

    delete_var = StringVar(delete_window)
    delete_var.set("Select Student")  # Default text for the dropdown
    student_dropdown_delete = OptionMenu(delete_window, delete_var, "")
    student_dropdown_delete.pack(pady=10)

    # Function to populate the dropdown with current students
    def populate_dropdown():
        students = LoadData()  # Load current students from the file
        student_dropdown_delete['menu'].delete(0, 'end')  # Clear current options
        for student in students:
            student_name = student[1]  # Get student name
            student_dropdown_delete['menu'].add_command(label=student_name, command=lambda value=student_name: delete_var.set(value))

    # Populate the dropdown when the window opens
    populate_dropdown()

    def delete_record():#Function for deleting
        selected_student = delete_var.get()
        if selected_student == "Select Student":
            txtarea.delete("1.0", 'end')
            txtarea.insert(END, "Please select a student to delete.")
            return

        # Read the current student data
        students = LoadData()
        new_data = []

        for student in students:
            if student[1] != selected_student:  # Skip the student to delete
                new_data.append(student)

        # Rewrite the file without the deleted student
        with open("marks.txt", "w") as filehandler:
            filehandler.write(f"{len(new_data)}\n")  # Update the student count
            for student in new_data:
                student_code, student_name, marks = student
                filehandler.write(f"{student_code},{student_name},{','.join(map(str, marks))}\n")

        txtarea.delete("1.0", 'end')
        txtarea.insert(END, f"Deleted student: {selected_student}")

        delete_window.destroy()  # Close the delete window

        dropdown(new_data)  # Refresh dropdown menu after deletion

    # Button to confirm deletion
    Button(delete_window, text="Delete Student", command=delete_record).pack(pady=20)

def updateStudent():#Function to update student info
    # Create a new window for updating a student
    update_window = Toplevel(root)
    update_window.title("Update Student")
    update_window.geometry("400x300")

    # Label for selecting a student
    Label(update_window, text="Select Student to Update:").pack(pady=10)

    update_var = StringVar(update_window)
    update_var.set("Select Student")  # Default text for the dropdown
    student_dropdown_update = OptionMenu(update_window, update_var, "")
    student_dropdown_update.pack(pady=10)

    # Function to populate the dropdown with current students
    def populate_dropdown():
        students = LoadData()  # Load current students from the file
        student_dropdown_update['menu'].delete(0, 'end')  # Clear current options
        for student in students:
            student_name = student[1]  # Get student name
            student_code = student[0]  # Get student code
            # Combine student name and code for display
            student_dropdown_update['menu'].add_command(label=f"{student_name} ({student_code})", command=lambda value=student: update_var.set(value))

    # Populate the dropdown when the window opens
    populate_dropdown()

    # Label for update options
    Label(update_window, text="Choose what to update:").pack(pady=10)
    
    update_choice = StringVar(update_window)
    update_choice.set("Select Update Option")  # Default text for the dropdown
    update_option_dropdown = OptionMenu(update_window, update_choice, "Name", "Marks")
    update_option_dropdown.pack(pady=10)

    # Entry fields for updating
    update_entry = Entry(update_window)
    update_entry.pack(pady=10)
    
    def update_record():
        selected_student = update_var.get()
        if selected_student == "Select Student":
            txtarea.delete("1.0", 'end')
            txtarea.insert(END, "Please select a student to update.")
            return

        update_option = update_choice.get()
        if update_option == "Select Update Option":
            txtarea.delete("1.0", 'end')
            txtarea.insert(END, "Please select an option to update.")
            return
        
        if update_option == "Name":
            new_name = update_entry.get()
            if new_name.strip() == "":
                txtarea.delete("1.0", 'end')
                txtarea.insert(END, "New name cannot be empty.")
                return
            
            student_code = selected_student[0]  # Get student code
            student_code, _, marks = selected_student  # Keep marks unchanged
            
            # Update the student's name
            students = LoadData()
            for idx, student in enumerate(students):
                if student[0] == student_code:
                    students[idx] = (student_code, new_name, student[2])  # Update name
                    break

            # Write updated data back to the file
            with open("marks.txt", "w") as filehandler:
                filehandler.write(f"{len(students)}\n")  # Update the student count
                for student in students:
                    student_code, student_name, marks = student
                    filehandler.write(f"{student_code},{student_name},{','.join(map(str, marks))}\n")

            txtarea.delete("1.0", 'end')
            txtarea.insert(END, f"Updated name for student: {new_name}")

        elif update_option == "Marks":
            marks_text = update_entry.get()
            try:
                new_marks = list(map(int, marks_text.split(',')))
                if len(new_marks) < 5:  # Assuming a minimum of 5 marks
                    txtarea.delete("1.0", 'end')
                    txtarea.insert(END, "Please enter at least 5 marks.")
                    return
            except ValueError:
                txtarea.delete("1.0", 'end')
                txtarea.insert(END, "Please enter valid marks (comma-separated integers).")
                return
            
            student_code = selected_student[0]  # Get student code
            student_name = selected_student[1]  # Get student name
            
            # Update the student's marks
            students = LoadData()
            for idx, student in enumerate(students):
                if student[0] == student_code:
                    students[idx] = (student_code, student_name, new_marks)  # Update marks
                    break

            # Write updated data back to the file
            with open("marks.txt", "w") as filehandler:
                filehandler.write(f"{len(students)}\n")  # Update the student count
                for student in students:
                    student_code, student_name, marks = student
                    filehandler.write(f"{student_code},{student_name},{','.join(map(str, marks))}\n")

            txtarea.delete("1.0", 'end')
            txtarea.insert(END, f"Updated marks for student: {student_name}")

    # Button to confirm update
    Button(update_window, text="Update Student", command=update_record).pack(pady=20)


btn = Button(root, text="Delete Student", command=deleteStudent).place(x=600, y=20)


# Create buttons for different actions
btn_frame = Frame(root)
btn_frame.pack(side=TOP, pady=20)
#placing the button and calling functions
Button(btn_frame, text="View All Records", command=viewAllRecord, width=20).grid(row=0, column=0, padx=5, pady=5)
Button(btn_frame, text="View Individual Record", command=individualRecord, width=20).grid(row=0, column=1, padx=5, pady=5)
Button(btn_frame, text="Highest Mark", command=highestMark, width=20).grid(row=0, column=2, padx=5, pady=5)
Button(btn_frame, text="Lowest Mark", command=lowestMark,width=20).grid(row=0, column=3, padx=5)
Button(btn_frame, text="Sort Ascending", command=lambda: sort('ascending'), width=20).grid(row=1, column=0, padx=5, pady=5)
Button(btn_frame, text="Sort Descending", command=lambda: sort('descending'),width=20).grid(row=1, column=1, padx=5, pady=5)
Button(btn_frame, text="Add Student", command=addStudent,width=20).grid(row=1, column=2, padx=5, pady=5)
Button(btn_frame, text="Update Student", command=updateStudent,width=20).grid(row=1, column=3, padx=5,pady=5)

# Create a text area for displaying results
txtarea = Text(root, wrap='word', height=30, width=60)
txtarea.pack(pady=(5, 10))

# Run the main event loop
root.mainloop() 