current_book_pages = int(input())
reading_pages_per_hour = int(input())
count_days_needed_to_read_book = int(input())

total_time = (current_book_pages / reading_pages_per_hour) / count_days_needed_to_read_book

print(int(total_time))


