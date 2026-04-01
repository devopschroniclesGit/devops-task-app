resource "aws_security_group" "devopschronicles-sg" {
  name = "devopschronicles-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
resource "aws_instance" "app_server" {
  ami                    = "ami-0c3389a4fa5bddaad"
  instance_type          = "t3.micro"
  key_name               = "devops-deploy"
  vpc_security_group_ids = [aws_security_group.devopschronicles-sg.id]

  user_data = file("userdata.sh")

  tags = {
    Name = "devopschronicles-app"
  }
}
resource "aws_eip" "app_eip" {
  instance = aws_instance.app_server.id

  tags = {
    Name = "devopschronicles-static-ip"
  }
}
