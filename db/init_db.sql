CREATE DATABASE ai_business CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE ai_business;
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    position VARCHAR(50),
    hire_date DATE,
    is_active BOOLEAN DEFAULT TRUE
);
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    status ENUM('present', 'absent', 'late'),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);
CREATE TABLE sales_reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);
