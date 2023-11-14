# Run ansible CLI

## ping all hosts
ansible all -m ping

## play one playbook for one hosts/host-groupe
ansible-playbook [playbook_file].yml --limit [host-name/host-groupe]

## check one playbook for one hosts
ansible-playbook [playbook_file].yml --check --limit [host-name/host-groupe]

## run one playbook for all hosts
ansible-playbook [playbook_file].yml

## run one playbook for one hosts
ansible-playbook docker_install.yml --check --limit [host-name/host-groupe]  

# Install testinfra
## require
-- pip install pytest-testinfra

-- ansible [core 2.12.7]

-- Python 3.10.4

-- pytest-7.1.2

-- pip install paramiko (to connect ssh without pwd)
-- pip install mysql-connector-python (query test)
# Run ansible tests
## run specific test
py.test --hosts=docker_hosts --connection=ansible --ansible-inventory=test_inventories/ --force-ansible tests/[file].py
## run all tests
py.test --hosts=docker_hosts --connection=ansible --ansible-inventory=test_inventories/ --force-ansible tests/*