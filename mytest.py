#!/usr/bin/python

def main():

    module = AnsibleModule(
        argument_spec = dict(
            birthday = dict(required=False, default=False, type='bool')
        ),
        supports_check_mode=True
    )
    birth = module.params['birthday']
    if birth:
        module.exit_json(changed=True, msg='It\'s my motherfucking birthday')
    else:
        module.fail_json(msg='Fuck you')

from ansible.module_utils.basic import *
main()