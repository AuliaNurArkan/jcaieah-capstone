-- DATABASE AND TABLE CREATION
CREATE DATABASE IF NOT EXISTS moduleone;
USE moduleone;

CREATE TABLE IF NOT EXISTS car_rental (
    rental_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    car_type VARCHAR(50) NOT NULL,
    rental_duration INT NOT NULL,
    rental_cost DECIMAL(10,2) NOT NULL,
    customer_gender VARCHAR(10) NOT NULL,
    rental_date DATE NOT NULL,
    branch_city VARCHAR(50) NOT NULL
);

INSERT INTO car_rental (car_type, rental_duration, rental_cost, customer_gender, rental_date, branch_city)
VALUES
('SUV',3,300,'Male','2024-01-01','Jakarta'),
('Sedan',2,200,'Female','2024-01-02','Jakarta'),
('SUV',5,450,'Female','2024-01-03','Bandung'),
('Hatchback',1,100,'Male','2024-01-04','Bandung'),
('Sedan',4,350,'Female','2024-01-05','Surabaya'),
('SUV',7,600,'Male','2024-01-06','Surabaya'),
('Sedan',3,280,'Female','2024-01-07','Medan'),
('Hatchback',2,150,'Male','2024-01-08','Medan'),
('SUV',6,500,'Female','2024-01-09','Jakarta'),
('Sedan',5,400,'Male','2024-01-10','Bandung');