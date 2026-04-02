output "elastic_ip" {
  description = "Elastic IP used by GitHub Actions deployment"
  value       = aws_eip.app_eip.public_ip
}
