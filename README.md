# Email-Spam-Detection

In today's digital age, the proliferation of unwanted and often malicious spam messages via email and SMS poses a significant challenge. This project addresses this issue by developing a robust spam detection system and deploying it as a user-friendly web application.

Leveraging a publicly available dataset from Kaggle, this project implements a comprehensive workflow to accurately classify incoming messages as either spam or legitimate ("ham"). The process begins with meticulous data cleaning and insightful Exploratory Data Analysis (EDA) to understand the characteristics of the data and identify key patterns.

Following this, feature engineering techniques are applied to extract meaningful information from the text data, transforming it into a format suitable for machine learning models. Text preprocessing steps, such as tokenization, stemming/lemmatization, and handling stop words, further refine the data to enhance model performance.

The core of the project involves model training and testing using various machine learning algorithms like GuassianNB, MultinomialNB and BernoulliNB in which BernoulliNB is the model with 98% of accuracy and 100% of precision. The performance of these models is rigorously evaluated to identify the most effective solution for spam detection. Finally, the trained model is seamlessly deployed in the form of a web application, allowing users to easily input text and instantly determine if it is likely to be spam.

This project showcases a practical application of data science and machine learning techniques to solve a real-world problem. By providing an accessible web interface, it empowers users to proactively identify and manage unwanted messages, ultimately improving their digital communication experience.
