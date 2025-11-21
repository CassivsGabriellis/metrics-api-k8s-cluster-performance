output "ec2_public_ip" {
  description = "Elastic IP of the k3s EC2 node"
  value       = aws_eip.k3s_eip.public_ip
}