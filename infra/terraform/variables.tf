variable "aws_region" {
  description = "AWS region to deploy the infrastructure"
  type = string
  default = "sa-east-1"
}

variable "project_name" {
  description = "Project name prefix for AWS resources"
  type = string
  default = "metrics-api"
}

variable "allowed_ssh_cidr" {
  description = "CIDR allowed to SSH into the EC2 instance"
  type        = string
  default     = "0.0.0.0/0"
}

variable "key_name" {
  description = "Existing AWS EC2 key pair name for SSH access"
  type        = string
}