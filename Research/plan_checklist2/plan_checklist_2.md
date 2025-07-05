# Exercises: Implementing an XAI Research Proposal in Python

This file contains a complete curriculum designed to take you from foundational setup to a practical, code-based implementation of a research proposal. The exercises are structured in three phases to build your skills progressively, turning the theoretical proposal into a tangible, working project. Tackle them in order to build momentum and master the concepts.

## Phase 1: Foundational Syntax & Setup (~15 Exercises)

_This phase is all about building your environment and mastering the basic commands for each library. The exercises are short, focused, and designed to provide "quick wins" that form the building blocks of the entire project._

---

### Exercise 1: Project Environment Setup
*   **Scenario:** Every good project starts with a clean, isolated environment to manage dependencies.
*   **Task:** Create a new directory for your project. Inside it, create a new Python virtual environment (e.g., using `venv` or `conda`). Activate the environment.
*   **Focus:** This tests your ability to use basic terminal commands and Python's environment management tools.
*   **Verification:**
    *   **Input:** Running `which python` (or `where python` on Windows) in your terminal.
    *   **Expected Output:** The command should show a path to a Python executable inside your newly created project directory.

### Exercise 2: Installing Your First Package
*   **Scenario:** The project requires the `pandas` library to handle the dataset. Let's install it.
*   **Task:** With your virtual environment active, use `pip` to install the `pandas` library.
*   **Focus:** Using the `pip` package manager.
*   **Verification:**
    *   **Input:** Run the command `pip freeze`.
    *   **Expected Output:** The output list should contain `pandas` along with its dependencies like `numpy`.

### Exercise 3: Creating a Project Script
*   **Scenario:** You need a primary file where your Python code will live.
*   **Task:** Create a new file named `main.py` in your project directory. Add a single `print("Project Initialized")` statement to it.
*   **Focus:** Basic file creation and running a Python script.
*   **Verification:**
    *   **Input:** Run `python main.py` from your terminal.
    *   **Expected Output (in console):** `Project Initialized`

### Exercise 4: Loading the Dataset
*   **Scenario:** The research is based on the Pima Indians Diabetes dataset. Your first coding task is to load this data into your script. The `ucimlrepo` library is perfect for this. (Hint: You'll need to `pip install ucimlrepo`).
*   **Task:** In `main.py`, write the code to import `fetch_ucirepo` and use it to fetch the Pima Indians Diabetes dataset (ID: 22). Store the features in a pandas DataFrame variable named `X`.
*   **Focus:** Using a library function to get data and storing it in a DataFrame.
*   **Verification:**
    *   **Input:** Add `print(type(X))` to your script.
    *   **Expected Output (in console):** `<class 'pandas.core.frame.DataFrame'>`

### Exercise 5: Initial Data Inspection
*   **Scenario:** Before any analysis, a good researcher always takes a quick look at their data's structure.
*   **Task:** Use pandas functions to print the first 5 rows of the DataFrame `X` and its overall dimensions (shape).
*   **Focus:** Using the `.head()` and `.shape` attributes/methods of a pandas DataFrame.
*   **Verification:**
    *   **Input:** Running your script.
    *   **Expected Output (in console):** The script should first print the first 5 rows of the Pima dataset, followed by the tuple `(768, 8)`.

### Exercise 6: Basic Data Summarization
*   **Scenario:** You need to get a high-level statistical overview of the dataset's features.
*   **Task:** Use a single pandas function to generate and print descriptive statistics (count, mean, std, etc.) for all columns in the DataFrame `X`.
*   **Focus:** Using the `.describe()` method.
*   **Verification:**
    *   **Input:** Running your script.
    *   **Expected Output (in console):** A table showing statistics for each of the 8 features. For the 'age' column, the `mean` should be approximately `33.24`.

### Exercise 7: Identifying Missing Data
*   **Scenario:** The proposal mentions "k-NN imputation for missing values." First, you must confirm if and where data is missing. Some datasets hide missing values as `0` in columns where that's biologically impossible (e.g., 'Glucose', 'BloodPressure').
*   **Task:** For the 'Glucose' column, count how many rows have a value of `0`.
*   **Focus:** DataFrame column selection and conditional filtering.
*   **Verification:**
    *   **Input:** `print((X['Glucose'] == 0).sum())`
    *   **Expected Output (in console):** `5`

### Exercise 8: Basic Data Cleaning
*   **Scenario:** To properly use an imputer, you must replace the "hidden" missing values (`0`) with a proper `NaN` (Not a Number) value.
*   **Task:** Replace all `0` values in the 'Glucose', 'BloodPressure', and 'BMI' columns with NumPy's `NaN`. (Hint: You'll need to `import numpy as np`).
*   **Focus:** Using `numpy` and advanced DataFrame assignment with `.loc`.
*   **Verification:**
    *   **Input:** After your replacement code, print the number of null values in the 'Glucose' column using `.isnull().sum()`.
    *   **Expected Output (in console):** `5`

