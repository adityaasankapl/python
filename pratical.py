marks = []
while True: 

    print("\n-----Student Marks Data-----")
    print("1. Enter Marks:")
    print("2. Display Marks:")
    print("3. Update marks:")
    print("4.Delete Marks:")
    print("5. Exit")

    choice = int(input("enter the choice :"))
        
    if choice == 1:
        mark = int(input("Enter the marks :"))
        marks.append(marks)
        print("Marks enter successfully !!")
        
    elif choice == 2:    
        if len(marks) == 0:
            print("No marks avilable !!")
            
        else:
            print("student marks :")
            for i in range(len(marks)):
             print("student", i + 1, "=", marks[i])
              
    elif choice == 3:           
        student = int(input("Enter student number to update :"))
        
        if 1<= student <= len(marks):
            new_marks = int(input("Enter new marks :"))
            marks[student - 1] = new_marks
            print("Marks updated !!!")
            
        else:
            print("Invaild choice !!!")
        
    elif choice == 4:
        student = int(input("Enter student number to delete :"))

        if 1<= student <= len(marks):
            marks.pop(student - 1)
            print("marks deleted !!")
        
        else:
            print("invalid student number !!!")                    
            
    elif choice == 5:  
        print("End !!!") 
        break

    else:
     print("Invalid choice !!!")