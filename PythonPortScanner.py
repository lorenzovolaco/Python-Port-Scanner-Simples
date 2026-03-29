import nmap  #instale nmap usando pip install python-nmap.

nm = nmap.PortScanner() #instancia da classe .PortScanner()

target = "45.33.32.156"         #Ip address do nmap
options = "-sV -sC scan_results"  #como vou usar o nmap

nm.scan(target, arguments=options)  #metodo do scan

for host in nm.all_hosts():  #loop que mostra as informaçoes
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():  #nm[host] loop
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():   #utiliza o .items()
            print("Port: %s\tState: %s" % (port, state))



