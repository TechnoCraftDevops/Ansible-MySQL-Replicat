# def test_system_check(host):
#     os = host.system_info.type
#     assert os == 'linux'
#     distro = host.system_info.distribution
#     assert distro == 'ubuntu'
#     userExist = host.user("root").exists
#     assert userExist == False

def test_mysql_service_running(host):
    # mysqlService = host.service('mysql')
    # assert mysqlService.is_enabled
    # assert mysqlService.is_running

    mysqlPackage = host.package('mysql-server')
    assert mysqlPackage.is_installed == True
    assert mysqlPackage.version == '8.0.30-0ubuntu0.20.04.2'

# def test_master_isListned(host):
#     host.socket("tcp://172.18.30.1").is_listening

# def test_mysql_conf(host):
#     assert host.file("/etc/mysql/mysql.conf.d/mysqld.cnf").exists == True
#     assert host.file("/etc/mysql/mysql.conf.d/mysqld.cnf").contains('binlog_do_db = ansible_test_db') == True

#     if host != 'ansible://docker-host1':
#         assert host.file("/etc/mysql/mysql.conf.d/mysqld.cnf").contains('bind-address            = 172.18.30.1') == True
#         assert host.file("/etc/mysql/mysql.conf.d/mysqld.cnf").contains('server-id             = 1') == True

#     if host != 'ansible://docker-host2':
#         assert host.file("/etc/mysql/mysql.conf.d/mysqld.cnf").contains('bind-address            = 172.18.30.2') == True
#         assert host.file("/etc/mysql/mysql.conf.d/mysqld.cnf").contains('server-id             = 2') == True

#     if host != 'ansible://docker-host3':
#         assert host.file("/etc/mysql/mysql.conf.d/mysqld.cnf").contains('bind-address            = 172.18.30.3') == True
#         assert host.file("/etc/mysql/mysql.conf.d/mysqld.cnf").contains('server-id             = 3') == True


# def test_ansible_hosts(host):
#     ansibleHost2 = host.addr("docker-host2")
#     assert ansibleHost2.is_resolvable == True
#     assert ansibleHost2.ipv4_addresses == ['172.18.30.2']



    