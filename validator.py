def validate_choice(choice: int,allowed_choices : list[int]) -> bool:
    if choice in allowed_choices:
        return True
    else:  
        return False