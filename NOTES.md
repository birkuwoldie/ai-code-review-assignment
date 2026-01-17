### Notes

### Assumptions:

- Input data may be partially malformed or mixed-type, so defensive checks were added to prevent runtime errors.

- For Tasks 1 and 3, returning 0 when no valid values exist was chosen as a safe default; alternative behaviors (e.g., raising an exception or returning None) were not specified by the requirements.

### Validation Scope:

- Email validation in Task 2 is intentionally minimal and does not fully comply with RFC standards. The goal was to improve correctness and safety while keeping changes small and understandable.

### Design Trade-offs:

- More robust validation or stricter error handling could have been implemented, but these were avoided to keep fixes minimal and aligned with the original intent of each function.

- Logging or explicit error reporting was not added, as it would change the behavior beyond a simple corrective fix.

### Limitations:

- The solutions prioritize correctness and safety over performance, which is acceptable given the expected input sizes implied by the assignment.