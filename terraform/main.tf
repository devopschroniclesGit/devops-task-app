resource "aws_security_group" "devopschronicles_sg" {
  name        = "devopschronicles-sg"
  description = "Allow SSH and HTTP access for application deployment"

  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP application traffic"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP application traffic"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "devopschronicles-sg"
  }
}

resource "aws_instance" "app_server" {
  ami                    = "ami-0c3389a4fa5bddaad"
  instance_type          = "t3.micro"
  key_name               = "devops-deploy"
  vpc_security_group_ids = [aws_security_group.devopschronicles_sg.id]

  user_data = file("userdata.sh")

  tags = {
    Name = "devopschronicles-app"
  }
}

resource "aws_eip" "app_eip" {
  instance = aws_instance.app_server.id
  domain   = "vpc"

  tags = {
    Name = "devopschronicles-static-ip"
  }
}

