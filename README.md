# FARM Stack Project (Aqua Task Manager)

A CRUD To-Do Application built using the FARM Stack (FastAPI, React, MongoDB).

## Project Overview

This project is a Full Stack CRUD application that manages tasks using the FastAPI framework for the backend, React for the frontend, and MongoDB for the database. The Aqua Task Manager allows users to create, read, update, and delete tasks in a user-friendly interface.

## Technical Requirements for Each Framework

### FastAPI
- [x] Install Python

### React
- [x] Install Node.js
- [x] Install npm

### MongoDB
- [x] Create a Free Account on MongoDB Atlas
- [x] Deploy a Free DB Cluster in a Region Near You and Cloud Service Provider of your choice

## MongoDB Server Setup

### Download/Install the MongoDB Community Server
- [x] Download and install the MongoDB Community Server ("mongod") based on your platform: [Download Link](https://www.mongodb.com/try/download/community)

### Get MongoDB Atlas CLI on your Terminal
- [x] Install MongoDB Atlas CLI: [Download Link](https://www.mongodb.com/try/download/community)

### Download/Install MongoDB Developer Tools
- [x] MongoDB Shell (CLI): [Download Link](https://www.mongodb.com/developer-tools)
- [x] MongoDB Compass (GUI): [Download Link](https://www.mongodb.com/developer-tools)

### Set up the MongoDB Server in the Terminal (For Macbook)

1. If You Have Not Yet Created/Downloaded the MongoDB Community Server and Created a Separate MongoDB Server File Path
    1. Create a Folder (in the place of your choosing) in Your Home Directory "mongodb" and put in it the MongoDB Community Server.
    2. Add to PATH in your shell Configuration file (such as ~/.zshrc for the Zsh shell):
        1. Open terminal: `nano ~/.zshrc` to open the file.
        2. Add `export PATH="$PATH:$HOME/mongodb/mongodb-macos-aarch64-7.0.0/bin"` to ~/.zshrc file.
        3. Run `source ~/.zshrc` to activate changes in the file.
    3. Create a "mongodb-data" folder (in the place of your choosing) in your home directory.
    4. Start the MongoDB Server with: `mongod --dbpath ~/mongodb-data`.

2. Run the MongoDB Server and Shell
    - Start the Server: `mongod --dbpath ~/mongodb-data`.
    - Start the Shell: `mongosh`.

Note: If you're using a different operating system, make sure to download and install the appropriate MongoDB Community Server version for your system. Adjust the PATH and setup instructions accordingly.

## Running the MongoDB Server on your machine

1. Start the MongoDB Server: `mongod --dbpath ~/mongodb-data`
2. Start the Backend and Frontend Servers (refer to your project's documentation)
3. Interact with the Aqua Task Manager by accessing the provided URLs.

