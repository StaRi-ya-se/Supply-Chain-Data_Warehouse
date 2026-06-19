# Supply Chain Data Warehouse and Analytics Platform

## Project Overview

This project implements an end-to-end Supply Chain Data Warehouse using PostgreSQL and Python ETL pipelines.

The platform models key supply chain entities such as products, suppliers, warehouses, and orders using a dimensional star schema.

## Technologies Used

* Python
* PostgreSQL
* SQLAlchemy
* Pandas
* Faker
* Git & GitHub
* Cursor

## Current Progress

* Database setup completed
* Star schema designed and implemented
* Product dimension populated through ETL pipeline
* Environment variable based configuration implemented

## Planned Features

* Supplier dimension
* Warehouse dimension
* Date dimension
* Fact orders table population
* Analytical SQL queries
* KPI dashboards
* Data quality checks

## Architecture

Python ETL → PostgreSQL Data Warehouse → Analytics Queries → Dashboards


STAR SCHEMA (VERSION 1)

                    Dim_Product
                         |
                         |
                         |
Dim_Supplier ---- Fact_Orders ---- Dim_Warehouse
                         |
                         |
                         |
                      Dim_Date

KPIs to Track
--Revenue KPIs
    Total Revenue
    Revenue by Product
    Revenue by Supplier

--Inventory KPIs
    Quantity Sold
    Top Products

--Warehouse KPIs
    Orders Processed
    Average Delivery Time

--Supplier KPIs
    Supplier Revenue Contribution
    Supplier Order Volume

Supply-Chain-Data-Warehouse/

│
├── data/
│
├── sql/
│   └── schema.sql
│
├── notebooks/
│
├── etl/
│   └── etl.py
│
├── dashboard/
│
└── README.md
