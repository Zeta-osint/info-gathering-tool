import nmap3

def scanPorts(url, tPorts=20):
    nmap = nmap3.Nmap();
    ports_results = nmap.scan_top_ports(target=url, default=tPorts);
    return ports_results;

def detectOS(url):
    nmap = nmap3.Nmap()
    nmap.require_root(True)
    os_results = nmap.nmap_os_detection(url)
    return os_results
