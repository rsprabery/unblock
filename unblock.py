import argparse
import os
import subprocess

def CMD(cmd) :
  p = subprocess.Popen(cmd, shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    close_fds=False)
  return (p.stdin, p.stdout, p.stderr)


denyhost_files = ['/etc/hosts.deny', 'hosts', 'hosts-restricted', 'hosts-root', 'hosts-valid', 'users-hosts']


def remove_line(text, path):
    temp_file_path = path + ".temp"
    read_file = file(path, 'r')
    write_file = file(temp_file_path, 'w+')

    for line in read_file.readlines():
        if text not in line:
            write_file.write(line)

    read_file.close()
    write_file.close()
    os.remove(path)
    os.rename(temp_file_path, path)


def check_sudo():
    flag = False
    if os.getenv('USER') == 'root':
        flag = True
    return flag


def unblock(ip_address):
    os.chdir('/var/lib/denyhosts/')

    for deny_file in denyhost_files:
        remove_line(ip_address, deny_file)
    CMD("iptables -D INPUT -s %s -j DROP" %(ip_address))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Remove an IP address from DenyHost, allowing access to the machine from that IP again")
    parser.add_argument("ip_address", help="The IP address to be removed from denyhost files", type=str)
    args = parser.parse_args()

    if not check_sudo() and args.host_addr is None:
        print "If you want to run this locally, please run with `sudo`"
    CMD("sudo service denyhosts stop")
    unblock(args.ip_address)
    CMD("sudo service denyhosts start")
