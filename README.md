# UNBLOCK (for denyhost)
Tool to unblock an IP address if it has been blocked by the denyhost daemon
### Usage:
        git clone  https://github.com/rsprabery/unblock.git
        cd unblock
        sudo python unblock.py IP_ADDRESS
where `IP_ADDRESS` is the IP address that is currently blocked by denyhost.

Usage is currently limited to the local machine only (which will be the use case for singly owned servers).  So if you've locked yourself out of your VPS you'll have to get access via a web-shell or similar and then run this program.

## FILES MODIFIED
#### In denyhosts folder (limited to /var/lib/denyhost at the moment)
1. hosts
2. hosts-restricted
3. hosts-root
4. hosts-valid
5. users-hosts

#### Other system files modified
1. /etc/hosts.deny

#####Thanks to:
http://www.cyberciti.biz/faq/linux-unix-delete-remove-ip-address-that-denyhosts-blocked/
for providing information on how to remove an IP from being blocked; this utility is based on that blog post.