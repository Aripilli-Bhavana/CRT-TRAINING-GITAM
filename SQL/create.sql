
-- create
CREATE TABLE EMPLOYEE (
  empId int,
  emp_name varchar(15),
  emp_age int,
  emp_sal float,
  emp_place varchar(20)
);

INSERT INTO EMPLOYEE(empId,emp_name,emp_age,emp_sal,emp_place) VALUES (1, 'Bhavana',21,5000, 'Vizag');
INSERT INTO EMPLOYEE(empId,emp_name,emp_age,emp_sal,emp_place) VALUES (2, 'Fathima',21,5000, 'Hyd');
INSERT INTO EMPLOYEE(empId,emp_name,emp_age,emp_sal,emp_place) VALUES (3, 'Priya',20,5000, 'Blr');
INSERT INTO EMPLOYEE(empId,emp_name,emp_age,emp_sal,emp_place) VALUES (1, 'Homa',22,5000, 'Chennai');

SELECT * FROM EMPLOYEE;
select emp_name from EMPLOYEE;
