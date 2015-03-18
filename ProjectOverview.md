#overview of the whole project

# Introduction #

This project shall provide a backend which saves PDF files supplied by an external source, like a FTP-Server, and saves them in a database to make them searchable. Through a Web Frontend these PDFs can be viewed and searched with different criterias.


## Project Paper ##

The following chart should describe all functions of opal.

(will be inserted later)


# Work Packages #

To make it easier to handle this project different tasks are organized in work packages.
They are arranged like this: Layer.Thread.Work package whereas each point is replaced by a corresponding number specified in the following table:


| **Layer** | **Thread** | **Work Package** | **Arranged Numbers** |
|:----------|:-----------|:-----------------|:---------------------|
| FileSystem | - | FileSystem Storage | 0.0.0 |
| Backend | both | MySQL-Database | 1.0.0 |
| Backend | both | Database API | 1.0.1 |
| Deamon | - | Archive Deamon | 1.0.2 |
| Backend | Listening Thread | Listen for PDF files send via FTP | 1.1.0 |
| Backend | Listening Thread | Put incoming files in queue | 1.1.1 |
| Backend | Listening Thread | Take file from queue and get indicate data | 1.1.2 |
| Backend | Listening Thread | Write indicate data and fs path of file in database | 1.1.3 |
| Backend | Searching Thread | Listen for search requests | 1.2.0 |
| Backend | Searching Thread | Send search request to database | 1.2.1 |
| Backend | Searching Thread | Send request data to web frontend | 1.2.2 |
| Frontend | Web Frontend Thread | Authenticate User | 2.1.0 |
| Frontend | Web Frontend Thread | Search request for all data | 2.1.1 |
| Frontend | Web Frontend Thread | Show request data | 2.1.2 |
| Frontend | Web Frontend Thread | Define search criteria | 2.1.3 |
| Frontend | Web Frontend Thread | Send search request | 2.1.4 |