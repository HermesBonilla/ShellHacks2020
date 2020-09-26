# ShellHacks2020 Neural Network Workshop

Welcome to our Neural Network Workshop at [ShellHacks 2020](https://shellhacks.net/)!

## Contents
  #### DeRes Script
    - To run the script to create a deresolution face dataset (Not used in this workshop, but useful anyhow!)
  
  #### Django Image Classifier
    - The Django folder contains all the files needed for our netlify site implmentation
    - Model used: Convolutional Neural Network (CNN)
    
    ##### Steps to start the Django Server in localhost:8000
      1. Open up Anaconda3 command prompt or regular command prompt
      2. change directory to where django folder is located
      ```cd [file location]```
      
      3. Create virtual environment:
      **conda**
      NOTE: environment name does not matter
      ```conda create --name [environment name]```
      
      4. Activate your virtual environment by:
      **conda**
      ```conda activate [environment name]```
      
      5. Install dependencies from requirements.txt file:
      ```pip install -r requirements.txt```
                      or
      ```pip3 install -r requirements.txt```
      
      6. Change your directory into the django project folder:
      
      ```cd django_image_classifier```
      
      7. Activate the server in localhost:8000:
      ```python manage.py runserver```
      
      8. Go to the browser and access local host:
      In url bar, search "localhost:8000" or any similar local hosts.
      

## Resources

- [Workshop Slides](https://docs.google.com/presentation/d/1a0WRuEHIr7HNCJbs-l3ocstHtAtfSL8GbBNvRIgH0lU/edit#slide=id.g96c15fa444_1_3)
- Youtube Video [TBA]
- [Become a DSC FIU Member!](https://go.fiu.edu/dscapplication)

