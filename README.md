# Loan Automation Approval Process (Mini_Project)

### [Assignment](assignment.md)

## Project/Goals
In this project the goal is do design a machine learning model that predicts Loan Approval Status automatically given these 11 features about a client, 
Loan_ID, Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area.

The main focus for me was on Deployment (locally and in the cloud) and pipelines and model improvement. 

## Hypothesis

* Applicants with prior credit score get more approvals 
* Applicants with graduate education get more approvals 
* Emplyed Applicant have a better chance vs self employed
* Male applicants get more approvals

## EDA 

* Targe variable distribution 68% approval (One can of this result as a base model for accuracy. A very stupid model that just guesses yes would have a 68% accuracy)
* Applicants with prior credit score get more approvals, yes we can see that this is the case for our data set. 
* Applicants with graduate education get more approvals, yes but not as derastic as one would assume, very minute difference here
* Employed Applicant have a better chance vs self employed. No, not much of a difference between employed and self employed in the loan approval proprotions 
* Male applicants get more approvals, no not much of a difference in approval between male and female proportions  


## Process
### As I started the project a bit later, time was a constraint. So I broke down the process into two steps 

### Base_Model_1 (MVP) 
Main focus on setps 5 & 6

1. Simple base model 1
2. Null values replaced with mean 
3. Categorical variables to numerical 
4. Split Data and train the model 
5. Serialize Using Pickle 
6. Deploy using flask locally and on AWS VM


### Model_1 

1. Pipleine build
    1. Processing 
           -Impute mean
           -Impute mode and one hot incode 
    2. Scaling Data
    3. PCA and k best 
    4. RandomForestClassifier(), LogisticRegression(), SVC(), (which ever has better results)
    3. Hyperparameters tunning (Gridsearch)
    
2. Model prediction improvement 


## Results/Demo
* Base_model_1 score was 69% in terms of accuracy and 78% F1 score, so not much better than just guessing yes everytime, however the goal was an MVP to practice both local & cloud deployment. 

* Model 1 score was 81.3% in terms of accuracy and 88% F1 score, which overal I am happy with, but there is always room for improvment. 


## Challanges 
Two main challenges 

* Time constraints
* Learning how to work with AWS and AWS documentation. 

## Future Goals
This is actually a very interesting project (from a project problem angle), as I have ineterest in banking and finance sectors. In the future I would like to visit this project again with a much larger data set, learn more about the features and play around with more model to improve predictive power. 
