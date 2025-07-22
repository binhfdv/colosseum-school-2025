def generate_config(filename="users.conf"):
    with open(filename, "w") as f:
        for x in range(256):
            section = f"[001010000000{x:03}]"  # x as 3-digit int
            fullname = f"user{x}"
            config_block = (
                f"{section}\n"
                f"fullname = {fullname}\n"
                f"hassip = yes\n"
                f"context = users\n"
                f"host = dynamic\n"
                f"transport = udp\n\n"
            )
            f.write(config_block)

if __name__ == "__main__":
    generate_config()