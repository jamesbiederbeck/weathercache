# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "centos" do |centos|
    centos.vm.box = "pascalhegy/centos-7.2-64-puppet-hyperv"
    centos.vm.box_version = "1.0.1"
    centos.trigger.before :destroy do |trigger|
      trigger.warn = "Copying database to /vagrant/temperature_cache.db"
      trigger.run_remote = {inline: "cp /tmp/temperature_cache.db /vagrant/temperature_cache.db"}
    end
  end
  config.vm.network "forwarded_port", guest: 80, host: 80, host_ip: "127.0.0.1"
  config.vm.provision "file", source: "./temperature_cache.db", destination: "/tmp/temperature_cache.db"
  config.vm.provision "puppet"
end
