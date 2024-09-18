#  Implementation of Big Data Pipeline for E-commerce Insight Retrieval

# Project Overview
My goal is to choreograph a smooth flow of data, streamlining extraction, transformation, and loading (ETL) processes. Through the periodic submission of Spark jobs, I delve into exploratory data analysis (EDA) and data transformation, unearthing insights and fine-tuning my data for deeper analysis. Come along as I navigate the realms of distributed computing and database management, crafting a resilient and flexible pipeline to handle my data with accuracy and agility.

# Tools Used
- Jet2 Stream
- MongoDB
- Spark
- Ngrok
- Pyspark

# Repository Folders
- data_generator - Contain orignal asofashion data and data generation module to simulate real world interaction with database.
- data_pipeline - Contain data transformation module along with scheduler which executes the module every 37 seconds.
- dashboard - Contain flask api which computes necessary information using spark cluster and plots visualization on GET request.
- report - Contains the project report which contains detailed steps and results about how the project was performed and analysed.
- result screenshots - Includes screenshots showing the results of different stages of the data pipeline.
- data flowcharts - Includes flowcharts showing the data flow in different stages of the data pipeline.
- tested code - Contains code files of different pipeline approaches tested before finalizing current one.

# How to use
Refer to the Project report for a detailed description of the steps . All the files utilised for the project are present in this repository in respective folders.

# Published Results
The results from the analysis are published using Flask API on https://large-bee-oddly.ngrok-free.app/dashboard. Refer to the project report for a detailed explanation of the graphs
