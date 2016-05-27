require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'lynis Ansible role' do

    # Installation dir should be owned by root
    describe file('/var/lib/lynis') do
        it { should exist }
        it { should be_directory }
        it { should be_owned_by 'root' }
        it { should be_grouped_into 'root' }
    end

    # Reports directory should exists and owned by root
    describe file('/var/log/lynis-reports') do
        it { should exist }
        it { should be_directory }
        it { should be_owned_by 'root' }
        it { should be_grouped_into 'root' }
    end

    # Crontab file should be defined and executed by root
    describe file('/etc/cron.d/lynis') do
        it { should exist }
        it { should be_file }
        it { should be_owned_by 'root' }
        it { should be_grouped_into 'root' }
        its(:content) { should match /\*\s+root/ }
    end
end
