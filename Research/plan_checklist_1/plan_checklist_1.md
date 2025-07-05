### **Research Execution Plan: Assessing LLM Explanations for Clinical AI**

This plan operationalizes the research proposal, breaking it down into concrete, actionable steps.

### **Phase 1: Foundation & Modeling (Target: Weeks 1-2)**

This phase is about building the technical bedrock for your experiment.

#### **1.1. Project & Environment Setup**
- [ ] Create a new project folder on your computer.
- [ ] Set up a Python virtual environment (e.g., using `venv` or `conda`).
- [ ] Activate the virtual environment.
- [ ] Create a `requirements.txt` file to track dependencies.
- [ ] Install essential libraries:
    - [ ] `pip install notebook jupyterlab pandas numpy scikit-learn`
    - [ ] `pip install matplotlib seaborn`
- [ ] Initialize a version control system: `git init`.
- [ ] Create an initial project structure (e.g., folders for `/data`, `/notebooks`, `/scripts`, `/models`).

#### **1.2. Data Acquisition and Preprocessing**
- [ ] Locate and download the "Pima Indians Diabetes Database" from the UCI Machine Learning Repository.
- [ ] Place the raw data file in your `/data` directory.
- [ ] Start a new Jupyter Notebook for "01-Data-Preprocessing-and-Modeling".
- [ ] Load the dataset into a pandas DataFrame.
- [ ] Perform initial exploratory data analysis (EDA):
    - [ ] Use `.head()` to inspect the first few rows.
    - [ ] Use `.info()` to check data types and null values.
    - [ ] Use `.describe()` to get summary statistics.
    - [ ] Visualize distributions of key features (e.g., histograms for Glucose, BMI).
- [ ] Implement the preprocessing pipeline as per the proposal:
    - [ ] Handle missing values using `sklearn.impute.KNNImputer`.
    - [ ] Separate features (X) and the target variable (y).
    - [ ] Split the data into training and testing sets using `train_test_split`.
    - [ ] Apply standard scaling (`StandardScaler`) to the features. **Important:** Fit the scaler on the training data *only* and then transform both training and testing data.
- [ ] Save the processed training and testing sets to disk (e.g., as `.csv` or `.pkl` files).

#### **1.3. Black-Box Model Training & Evaluation**
- [ ] In the same notebook, import `RandomForestClassifier` and `XGBClassifier`.
- [ ] Install `xgboost` if needed: `pip install xgboost`.
- [ ] Define a hyperparameter grid for `GridSearchCV` for the Random Forest model.
- [ ] Instantiate and run `GridSearchCV` on the training data to find the best Random Forest model.
- [ ] Repeat for XGBoost: define the grid, instantiate, and run the search.
- [ ] Select the best-performing model (or both, if you plan to use both).
- [ ] Evaluate the final model on the held-out test set to confirm performance (calculate accuracy, F1-score, confusion matrix).
- [ ] Save the final, trained model object to your `/models` folder using `joblib` or `pickle`.

### **Phase 2: Explanation Generation (Target: Weeks 3-4)**

Now you build the systems that produce the two types of explanations you will compare.

#### **2.1. Baseline Explanations (SHAP)**
- [ ] Install the SHAP library: `pip install shap`.
- [ ] Create a new Jupyter Notebook: "02-Explanation-Generation".
- [ ] Load your saved model and the processed test data.
- [ ] Select a subset of test cases (e.g., 20-30 diverse examples) for which you will generate explanations.
- [ ] Instantiate the SHAP explainer appropriate for your model (`shap.TreeExplainer`).
- [ ] Calculate SHAP values for your selected subset of test cases.
- [ ] For each case, identify the top 5 most influential features based on their SHAP values.
- [ ] Store the results systematically (e.g., in a dictionary or DataFrame mapping a patient ID to its SHAP values and top features).

#### **2.2. Novel Explanations (LLM via API)**
- [ ] Obtain an OpenAI API key.
- [ ] Install the OpenAI Python library: `pip install openai`.
- [ ] **Crucial:** Store your API key securely as an environment variable, not hardcoded in your notebook.
- [ ] In your "02-Explanation-Generation" notebook, write a helper function to format a patient's data into a human-readable string.
- [ ] Draft the core prompt template based on the proposal.
- [ ] Write a function that:
    - [ ] Takes a patient's data and the model's prediction as input.
    - [ ] Inserts them into the prompt template.
    - [ ] Calls the GPT-4 API.
    - [ ] Parses the response and extracts the explanation text.
- [ ] Loop through the *exact same subset* of test cases you used for SHAP.
- [ ] Call your function to generate and save the LLM explanation for each case.
- [ ] Store the LLM text explanations, mapping them to the patient ID.

