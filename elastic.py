import boto3

region_list = ["us-east-1", "us-east-2"]

for region in region_list:
    ec2 = boto3.client("ec2", region_name=region)
    ip = ec2.describe_addresses()
    # print("elastic ip of the instance :",ip)
    # elastic_ip = ip["Addresses"][0]["AllocationId"]
    EL_ip = []
    for e_ip in ip["Addresses"]:
        elastic_ip = e_ip["AllocationId"]
        print("elastic ip in the", region, "is :", elastic_ip)
        EL_ip.append(elastic_ip)

    for eip in EL_ip:
        ec2.release_address(AllocationId=eip)
        print("succusfully release all elastic ip from all", region)

else:
    print("elastic ip not found")

