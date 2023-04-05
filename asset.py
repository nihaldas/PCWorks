import json
f = open('PCgames.json')
data_PCgames = json.load(f)

f = open('PCsoftware.json')
data_PCsoftwares = json.load(f)

gameslist = []
for gametype in data_PCgames.keys():
    gamesdata = data_PCgames[gametype]
    for r in range(len(gamesdata)):
        gametitle = gamesdata[r]['title']
        gameslist.append(gametitle)

softwarelist = [] 
for softwaretype in data_PCsoftwares.keys():
    softwdata = data_PCsoftwares[softwaretype]
    for r in range(len(softwdata)):
        softwtitle = softwdata[r]['name']
        softwarelist.append(softwtitle)


pcgaming_faq = """

- Choose a CPU with high clock speeds and multiple cores for better gaming performance.
- Select a compatible motherboard with enough expansion slots for any additional components you may want to add later on.
- Choose a powerful graphics card with plenty of video RAM and support for the latest graphics technologies.
- Don't skimp on RAM, and choose at least 8GB or more if you can afford it.
- Make sure your components are properly cooled to keep your gaming PC running cool and quiet.

"""

pcml_faq = """

- Choose a CPU and motherboard that support multiple GPUs, as machine learning tasks can benefit from parallel processing.
- Choose a powerful GPU with high memory bandwidth and support for the latest deep learning frameworks.
- Consider adding a high amount of RAM to handle large datasets and complex machine learning models.
- Choose a power supply with enough wattage to handle your components and support for multiple GPUs.
- Make sure your components are properly cooled, as machine learning tasks can generate a lot of heat.

"""
pcmining_faq = """

- Choose a GPU with high hash rates and low power consumption to maximize your mining profitability.
- Select a compatible motherboard with enough PCIe slots to support multiple GPUs.
- Choose a power supply with enough wattage to handle your GPUs and support for multiple PCIe connectors.
- Consider adding a high amount of RAM to handle large datasets and mining software.
- Make sure your components are properly cooled to maximize your mining performance and prevent overheating.

"""

pc3d_faq = """

- Choose a CPU with high clock speeds and multiple cores for faster rendering times.
- Select a motherboard with enough expansion slots for any additional components you may want to add later on.
- Choose a powerful GPU with high memory bandwidth and support for the latest 3D modeling software.
- Don't skimp on RAM, and choose at least 16GB or more if you can afford it.
- Make sure your components are properly cooled to keep your PC running cool and quiet during intensive rendering tasks.

"""

faqs = {'Gaming':pcgaming_faq,
        'ML':pcml_faq,
        'Mining':pcmining_faq,
        '3D':pc3d_faq}

# Component options and prices
cpu_options = {
    'Intel Core i5-11600K': 299,
    'Intel Core i7-11700K': 419,
    'Intel Core i9-11900K': 599,
    'AMD Ryzen 5 5600X': 299,
    'AMD Ryzen 5 5600G': 259,
    'AMD Ryzen 7 5800X': 449,
    'AMD Ryzen 7 5800G': 399,
    'AMD Ryzen 9 5900X': 549,
    'AMD Ryzen 9 5950X': 799,
    'Apple M1': 699
}
gpu_options = {
    'NVIDIA GeForce GTX 1650': 149,
    'NVIDIA GeForce GTX 1660 Super': 229,
    'NVIDIA GeForce RTX 3060': 329,
    'NVIDIA GeForce RTX 3070 Ti': 599,
    'NVIDIA GeForce RTX 3080 Ti': 1199,
    'NVIDIA GeForce RTX 3090 Ti': 1999,
    'AMD Radeon RX 5500 XT': 199,
    'AMD Radeon RX 5600 XT': 279,
    'AMD Radeon RX 5700 XT': 449,
    'AMD Radeon RX 6800': 579,
    'AMD Radeon RX 6900 XT': 999
}

mb_options = {
    'ASUS ROG Strix X570-E Gaming': 299,
    'Gigabyte AORUS X570 Master': 359,
    'MSI MEG X570 UNIFY': 299,
    'ASRock X570 Taichi': 299,
    'ASUS Prime X570-Pro': 249,
    'ASUS ROG Crosshair VIII Dark Hero': 439,
    'Gigabyte B550I AORUS PRO AX': 179,
    'ASRock B550M Steel Legend': 119,
    'MSI MAG B550 Tomahawk': 179,
    'ASUS ROG Strix B550-F Gaming': 189,

}

cooling_options = {
    'Noctua NH-D15': 89,
    'Corsair iCUE H115i Elite Capellix': 169,
    'NZXT Kraken X63': 149,
    'Arctic Freezer 34 eSports DUO': 49,
    'be quiet! Dark Rock Pro 4': 89,
    'Cooler Master MasterLiquid ML240L': 79,
    'Thermaltake Water 3.0 ARGB Sync': 129,
    'Deepcool Gammaxx GT BK': 49,
    'Corsair Hydro Series H100i': 159
}

psu_options = {
    'EVGA SuperNOVA 850 GA': 139,
    'Corsair RM850x': 149,
    'Seasonic PRIME TX-850': 219,
    'be quiet! Straight Power 11 850W': 159,
    'NZXT C850': 149,
    'Thermaltake Toughpower PF1 ARGB 850W': 169
}