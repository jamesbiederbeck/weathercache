
Package { ensure => 'installed'}

# install python3
package { 'python3': }

# normally I would use a shell script to run pip install --requirements,
# but this is simpler to install depdendencies given the "no bash" constraint
$pip_packages = ['flask', 'requests']
package { $pip_packages: provider => 'pip3'}

exec { 'Start Flask app':
  command => '/usr/local/bin/flask run --host=0.0.0.0 &',
  cwd => '/vagrant',
  environment => ['PYTHON_PATH=/vagrant', 'FLASK_APP=weathercache'],
  timeout => 0
}

exec { 'Open firewall on port 80':
  command => '/usr/bin/firewall-cmd --permanent --zone=public --add-port=80/tcp',
  timeout => 5
}
