# segmentation
data_set <- read.csv("mydata.csv",TRUE,",")
cluster <- data_set$cluster(ifelse(data_set$Tap.Life %in% c(1,2,3,9,14),1, 
                                   ifelse(data_set$Tap.Life %in% c(4,6,7,10,11),2),
                                   ifelse(data_set$Tap.Life %in% c(5,8,12,13),3,4)))

write.csv(data_set, "D:/1_pppppthon/abuan6390/newdata.csv")

# load data
data_seg <- read.csv("newdata.csv",TRUE,",")

# see the coefficient correlation
temp <- data_seg[c(6,7,14,20,24,26)]
library(corrplot)
a <- cor(temp,method="kendall")
corrplot(data=a,model="circle",type="upper",order="hclust")

# split data to training and testing data
set.seed(12345)  # for repeatability of samples
temp_data<- sample(0.7*nrow(segment1))  
segment1_training <- segment1[temp_data, ] 

# Create Test Data
segment1_testing <- segment1[-temp_data, ]
library(caret) 
library(e1071) 
mod_fit <- train(zdw ~ Curryeartotal.Transamount+Curryeartotal.Transcount+
                   Fundraising.Goal+ Medhinc.Cy+
                   Prevyeartotal.Transamount+Prevyeartotal.Transcount+
                   Registration.Gift, 
                 data=segment1_training, method = "glm", family="binomial")

# choose important variables
varImp(mod_fit)

# regression modeling
segment1_model <- glm(zdw ~ Prevyeartotal.Transcount+Curryeartotal.Transcount+Medhinc.Cy+
                        Curryeartotal.Transamount+Prevyeartotal.Transamount,
                      data=segment1_training, family="binomial" )

segment1_predicted <- plogis(predict(segment1_model,segment1_testing))# predict score

# ROC curve
plotROC(segment1_testing$zdw, segment1_predicted)

# misclassification error
misClassError(segment1_testing$zdw, segment1_predicted)

# confusion matrix
confusionMatrix(round(segment1_predicted),segment1_testing$zdw)

# create financial modeling dataset
export<-cbind(segment1_testing, segment1_predicted)
names(export)
write.csv(export, 'segment1.csv')

export<-cbind(segment2_testing, segment2_predicted)
write.csv(export, 'segment2.csv')

export<-cbind(segment3_testing, segment3_predicted)
write.csv(export, 'segment3.csv')