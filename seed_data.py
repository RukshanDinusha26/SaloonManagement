from salonManagement import app, db, User, Employee, Service, Appointment, bcrypt
from datetime import datetime, time, date

def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Appointment).delete()
        db.session.query(Employee).delete()
        db.session.query(Service).delete()
        db.session.query(User).delete()
        db.session.commit()

        print("Cleared existing data.")

        # Create Admin
        hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
        admin = User(
            username='admin',
            email='admin@salon.lk',
            password=hashed_password,
            firstname='Kamal',
            lastname='Perera',
            age=35,
            gender='Male',
            address='123, Galle Road, Colombo 03',
            created_at=datetime.utcnow()
        )
        db.session.add(admin)

        # Create Employee User
        emp_user = User(
            username='sunil_stylist',
            email='sunil@salon.lk',
            password=hashed_password,
            firstname='Sunil',
            lastname='Silva',
            age=28,
            gender='Male',
            address='45, Temple Road, Kalutara',
            created_at=datetime.utcnow()
        )
        db.session.add(emp_user)
        db.session.commit() # Commit to get ID

        # Create Employee Record
        employee = Employee(id=emp_user.id) # Use user ID as employee ID or link them
        db.session.add(employee)
        
        # Link user to employee
        emp_user.employee_id = employee.id
        db.session.commit()

        # Create Customer
        customer = User(
            username='nimali_client',
            email='nimali@client.lk',
            password=hashed_password,
            firstname='Nimali',
            lastname='Fernando',
            age=25,
            gender='Female',
            address='89, Flower Road, Colombo 07',
            created_at=datetime.utcnow()
        )
        db.session.add(customer)

        # Create Services (Prices in LKR)
        services = [
            Service(service_name='Haircut (Men/Women)', price=2500.0, service_image='home-1.avif'),
            Service(service_name='Bridal Dressing', price=45000.0, service_image='home-2.avif'),
            Service(service_name='Hair Coloring', price=8500.0, service_image='home-3.webp'),
            Service(service_name='Manicure & Pedicure', price=3500.0, service_image='service1.jpg')
        ]
        db.session.add_all(services)
        db.session.commit()

        # Assign Service to Employee
        employee.services.append(services[0]) # Sunil does Haircuts
        employee.services.append(services[2]) # Sunil does Hair Coloring
        db.session.commit()

        # Create Appointment
        appointment = Appointment(
            token_number='TKN-LK-001',
            username=customer.username,
            employee_id=employee.id,
            service_id=services[0].service_id,
            date=date.today(),
            time=time(10, 0), # 10:00 AM
            payment_status='Paid',
            status='Confirmed'
        )
        db.session.add(appointment)
        db.session.commit()

        print("Sri Lankan dummy data added successfully!")

if __name__ == '__main__':
    seed_data()