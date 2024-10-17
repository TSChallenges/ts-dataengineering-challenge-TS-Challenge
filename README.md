# Data Engineering Challenge

An implementation of core data engineering concepts using Python and SQL, with GitHub Codespaces integration.

## Objective
In this challenge, you are working as a Data Engineer for a retail banking company. Your task is to build an ETL (Extract, Transform, Load) pipeline that processes the bank’s transaction data. The company collects various transaction types, customer ages, and balances, and they need a system to extract this data from raw files, clean and transform it, and load it into a database for analysis.

You will be working with a dataset containing 100 rows of customer IDs, ages, transaction types, and balances, which is provided in the repository as `bank_transactions_dataset.csv`. Your task is to implement the ETL pipeline to process this data.

---

## Getting Started
1. Once you accept the assignment, you will be redirected to your own copy of the repository.
2. the repo is forked, and you only need to commit the changes that you make in the Python files. 
3. **Use GitHub Codespaces**:
   - Click on the green **Code** button in your forked repository.
   - Select **Codespaces** and choose "Create codespace on main" to open your development environment.

4. The repository includes a pre-configured `devcontainer.json` file, which automatically sets up the Python environment in Codespaces.
5. Once the Codespace is ready and the environment is set up, review the code in the Python files to understand the structure.
6. Implement the missing functions marked with **TODO** comments.
7. Test your implementation by running the `main.py` file inside GitHub Codespaces.

---

## Files to Work On
- `extract.py`: Implement data extraction from the provided CSV file.
- `transform.py`: Implement data transformation logic (data cleaning, feature engineering).
- `load.py`: Implement loading the cleaned data into a SQLite database.
- `main.py`: Control the ETL pipeline and test your implementation.

---

## Requirements
- **`extract.py`**:
  - Implement the `extract_data` function to read the data from `bank_transactions_dataset.csv`.

- **`transform.py`**:
  - Implement the `transform_data` function to clean and transform the data (handle missing values, format changes, etc.).

- **`load.py`**:
  - Implement the `load_data` function to load the transformed data into a SQLite database.

- **`main.py`**:
  - Implement the pipeline flow (call extract, transform, and load functions).

---

## Steps to Follow
1. Accept the assignment to get your forked repository and set up your environment using **GitHub Codespaces**.
2. **extract.py**: Implement the logic to extract data from the `bank_transactions_dataset.csv`.
3. **transform.py**: Implement the transformation logic (e.g., handle missing values, data normalisation).
4. **load.py**: Implement the loading logic to insert the cleaned data into a SQLite database.
5. Run the codes inside **GitHub Codespaces** to test your implementation.
6. After completing the coding on those three files, examine the ETL pipeline in **main.py**.
7. Run the **main.py** to complete the ETL challenge; your final SQL_database will be created in the repo.
8. Commit the changes using the commit button available in the codespace.
 

---

## Tips
- Make sure you handle different data types properly (e.g., strings, integers, floats).
- Use the SQLite library in Python to interact with the database.
- Ensure data quality checks are in place after the transformation step.

---

## Submission Guidelines
After completing the challenge, commit the changes using the commit button available in the codespace. Make sure the changes have been successfully committed.

---

## Evaluation Criteria
- Correct implementation of the ETL pipeline (extract, transform, load).
- Proper handling of missing or invalid data.
- Accurate data insertion into the SQLite database.
- Clean and readable code with appropriate comments and structure.
- Successful execution of the project within **GitHub Codespaces**.

Good luck, and happy coding!
