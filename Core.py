print(r"""
  _   _           _     ____                     _ 
 | \ | | ___  ___| |_  | __ ) _ __ __ ___      _| |
 |  \| |/ _ \/ __| __| |  _ \| '__/ _` \ \ /\ / / |
 | |\  | (_) \__ \ |_  | |_) | | | (_| |\ V  V /| |
 |_| \_|\___/|___/\__| |____/|_|  \__,_| \_/\_/ |_|
                                                   
    """)
print("[Server] Starting...\n")

from Networking.ServerThread import Server

server = Server('0.0.0.0', 9339)
server.start()