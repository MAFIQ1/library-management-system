def calculate_fine(days_overdue):
    # Combined logic: no fine if early, max fine 100
    if days_overdue <= 0:
        return 0
    fine = days_overdue * 0.5
    return min(fine, 100)

def format_book_title(title):
    return title.strip().title()