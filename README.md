# MINE_VS_ROCK_PREDICTION USING MACHINE LEARNING    

## OVERVIEW

This project is about predicting rocks against Mines by the SONAR technology with the help of Machine Learning. SONAR is an abbreviated form of Sound Navigation and Ranging. It uses sound waves to detect objects underwater. Machine learning-based tactics, and deep learning-based approaches have applications in detecting sonar signals and hence targets.The three stages of Machine Learning are taking some data as input, extracting features, and predicting new patterns. The most common ML 
algorithms in this field are Logistic Regression, support vector machine, principal component analysis, k-nearest neighbors (KNN), etc.

## OBJECTIVE  
 
The main aim is to predict the rock or mine in the underwater(sea , oceans) using SONAR that uses sound propagation (usually underwater, as in submarine navigation) to navigate, measure distances (ranging), communicate with or detect objects on or under the surface of the water , which will help the sea divers , submarines to know whether the object is mine or rock . I am using machine learning algorithms to predict these by using the dataset.

## LIBRARIES USED

A Python library is a collection of related modules. It contains bundles of code that can be used repeatedly in different programs. It makes Python Programming simpler and convenient for the programmer. As we don’t need to write the same code again and again for different programs. Python libraries play a very vital role in fields of Machine Learning, Data Science, Data Visualization, etc.Python libraries that are used in the project are:
• Pandas
• Pickle 
• Numpy
• Matplotlib

## MODULES DESCRIPTION 

### Data Acquisition and Data Preprocessing:
• Here the dataset is downloaded from https://www.kaggle.com/datasets/reshmaduseja/rock-vs-mine-predictionmachine-learning
• The dataset has been collected from UCI Repository. It has come across 61 features which define and differentiate Rocks and Mines and comprises of 209 samples. This data is used for training and testing purpose. The Last column in this dataset indicates that, whether it's a mine or a rock, which is useful in prediction.The dataset is included in this repository.
• The dataset is now pre processed to get the summary statistics of the dataset to decide the optimal prediction..

### Feature Extraction:
Feature extraction refers to the process of transforming raw data into numerical features that can be processed while preserving the information in the original data set. It yields better results than applying machine learning directly to the raw data.
Feature extraction can be accomplished manually or automatically:
• Manual feature extraction requires identifying and describing the features that are relevant for a given problem and implementing a way to extract those features. 
• Automated feature extraction uses specialized algorithms or deep networks to extract features automatically from signals or images without the need for human intervention. This technique can be very useful when you want to move quickly from raw data to developing machine learning algorithms. 

### Training and testing of the Model:
 Next we train the machine to recognize mine and rock and pick the appropriate intent and we use the Machine Learning Algorithm like the Logistic regression for the complete training of the model. Every time we make changes to the dataset we need to train the machine to include the changes that have been made.It will train about 60% of the dataset inorder to make the machine well trained for the inputs
• Training — Up to 75 percent of the total dataset is used for training. The model learns on the training set; in other words, the set is used to assign the weights 
and biases that go into the model.
• Validation — Between 15 and 20 percent of the data is used while the model is being trained, for evaluating initial accuracy, seeing how the model learns and fine-tuning hyperparameters. The model sees validation data but does not use it to learn weights and biases.
• Test — Between five and 10 percent of the data is used for final evaluation. Having never seen this dataset, the model is free of any of its bias..

### Implementing User Interface using Streamlit:
 Now we create the actual web application that makes use of all the processed and trained data that we have up till now to take in user queries and give proper responses. Here we use the streamlit python library for the user interface. Here we load the model created and using the saved models from the google colab using pickle library and using various functions to take the user input and predict the responses. Once we run this web application ,it will ask to enter 60 inputs that are nothing but the frequencies that are taken from 60 different angles it will predict whether the object is mine or rock.
 



 
 #  HAPPY LEARNING 




