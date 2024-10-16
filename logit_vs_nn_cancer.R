library(readxl)
#Set working directory
setwd('c:/Users/Nelson.Chung/Downloads/')

#Read in data
cancer <- read.csv('lung_cancer.csv')

#Create a Dummy for whether individual has cancer
cancer$cancer <- ifelse(is.na(cancer$days_to_cancer),0,1)

#Change categoricals to factor
cancer$gender<-as.factor(cancer$gender)
cancer$race<-as.factor(cancer$race)
cancer$smoker<-as.factor(cancer$smoker)

#Run and summarize logistic regression
logit<-glm(cancer ~ age + gender + race + factor(smoker), family = binomial(link = 'logit'), data = cancer)
summary(logit)

#Calculate Predicted Values
cancer$log_predict <- round(plogis(predict(logit,cancer)))
#Calculate True Positives
cancer$log_correct <- ifelse(cancer$cancer - cancer$log_predict == 0,1,0)
#Calculate % Correctly Predicted
print(sum(cancer$log_correct)/nrow(cancer))

#Use neural networks
library(neuralnet) 

f <- as.formula(cancer ~ .)

#Create categoricals \
cancer_encoded <- model.matrix(cancer ~ age + gender + race + smoker, data = cancer)
cancer_encoded <- data.frame(cancer <- cancer$cancer,cancer_encoded)

#Fit and summarize neural network
nn <- neuralnet(f, data = cancer_encoded,hidden = c(5,3),linear.output = F)
summary(nn)

#Calculate Predicted Values
cancer_encoded$nn_predict <- round(predict(nn,cancer_encoded))
#Calculate True Postiives
cancer_encoded$nn_correct <- ifelse(cancer_encoded$nn_predict - cancer_encoded$cancer == 0,1,0)
#Calculate % correctly predicted
print(sum(cancer_encoded$nn_correct)/nrow(cancer_encoded))

