import boto3 as b3
from datetime import date

def start():
	console      = b3.session.Session(region_name = 'ap-south-1')
	ec2_access	 = console.client(service_name = 'ec2')

	instance_ids = ['']

	ec2_access.start_instances(InstanceIds = instance_ids)
	waiter       =  ec2_access.get_waiter('instance_running')
	waiter.wait(InstanceIds = instance_ids)
	print("Instances started on:", date.today())


start()
