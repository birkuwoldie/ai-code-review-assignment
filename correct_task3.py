def average_valid_measurements(values):
    total = 0
    valid_count = 0

    for v in values:
        if v is None:
            continue
        try:
            total += float(v)
            valid_count += 1
        except (TypeError, ValueError):
            continue

    if valid_count == 0:
        return 0

    return total / valid_count
