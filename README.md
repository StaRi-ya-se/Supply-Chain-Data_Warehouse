# Supply-Chain-Data_Warehouse

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
