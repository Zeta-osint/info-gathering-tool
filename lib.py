import nmap3
import masscan
import webtech
import socket

# url: https://example.com
def nmap_scanPorts(url, tPorts=20):
    url = url.split("://")[1] # Split https:// part
    nmap = nmap3.Nmap();
    ports_results = nmap.scan_top_ports(target=url, default=tPorts);
    return ports_results;

def nmap_detectOS(url):
    url = url.split("://")[1]
    nmap = nmap3.Nmap()
    nmap.require_root(True)
    os_results = nmap.nmap_os_detection(url)
    return os_results

def nmap_scanPortsService(url):
    url = url.split("://")[1]
    nmap = nmap3.Nmap()
    os_results = nmap.nmap_version_detection(url)
    return os_results

def urlToIp(url):
    url = url.split("://")[1]
    ip = socket.gethostbyname(url)
    return ip

# ip: 127.0.0.1
# ports: 0-65535
# or
# ports: 22,80,443
def masscan_scanPorts(ip, ports="80,443,22,8080"):
    mas = masscan.PortScanner()
    mas.scan(ip+"/24", ports=ports, sudo=True)
    return mas.scan_result

def scanWebTech(url):
    wt = webtech.WebTech(options={"json": True})
    try:
        result = wt.start_from_url(url)
        return result
    except webtech.utils.ConnectionException:
        print("Connection error")
