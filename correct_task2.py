def count_valid_emails(emails):
    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        parts = email.split("@")
        if len(parts) == 2 and parts[0] and parts[1]:
            count += 1

    return count
