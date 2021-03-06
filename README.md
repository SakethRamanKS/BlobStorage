# BlobStorage

Saketh Raman KS

Cloudwiry Hackathon 2022

## Solution

The solution uses a FastAPI backend along with a CLI Frontend and PostgreSQL for the database.

Streaming is supported during both upload and download to enable transfer of large files.

The server compresses files using gzip compression before writing them to disk.

The solution is deployed on a Microsoft Azure Virtual Machine.

## Features
* Supported operations:
  * Upload
  * Download
  * Rename
  * Update
  * Share
  * Revoke
  * Delete
* Support for streaming uploads and downloads
* Easy to use CLI client
* Compression using gzip
* User based access control using three permission levels - Owner, Editor, and Viewer

## Demo
Click [here](https://drive.google.com/file/d/1tbDWKl9hdr7QoaxwOYT8NB_GX9F4qFXB/view?usp=sharing) for a demo of the application.

## Setup Instructions

### Server

**Note**: An instance of the server is deployed at the IP address 20.127.120.66 on port 4567

#### Requirements
* Python 3.8 
* virtualenv
* A server running PostgreSQL

1. Clone the repository to a local machine
2. Install Python 3.8 if not installed already
3. Navigate to the folder `Server`
4. Create a virtual environment using *virtualenv* with Python 3.8
5. Activate the virtual environment
6. Install dependencies using ``pip install -r requirements.txt``
7. Run ``alembic upgrade head`` to create the necessary tables in the database
8. Create a file ``.env`` with the necessary configuration information. A sample ``.env.example`` is provided in the repository
9. Start the server with ``python main.py``
10. Done!

### Client


#### Requirements
* Python 3.8 
* virtualenv
* A BlobStorage server 

1. Clone the repository to a local machine
2. Install Python 3.8 if not installed already
3. Navigate to the folder `Client`
4. Create a virtual environment using *virtualenv* with Python 3.8
5. Activate the virtual environment
6. Install dependencies using ``pip install -r requirements.txt``
7. Create a file ``.env`` with the necessary configuration information. A sample ``.env.example`` is provided in the repository
8. Start the server with ``python main.py``
9. Done! The client can be terminated by pressing ``Ctrl + D``

*Note*: Occasional connection resets occur while using the deployed server. In such cases restart the client and re-run the command.

## Database Design

![Database Diagram](/readme-assets/ER_BlobStorage.png)

## Access Control Rules

| Operation     |     Owner      | Editor  |  Viewer  |
|---------------|:--------------:|:-------:|:--------:|
| Download     |       ???        |    ???    |    ???     |
| Rename    |       ???        |   ???      |    ???     |
| Update |       ???        |     ???    |      ???    |
|    Share    |       ???        |   ???      |     ???     |
|    Revoke    |       ???        |    ???     |      ???    |
|      Delete        |       ???        |   ???      |    ???      |


## Author
* Saketh Raman KS