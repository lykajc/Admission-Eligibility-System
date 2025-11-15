applicants = []


def menu():
    print("\n ---------- ADMISSION SYSTEM -----------")
    print("1. Add applicants")
    print("2. View All Applicants")
    print("3. Check Admission Results")
    print("4. View Summary Report")
    print("5. Exit System")

#Add applicants / store applicants
def add_applicant():
    global applicants
    print("\n ---------- ADD APPLICANTS -----------")
    try:
        num = int(input("Enter how many applicants: "))
    except ValueError:
        print("Invalid Input, Please enter a number")
        return

    for i in range(1, num + 1):
        print(f"\n-----Applicant no. {i}------")
        name = input("Applicant full name: ")
        age = int(input("Applicant Age: "))
        score = int(input("Applicant Exam Score: "))
        interview = int(input("Interview Score: "))

        applicant = {
            "Name": name,
            "Age": age,
            "Score": score,
            "Interview": interview
        }
        applicants.append(applicant)
    print("\nApplicants added successfully")

#Show applicants recorded
def view_applicants():
    print("\n ---------- VIEW APPLICANTS -----------")
    if len(applicants) == 0:
        print("No Applicants exist")
        return

    for i, ap in enumerate(applicants, start=1):
        print(f"{i}. {ap['Name']} - Age: {ap['Age']} - Exam Score: {ap['Score']} "
              f"- Interview {ap['Interview']}")

        print()

#Check resulta
def check_applicants():
    print("\n ---------- CHECKING APPLICANTS RESULTS -----------")
    if len(applicants) == 0:
        print("No Applicants record found")
        return

    print("\nChecking Admission Results...")
    for ap in applicants:
        name = ap['Name']
        age = ap['Age']
        exam_score = ap['Score']
        interview = ap['Interview']

        #age Kondisyones
        if age >= 18:
            if exam_score >= 80:
                if interview >= 75:
                    print(f"{name} -> Accepted")
                else:
                    print(f"{name} -> Rejected")
            else:
                print(f"{name} -> Rejected")
        else:
            print(f"{name} -> Rejected")

        print()

#Summation
def summary_report():
    print("\n ---------- SUMMARY REPORT -----------")
    if len(applicants) == 0:
        print("No Applicants record found")
        return

    total = len(applicants)
    accepted = 0
    accepted_ap = []

    for ap in applicants:
        if ap['Age'] >= 18 and ap['Score'] >= 80 and ap['Interview'] >= 75:
            accepted += 1
            accepted_ap.append(ap['Name'])
    rejected = total - accepted
    rate = (rejected / total) * 100

    print(f"Total Applicants: {total}")
    print(f"Accepted: {accepted}")
    print(f"Rejected: {rejected}")
    print(f"Acceptance Rate: {rate}%")
    print(f"Accepted Applicants:", ",".join(accepted_ap))
    print("==================================")

#Menu Loop
def main():
    while True:
        menu()
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            add_applicant()
        elif choice == 2:
            view_applicants()
        elif choice == 3:
            check_applicants()
        elif choice == 4:
            summary_report()
        elif choice == 5:
            print("Thank you for using this program, Goodbye.!")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()