# Aqua Task Manager - FARM Stack Project

A Full Stack CRUD To-Do Application built using the FARM Stack (FastAPI, React, MongoDB).

## Project Overview

The Aqua Task Manager is a Full Stack CRUD application that simplifies task management. It leverages the FastAPI framework for the backend, React for the frontend, and MongoDB for the database. With this application, users can efficiently create, read, update, and delete tasks in an intuitive user interface.

## Technical Requirements

### Backend (FastAPI)

- Python Installation: Ensure that Python is installed on your system.

### Frontend (React)

- Node.js and npm Installation: Make sure Node.js and npm are installed on your system.

### Database (MongoDB)

- MongoDB Atlas Account: Create a free account on MongoDB Atlas.
- Database Cluster Deployment: Deploy a free DB cluster in a region of your choice and with your preferred cloud service provider.

## MongoDB Server Setup

### Installing MongoDB Community Server

1. Download and install MongoDB Community Server ("mongod") for your platform: [Download Link](https://www.mongodb.com/try/download/community).

### MongoDB Atlas CLI

1. Install the MongoDB Atlas CLI: [Download Link](https://www.mongodb.com/try/download/community).

### MongoDB Developer Tools

1. Download and install MongoDB Shell (CLI): [Download Link](https://www.mongodb.com/developer-tools).
2. Download and install MongoDB Compass (GUI): [Download Link](https://www.mongodb.com/developer-tools).

### Set up the MongoDB Server (For Macbook)

#### If MongoDB Community Server Is Not Yet Installed

1. Create a folder named "mongodb" in your home directory.
2. Place the downloaded MongoDB Community Server in this folder.
3. Add MongoDB to your PATH by editing your shell configuration file (e.g., ~/.zshrc):

   ```shell
   nano ~/.zshrc

Add the following line to the file:

export PATH="$PATH:$HOME/mongodb/mongodb-macos-aarch64-7.0.0/bin"

Save the file and run:

source ~/.zshrc

Add the following line to the file:
export PATH="$PATH:$HOME/mongodb/mongodb-macos-aarch64-7.0.0/bin"

Save the file and run:
source ~/.zshrc

Create a "mongodb-data" folder in your home directory.
Start the MongoDB Server using:
mongod --dbpath ~/mongodb-data

Running the MongoDB Server
Start the MongoDB Server:
mongod --dbpath ~/mongodb-data

Start the Backend and Frontend Servers (refer to your project's documentation).

Interact with the Aqua Task Manager by accessing the provided URLs.