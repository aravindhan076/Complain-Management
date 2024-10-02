class ComplaintSystem:
    complaint_id = 1
    def __init__(self):
        self.complaints = []

    def add_complaint(self):
        name = input("Enter your name: ")
        complaint = input("Enter your complaint: ")
        self.complaints.append({"name": name, "complaint": complaint})
        print("Complaint submitted successfully!\nYour complaint id is: ",self.complaint_id)
        self.complaint_id+=1

    def view_complaints(self):
        if not self.complaints:
            print("No complaints to show.\n")
        else:
          idx = int(input("\nEnter your complaint ID: "))
          for i, complaint in enumerate(self.complaints, 1):  # Enumerate to get index starting from 1
              if idx == i:
                print(f"{i}. {complaint['name']}: {complaint['complaint']}")
          print()



    def run(self):
        while True:
            print("Complaint Management System")
            print("1. Submit Complaint")
            print("2. View All Complaints")
            print("3. Exit")

            choice = input("Choose an option (1-3): ")
            if choice == '1':
                self.add_complaint()
            elif choice == '2':
                self.view_complaints()
            elif choice == '3':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice, please try again.\n")



system = ComplaintSystem()
system.run()
print(system.__dict__)
