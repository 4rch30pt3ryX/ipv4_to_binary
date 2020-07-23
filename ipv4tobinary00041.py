#!usr/bin/python
"""
                        *******************************
                        *   Created by 4rch30pt3ryX   *
                        *******************************

IPv4 to binary converter.

Notes:
pyhon3.6
"""
import ipaddress as ip
import sys
    
class Ipv4:  

    def getip(self):
        
        while True:
            try:                
                iptoconvert = input(
                    '\n\nType "quit" to exit or provide an IPv4 address to be converted to its Binary address: '
                    )
                ipadd = ip.IPv4Address(iptoconvert)
                getoctet = str(ipadd)
                self.getoctets = getoctet.split('.')
                return self.getoctets
                           
            except ValueError:
                
                usrquit = 'quit'                
                if iptoconvert != usrquit:
                    print('\n\nNot a valid IPv4 address.\n')
                    continue
                    
                elif iptoconvert == usrquit:
                    print('\n\nYou have chosen to quit. Exiting program.\n')
                    sys.exit(0)
                     
        return (self.getoctets)

    def iptobinary(self):    
        
        sotrue = 1
        sofalse = 0
        binarylist = []
        octets = self.getoctets
        
        for ipoctet in octets:
        
            if int(ipoctet) > 128:
            
                binarylist.append(sotrue)
                ipoctet = int(ipoctet) - 128
                        
            else:

                binarylist.append(sofalse)
                ipoctet = int(ipoctet) - 0
            
            if ipoctet > 64:

                binarylist.append(sotrue)
                ipoctet -= 64
            
            else:

                binarylist.append(sofalse)
                ipoctet -= 0
            
            if ipoctet > 32:
            
                binarylist.append(sotrue)
                ipoctet -= 32
            
            else:

                binarylist.append(sofalse)
                ipoctet -= 0
            
            if ipoctet > 16:
            
                binarylist.append(sotrue)
                ipoctet -= 16
            
            else:
            
                binarylist.append(sofalse)
                ipoctet -= 0
            
            if ipoctet > 8:
            
                binarylist.append(sotrue)
                ipoctet -= 8
            
            else:
            
                binarylist.append(sofalse)
                ipoctet -= 0
            
            if ipoctet > 4:
            
                binarylist.append(sotrue)
                ipoctet -= 4
            
            else:
            
                binarylist.append(sofalse)
                ipoctet -= 0
            
            if ipoctet > 2:
            
                binarylist.append(sotrue)
                ipoctet -= 2
            
            else:
            
                binarylist.append(sofalse)
                ipoctet -= 0
            
            if ipoctet == 1:
            
                binarylist.append(sotrue)
                ipoctet -= 1
            
            else:
            
                binarylist.append(sofalse)
                ipoctet -= 0
            
            binstr = ''.join(str(item) for item in binarylist)

        ipvfour = '.'.join(str(x) for x in octets)
        print('\n\n\n\nBinary address for ' + ipvfour + ':\n\n' + binstr + '\n')        

ipv4 = Ipv4()
ipv4.getip()
ipv4.iptobinary()
