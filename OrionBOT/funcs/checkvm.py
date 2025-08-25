import requests
import psutil
import subprocess
import os
try:
    def check():
        def ip_check():
            try:
                IPS = [
                    "None",
                    "88.132.231.71",
                    "78.139.8.50",
                    "20.99.160.173",
                    "88.153.199.169",
                    "84.147.62.12",
                    "194.154.78.160",
                    "92.211.109.160",
                    "195.74.76.222",
                    "188.105.91.116",
                    "34.105.183.68",
                    "92.211.55.199",
                    "79.104.209.33",
                    "95.25.204.90",
                    "34.145.89.174",
                    "109.74.154.90",
                    "109.145.173.169",
                    "34.141.146.114",
                    "212.119.227.151",
                    "195.239.51.59",
                    "192.40.57.234",
                    "64.124.12.162",
                    "34.142.74.220",
                    "188.105.91.173",
                    "109.74.154.91",
                    "34.105.72.241",
                    "109.74.154.92",
                    "213.33.142.50",
                    "109.74.154.91",
                    "93.216.75.209",
                    "192.87.28.103",
                    "88.132.226.203",
                    "195.181.175.105",
                    "88.132.225.100",
                    "92.211.192.144",
                    "34.83.46.130",
                    "188.105.91.143",
                    "34.85.243.241",
                    "34.141.245.25",
                    "178.239.165.70",
                    "84.147.54.113",
                    "193.128.114.45",
                    "95.25.81.24",
                    "92.211.52.62",
                    "88.132.227.238",
                    "35.199.6.13",
                    "80.211.0.97",
                    "34.85.253.170",
                    "23.128.248.46",
                    "35.229.69.227",
                    "34.138.96.23",
                    "192.211.110.74",
                    "35.237.47.12",
                    "87.166.50.213",
                    "34.253.248.228",
                    "212.119.227.167",
                    "193.225.193.201",
                    "34.145.195.58",
                    "34.105.0.27",
                    "195.239.51.3",
                    "35.192.93.107",
                    "213.33.190.22",
                    "194.154.78.152",
                ]
                IP = requests.get("https://api.myip.com").json()["ip"]

                if IP in IPS:
                    os.exit(1)
            except:
                pass
        def user_check():
                USERS = [
                    "Admin"
                    "plasma",
                    "BEE7370C-8C0C-4",
                    "DESKTOP-NAKFFMT",
                    "WIN-5E07COS9ALR",
                    "B30F0242-1C6A-4",
                    "DESKTOP-VRSQLAG",
                    "Q9IATRKPRH",
                    "XC64ZB",
                    "DESKTOP-D019GDM",
                    "DESKTOP-WI8CLET",
                    "SERVER1",
                    "LISA-PC",
                    "JOHN-PC",
                    "DESKTOP-B0T93D6",
                    "DESKTOP-1PYKP29",
                    "DESKTOP-1Y2433R",
                    "WILEYPC",
                    "WORK",
                    "6C4E733F-C2D9-4",
                    "RALPHS-PC",
                    "DESKTOP-WG3MYJS",
                    "DESKTOP-7XC6GEZ",
                    "DESKTOP-5OV9S0O",
                    "QarZhrdBpj",
                    "ORELEEPC",
                    "ARCHIBALDPC",
                    "JULIA-PC",
                    "d1bnJkfVlH",
                    "WDAGUtilityAccount",
                    "Abby",
                    "patex",
                    "RDhJ0CNFevzX",
                    "kEecfMwgj",
                    "Frank",
                    "8Nl0ColNQ5bq",
                    "Lisa",
                    "John",
                    "george",
                    "PxmdUOpVyx",
                    "8VizSM",
                    "w0fjuOVmCcP5A",
                    "lmVwjj9b",
                    "PqONjHVwexsS",
                    "3u2v9m8",
                    "Julia",
                    "HEUeRzl",
                    "fred",
                    "server",
                    "BvJChRPnsxn",
                    "Harry Johnson",
                    "SqgFOf3G",
                    "Lucas",
                    "mike",
                    "PateX",
                    "h7dk1xPr",
                    "Louise",
                    "User01",
                    "test",
                    "RGzcBUyrznReg",
                    "OgJb6GqgK0O",
                ]

                try:
                    USER = os.getlogin()
                    if USER in USERS:
                        os.exit(1)
                except:
                    pass

        def hwid_check():
                HWIDS = [
                    "7AB5C494-39F5-4941-9163-47F54D6D5016",
                    "03DE0294-0480-05DE-1A06-350700080009",
                    "11111111-2222-3333-4444-555555555555",
                    "6F3CA5EC-BEC9-4A4D-8274-11168F640058",
                    "ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548",
                    "4C4C4544-0050-3710-8058-CAC04F59344A",
                    "00000000-0000-0000-0000-AC1F6BD04972",
                    "00000000-0000-0000-0000-000000000000",
                    "5BD24D56-789F-8468-7CDC-CAA7222CC121",
                    "49434D53-0200-9065-2500-65902500E439",
                    "49434D53-0200-9036-2500-36902500F022",
                    "777D84B3-88D1-451C-93E4-D235177420A7",
                    "49434D53-0200-9036-2500-369025000C65",
                    "B1112042-52E8-E25B-3655-6A4F54155DBF",
                    "00000000-0000-0000-0000-AC1F6BD048FE",
                    "EB16924B-FB6D-4FA1-8666-17B91F62FB37",
                    "A15A930C-8251-9645-AF63-E45AD728C20C",
                    "67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3",
                    "C7D23342-A5D4-68A1-59AC-CF40F735B363",
                    "63203342-0EB0-AA1A-4DF5-3FB37DBB0670",
                    "44B94D56-65AB-DC02-86A0-98143A7423BF",
                    "6608003F-ECE4-494E-B07E-1C4615D1D93C",
                    "D9142042-8F51-5EFF-D5F8-EE9AE3D1602A",
                    "49434D53-0200-9036-2500-369025003AF0",
                    "8B4E8278-525C-7343-B825-280AEBCD3BCB",
                    "4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27",
                    "79AF5279-16CF-4094-9758-F88A616D81B4",
                    "FF577B79-782E-0A4D-8568-B35A9B7EB76B",
                    "08C1E400-3C56-11EA-8000-3CECEF43FEDE",
                    "6ECEAF72-3548-476C-BD8D-73134A9182C8",
                    "49434D53-0200-9036-2500-369025003865",
                    "119602E8-92F9-BD4B-8979-DA682276D385",
                    "12204D56-28C0-AB03-51B7-44A8B7525250",
                    "63FA3342-31C7-4E8E-8089-DAFF6CE5E967",
                    "365B4000-3B25-11EA-8000-3CECEF44010C",
                    "D8C30328-1B06-4611-8E3C-E433F4F9794E",
                    "00000000-0000-0000-0000-50E5493391EF",
                    "00000000-0000-0000-0000-AC1F6BD04D98",
                    "4CB82042-BA8F-1748-C941-363C391CA7F3",
                    "B6464A2B-92C7-4B95-A2D0-E5410081B812",
                    "BB233342-2E01-718F-D4A1-E7F69D026428",
                    "9921DE3A-5C1A-DF11-9078-563412000026",
                    "CC5B3F62-2A04-4D2E-A46C-AA41B7050712",
                    "00000000-0000-0000-0000-AC1F6BD04986",
                    "C249957A-AA08-4B21-933F-9271BEC63C85",
                    "BE784D56-81F5-2C8D-9D4B-5AB56F05D86E",
                    "ACA69200-3C4C-11EA-8000-3CECEF4401AA",
                    "3F284CA4-8BDF-489B-A273-41B44D668F6D",
                    "BB64E044-87BA-C847-BC0A-C797D1A16A50",
                    "2E6FB594-9D55-4424-8E74-CE25A25E36B0",
                    "42A82042-3F13-512F-5E3D-6BF4FFFD8518",
                    "38AB3342-66B0-7175-0B23-F390B3728B78",
                    "48941AE9-D52F-11DF-BBDA-503734826431",
                    "A7721742-BE24-8A1C-B859-D7F8251A83D3",
                    "3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E",
                    "D2DC3342-396C-6737-A8F6-0C6673C1DE08",
                    "EADD1742-4807-00A0-F92E-CCD933E9D8C1",
                    "AF1B2042-4B90-0000-A4E4-632A1C8C7EB1",
                    "FE455D1A-BE27-4BA4-96C8-967A6D3A9661",
                    "921E2042-70D3-F9F1-8CBD-B398A21F89C6",
                    "6AA13342-49AB-DC46-4F28-D7BDDCE6BE32",
                    "F68B2042-E3A7-2ADA-ADBC-A6274307A317",
                    "07AF2042-392C-229F-8491-455123CC85FB",
                    "4EDF3342-E7A2-5776-4AE5-57531F471D56",
                    "032E02B4-0499-05C3-0806-3C0700080009",
                ]

                try:
                    HWID = (
                        subprocess.check_output(
                            r"wmic csproduct get uuid", creationflags=0x08000000
                        )
                        .decode()
                        .split("\n")[1]
                        .strip()
                    )

                    if HWID in HWIDS:
                        os.exit(1)
                except Exception:
                    pass
        hwid_check()
        ip_check()
except Exception:
     pass
check()