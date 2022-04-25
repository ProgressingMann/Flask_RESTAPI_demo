# Instructions on how to deplot our flask application on AWS-elastic-beanstalk using the eb CLI

<ol>
  <li> We will first need to install the aws-elastic-bean (eb) CLI, if it is not already installed. Instructions on how to install eb CLI are provided 
    <a href="https://github.com/aws/aws-elastic-beanstalk-cli-setup">here</a>.
  <li> After installing the eb-CLI, clone this repository to the local machine, and let's say this directory is named as aws_demo. 
  <li> Open the terminal and go to the directory where this repository is cloned, aws_demo.
  <li> <strong>NOTE:</strong> We may need to change the folder structure where we would move all the files
        from the app folder to the aws_demo folder and then get rid of the app folder.
  <li> Create a .ebignore file to tell the aws-eb which files not to include.
  <li> We will now make changes to the python files. AWS looks for the keyword <strong>application</strong> to find our flask application instance from our python 
       files. So to adjust with this behavior, we will <strong>change the name of our flask application instance from app to application in our python files.</strong> 
  <li> In addition to this, we will have to set <strong>DEBUG=FALSE</strong>, as this application will be deployed on production.
  <li> Now we move back to our terminal with directory aws_demo. 
  <li> We now initialize our aws_demo repository with the command <strong>eb init -p python-3.7 flask-tutorial --region us-east-2 </strong>.
  <li> Create an environment and deploy our application with the command <strong>eb create flask-env</strong>.
</ol>
