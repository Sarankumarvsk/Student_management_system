CREATE DATABASE student_management;
USE student_management;
CREATE TABLE studentdetails (
    S_id INT PRIMARY KEY,
    S_name VARCHAR(100) NOT NULL,
    Dept VARCHAR(50),
    Type VARCHAR(50)
);
CREATE TABLE details (
    S_id INT,
    Name VARCHAR(100),
    DOB VARCHAR(15),
    Mail_id VARCHAR(100),
    Phone_No VARCHAR(15),
    Locality VARCHAR(100),
    City VARCHAR(50),
    Pincode INT,
    PRIMARY KEY (S_id),
    FOREIGN KEY (S_id) REFERENCES studentdetails(S_id)
);
CREATE TABLE attendance (
    S_id INT,details
    S_name VARCHAR(100),
    Date VARCHAR(15),
    Status CHAR(1),
    FOREIGN KEY (S_id) REFERENCES studentdetails(S_id)
);

select *from studentdetails;