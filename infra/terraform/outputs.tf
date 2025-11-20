output "ec2_public_ip" {
  description = "Public IP of the k3s EC2 node"
  value = aws_instance.k3s_node.public_ip
}

output "ec2_public_dns" {
  description = "Public DNS of the k3s EC2 node"
  value = aws_instance.k3s_node.public_dns
}