### Exercise 9: Installing a Machine Learning Library
*   **Scenario:** The project requires `scikit-learn` for preprocessing and modeling.
*   **Task:** Install the `scikit-learn` library using `pip`.
*   **Focus:** Dependency management with `pip`.
*   **Verification:**
    *   **Input:** Run `pip freeze`.
    *   **Expected Output:** The output list should now include `scikit-learn`.

### Exercise 10: Splitting Data for Training
*   **Scenario:** To train and evaluate a model, you must separate your data into training and testing sets.
*   **Task:** Use `scikit-learn`'s `train_test_split` function to split your data (`X` and the target `y`) into training and testing sets. Use a test size of 20% and a `random_state` of 42 for reproducibility.
*   **Focus:** Using a core `scikit-learn` utility function.
*   **Verification:**
    *   **Input:** Print the shape of the resulting `X_train` DataFrame.
    *   **Expected Output (in console):** `(614, 8)`

### Exercise 11: Training a Basic Model
*   **Scenario:** As a first step, train one of the black-box models mentioned in the proposal: the Random Forest.
*   **Task:** Import `RandomForestClassifier` from `scikit-learn`. Initialize it with `random_state=42` and train it on your training data (`X_train`, `y_train`). (Note: You'll need to handle the `NaN` values from Exercise 8 first, perhaps by simply dropping them for this exercise).
*   **Focus:** The `.fit()` method, a cornerstone of `scikit-learn` modeling.
*   **Verification:**
    *   **Input:** No direct output, but the script should run without errors.
    *   **Expected Output:** Successful execution.

### Exercise 12: Making a Prediction
*   **Scenario:** Now that the model is trained, use it to make a prediction on a single, unseen data point from your test set.
*   **Task:** Select the first row of your `X_test` data and use the trained model's `.predict()` method to predict the outcome.
*   **Focus:** The `.predict()` method.
*   **Verification:**
    *   **Input:** Print the prediction for the first row of `X_test`.
    *   **Expected Output (in console):** `[0]` (representing 'No Diabetes').

### Exercise 13: Installing the XAI Library
*   **Scenario:** The core of the project involves SHAP. You need to install the `shap` library.
*   **Task:** Install the `shap` library using `pip`.
*   **Focus:** Dependency management with `pip`.
*   **Verification:**
    *   **Input:** Run `pip freeze`.
    *   **Expected Output:** The output list should now include `shap`.

### Exercise 14: Installing the LLM Library
*   **Scenario:** To generate explanations, you'll need to communicate with OpenAI's API.
*   **Task:** Install the `openai` library using `pip`.
*   **Focus:** Dependency management with `pip`.
*   **Verification:**
    *   **Input:** Run `pip freeze`.
    *   **Expected Output:** The output list should now include `openai`.

### Exercise 15: Setting up API Key
*   **Scenario:** To use the `openai` library, you must configure your API key securely. Using an environment variable is best practice.
*   **Task:** Set an environment variable named `OPENAI_API_KEY` to your secret key. In your Python script, import the `os` library and write code to load this key into a variable.
*   **Focus:** Securely managing credentials and using the `os` library.
*   **Verification:**
    *   **Input:** Print the loaded API key variable.
    *   **Expected Output (in console):** Your secret API key string. (Be careful not to commit this code!).

---

## Phase 2: Conceptual Integration & Problem-Solving (~10 Exercises)

_Now it's time to connect the blocks from Phase 1. These exercises require you to build small, multi-step functions that replicate key parts of the research methodology._

---

### Exercise 16: Building a Preprocessing Pipeline
*   **Scenario:** The proposal requires a two-step preprocessing: k-NN imputation for missing values followed by standard scaling. Let's build a reusable pipeline for this.
*   **Task:** Use `scikit-learn`'s `Pipeline` object. The pipeline should contain two steps: a `KNNImputer` (with `n_neighbors=5`) and a `StandardScaler`. Fit this pipeline on your `X_train` data.
*   **Focus:** Combining `scikit-learn` transformers into a single, reusable `Pipeline`.
*   **Verification:**
    *   **Input:** Use the fitted pipeline to `.transform()` your `X_train` data and print the mean of the first column of the result.
    *   **Expected Output:** A number very close to `0.0` (as the data is now standardized).

### Exercise 17: Generating a SHAP Explanation
*   **Scenario:** You need to generate a SHAP explanation for a single patient case to identify the most influential features, which is the baseline for comparison in RQ1.
*   **Task:** After training a `RandomForestClassifier` on the preprocessed data, create a `shap.TreeExplainer` for the model. Use the explainer to calculate SHAP values for the first instance of your (preprocessed) `X_test`.
*   **Focus:** Integrating `shap` with a trained `scikit-learn` model.
*   **Verification:**
    *   **Input:** Print the `.shape` of the resulting SHAP values object for that single instance.
    *   **Expected Output:** `(8,)`, representing one SHAP value for each of the 8 features.

### Exercise 18: Extracting Top-K Features from SHAP
*   **Scenario:** For Hypothesis 1, you need to compare against the "top-5 features identified by SHAP." You must write code to extract these programmatically.
*   **Task:** From the SHAP values generated in the previous exercise, find the names of the 5 features with the largest absolute SHAP values.
*   **Focus:** Manipulating `numpy` arrays (for SHAP values) and `pandas` DataFrames (for feature names) to rank and select data.
*   **Verification:**
    *   **Input:** Print the list of the top 5 feature names.
    *   **Expected Output:** A list of 5 strings, which will likely include `'Glucose'`, `'BMI'`, `'Age'`, etc.

### Exercise 19: Crafting an LLM Prompt
*   **Scenario:** To generate an LLM explanation, you must create the exact prompt described in the proposal. This involves formatting a patient's data into a string.
*   **Task:** Write a function that takes a single row of patient data (a pandas Series) and the model's prediction, and returns the formatted prompt string: `“Model prognosis: Diabetes=Yes/No for patient with features {...}. In plain language, explain why.”`
*   **Focus:** String formatting (f-strings) and working with pandas Series.
*   **Verification:**
    *   **Input:** Call the function with the first row of `X_test` and a prediction of 'No'. Print the result.
    *   **Expected Output:** A string like `“Model prognosis: Diabetes=No for patient with features {'Pregnancies': 6.0, 'Glucose': 148.0, ...}. In plain language, explain why.”`

### Exercise 20: Calling the LLM API
*   **Scenario:** Now, let's wire up the prompt to the OpenAI API to get a real explanation.
*   **Task:** Write a function that takes a prompt string, uses the `openai` client to send it to the `gpt-4` model, and returns the text content of the model's response.
*   **Focus:** Using the `openai.chat.completions.create` method.
*   **Verification:**
    *   **Input:** Call the function with a simple prompt like `"Explain what SHAP is in one sentence."`. Print the result.
    *   **Expected Output:** A single, coherent sentence defining SHAP.

### Exercise 21: Extracting Features from LLM Text
*   **Scenario:** To test Hypothesis 1 (faithfulness), you must extract the features the LLM *mentions* in its narrative explanation.
*   **Task:** Write a simple function that takes the LLM's text response and a list of all possible feature names (e.g., `['Glucose', 'BMI', ...]`). The function should return a list of the feature names found within the text. (A simple substring check is sufficient).
*   **Focus:** Basic string manipulation and list comprehensions.
*   **Verification:**
    *   **Input:** `extract_features("The model focused on high Glucose and the patient's BMI.", ['Glucose', 'BMI', 'Age'])`
    *   **Expected Output:** `['Glucose', 'BMI']`

### Exercise 22: Calculating Jaccard Similarity
*   **Scenario:** Hypothesis 1 uses Jaccard similarity to measure feature overlap. You need a function to calculate this metric.
*   **Task:** Write a function that takes two lists of features (e.g., one from SHAP, one from the LLM) and returns their Jaccard similarity score (size of intersection / size of union).
*   **Focus:** Working with Python `set` objects and their methods (`.intersection()`, `.union()`).
*   **Verification:**
    *   **Input:** `jaccard(['a', 'b', 'c'], ['b', 'c', 'd'])`
    *   **Expected Output:** `0.5` (Intersection is {'b', 'c'} (size 2), Union is {'a', 'b', 'c', 'd'} (size 4)).

### Exercise 23: Simulating a Statistical Test (t-test)
*   **Scenario:** The proposal uses a paired t-test for Hypothesis 2. Let's practice using the statistical function.
*   **Task:** Import `ttest_rel` from `scipy.stats`. Create two mock lists of Likert scores, e.g., `llm_scores = [6, 7, 5, 6, 7]` and `shap_scores = [4, 5, 4, 3, 5]`. Run a paired t-test on them.
*   **Focus:** Using the `scipy.stats` library for hypothesis testing.
*   **Verification:**
    *   **Input:** Print the p-value from the t-test result.
    *   **Expected Output:** A p-value less than 0.05 (for the sample data, it should be around `0.015`).

### Exercise 24: Training the Second Model (XGBoost)
*   **Scenario:** The proposal compares two models. You need to install and train an `XGBoost` classifier.
*   **Task:** Install the `xgboost` library. Import `XGBClassifier`, initialize it, and train it on your preprocessed training data.
*   **Focus:** Installing and using a third-party ML library with an `scikit-learn`-like interface.
*   **Verification:**
    *   **Input:** Use the trained XGBoost model to predict the first 5 instances of `X_test` and print the results.
    *   **Expected Output:** An array of 5 predictions, e.g., `[0 1 0 0 1]`.

### Exercise 25: Saving and Loading a Model
*   **Scenario:** For a real application, you don't want to retrain your model every time. You need to save your trained model to a file.
*   **Task:** Use the `joblib` library (installed with scikit-learn) to save your trained RandomForest model to a file named `rf_model.joblib`. Then, write code to load it back into a new variable and verify it works.
*   **Focus:** Model persistence using `joblib.dump` and `joblib.load`.
*   **Verification:**
    *   **Input:** Load the model and use it to make a prediction on the first row of `X_test`. Print the result.
    *   **Expected Output:** `[0]`, the same prediction as the original model made.

---

## Phase 3: Applied Mini-Projects (5 Projects)

_This is where it all comes together. Each mini-project implements a major component of the research proposal, resulting in a functional, code-based version of the study's methodology._

---

### Project 1: The Full Data-to-Model Pipeline
*   **Objective:** To create a single, executable script that handles the entire data preparation and model training process, resulting in a saved, production-ready model.
*   **Background Scenario:** You are preparing the foundational "black-box" model for the study. This script will be the repeatable, reliable source for that model.
*   **Core Tasks:**
    1.  **Load Data:** Fetch the Pima dataset from `ucimlrepo`.
    2.  **Clean Data:** Perform the `0`-to-`NaN` replacement for specified columns.
    3.  **Separate Features/Target:** Split the data into `X` and `y`.
    4.  **Build Preprocessing Pipeline:** Create and fit the `KNNImputer` + `StandardScaler` pipeline on the *entire* dataset (for a final model, we train on all data).
    5.  **Train Model:** Initialize and train an `XGBClassifier` on the fully preprocessed data.
    6.  **Save Artifacts:** Save the fitted preprocessing pipeline to `preprocessor.joblib` and the trained XGBoost model to `xgb_model.joblib`.
*   **Key Concepts Utilized:** `pandas` DataFrames, `scikit-learn` Pipelines, `XGBoost` modeling, `joblib` for serialization.
*   **Deliverable:** A script `01_train_model.py` that, when run, produces the two `.joblib` files.
*   **Success Criteria:**
    *   ✅ The script runs from start to finish without errors.
    *   ✅ The files `preprocessor.joblib` and `xgb_model.joblib` are created in the project directory.
    *   ✅ When you manually load `xgb_model.joblib`, its `.is_fitted()` attribute is `True`.

### Project 2: The SHAP Explainer Module
*   **Objective:** To build a reusable script that can load the trained model and generate a structured SHAP explanation for any given patient case.
*   **Background Scenario:** This module will serve as the engine for generating the "baseline" technical explanations used for comparison in every part of the study.
*   **Core Tasks:**
    1.  **Load Artifacts:** Load the `preprocessor.joblib` and `xgb_model.joblib` files.
    2.  **Define a Sample Patient:** Create a pandas DataFrame with a single row representing one patient from the original dataset (e.g., row index 15).
    3.  **Process Input:** Apply the loaded preprocessor to the sample patient data.
    4.  **Generate Explanation:** Create a `shap.TreeExplainer` and calculate SHAP values for the processed sample patient.
    5.  **Extract & Format Output:** Identify the top 5 features by absolute SHAP value and print them to the console in a clean, readable format (e.g., `Feature: Glucose, Contribution: 0.45`).
*   **Key Concepts Utilized:** `joblib`, `shap`, `pandas`, `numpy` array manipulation.
*   **Deliverable:** A script `02_generate_shap.py` that prints a formatted SHAP explanation for a hardcoded patient case.
*   **Success Criteria:**
    *   ✅ The script successfully loads the model and preprocessor.
    *   ✅ The script prints a list of exactly 5 features.
    *   ✅ Each printed line includes the feature name and its corresponding SHAP value.

### Project 3: The LLM Explainer Module
*   **Objective:** To build a script that generates a narrative, LLM-based explanation for a patient case, mirroring the proposed methodology.
*   **Background Scenario:** This is the engine for generating the "proposed" explanations. It needs to encapsulate prompt engineering and the API call.
*   **Core Tasks:**
    1.  **Load Artifacts:** Load the model and preprocessor.
    2.  **Load Patient Data:** Use the same sample patient as in Project 2.
    3.  **Make Prediction:** Use the loaded model to predict the outcome for the patient.
    4.  **Construct Prompt:** Use your prompt-generating function from Phase 2 to create the specific prompt for the patient's data and the model's prediction.
    5.  **Call API:** Send the prompt to the OpenAI API (using your function from Phase 2).
    6.  **Save Output:** Print the LLM's narrative explanation to the console and also save it to a text file, e.g., `patient_15_explanation.txt`.
*   **Key Concepts Utilized:** `joblib`, `openai` API calls, string formatting, file I/O.
*   **Deliverable:** A script `03_generate_llm_explanation.py` that produces a `.txt` file containing the explanation.
*   **Success Criteria:**
    *   ✅ The script runs without errors and makes an API call.
    *   ✅ The file `patient_15_explanation.txt` is created.
    *   ✅ The content of the file is a plausible, natural language explanation related to diabetes risk factors.

### Project 4: The Faithfulness Analyzer (H1)
*   **Objective:** To create a single script that automates the faithfulness analysis for one patient case, directly testing Hypothesis 1.
*   **Background Scenario:** This is the heart of RQ1. This script orchestrates the previous modules to produce a quantitative faithfulness score.
*   **Core Tasks:**
    1.  **Generate Explanations:** Programmatically call the logic from Project 2 (SHAP) and Project 3 (LLM) to get both explanations for a single patient.
    2.  **Extract SHAP Features:** Get the list of top-5 feature names from the SHAP explanation.
    3.  **Extract LLM Features:** Use your text-parsing function to extract the list of feature names mentioned in the LLM's response.
    4.  **Calculate Similarity:** Use your Jaccard similarity function to compare the two lists of features.
    5.  **Report Results:** Print the two feature lists and the final Jaccard score in a clear, final report to the console.
*   **Key Concepts Utilized:** Function composition, data flow management, and application of custom metrics.
*   **Deliverable:** A script `04_analyze_faithfulness.py` that outputs a final analysis report for one patient.
*   **Success Criteria:**
    *   ✅ The script runs the full pipeline for one patient.
    *   ✅ The output clearly labels and lists the SHAP features.
    *   ✅ The output clearly labels and lists the LLM-mentioned features.
    *   ✅ The script prints a final line: `Jaccard Similarity (Faithfulness Score): [a number between 0.0 and 1.0]`.

### Project 5: The User Study Asset Generator
*   **Objective:** To automate the generation of all materials needed for the human-centered evaluation (H2 and H3).
*   **Background Scenario:** You're preparing for the user study with 10 clinicians. You need to generate the explanation pairs for a set of 20 patient cases that they will review. This project builds the tool to do that at scale.
*   **Core Tasks:**
    1.  **Select Cases:** Randomly select 20 patient cases from the test set.
    2.  **Create Output Directory:** Create a directory named `user_study_assets`.
    3.  **Loop and Generate:** Loop through each of the 20 selected patients. For each patient:
        *   Generate the SHAP explanation (top 5 features and values).
        *   Generate the LLM narrative explanation.
        *   Save the SHAP explanation to a file like `user_study_assets/patient_XX_shap.txt`.
        *   Save the LLM explanation to a file like `user_study_assets/patient_XX_llm.txt`.
    4.  **Log Progress:** Print a message to the console each time a patient's assets are successfully generated.
*   **Key Concepts Utilized:** Loops, file I/O, string formatting, and project orchestration.
*   **Deliverable:** A script `05_generate_study_assets.py` that populates the `user_study_assets` directory.
*   **Success Criteria:**
    *   ✅ After running, the `user_study_assets` directory exists.
    *   ✅ The directory contains exactly 40 files (20 `_shap.txt` and 20 `_llm.txt`).
    *   ✅ The filenames are correctly numbered corresponding to the patient indices used.
    *   ✅ The script completes without any errors.