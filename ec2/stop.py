import boto3 as b3
from datetime import date

def stop():
	console      = b3.session.Session(region_name = 'ap-south-1')
	ec2_access	 = console.client(service_name = 'ec2')

	instance_ids = [''] #add instance ids

	ec2_access.stop_instances(InstanceIds = instance_ids)
	waiter       =  ec2_access.get_waiter('instance_stopped')
	waiter.wait(InstanceIds = instance_ids)
	print("Instances stopped at:", date.today())


stop()
