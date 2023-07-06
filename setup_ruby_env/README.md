## Ansible Playbook: install_ruby

This playbook installs Ruby using RVM (Ruby Version Manager) on the local machine.

### Usage

1. Open a terminal and Clone this repo

2.  avigate to the directory containing the playbook we jus cloned.

3. Run the following command to execute the playbook:

   ```shell
   ansible-playbook install_ruby.yml
   ```

### Playbook Details

The playbook performs the following tasks:

1. Installs RVM and sets up the environment for Ruby installation.

2. Installs the dependencies required for Ruby, such as build-essential, libssl-dev, libreadline-dev, and zlib1g-dev.

3. Installs the specified Ruby version using RVM.

4. Optionally, adds alternative beta Ruby versions if specified in the `rvm_rubies` variable.

### Customization

You can customize this playbook by modifying the `ruby_version` variable to specify a specific Ruby version. Additionally, you can add or remove dependencies based on your requirements.

---

## Ansible Playbook: podman_rails

This playbook builds a Podman container running Ruby on Rails on the local machine.

### Usage

1.  Open a terminal and clone this playbook repo.

2. navigate to the directory containing the playbook.

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

You can customize this playbook by modifying the package names in the `dnf` task to include any additional required packages. Additionally, you can change the Rails version by modifying the `gem install rails` command.
