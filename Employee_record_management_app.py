class Employee:
    def __init__(self, emp_id, name, department, manager_id=None):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.manager_id = manager_id

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, department, manager_id=None):
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
            return
        self.employees[emp_id] = Employee(emp_id, name, department, manager_id)
        print(f"Employee {name} added successfully.")

    def update_employee(self, emp_id, name=None, department=None, manager_id=None):
        if emp_id not in self.employees:
            print(f"Employee with ID {emp_id} does not exist.")
            return
        employee = self.employees[emp_id]
        if name:
            employee.name = name
        if department:
            employee.department = department
        if manager_id:
            if self.detect_circular_reference(emp_id, manager_id):
                print("Error: Circular reference detected. Manager not updated.")
                return
            employee.manager_id = manager_id
        print(f"Employee {emp_id} updated successfully.")

    def delete_employee(self, emp_id):
        if emp_id not in self.employees:
            print(f"Employee with ID {emp_id} does not exist.")
            return
        del self.employees[emp_id]
        print(f"Employee {emp_id} deleted successfully.")

    def search_employee(self, **criteria):
        results = []
        for emp in self.employees.values():
            match = True
            for key, value in criteria.items():
                if getattr(emp, key, None) != value:
                    match = False
                    break
            if match:
                results.append(emp)
        return results

    def display_hierarchy(self, emp_id, level=0):
        if emp_id not in self.employees:
            print(f"Employee with ID {emp_id} does not exist.")
            return
        employee = self.employees[emp_id]
        print("    " * level + f"{employee.name} (ID: {employee.emp_id}, Dept: {employee.department})")
        for e in self.employees.values():
            if e.manager_id == emp_id:
                self.display_hierarchy(e.emp_id, level + 1)

    def detect_circular_reference(self, emp_id, manager_id):
        current_id = manager_id
        while current_id:
            if current_id == emp_id:
                return True
            current_id = self.employees.get(current_id, None).manager_id if current_id in self.employees else None
        return False

    def run(self):
        while True:
            command = input("Enter command (add, update, delete, search, display, exit): ").strip().lower()
            if command == "add":
                emp_id = input("Enter employee ID: ").strip()
                name = input("Enter employee name: ").strip()
                department = input("Enter employee department: ").strip()
                manager_id = input("Enter manager ID (optional): ").strip() or None
                self.add_employee(emp_id, name, department, manager_id)
            elif command == "update":
                emp_id = input("Enter employee ID: ").strip()
                name = input("Enter new name (leave blank to skip): ").strip() or None
                department = input("Enter new department (leave blank to skip): ").strip() or None
                manager_id = input("Enter new manager ID (leave blank to skip): ").strip() or None
                self.update_employee(emp_id, name, department, manager_id)
            elif command == "delete":
                emp_id = input("Enter employee ID: ").strip()
                self.delete_employee(emp_id)
            elif command == "search":
                criteria = {}
                name = input("Search by name (leave blank to skip): ").strip()
                if name:
                    criteria["name"] = name
                department = input("Search by department (leave blank to skip): ").strip()
                if department:
                    criteria["department"] = department
                results = self.search_employee(**criteria)
                for emp in results:
                    print(f"ID: {emp.emp_id}, Name: {emp.name}, Dept: {emp.department}, Manager ID: {emp.manager_id}")
            elif command == "display":
                emp_id = input("Enter employee ID to display hierarchy: ").strip()
                self.display_hierarchy(emp_id)
            elif command == "exit":
                break
            else:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.run()
