def calculate_fine(days_overdue):
    # New logic: maximum fine is 100
    fine = days_overdue * 0.5
    return min(fine, 100)

def format_book_title(title):
    return title.strip().title()
