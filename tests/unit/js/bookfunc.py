def dimension_check(height, width, depth):
    if height<=0 or width<=0 or depth<=0:
        raise ValueError("Book dimensions must be greater than 0")

    return True
