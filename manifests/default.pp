
Package { ensure => 'installed'}

# install python3
package { 'python3': }

# normally I would use a shell script to run pip install --requirements,
# but this is simpler to install depdendencies given the "no bash" constraint
$pip_packages = ['flask', 'requests']
package { $pip_packages: provider => 'pip3'}