### **Phase 3: User Study Design & Ethics (Target: Weeks 5-6)**

This phase involves careful planning of the human-computer interaction part of your research.

#### **3.1. IRB (Ethical Review) Application**
- [ ] Identify your institution's Institutional Review Board (IRB) and their submission deadlines.
- [ ] Download all required IRB application forms.
- [ ] Draft the study protocol, detailing every step a participant will take.
- [ ] Draft the informed consent form.
- [ ] Draft the participant recruitment email.
- [ ] Assemble and submit the complete IRB application package. **(Start this early!)**

#### **3.2. Survey Instrument & Materials**
- [ ] Choose your survey platform (e.g., Google Forms, Qualtrics).
- [ ] Create the full survey flow:
    - [ ] Page 1: Introduction and link to consent form.
    - [ ] Page 2: Participant consent checkbox.
    - [ ] Page 3: Brief demographic questions (as approved by IRB).
    - [ ] Page 4: Clear instructions for the task.
    - [ ] Main Task Loop (repeated for ~20 cases per participant):
        - [ ] Present patient data and model prediction.
        - [ ] Present *either* the SHAP explanation or the LLM explanation.
        - [ ] Ask the comprehension questions (1-7 Likert scales for clarity, usefulness).
        - [ ] Ask the decision-making question ("Treat" vs. "Monitor").
    - [ ] Final Page: Debriefing statement and thank you note.
- [ ] Create the matched sets of cases for the within-subjects design.
- [ ] Pilot the survey with a friend or colleague to check for clarity and technical issues. Refine based on feedback.

#### **3.3. Participant Recruitment**
- [ ] Finalize the list of professional networks or contacts for recruitment.
- [ ] Prepare the system for distributing compensation (e.g., gift card codes).

### **Phase 4: Study Execution & Data Collection (Target: Weeks 7-8)**

The experiment goes live.

- [ ] **Wait for and receive official IRB approval.** Do not proceed without it.
- [ ] Send out recruitment emails containing the link to your live survey.
- [ ] Monitor incoming responses.
- [ ] Send one polite reminder email if needed.
- [ ] Close the survey once you reach your target of 10 clinicians.
- [ ] Download the complete set of responses as a CSV file.
- [ ] Process and distribute the compensation to participants.

### **Phase 5: Analysis & Writing (Target: Weeks 9-10)**

You have the data. Now, you test your hypotheses and write your story.

#### **5.1. Data Analysis**
- [ ] Create a new Jupyter Notebook: "03-Results-Analysis".
- [ ] Load the survey data and the explanation data you generated.
- [ ] Clean and structure the survey data for analysis.
- [ ] **Hypothesis 1 (Faithfulness):**
    - [ ] Write a script to parse features from the LLM text for each case.
    - [ ] For each case, calculate the Jaccard similarity between LLM features and top-5 SHAP features.
    - [ ] Perform a one-sample t-test on the Jaccard scores against the 0.8 threshold.
- [ ] **Hypothesis 2 (Comprehensibility):**
    - [ ] Isolate the Likert scale ratings for both explanation types.
    - [ ] Perform a paired t-test comparing the LLM ratings to the SHAP ratings.
- [ ] **Hypothesis 3 (Clinical Utility):**
    - [ ] Create a contingency table comparing accuracy for decisions made with LLM vs. SHAP.
    - [ ] Perform McNemar's test on the paired responses.
- [ ] Create high-quality plots and tables summarizing your findings.

#### **5.2. Manuscript Drafting**
- [ ] Create a new document for your research paper.
- [ ] Write the **Methods** section first (you just did all this).
- [ ] Write the **Results** section, populating it with your statistical outcomes and figures.
- [ ] Write the **Introduction** and **Literature Review/Background**.
- [ ] Write the **Discussion**, interpreting your results, connecting them back to the research problem, and acknowledging limitations.
- [ ] Write the **Conclusion** and **Abstract**.
- [ ] Compile your **References**.

### **Phase 6: Finalization & Submission**

The final push to get your work out into the world.

- [ ] Share the draft with your supervisor for feedback.
- [ ] Revise the manuscript based on feedback.
- [ ] Proofread the entire paper multiple times.
- [ ] Format the paper according to the requirements of your target journal or conference.
- [ ] Submit your work.
- [ ] **Celebrate a completed research cycle!**

### Refs:
- https://aistudio.google.com/prompts/1hw-1wSJ1s4ZWQtbPUpcWlGHJDSEFUs5d
- https://notebooklm.google.com/notebook/80586287-e2e7-491a-bbca-f99a231b621f (notebooklm)