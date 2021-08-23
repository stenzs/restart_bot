from jumpssh import SSHSession
gateway_session = SSHSession('gateway.example.com', 'my_user', password='my_password').open()
remote_session = gateway_session.get_remote_session('remote.example.com', password='my_password2')