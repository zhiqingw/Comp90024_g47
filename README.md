# Comp90024_g47

Leqi Wang, 1126066,  Shanghai China
leqi.wang1@student.unimelb.edu.au

Oliver Cheng, 912834, Melbourne Australia 
o.cheng1@student.unimelb.edu.au

Xuxu Xue, 956895, Guangzhou China
xuxux@student.unimelb.edu.au

Zhiqing Wu, 931919, Guangzhou China
zhiqingw@student.unimelb.edu.au



The following commands are executed under the ./Comp90024_g47/mrc directory.

There is an automated operation and maintenance tool Ansible which we used to achieve our goals below. It collects the advantages of many operation and maintenance tools (puppet, chef, func, fabric) and realizes the functions of the batch system such as configuration, batch program deployment, and batch running commands.

#2.1 Deploy instances
To run our program in Melbourne Research Cloud, resource allocation to each virtual machine and installation of the development environment are necessary. In particular, the creation and maintenance of cloud infrastructures such as cloud instances, volumes, and security groups are required.

Firstly, we install the required dependencies on our host which are required by the Ansible playbook. Then for each virtual machine, We use NeCTAR Ubuntu 18.04 LTS (Bionic) amd64 (with Docker) as their operating system image. Volumes need to be assigned and attached to each instance, hence 60 GigaByte space was set to each instance in our project to store data. After that, we set up the security group for each instance. This operation is designed to allow multiple instances to communicate with each other and to block any potentially malicious access. For example, to allow HTTP requests between instances, we open the HTTP default port(80) for each instance. Finally, we used the openstack.cloud.server module for creating instances. In the meanwhile, once the instances are created, their corresponding IP address will be written in ./mrc/inventory/_inventory.ini file so we can assign different tasks to each host later. At this stage, every instance has been set up properly and is ready to take command.


#2.2 Deploy CouchDB database using Ansible
1. Install required dependencies to be able to run our couchdb on a remote instance.
For example, python modules like “couchdb”, and “curl” are needed. 
2. Create docker containers for each couchdb node so they can run as if they were running on different hosts.
3. Set up the couchdb cluster by using the <curl -X POST> command
4. Enable the CORS policy so we can access our database in different domains.
5. Finish couchdb setup

#2.3 Deploy crawler server using Ansible
1. Install required dependencies to be able to run our couchdb on a remote instance.
For example, python modules like “tweepy”, and “request” are needed.
2. Copy the crawler dictionary to the crawler server.
3. Compile the python program by using the nohup command so it will run continuously even though the connection of ssh is lost.
4. Now the program can read tweets by using Twitter API and save useful tweets to our database.

#2.4 Deploy backend server using Ansible
1. Install required dependencies to be able to run our couchdb on a remote instance.
For example, python modules like “pandas”, and “geopy” are needed.
2. Copy the data_processing dictionary to the backend server.
3. Start the data processing program by using the nohup command so it will keep running in the background. 
4. Now the program would read tweets and analyze the location and sentiments from the existing database.

#2.5 Deploy front-end server using Ansible
1. Copy the frontend dictionary to the frontend server.
2. Terminate the remote front end server if it is already running. 
3. Remove all existing node_modules using <rm -rf node_modules> command
4. Reinstall all the necessary node modules using <npm install> command
5. Start the front-end server by using the <forever start> command so it won’t be terminated after the ssh connection is closed.
6. Now our front-end server has been deployed and can present our analysis results on (http://172.26.130.158:3000)


#2.6 How to run
```
/bin/bash ./Comp90024_g47/mrc/run-nectar.sh
```


#Note:

To use an OpenStack cloud, authentication against the Identity service named keystone is required, which needs a token and service catalog. These two can be found on the MRC website.

To enable the creation of the file and save the file on your local device, the Ansible playbook would require a password for your device.
