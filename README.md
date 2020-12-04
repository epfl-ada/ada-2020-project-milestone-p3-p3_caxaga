# Milestone P3: Creative Extension - Tesco Dataset
## 1. Title
**Predicting the food consumption behavior of an area based on publicly available data related to well-being**
## 2. Abstract
The idea is to study the consumption of different nutrients based on well-being improvement data as well as predicting dietary patterns for other areas for which we have indicators of well-being. When talking about well-being, we refer to both objective aspects (financial, health, family data) and subjective well-being (happiness). The ultimate goal is to better target people likely to be affected by diseases related to unhealthy food consumption in order to give them nutritional recommendations and predict nutritional properties in a given area to adapt the products proposed to the consumers. We will try to find a correlation between nutritional habits and well-being as well as the identification of sub-groups of criteria (financial, education, etc.) particularly linked to nutrition. Then, a regression model will be implemented to predict dietary patterns based on well-being measures. Our analysis will rely on the dataset “London ward well-being probability scores,” which uses 12 measures to calculate the well-being scores as well the Tesco datasets provided. We will link those two datasets to a happiness score obtained per borough that will be adapted to the ward scale.  We will use cross-validation to assess the validity of our predictions.
## 3. Research Questions
* Can we predict nutritional patterns in an unknown area given publicly available data related to well-being?
* Which well-being factors are highly correlated with food consumption and therefore are worth being targeted when trying to improve food habits in an area? 
*How can we explain when well being scores are the same for different nutritional values? 
* How can we use these predictions to make better recommendations to help the population of an area improve its health?


## 4. Proposed dataset
We use three datasets that are publicly available at the [London Datastore](https://data.london.gov.uk/). The London Datastore is a free and open data-sharing portal where anyone can access data relating to the city of London.  The site provides over 900 datasets with the goal of developing solutions for the city.
### [London ward well-being probability scores](https://data.london.gov.uk/dataset/london-ward-well-being-scores)
The dataset we will use with well-being measures is from 2013 whereas Tesco is from 2015. However, we can make the assumption that, in two years, well-being does not change drastically. Therefore, those two datasets can be linked. It provides well-being scores at the ward level using indicators based on 12 measures covering different themes like health, economic security, safety, education, children, families, access, and environment.
### [Subjective personal well-being](https://data.london.gov.uk/dataset/subjective-personal-well-being-borough)
Estimates of personal well-being from the Annual Population Survey (APS) well-being dataset. Data shows life satisfaction, how worthwhile people feel, whether people feel happy or anxious.
### [From Borough to ward](https://data.london.gov.uk/download/land-area-and-population-density-ward-and-borough/d961f13b-6726-4fa8-823f-03b379429b72/housing-density-ward.csv)
As we know the happiness score at the borough scale, we obtained a dataset giving the ward per borough. We would therefore be able to know the happiness score per ward. 

## 5. Methods
### Pre-processing
1. Data consolidation: merging the different datasets according to the ward code, handling missing values.
### Data correlation
1. Evaluation of the correlation between the different variables of the merged dataset
2. Feature selection, reduction.
3. Observational study to understand if the consumption behavior of a zone is caused by specific factors of well-being.
### Predictive models
1. Regression model with different models
* Linear regression
* Logistic regression
* Support vector machine
* Decision tree, random forest
* Neural network (TBD)
### Validation
1. Cross-validation in order to assess the validity of our predictions.
### Visualization 
1. Visual representation of the obtained results
* Geomap to visually explore the data
* Bar plot to visualize correlations
* ROC curve to compare predictive models

## 6-7. Proposed timeline and organization within the team
We will organize the next weeks as follows:
### 1. Week: November 28 - December 4
* Set-up of the environment (Camille)
* Preprocessing, Merge datasets (Xavi)
### 2. Week: December 5 - December 11
* Exploratory Data Analysis (Agathe)
* Correlation analysis + observational study (Camille)
* Create a predictive model (Xavi)
* Testing the model (Xavi)
### 3. Week: December 12 - December 18
* Visualize our results (Xavi, Agathe, Camille)
* Preparation of final video and the report (Xavi, Agathe, Camille)
### 4. Week: December 19 - December 23
* Finalization of final video (creative director: Xavi, makeup artist: Camille, producer: Agathe, film critic: Bob West + TAs)

As in the previous homework, all team members like to be involved in every task. Thus, we mention the person that will lead the subsections of our analysis, but all of us will contribute to each of them. 

## 8. Questions for TAs
* Are we allowed to deviate a bit from our original plan according to the results we will get during the observational studies? We know that we are a bit ambitious through our methods. However, depending on the results we will get throughout the initial part of the project, we will adapt our plan to make it feasible. 
## 9. Open questions within the team
* Does London organize nutritional prevention campaigns for its inhabitants? (cooking activities, workshops in schools, ...)
* Can we extend the nutrition awareness program to other British cities? 

## 10. TO DO
*[ ] Plot les corrélation pr chaque nutrition variable
*[ ] PCA pr voir si on fait K-mean
*[ ] Clustering pr essayer de voir si on déter des trends
*[ ] Attribuer un nutriscore
*[ ] Split en training et test
*[ ] Régression: prédire nutriscore à partir des well being
	*[ ] Plusieurs méthodes --> choisir celle avec loss function 
	*[ ] sélectionner les variables utiles
*[ ] Tester notre régression