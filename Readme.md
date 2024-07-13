
This program how to solve Three query questions on the news database of 
The first project of the full-stack course of Udacity
which have Three tables articles, authors, and logs.

Before starting you should run a virtual machine and vagrant 

#NOTE: these are the steps of installing and running virtual Machin and Vagrant taken from the Udacity course 
https://classroom.udacity.com/nanodegrees/nd004-connect/parts/4237300b-ed78-4462-a353-a0bd14af33bc/modules/b632715b-7aae-4670-9137-bcd880561475/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0


# First
Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from 
https://www.vagrantup.com/downloads.
html Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
# To make sure you install Vagarent run this command (vagrant --version)
 

# Second
Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternatively, you can use GitHub to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called Vagrant. Change the directory to the vagrant directory:

# Third
Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command (vagrant up). This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
When (vagrant up) is finished running, you will get your shell prompt back. At this point, you can run (vagrant ssh) to log in to your newly installed Linux VM!



# Fourth
The files for this course
Inside the VM, change the directory to /vagrant and look around with ls.

The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

# Fifth
Running the database
The PostgreSQL database server will automatically be started inside the VM. You can use the psql command-line tool to access it and run SQL statements:


# Sixth
Logging out and in
If you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.

If you reboot your computer, you will need to run Vagrant to restart the VM.


# Seventh
Download and Load the Data
	a. For this project, you need to download “newsdata.sql” from the project page or by clicking on the following link: 
		https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

	b. Move the “newsdata.sql” to your project folder “log-analysis-project”
	
	c. Load the data from the “newsdata.sql” by using the following command: Note that we are using PostgreSQL for this project:psql -d news -f newsdata.sql

	d. Once you have the data loaded into your database, connect to your database using: psql -d news

# eighth
Explore the Data
	
	\dt: display tables — lists the tables that are available in the database
	\d table_name: shows the database schema for that particular table

# NOTE:
The “newsdata.sql” has three different tables:
i. Authors: The table includes information about the authors of articles.
ii. Articles: The table includes the articles themselves.
iii.Log: table includes one entry for each time a user has accessed the site.



 The Three questions are:-
 1. What are the most popular three articles of all time? 
	the answer in this format "Princess Shellfish Marries Prince Handsome" — 1201 views
 
 2. Who are the most popular article authors of all time?
	the answer in this format Ursula La Multa — 2304 views

 3. On which days did more than 1% of requests lead to errors?
	the answer in this format July 29, 2016 — 2.5% errors


 The Answers are;
  1- I answered the First question by using next View and you will find psql statement in the ProjectOne.py file.
	a-CREATE VIEW listview AS 
	  SELECT COUNT(*) AS count, SUBSTRING(path, 10) AS newpath 
	  FROM log 
	  GROUP BY newpath 
	  ORDER BY count DESC;

	
 2- I answered the second question by using psql statement you will find it in the ProjectOne.py file.
	

 3- I answered the third question by using the next Views and you will find psql statement in the ProjectOne.py file.

	a-CREATE VIEW errors AS 
	  SELECT DATE(time), COUNT(DATE(time)) AS Total, ROUND((COUNT(DATE(time))*1/100.0),2) AS onePercentage 
	  FROM log 
	  WHERE status = '404 NOT FOUND' 
	  GROUP BY DATE(time) 
	  ORDER BY DATE(time);
	
	b-CREATE VIEW original AS 
	  SELECT date(time), COUNT(date(time)) AS Total, ROUND((COUNT(DATE(time))*1/100.0),2) AS onePercentage 
	  FROM log 
	  GROUP BY DATE(time);

# ProjectOne.py file
in the ProjectOne.py file, I used the psycopg2 module to connect to the database and, I used the database_conniction function that receives a string as a query then I used 
three statements to call the database_conniction function. receive query then print the result.

# How to run the code?
you can run the code by using this command
(python ProjectOne.py)
