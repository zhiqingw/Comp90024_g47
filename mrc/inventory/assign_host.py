from configparser import ConfigParser

if __name__ == "__main__":

    config = ConfigParser(allow_no_value=True)
    config.read("_inventory.ini")
    values = config['COMP90024']
    ipv4s = []
    servers = ["crawler", "backend", "frontend", "database"]
    slave_node_num = 2
    slave_nodes = []
    for i in values:
        ipv4s.append(i)
    for i in range(len(ipv4s)):
        config.add_section(servers[i])
        config.set(servers[i],servers[i],ipv4s[i])
    for i in range(slave_node_num):
        slave_nodes.append(ipv4s[i])
    config.set("database", "slave_nodes", str(slave_nodes))

    config.write(open("_inventory.ini", "w"))
