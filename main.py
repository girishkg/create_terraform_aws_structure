# Generate a full fledged Terraform Directory Structure for AWS infrastructure
# This script creates an advanced directory structure and essential files for managing AWS infrastructure using Terraform.
# This script will create a directory named 'terraform-aws-infra' with subdirectories and files.
# A standard, scalable Terraform project structure for AWS involves separating reusable modules from
# the environment-specific configurations that call them, often within a monorepo or a multi-repo setup.
# This approach promotes the DRY (Don't Repeat Yourself) principle, facilitates testing, and allows for
# independent state management for different environments.
# This script will take mudules files for common AWS components like VPC, ALB, S3, RDS, IAM, etc.,
# and create a modular structure under a 'modules' directory. It will also create separate directories according
# to different environments (e.g., development, staging, production) under an 'environments' directory.
# This script will create the following structure:
# terraform-aws-infra/
# ├── main.tf
# ├── variables.tf
# ├── outputs.tf
# ├── provider.tf
# ├── README.md
# ├── modules/
# │   ├── alb/
# │   │   ├── main.tf
# │   │   ├── variables.tf
# │   │   ├── outputs.tf
# │   │   └── README.md
# │   ├── vpc/
# │   │   ├── main.tf
# │   │   ├── variables.tf
# │   │   ├── outputs.tf
# │   │   └── README.md
# │   └── ... (other AWS components like s3, rds, iam, etc.)
# └── environments/
#     ├── development/
#     │   ├── main.tf
#     │   ├── variables.tf
#     │   ├── terraform.tfvars
#     │   └── versions.tf
#     ├── staging/
#     │   ├── main.tf
#     │   ├── variables.tf
#     │   ├── terraform.tfvars
#     │   └── versions.tf
#     └── production/
#         ├── main.tf
#         ├── variables.tf
#         ├── terraform.tfvars
#         └── versions.tf

# It includes main.tf, variables.tf, outputs.tf, and provider configuration.
############################
# (1) Function to call the aws_get_services_list.py to get all AWS services list
import os
from lib.aws_get_services_list import get_all_aws_service_names
all_services = get_all_aws_service_names()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"Total number of services available in Boto3: {len(all_services)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# End of function to call the aws_get_services_list.py to get all AWS services list
############################
# (2) Function to create the Terraform directory structure using the AWS services list
# Create the Terraform directory structure and files
# Populate all the necessary files with basic content for git initialization
# Add README.md files with basic descriptions in each directory

# Accepts the base directory name as input


def create_terraform_structure(base_dir):
    # Define the main directories and subdirectories
    directories = {
        base_dir: [
            "modules",
            "environments"
        ],
        os.path.join(base_dir, "modules"): all_services,
        os.path.join(base_dir, "environments"): [
            "development",
            "staging",
            "production"
        ]
    }

    # Create the base directory
    # Prompt for confirmation before deleting existing directory
    if os.path.exists(base_dir):
        print(
            f"Directory {base_dir} already exists. Please remove it or choose a different name.")
        print("This is to make sure that we are not overwriting any existing data.")
        print("Exiting Now...")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return
    os.makedirs(base_dir, exist_ok=True)

    # Create main files in the base directory
    main_files = ["main.tf", "variables.tf",
                  "outputs.tf", "provider.tf", "README.md"]
    for file in main_files:
        with open(os.path.join(base_dir, file), "w") as f:
            f.write(f"# {file} for Terraform AWS Infrastructure\n")

    # Create modules and their files
    for service in all_services:
        module_path = os.path.join(base_dir, "modules", service)
        os.makedirs(module_path, exist_ok=True)
        module_files = ["main.tf", "variables.tf", "outputs.tf", "README.md"]
        for file in module_files:
            with open(os.path.join(module_path, file), "w") as f:
                f.write(f"# {file} for {service} module\n")

    # Create environment directories and their files
    for env in ["development", "staging", "production"]:
        env_path = os.path.join(base_dir, "environments", env)
        os.makedirs(env_path, exist_ok=True)
        env_files = ["main.tf", "variables.tf",
                     "terraform.tfvars", "versions.tf"]
        for file in env_files:
            with open(os.path.join(env_path, file), "w") as f:
                f.write(f"# {file} for {env} environment\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Terraform directory structure created at: {base_dir}")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# End of function to create the Terraform directory structure using the AWS services list
# This script generates a full-fledged Terraform directory structure for AWS infrastructure.
# It creates modular directories for each AWS service and environment-specific configurations.
##############################################################################################
###### Main Execution ######
# Prompt for the targtet directory name input from the user
if __name__ == "__main__":
    target_dir = input(
        "Enter the target directory name for Terraform AWS infrastructure (default: /c/study/terraform/terraform-aws-infra): \n").strip()
    if not target_dir:
        target_dir = "C:/D-Drive/STUDY/Terraform/terraform-aws-infra"
    create_terraform_structure(base_dir=target_dir)
