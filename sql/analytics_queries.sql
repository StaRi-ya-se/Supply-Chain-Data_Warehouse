-- EXECUTIVE KPI QUERIES (Total Revenue, Orders & Average Order Value)

SELECT
    COUNT(*) AS total_orders,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_order_value
FROM Fact_Orders;

-- REVENUE DRIVERS (Top 10 Revenue Generating Products)

SELECT
    p.product_name,
    p.category,
    ROUND(SUM(f.revenue), 2) AS total_revenue
FROM Fact_Orders f
JOIN Dim_Product p
    ON f.product_id = p.product_id
GROUP BY p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 10;

-- CATEGORY CONTRIBUTIONN ANALYSIS (Which categories contribute most to company revenue? TOP5)

SELECT
    p.category,
    ROUND(SUM(f.revenue), 2) AS total_revenue,
    ROUND(
        100.0 * SUM(f.revenue)
        / SUM(SUM(f.revenue)) OVER (),
        2
    ) AS revenue_percentage
FROM Fact_Orders f
JOIN Dim_Product p
    ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- SUPPLY CHAIN INSIGHTS (Supplier Performance Ranking TOP 10)

SELECT
    s.supplier_name,
    ROUND(SUM(f.revenue), 2) AS total_revenue,
    COUNT(*) AS total_orders
FROM Fact_Orders f
JOIN Dim_Supplier s
    ON f.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY total_revenue DESC
LIMIT 10;

-- WAREHOUSE THROUGHPUT ANALYSIS (Which warehouses handle the highest volume?)

SELECT
    w.warehouse_name,
    w.city,
    COUNT(*) AS total_orders,
    ROUND(SUM(f.revenue), 2) AS total_revenue
FROM Fact_Orders f
JOIN Dim_Warehouse w
    ON f.warehouse_id = w.warehouse_id
GROUP BY
    w.warehouse_name,
    w.city
ORDER BY total_orders DESC;

-- TIME-SERIES ANALYSIS (Monthly Revenue Trends)

SELECT
    d.month,
    ROUND(SUM(f.revenue), 2) AS total_revenue
FROM Fact_Orders f
JOIN Dim_Date d
    ON f.date_id = d.date_id
GROUP BY d.month
ORDER BY d.month;

-- Revenue by Warehouse and Product Category

SELECT
    w.city,
    p.category,
    ROUND(SUM(f.revenue), 2) AS total_revenue
FROM Fact_Orders f
JOIN Dim_Warehouse w
    ON f.warehouse_id = w.warehouse_id
JOIN Dim_Product p
    ON f.product_id = p.product_id
GROUP BY
    w.city,
    p.category
ORDER BY total_revenue DESC;

-- Top Product Within Each Category

WITH ProductRevenue AS (
    SELECT
        p.category,
        p.product_name,
        SUM(f.revenue) AS total_revenue,
        RANK() OVER (
            PARTITION BY p.category
            ORDER BY SUM(f.revenue) DESC
        ) AS rank_num
    FROM Fact_Orders f
    JOIN Dim_Product p
        ON f.product_id = p.product_id
    GROUP BY
        p.category,
        p.product_name
)

SELECT *
FROM ProductRevenue
WHERE rank_num = 1;