student_tickets_count = 0
kid_tickets_count = 0
standard_tickets_count = 0
command = input()
total_tickets_count = 0

while command != "Finish":
    free_tickets = int(input())
    movie_name = command
    total_places = free_tickets
    sold_tickets = 0
    while free_tickets > 0:
        ticket_type = input()
        if ticket_type == "student":
            student_tickets_count += 1
        elif ticket_type == "standard":
            standard_tickets_count += 1
        elif ticket_type == "kid":
            kid_tickets_count += 1
        elif ticket_type == "End":
            break
        free_tickets -= 1
        sold_tickets += 1
        total_tickets_count += 1
    percent_full_hall = sold_tickets / total_places * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    command = input()

students_percent = student_tickets_count / total_tickets_count * 100
kids_percent = kid_tickets_count / total_tickets_count * 100
standard_percent = standard_tickets_count / total_tickets_count * 100
print(f"Total tickets: {total_tickets_count}")
print(f"{students_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")