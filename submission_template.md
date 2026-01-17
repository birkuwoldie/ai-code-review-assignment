# AI Code Review Assignment (Python)

## Candidate
- Name:Birku Woldie Telele
- Approximate time spent: 

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function divides the total of non-cancelled orders by the total number of orders, including cancelled ones, which produces an incorrect average.
- The function can raise a ZeroDivisionError when the input list is empty.

### Edge cases & risks
- If all orders are cancelled, the function returns an incorrect average instead of handling the absence of valid orders.

- The function assumes that every order dictionary contains "status" and "amount" keys, which may raise KeyError if the input data is malformed.

### Code quality / design issues
- The logic for calculating the numerator (non-cancelled orders) and denominator (all orders) is inconsistent.

- There is no explicit handling or documentation of what should happen when there are no valid orders.

## 2) Proposed Fixes / Improvements
### Summary of changes

- Count only non-cancelled orders when computing the average.

- Add a guard clause to avoid division by zero.

- Use safer dictionary access to reduce the risk of runtime errors.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


> If testing this function, focus on:

- An empty list of orders (should return 0 without error).

- A list where all orders are cancelled.

- A mix of cancelled and non-cancelled orders.

- Orders missing "status" or "amount" keys.

- Orders with zero or negative amounts.

> These cases ensure correctness, robustness, and safe failure behavior.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It incorrectly claims that cancelled orders are excluded from the calculation, even though they are included in the denominator.

- It does not mention how empty input or all-cancelled orders are handled.

- It overstates correctness despite logical flaws in the implementation.

### Rewritten explanation
- This function calculates the average value of non-cancelled orders. It iterates through the input list, sums the amounts of orders whose status is not "cancelled", and counts only those valid orders. If no valid orders exist, the function returns 0 to avoid division by zero; otherwise, it returns the total divided by the number of valid orders.

## 4) Final Judgment

- Decision: Request Changes

- Justification: The original implementation produces incorrect results and fails to handle empty or fully cancelled datasets safely.

- Confidence & unknowns: High confidence after fixes. Behavior for malformed order objects is handled defensively, but stricter validation may be required depending on upstream data guarantees.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 
- The function assumes every item in emails is a string; if a non-string value (e.g., None or an integer) is present, "@" in email will raise a TypeError.

- The function treats any string containing "@" as a valid email, which allows many invalid email formats.

### Edge cases & risks
- An empty list returns 0, which is acceptable but not explicitly documented.

- Strings with whitespace, multiple "@" symbols, or missing domain/user parts are incorrectly counted as valid.

- Mixed-type input lists may cause runtime errors.

### Code quality / design issues
- Email validation logic is overly simplistic and does not align with the function’s stated intent.

- There is no input validation or type checking.

- The function name implies correctness that the implementation does not provide.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Ensure the function safely skips non-string values.

- Apply a minimal, clearer validation rule that checks for exactly one "@" and non-empty local and domain parts.

- Preserve simple logic while improving correctness and safety.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

> If testing this function, focus on:

- Empty input lists.

- Lists containing non-string values (None, integers, objects).

- Valid email formats (e.g., user@example.com).

- Invalid formats (missing "@", multiple "@", empty local or domain parts).

- Strings with leading/trailing whitespace.

> These cases ensure both correctness and robustness.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The original implementation does not safely ignore invalid entries and may raise runtime errors.

- It overstates correctness by implying proper email validation.

- It does not describe the actual validation logic used.

### Rewritten explanation
- This function counts email addresses that meet a basic validity check. It iterates through the input list, ignores non-string values, and counts entries that contain exactly one "@" with non-empty local and domain parts. Empty input results in a count of zero.

## 4) Final Judgment
- Decision: Request Changes

- Justification: The original code performs unsafe type assumptions and applies an insufficient validation rule that does not match the stated intent.

- Confidence & unknowns: Moderate confidence after fixes. The function performs basic validation but does not fully comply with formal email standards, which may be acceptable depending on requirements.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function divides the sum of non-None values by the total number of input values, including None, producing an incorrect average.

- A ZeroDivisionError occurs when the input list is empty.

### Edge cases & risks
- If all values are None, the function returns an incorrect result instead of handling the absence of valid measurements.

- Calling float(v) may raise a ValueError if a non-numeric, non-None value is present.

- Mixed-type input lists can cause runtime exceptions.

### Code quality / design issues
- The numerator and denominator are logically inconsistent.

- The function lacks explicit handling or documentation for invalid or missing values.

- The name implies safety and correctness that the implementation does not deliver.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only valid (non-None) measurements.

- Add a guard clause to prevent division by zero.

- Skip values that cannot be safely converted to floats.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

> If testing this function, focus on:

- Empty input lists.

- Lists where all values are None.

- Lists containing numeric strings, integers, and floats.

- Lists with invalid non-numeric values (e.g., "abc", objects).

- Mixed valid and invalid inputs.

> These scenarios verify correctness, safety, and resilience to malformed data

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The original code does not exclude None values from the denominator.

- It does not safely handle mixed input types and may raise exceptions.

- The explanation claims accuracy that the implementation does not achieve.

### Rewritten explanation
- This function calculates the average of valid measurements by iterating through the input list, converting non-None values to floats, and ignoring values that cannot be converted. Only successfully converted measurements are included in both the sum and the count. If no valid measurements exist, the function returns 0 to avoid division by zero.

## 4) Final Judgment
- Decision: Request Changes

- Justification: The original implementation produces incorrect averages and is unsafe when handling empty or malformed input.

- Confidence & unknowns: High confidence after fixes. The behavior for invalid numeric inputs is conservative and may be adjusted based on stricter data requirements.