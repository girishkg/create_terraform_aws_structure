import os
import boto3


def get_all_aws_service_names():
    # Create a session to access available services
    session = boto3.session.Session()

    # Use the get_available_services method to list all service names
    service_names = session.get_available_services()

    # Sorting the list for easier reading (optional)
    service_names.sort()

    return service_names


if __name__ == "__main__":
    all_services = get_all_aws_service_names()
    print(f"Total number of services available in Boto3: {len(all_services)}")
    print("List of service names:")
    # Save the service names to a text file inside tmp directory
    # Create the tmp directory in current working directory if it doesn't exist

    tmp_dir = "tmp"
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    # Remove existing file if it exists
    file_to_remove = os.path.join(tmp_dir, "aws_services_list.txt")

    # Write the service names to a file
    file_path = os.path.join(tmp_dir, "aws_services_list.txt")
    with open(file_path, "w") as f:
        for service in all_services:
            f.write(f"{service}\n")
    print(f"Service names saved to: {file_path}")
# This script retrieves and prints all available AWS service names using Boto3.
