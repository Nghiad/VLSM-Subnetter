def subneting_mask(number):
    if (number <= 2):
        mask = "/30"
    if (((2**3)-2)  >= number > 2):
        mask = "/29"
    if (((2**4)-2) >= number > ((2**3)-2)):
        mask = "/28"
    if (((2**5)-2) >= number > ((2**4)-2)):
        mask = "/27"
    if (((2**6)-2) >= number > ((2**5)-2)):
        mask = "/26"
    if (((2**7)-2) >= number > ((2**6)-2)):
        mask = "/25"
    if (((2**8)-2) >= number > ((2**7)-2)):
        mask = "/24"
    if (((2**9)-2) >= number > ((2**8)-2)):
        mask = "/23"
    if (((2**10)-2) >= number > ((2**9)-2)):
        mask = "/22"
    if (((2**11)-2) >= number > ((2**10)-2)):
        mask = "/21"
    if (((2**12)-2) >= number > ((2**11)-2)):
        mask = "/20"
    if (((2**13)-2) >= number > ((2**12)-2)):
        mask = "/19"
    if (((2**14)-2) >= number > ((2**13)-2)):
        mask = "/18"
    if (((2**15)-2) >= number > ((2**14)-2)):
        mask = "/17"
    if (((2**16)-2) >= number > ((2**15)-2)):
        mask = "/16"
    if (((2**17)-2) >= number > ((2**16)-2)):
        mask = "/15"
    if (((2**18)-2) >= number > ((2**17)-2)):
        mask = "/14"
    if (((2**19)-2) >= number > ((2**18)-2)):
        mask = "/13"
    if (((2**20)-2) >= number > ((2**19)-2)):
        mask = "/12"
    if (((2**21)-2) >= number > ((2**20)-2)):
        mask = "/11"
    if (((2**22)-2) >= number > ((2**21)-2)):
        mask = "/10"
    if (((2**23)-2) >= number > ((2**22)-2)):
        mask = "/9"
    if (((2**24)-2) >= number > ((2**23)-2)):
        mask = "/8"
    if (((2**25)-2) >= number > ((2**24)-2)):
        mask = "/7"
    if (((2**26)-2) >= number > ((2**25)-2)):
        mask = "/6"
    if (((2**27)-2) >= number > ((2**26)-2)):
        mask = "/5"
    if (((2**28)-2) >= number > ((2**27)-2)):
        mask = "/4"
    if (((2**29)-2) >= number > ((2**28)-2)):
        mask = "/3"
    if (((2**30)-2) >= number > ((2**29)-2)):
        mask = "/2"
    if (((2**31)-2) >= number > ((2**30)-2)):
        mask = "/1"
    if (((2**32)-2) >= number > ((2**31)-2)):
        mask = "/0"
    return mask

def subneting_range(mask):
    if mask == "/30":
        address_range = 2**2
    if mask == "/29":
        address_range = 2**3
    if mask == "/28":
        address_range = 2**4
    if mask == "/27":
        address_range = 2**5
    if mask == "/26":
        address_range = 2**6
    if mask == "/25":
        address_range = 2**7
    if mask == "/24":
        address_range = 2**8
    if mask == "/23":
        address_range = 2**9
    if mask == "/22":
        address_range = 2**10
    if mask == "/21":
        address_range = 2**11
    if mask == "/20":
        address_range = 2**12
    if mask == "/19":
        address_range = 2**13
    if mask == "/18":
        address_range = 2**14
    if mask == "/17":
        address_range = 2**15
    if mask == "/16":
        address_range = 2**16
    if mask == "/15":
        address_range = 2**17
    if mask == "/14":
        address_range = 2**18
    if mask == "/13":
        address_range = 2**19
    if mask == "/12":
        address_range = 2**20
    if mask == "/11":
        address_range = 2**21
    if mask == "/10":
        address_range = 2**22
    if mask == "/9":
        address_range = 2**23
    if mask == "/8":
        address_range = 2**24
    if mask == "/7":
        address_range = 2**25
    if mask == "/6":
        address_range = 2**26
    if mask == "/5":
        address_range = 2**27
    if mask == "/4":
        address_range = 2**28
    if mask == "/3":
        address_range = 2**29
    if mask == "/2":
        address_range = 2**30
    if mask == "/1":
        address_range = 2**31
    if mask == "/0":
        address_range = 2**32
    return address_range

subnethosts = []
subnetmasks = []
subnetrange = []

if __name__ == "__main__":
    print ("Format: 111.222.333.444 /32")
    while True:
        try:
            initialnetwork = input("Network address: ")             #Input IP address /mask and checks for correct format
            token = initialnetwork.split()
            networkaddress, subnetmask = token
            network_range = subneting_range(subnetmask)
            octet1, octet2, octet3, octet4 = map(int, networkaddress.split('.'))
            if octet1 > 255 or octet2 > 255 or octet3 > 255 or octet4 > 255:
                raise ValueError
            numsubnet = int(input("number of subnets: "))           #Input subnet and number of hosts
            for i in range(numsubnet):
                hosts = int(input("number of host for subnet: "))
                subnethosts.append(hosts)
            subnethosts.sort(reverse=True)
            if sum(subnethosts) > network_range:
                raise TypeError
            break                                                   #Proceeds if ip address and subnets are valid
        except ValueError:
            print ("Invalid IP Address")
        except TypeError:
            print ("Not enough available IP addresses for number of host required")

    for i in subnethosts:
        subnetmasks.append(subneting_mask(i))

    for i in subnetmasks:
        subnetrange.append(subneting_range(i))

    for i in range(len(subnetrange)):                               #Subnetting function
        octet4 = octet4 + subnetrange[i]
        while octet4 > 255:
            octet4 = octet4 - 256
            octet3 += 1
            while octet3 > 255:
                octet3 = octet3 - 256
                octet2 += 1
                while octet2 > 255:
                    octet2 = octet2 - 256
                    octet1 += 1
        print ('{}.{}.{}.{} {}'.format(octet1, octet2, octet3, octet4, subnetmasks[i]))
