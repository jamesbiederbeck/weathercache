# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "centos" do |centos|
    #   config.vm.box = "genebean/centos-7-puppet-latest"
    centos.vm.box = "pascalhegy/centos-7.2-64-puppet-hyperv"
    centos.vm.box_version = "1.0.1"
    # If you'd like to use a different box and provider than this one, which supports only hyper-v,
    # consider uncommenting the following line for easier access
    # centos.vm.network "forwarded_port", guest: 80, host: 80, host_ip: "127.0.0.1"
    #
    # You can uncomment this line if you'd like to access the service with port 
    # forwarding over ssh
    # config.ssh.forward_agent = "True"
    centos.vm.provision "file", source: "./temperature_cache.db", destination: "/tmp/temperature_cache.db"
    centos.vm.provision "puppet"
    centos.trigger.before :destroy do |trigger|
      trigger.warn = "Copying database to /vagrant/temperature_cache.db"
      trigger.run_remote = {inline: "cp /tmp/temperature_cache.db /vagrant/temperature_cache.db"}
    end
  end
end
