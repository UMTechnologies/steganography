import cv2


def color_bd_generator():
    d, c = {}, {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)
    return d, c


if __name__ == '__main__':
    print("Welcome to Steganography encrypt / decrypt service. Please select what do you want: ")

    while True:
        print("------------------------------------------------------------")
        print("Type 1: To encrypt by default - bmw.jpg")
        print("Type 2: To encrypt your file - specify your path to the image")
        print("------------------------------------------------------------")
        print(">>>>>>>>>>>>>>>>> To quit press control + C <<<<<<<<<<<<<<<<")
        print("------------------------------------------------------------")
        cmd = int(input("Select command: "))

        d, c = color_bd_generator()

        if cmd == 1:
            x = cv2.imread("bmw.jpg")
        elif cmd == 2:
            cmd_str = str(input("Your path: "))
            x = cv2.imread(cmd_str)
        else:
            print("Err: bad command :(")
            break

        print("Image resolution: " + str(x.shape[0]) + " x " + str(x.shape[1]) + " pix with " + str(
            x.shape[2]) + " channels.")

        # key = raw_input("Type your security key: ")
        # os.system("stty echo") - for illustration
        key = input("Type your security key: ")
        text = input("Write your encrypted message: ")

        kl = 0
        tln = len(text)
        z, n, m = 0, 0, 0  # decides plane, number of row, number of column

        l = len(text)

        for i in range(l):
            x[n, m, z] = d[text[i]] ^ d[key[kl]]
            n = n + 1
            m = m + 1
            m = (m + 1) % 3  # this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
            # whatever be the value of z , z=(z+1)%3 will always between 0,1,2 .
            kl = (kl + 1) % len(key)

        cv2.imwrite("encrypted_img.jpg", x)

        print("Encrypted successfully.")

        # x = cv2.imread("encrypted_img.jpg")

        kl = 0
        z, n, m = 0, 0, 0  # decides plane, number of row, number of column

        cmd = int(input("\nType 5 to extract data from Image: "))

        if cmd == 5:
            key1 = input("\nType your security key: ")
            decrypt = ""

            if key == key1:
                for i in range(l):
                    decrypt += c[x[n, m, z] ^ d[key[kl]]]
                    n = n + 1
                    m = m + 1
                    m = (m + 1) % 3
                    kl = (kl + 1) % len(key)
                print("------------------------------------------------------------")
                print("------------------------------------------------------------")
                print("------------------------------------------------------------")
                print("Encrypted text: ", decrypt)
                print("------------------------------------------------------------")
                print("------------------------------------------------------------")
                print("------------------------------------------------------------")
            else:
                print("Password is not correct.")
        else:
            print("\nRestarting...")
