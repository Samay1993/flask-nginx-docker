from app import app

@app.route('/')
def index():
  return "Hello from Flask in Master Branch"
  return "This is a production environment."
  return "Deployed in Amazon EC2 Instance"
  return "This is Jenkins Slave Node Fetching changes from Master branch of git Repository, then Building and Deploying the application"