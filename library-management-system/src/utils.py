def calculate_fine(days_overdue):
    # Alternative: no fine if returned early
    if days_overdue <= 0:
        return 0
    return days_overdue * 0.5

def format_book_title(title):
    return title.strip().title()
