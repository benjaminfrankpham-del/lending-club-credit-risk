# Credit Risk Analytics: Predicting Loan Default & Optimizing Approval Decisions

## Dashboard Preview

![Lending Club Credit Risk Analytics Dashboard](reports/figures/dashboard.png)

## Business Problem

Lenders must decide which applicants to approve for a loan. Approving too many risky borrowers leads to losses from defaults, while declining too many good borrowers means lost revenue.

With roughly one in five loans in this dataset ending in default, the challenge is to estimate each applicant's default risk accurately and choose an approval cutoff that balances risk against profit.

## Objective

Develop an end-to-end credit risk analytics project that uses SQL, Python, machine learning, and Tableau to identify the borrower and loan characteristics that drive default, predict the probability of default, and recommend an approval cutoff based on expected profit.

## Assessment Scope

The project uses Lending Club accepted loans issued from 2013 to 2015, approximately **733,000 loans with a resolved outcome** (Fully Paid, Charged Off, or Default) after cleaning. Data source: [Lending Club loan data on Kaggle](https://www.kaggle.com/wordsforthewise/lending-club). The raw data is not included in this repository.

The assessment covers:

- Data cleaning and preparation
- SQL-based data analysis
- Feature engineering
- Machine learning using logistic regression and gradient boosting
- Model performance evaluation and calibration
- Data leakage detection
- Approval cutoff and expected profit analysis
- Tableau dashboard development

## Skills Demonstrated

### Coding Languages

- Python
- SQL

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

### Database

- SQLite
- SQL data analysis
- Data cleaning with SQL
- Data transformation

### Business Intelligence

- Tableau
- Dashboard development
- KPI development
- Data visualization
- Risk analysis
- Business insights

### Development Tools

- Git
- GitHub
- Visual Studio Code
- Python Virtual Environment

## Skills Demonstrated

- Data Cleaning & Preparation
- Exploratory Data Analysis
- SQL Analytics
- Feature Engineering
- Machine Learning
- Credit Risk Analytics
- Model Evaluation & Calibration
- Data Leakage Detection
- Decision Threshold Optimization
- Data Visualization
- Tableau Dashboard Development
- Business Intelligence
- Data Storytelling

## Dashboard Highlights

- Default rate by loan term
- Predicted vs. actual default rate by risk decile (model calibration)
- Approval rate vs. default rate tradeoff by cutoff
- Expected profit by cutoff compared with approving every applicant
- Top drivers of default risk
- Approval cutoff recommendation

## Key Findings

- The cleaned dataset contains **733,283 loans**, with **18.8%** ending in default.
- **60-month loans defaulted at 32.6%**, compared with **14.1%** for 36-month loans.
- Default rates rose each year, from **15.6% in 2013 to 20.2% in 2015**. The trend also appears in 36-month loans alone (**12.3% to 14.9%**), so it is not just a shift in loan mix.
- **Loan term and FICO score** were the strongest drivers of default risk.
- A logistic regression using only applicant data achieved a **0.699 ROC-AUC**. Adding Lending Club's own grade and interest rate raised it to **0.718**, and gradient boosting reached **0.709**.
- Predicted default rates matched actual rates within about a point across risk deciles, and the riskiest decile defaulted **8.7x** as often as the safest (**43.7% vs. 5.0%**).
- A data leakage issue was identified and fixed: an early payment-to-income feature embedded Lending Club's interest rate through the installment amount, so it was replaced with a version using a fixed assumed rate.
- Approving applicants with predicted default risk under **20%** approves **64.8%** of applicants at a **12.1%** default rate (vs. 18.8% for approving everyone) and avoids **58.3%** of defaults.
- Under illustrative assumptions (15% profit on repaid loans, 60% loss on defaults), expected profit peaks at the 20% cutoff, about **4.3x** what approving everyone would earn.

## Recommendation

Approve applicants whose predicted default risk is under 20%.

| Cutoff | Approved | Default Rate of Approved | Defaults Avoided |
|---|---|---|---|
| 0.10 | 22.2% | 6.9% | 91.8% |
| 0.15 | 46.5% | 9.9% | 75.6% |
| **0.20** | **64.8%** | **12.1%** | **58.3%** |
| 0.25 | 76.1% | 13.6% | 44.9% |
| 0.30 | 83.6% | 14.8% | 34.2% |
| 0.40 | 93.4% | 16.8% | 16.5% |

The profit assumptions are illustrative, not Lending Club's actual economics. A real lender would use its own margins, loss rates, and risk appetite.

## Limitations

- Only approved loans are in the data, so the model cannot speak to applicants who were rejected (selection bias).
- Loans still being repaid were excluded, so default rates for later and longer-term loans may be overstated.
- The cutoff was chosen on the same test set used to evaluate the model.
- Default rates rose over time, so a model trained on past loans may be less accurate on future ones.
- Lending Club's own grade and rate were excluded from the main model, and state was left out because location can act as a proxy for protected characteristics.

## How to Reproduce

1. Download the accepted-loans file from the Kaggle link above and place it in the `data/archive/` folder.
2. Set up the environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```
3. Build the filtered dataset and database:
```bash
   python src/filter_data.py
   python src/load_to_sqlite.py
```
4. Run the notebooks in order: `notebooks/01_sql_exploration.ipynb`, `02_eda_and_features.ipynb`, and `03_modeling.ipynb`.