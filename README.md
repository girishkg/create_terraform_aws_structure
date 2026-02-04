# AWS Services Structure
 Generate a full fledged Terraform Directory Structure for AWS infrastructure    
 This script creates an advanced directory structure and essential files for managing AWS infrastructure using Terraform.   
 This script will create a directory named 'terraform-aws-infra' with subdirectories and files.   
 A standard, scalable Terraform project structure for AWS involves separating reusable modules from   
 the environment-specific configurations that call them, often within a monorepo or a multi-repo setup.   
 This approach promotes the DRY (Don't Repeat Yourself) principle, facilitates testing, and allows for   
 independent state management for different environments.   
 This script will take mudules files for common AWS components like VPC, ALB, S3, RDS, IAM, etc.,   
 and create a modular structure under a 'modules' directory. It will also create separate directories according   
 to different environments (e.g., development, staging, production) under an 'environments' directory.   

 ---
 ## This script will create the following structure:
 ```
 terraform-aws-infra/
 ├── main.tf
 ├── variables.tf
 ├── outputs.tf
 ├── provider.tf
 ├── README.md
 ├── modules/
 │   ├── alb/
 │   │   ├── main.tf
 │   │   ├── variables.tf
 │   │   ├── outputs.tf
 │   │   └── README.md
 │   ├── vpc/
 │   │   ├── main.tf
 │   │   ├── variables.tf
 │   │   ├── outputs.tf
 │   │   └── README.md
 │   └── ... (other AWS components like s3, rds, iam, etc.)
 └── environments/
     ├── development/
     │   ├── main.tf
     │   ├── variables.tf
     │   ├── terraform.tfvars
     │   └── versions.tf
     ├── staging/
     │   ├── main.tf
     │   ├── variables.tf
     │   ├── terraform.tfvars
     │   └── versions.tf
     └── production/
         ├── main.tf
         ├── variables.tf
         ├── terraform.tfvars
         └── versions.tf
```
 It includes main.tf, variables.tf, outputs.tf, and provider configuration.