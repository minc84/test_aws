variable "region" {
  description = "Please enter region AWS"
  type = string
  default = "eu-north-1"
}

variable "akey" {
  description = " AWS access_key"
  type = string
  default = ""
}

variable "skey" {
  description = "AWS secret_key"
  type = string
  default = ""
}

variable "instance_type" {
  description = "Please enter instance_type AWS"
  type = string
  default = "t3.micro"
}

variable "allow_ports" {
  description = "Please enter list allow_ports"
  type = list # map bool
  default = ["80","443","8080","22"]
}

variable "generated_key_name" {
  type        = string
  default     = "terraform-key-ans-master"
  description = "Key-pair generated by Terraform"
}
