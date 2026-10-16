# Data Cleaning Log

**Source:** Lending Club accepted loans, filtered to loans issued 2013-2015
with a resolved outcome (Fully Paid, Charged Off, or Default).

## Summary
- Rows before cleaning: 733,453
- Rows after cleaning: 733,283
- Rows removed: 170 (about 0.02%)

## Rows removed and why
| Rule | Rows | Reason |
|---|---|---|
| Annual income = 0 | 2 | Likely data entry errors |
| Annual income >= $1,000,000 | 147 | Extreme outliers that would distort averages and models |
| DTI > 60 | 21 | Implausible values (the maximum was 999, likely a placeholder) |
| DTI missing | 2 | Cannot be used in the model |

The counts above total 172, but 170 unique rows were removed because 2 loans
met more than one rule.

## Rows kept on purpose
- **revol_util above 100** (3064 rows): possible for borrowers over their credit
  limit, so kept. Will be capped during feature engineering.
- **emp_length missing** (5.4%): too large to drop, and may be informative.
  Will be labeled "Unknown" during feature engineering.

## Notes
- The original `loans` table is unchanged. All cleaning is applied in a new
  `loans_clean` table so the work is reproducible.