# Model_Deployment_Python
This Repository is a reference for model deployment in python. 
### Model deployment is usually the last step in the construction of a machine learning model. You've already solved the problem or completed the assignment, but your solution is a python script in a jupyter notebook or a Google colab notebook, which you have locally on your device in the best case scenario. When you post the code to a github repository, you're making your work available to folks who are familiar with ML/DS and Python. Those that may be interested in or relate to your work will not be able to comprehend it.  Let's say you have developed machine learning classifier that can classify the iris flower types and you want to present your work but instead of the code you'd like to create a web app that uses your model to classify iris types. The web app is clear and simple you can target those who are intrested in the solution and would actually use it. Instead of explaining the advanced python code, they will test the final predictions immediately. I can't believe that I am justifying to you why you should deploy your model ? dude just do it!

I'll assume you have no extensive experience designing web/mobile apps in this circumstance, therefore I'll point you resources and options that fit the situation: <br>
**I have other assumptions but I won't share them cause they might hurt your feeling (*lonely*) .** <br> 
You have the following options: </br>
-  Create a simple web app and use python tools like Flask to integrate your code.
-  Create a Rest API using python packages and use in your simple mobile app. 
-  Other option that need extensive experience : 
    - Convert your code to java and use it in android app .
    - Use app development packages such as kivy .
    - Integrate your code in android app using Tensorflow. <br>
 Before I address the options there are some steps you should take and they are highly recommended so please check them first :
 1. Maintain the folder structure: Before considering deployment you should make sure that you have an organized folder structure this will help you in delivering your work and maintaining the parts if needed. It's boring work but it will save you time later. 
 2. Prepare the code: Most algorithms run randomly or take random steps:
    -  It is best to organize the work environment from the beginning and define constant variables, hyper-parameters.
    -   Write useful and clear comments. 
    -   Create your own split function if necessary
  3.  Save you best model: There are many options for this step. 
  4.  Decide the final product type . 
  5.  Dont forget features engineering steps if you applied any on the training dataset. 
  6.  Interpret the results in the chosen way : you can interpet your results in the iris images instead of classes for example. 
 ### Resources:
  - Step 1 : 
    - https://neptune.ai/blog/how-to-organize-deep-learning-projects-best-practices
  - Step 2 : 
    - https://medium.com/@ODSC/properly-setting-the-random-seed-in-ml-experiments-not-as-simple-as-you-might-imagine-219969c84752
    - https://github.com/yuxiangdai/machine-learning-templates
    - https://github.com/philipperemy/keras-tcn/issues/66
  - Step 3 : 
    - https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
    - https://www.geeksforgeeks.org/saving-a-machine-learning-model/

 Some options are easier than the others so I'm gonna start by addressing them from the easiest to the hardest in my opinion:  
 ### - Build a REST API : 
  
  
