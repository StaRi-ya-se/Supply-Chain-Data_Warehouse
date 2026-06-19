CREATE TABLE Dim_Product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
);

CREATE TABLE Dim_Supplier (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE Dim_Warehouse (
    warehouse_id SERIAL PRIMARY KEY,
    warehouse_name VARCHAR(100),
    city VARCHAR(50),
    capacity INT
);

CREATE TABLE Dim_Date (
    date_id INT PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT,
    day_name VARCHAR(20),
    month_name VARCHAR(20)
);

CREATE TABLE Fact_Orders (
    order_id BIGSERIAL PRIMARY KEY,

    product_id INT REFERENCES Dim_Product(product_id),
    supplier_id INT REFERENCES Dim_Supplier(supplier_id),
    warehouse_id INT REFERENCES Dim_Warehouse(warehouse_id),
    date_id INT REFERENCES Dim_Date(date_id),

    quantity INT,
    revenue DECIMAL(12,2),
    shipping_cost DECIMAL(10,2)
);