import argparse
import sys
from configparser import ConfigParser

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="n stands for number of instances")
    parser.add_argument('-c', help="n stands for number of crawler")
    parser.add_argument('-d', help="d stands for number of database")
    parser.add_argument('-f', help="d stands for number of frontend")
    parser.add_argument('-b', help="b stands for number of backend")
    args = parser.parse_args()
    if not (args.n or args.c or args.d or args.b):
        print("missing input")
        sys.exit()
    num_n = int(args.n)
    num_c = int(args.c)
    num_d = int(args.d)
    num_f = int(args.f)
    num_b = int(args.b)

    config = ConfigParser(allow_no_value=True)
    config.read("_inventory.ini")
    values = config['COMP90024']
    ipv4s = []
    servers = ["crawler", "backend", "frontend", "database"]
    slave_node_num = 2
    slave_nodes = []
    for i in values:
        ipv4s.append(i)
    for i in range(num_n):
        add_section = True
        while num_c > 0:
            if add_section:
                config.add_section("crawler")
                add_section = False
            config.set("crawler", "crawler", ipv4s[(num_c-1) % num_n])
            num_c -= 1
    for i in range(num_n):
        add_section = True
        while num_d > 0:
            if add_section:
                config.add_section("backend")
                add_section = False
            config.set("backend", "backend", ipv4s[(num_d) % num_n])
            num_d -= 1
    for i in range(num_n):
        add_section = True
        while num_f > 0:
            if add_section:
                config.add_section("frontend")
                add_section = False
            config.set("frontend", "frontend", ipv4s[(num_f+1) % num_n])
            num_f -= 1
    for i in range(num_b):
        add_section = True
        while num_b > 0:
            if add_section:
                config.add_section("database")
                add_section = False
            config.set("database", "database", ipv4s[(num_b+2) % num_n])
            num_b -= 1
    for i in range(slave_node_num):
        slave_nodes.append(ipv4s[i])
    config.set("database", "slave_nodes", str(slave_nodes))

    config.write(open("_inventory.ini", "w"))
