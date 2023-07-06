# Project: setup_ruby_env

This project provides Ansible playbooks to set up a Ruby environment using RVM and Podman for running Ruby on Rails applications. It consists of two Ansible playbooks: `install_ruby` and `podman_rails`.

## Prerequisites

Before running the playbooks, ensure that you have the following prerequisites:

1. Ansible is installed on the local machine.
2. The target machine is running Fedora Server 38 or other RPM based distros.
3. You have appropriate permissions to execute the playbooks and install packages.

## Playbook 1: install_ruby

The `install_ruby` playbook installs Ruby using RVM on the local machine.

### Usage

1. Save the playbook to a file named `install_ruby.yml`.

2. Open a terminal and navigate to the directory containing the playbook.

3. Run the following command to execute the playbook:

   ```shell
   ansible-playbook install_ruby.yml
   ```

### Playbook Details

The playbook performs the following tasks:

1. Installs RVM and sets up the environment for Ruby installation.
2. Installs the dependencies required for Ruby using the DNF package manager.
3. Installs the specified Ruby version using RVM.
4. Optionally, adds alternative beta Ruby versions if specified in the `rvm_rubies` variable.

### Customization

You can customize the `ruby_version` variable to specify a specific Ruby version. Additionally, you can modify the list of dependencies in the `package` task to include any additional packages required by your project.

## Playbook 2: podman_rails

The `podman_rails` playbook builds a Podman container running Ruby on Rails on the local machine.

### Usage

1. Save the playbook to a file named `podman_rails.yml`.

2. Open a terminal and navigate to the directory containing the playbook.

3. Run the following command to execute the playbook:

   ```shell
   ansible-playbook podman_rails.yml
   ```

### Playbook Details

The playbook performs the following tasks:

1. Installs the required packages, including Podman, Ruby, SQLite, GCC, and other dependencies using the DNF package manager.
2. Builds a Docker container image for Ruby on Rails using Podman.
3. Creates and starts a container from the image, mapping port 3000 on the host to port 3000 in the container.
4. Installs the Rails gem with the specified version.
5. Creates a new Rails application in the `/app` directory.
6. Sets the ownership and permissions for the Rails application directory.
7. Changes the current working directory to the Rails application.
8. Installs the Rails dependencies using `bundle install`.
9. Creates the database for the Rails application.
10. Starts the local Rails server.

### Customization

You can customize the playbook by modifying the package names in the `dnf` task to include any additional required packages. Additionally, you can change the Rails version by modifying the `gem install rails` command.

## Conclusion

With the `install_ruby` and `podman_rails` playbooks from the `setup_ruby_env` project, you can easily set up a Ruby environment with RVM and run Ruby on Rails applications in a Podman container. Customize the playbooks and documentation according to your specific project requirements and enjoy developing Ruby applications with ease.

For further assistance, please refer to the official Ansible documentation and reach out if you have any questions or need support.

Happy coding!

---
