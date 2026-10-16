# Lending Club Credit Risk: Summary

## Question
Which loan applicants are most likely to default, and where should a lender
set its approval cutoff?

## Data
733,283 resolved Lending Club loans issued 2013-2015 after cleaning
(18.8% defaulted). Source: Lending Club accepted loans, via Kaggle.
Loans still being repaid were excluded.

## Approach
SQL for exploration and cleaning, Python for feature engineering and
modeling. Three models were compared on a held-out test set of 146,657 loans.

## Key findings
- **Longer loans are riskier.** 60-month loans defaulted at 32.6% vs. 14.1%
  for 36-month loans (partly because riskier borrowers were offered longer
  terms).
- **Small business loans were the riskiest purpose** (27.5%).
- **Default rates rose each year**, from 15.6% in 2013 to 20.2% in 2015.
  36-month loans alone rose from 12.3% to 14.9%, and the share of 60-month
  loans stayed flat, so the increase isn't just a shift in loan mix.
- **Loan term and FICO score were the strongest drivers** of default risk in
  the applicant-only model.
- **Model performance:** a logistic regression using applicant data alone
  reached an ROC AUC of 0.699. Adding Lending Club's own grade and interest
  rate raised it to 0.718, and gradient boosting on applicant data reached
  0.709. Applicant data captures most of the available signal.
- **Calibration:** predicted default rates matched actual rates within about
  a point across risk deciles. The riskiest decile defaulted about 8.7x as
  often as the safest (43.7% vs. 5.0%).

## Recommendation
Approve applicants with a predicted default risk under 20%. That approves
about 65% of applicants at a 12.1% default rate (vs. 18.8% for approving
everyone) and avoids about 58% of defaults. Under illustrative assumptions
(15% profit on repaid loans, 60% loss on defaults), expected profit peaks at
this cutoff, about 4.3x what approving everyone earns. A risk-averse lender
could tighten to 0.15, which approves about 46% of applicants at a 9.9%
default rate. A real bank would use its own margins, loss rates, and risk
appetite.

## Limitations
- Only approved loans are in the data, so the model can't speak to applicants
  who were rejected (selection bias).
- Loans still being repaid were excluded, so default rates for later and
  longer-term loans may be overstated.
- The profit figures rest on illustrative assumptions, not Lending Club's
  actual economics.
- The threshold was chosen on the same test set used to evaluate the model.
- Default rates rose over time, so a model trained on past loans may be less
  accurate on future ones. A time-based test would check this.
- I found and fixed a leakage problem: an early payment-to-income feature
  embedded Lending Club's interest rate through the installment amount, so I
  replaced it with a version that uses a fixed assumed rate.
- Features like state were left out of the model on purpose, because location
  can act as a proxy for protected characteristics.

## Next steps
Test on a time-based split (train on 2013-2014, test on 2015), compare
against a validation-set threshold choice, and add fairness checks.