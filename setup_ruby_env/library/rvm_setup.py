#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            version=dict(type='str', required=True),
            state=dict(type='str', choices=['present', 'absent'], default='present')
        )
    )

    version = module.params['version']
    state = module.params['state']

    # Check if RVM is already installed
    rc, out, err = module.run_command('rvm --version', check_rc=False)
    installed = rc == 0

    if state == 'present' and not installed:
        # Install RVM
        rc, out, err = module.run_command('curl -sSL https://get.rvm.io | bash -s stable')
        if rc != 0:
            module.fail_json(msg=f"Failed to install RVM: {err}", rc=rc)

        # Load RVM into current shell session
        rc, out, err = module.run_command('source ~/.rvm/scripts/rvm')
        if rc != 0:
            module.fail_json(msg=f"Failed to load RVM: {err}", rc=rc)

    elif state == 'absent' and installed:
        # Uninstall RVM
        rc, out, err = module.run_command('rvm implode --force')
        if rc != 0:
            module.fail_json(msg=f"Failed to uninstall RVM: {err}", rc=rc)

    module.exit_json(changed=(state == 'present'))

if __name__ == '__main__':
    main()

