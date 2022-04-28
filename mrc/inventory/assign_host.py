from configparser import ConfigParser

if __name__ == "__main__":

    config = ConfigParser(allow_no_value=True)
    config.read("_inventory.ini")
    values = config['COMP90024']
    ipv4s = []
    servers = ["crawler", "backend", "frontend", "database"]
    for i in values:
        ipv4s.append(i)
    for i in range(len(ipv4s)):
        config.add_section(servers[i])
        config.set(servers[i], ipv4s[i])
    config.write(open("_inventory.ini", "w"))
