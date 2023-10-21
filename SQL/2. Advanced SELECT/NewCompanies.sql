SELECT 
    Company.company_code , 
    founder,
    
    (SELECT COUNT(DISTINCT lead_manager_code)
    FROM Lead_Manager
    WHERE Company.company_code = Lead_Manager.company_code),
    
    (SELECT COUNT(DISTINCT senior_manager_code)
    FROM Senior_Manager
    WHERE Company.company_code = Senior_Manager.company_code),
    
    (SELECT COUNT(DISTINCT manager_code)
    FROM Manager
    WHERE Company.company_code = Manager.company_code),
    
    (SELECT COUNT(DISTINCT employee_code)
    FROM Employee
    WHERE Company.company_code = Employee.company_code)
from Company
order by company_code