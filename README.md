# Deploying Docker on AWS using Jenkins


## Setup 


This guide uses Ubuntu 18.04 LTS for the entire setup.


### Install Jenkins


`` # apt-get install jenkins ``

This will install jenkins and start the service at port 8080 by default.

Open [http://localhost:8080] on browser to complete initial setup. Jenkins asks one-time admin password

`` # cat /var/lib/jenkins/secrets/initialAdminPassword``

Copy the output of the above file to the browser and submit. 

Jenkins require a one time password for admin setup. It generates a random string in file `/var/lib/jenkins/secrets/initialAdminPassword` to authorize user for admin role. Jenkins deletes this file after successful authorization.

Next, Jenkins generate a form to create user. It will redirect to Dashboard once user is created.

Before we go ahead and create a New Item on the dashboard, Jenkins requires one configuration in order to execute `docker` commands inside the pipleine

`` # usermod -a -G docker jenkins ``


### Install and configure AWS CLI

`` # pip install awscli ``

After installing awscli, we need to configure credentials in jenkins user.

``
# su - jenkins 
# aws configure 
``

The above command will ask for Access Key, Secret Key and the region. The access keys can be created using [https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/]

 
### Create pipline in Jenkins


On dashboard, click on **New Item** that is present on the left of the screen. It opens a new page with input form. Enter a name for New Item eg. 'my-project-pipeline'. Select **Pipeline** as new option and click on **OK** to create.

Jenkins will now take you to configurations page. Make following configurations

1. (Description)Add description
1. Check option **GitHub project**. It will then show an input field **Project url** enter [https://github.com/ngala/jenkin-hook.git/]
1. Check option **GitHub hook trigger for GITScm polling**
1. Check option **Poll SCM** which will show and textarea. Add `* * * * *` in the field.
1. Under **Pipeline > Definition** choose `Pipeline script from SCM`. This will open a few fields.
    1. Add a **Repository URL** `https://github.com/ngala/jenkin-hook.git/` and change the **Branch Specifier** to `*/main`
1. Finally click on **Save**

