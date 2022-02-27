
provider "aws" {
  access_key = var.akey
  secret_key = var.skey
  region = var.region
}



resource "tls_private_key" "dev_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "aws_key_pair" "generated_key" {
  key_name   = var.generated_key_name
  public_key = tls_private_key.dev_key.public_key_openssh

  provisioner "local-exec" {    # Generate "terraform-key-pair.pem" in current directory
    command = <<-EOT
      echo '${tls_private_key.dev_key.private_key_pem}' > ./'${var.generated_key_name}'.pem
      chmod 600 ./'${var.generated_key_name}'.pem
    EOT
  }

}



data "aws_ami" "last_ubuntu"{ # получаем ами 

owners = ["099720109477"]
most_recent = true
filter {
  name = "name"
  values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
}
}

resource "aws_instance" "master_ansible" {
  ami =  data.aws_ami.last_ubuntu.id
  instance_type = var.instance_type
  vpc_security_group_ids = [aws_security_group.sec_ansible.id]
  key_name      = aws_key_pair.generated_key.key_name
  user_data = file( "user.sh")

tags = {
    Name = "Myster Ansible Kuber_Jenk"
    Project = "learn terraform"
  }

}


resource "aws_security_group" "sec_ansible" {

dynamic "ingress"{
    for_each = var.allow_ports
  content {
  from_port = ingress.value
  to_port = ingress.value
  protocol = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}
}

egress {
  from_port = 0
  to_port = 0
  protocol = "-1"
  cidr_blocks = ["0.0.0.0/0"]
}
}
