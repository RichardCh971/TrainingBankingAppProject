provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "fastapi_sg" {
  name = "fastapi-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
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

resource "aws_key_pair" "banking_key" {
  key_name   = "banking-api-key"
  public_key = file("ssh-keys/banking-api-key.pub")
}

resource "aws_instance" "fastapi_server" {
  ami           = "ami-020cba7c55df1f615"
  instance_type = "t2.micro"
  key_name = aws_key_pair.banking_key.key_name
  
  vpc_security_group_ids = [aws_security_group.fastapi_sg.id]

  tags = {
    Name = "fastapi-banking-server-richard-chong"
  }
}

output "instance_public_ip" {
  value = aws_instance.fastapi_server.public_ip
}

output "ssh_command" {
  value = "ssh -i ssh-keys/banking-api-key ubuntu@${aws_instance.fastapi_server.public_ip}"
}