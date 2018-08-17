# Item-Catalog-Application


## Overview:

This application provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.


## Launching the application:


### 1. Installation:

## Install Python

You can find the link to install Python [here](https://www.python.org/downloads/). This application works using Python 2.7 .

## Install Vagrant and VirtualBox

you'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser.

We're using tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.

  #### Use a terminal
    
  You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a Mac or Linux system,         your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the     Git software. If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/downloads).

  #### Install VirtualBox
  
  VirtualBox is the software that actually runs the virtual machine. You can download it from
  [virtualbox.org, here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your       operating system. You do not   need the extension pack or the SDK. You do not need to launch VirtualBox after installing     it; Vagrant will do that.
  
  **Ubuntu users:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a     reported bug, installing VirtualBox from the site may uninstall other software you need.
  
  #### Install Vagrant
  
  Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.   [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

  **Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure   to allow this.
  
### 2. Clone the fullstack-nanodegree-vm

You can find the link to the fullstack-nanodegree-vm [here](https://github.com/udacity/fullstack-nanodegree-vm).

### 3. Launch the Vagrant VM (vagrant up)

  #### Start the virtual machine
  
  From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the   Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet         connection is.

  When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log   in to your newly installed Linux VM!
  
  #### Logged in!
  
  If you are now looking at a shell prompt that starts with the word vagrant, congratulations — you've gotten logged into       your Linux VM.
  
  #### Logging out and in
  
  If you type `exit` (or `Ctrl-D`) at the shell prompt inside the VM, you will be logged out, and put back into your host         computer's shell. To log back in, make sure you're in the same directory and type `vagrant ssh` again.

  If you reboot your computer, you will need to run `vagrant up` to restart the VM.

### 4. Download project folder

You can download or clone Item Catalog Application from [this repo](https://github.com/DoaaMakhlouf/item_catalog_app)

### 5. Run your application within the VM

From yout terminal, run `python /vagrant/catalog_app/project.py`

### 6. Access your application locally

From your browser, open new window and visit your [local host](http://localhost:8000)
