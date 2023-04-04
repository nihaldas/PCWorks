import streamlit as st

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

# Set up the page layout
st.set_page_config(page_title='Custom PC Builder', page_icon='💻')



st.sidebar.write("Are you a seller or a buyer?")
user_type = st.sidebar.radio("", ["Welcome", "Buyer", "Seller"])

if user_type == "Welcome":
    html_code = """
    <div style="background-color:#F8F8F8;padding:10px;border-radius:5px">
        <h2 style="color:#3D405B;">VyaparX PC Category</h2>
        <p style="color:#4C4C4C;">Welcome to VyaparX, your one stop place for all 
        your custom PC needs. From buying new or old parts to selling, from helping you build 
        your own PC to lifetime support. We provide all the services</p>
    </div>
    """
    # Display the HTML code in your Streamlit app
    st.markdown(html_code, unsafe_allow_html=True)

elif user_type == "Buyer":
    html_code = """
    <div style="background-color:#F8F8F8;padding:10px;border-radius:5px">
        <h2 style="color:#3D405B;">VyaparX PC Forge Station</h2>
        <p style="color:#4C4C4C;">At our custom PC builder station ie Titans Forge, we believe that building a custom PC should be a seamless and enjoyable experience for everyone. Our platform will help you to determine your exact needs and requirements, whether you're a gamer, a machine learning professional, or a crypto miner. We'll help you choose the best components for your build, including the CPU, GPU, RAM, storage, and other peripherals, ensuring that everything is perfectly matched to your needs and budget..</p>
    </div>
    """
    # Display the HTML code in your Streamlit app
    st.markdown(html_code, unsafe_allow_html=True)
    st.write("# Custom PC Build Station")
    st.write("Welcome, buyer! Please fill out the following form to get a quote for a custom PC build.")
    # Get the user's component choices
    cpu_choice = st.sidebar.selectbox('CPU', list(cpu_options.keys()))
    gpu_choice = st.sidebar.selectbox('GPU', list(gpu_options.keys()))
    mb_choice = st.sidebar.selectbox('Motherboard', list(mb_options.keys()))
    cooling_choice = st.sidebar.selectbox('Cooling', list(cooling_options.keys()))
    psu_choice = st.sidebar.selectbox('Power Supply', list(psu_options.keys()))

    # Calculate the total price
    total_price = cpu_options[cpu_choice] + gpu_options[gpu_choice] + mb_options[mb_choice] + cooling_options[cooling_choice] + psu_options[psu_choice]

    # Display the component choices and total price
    st.header('')
    st.radio('Main Use Purpose', ['Gaming', 'Crypto Mining', '3D Modeling/Rendering'])

    st.slider('Choose your budget', 0, 500000)
    st.text_area('List the games you wish to play : ')
    st.text_area('Tell us how your day to day work looks like : ')
    st.text_area('Enter softwares you use or plan to use : ')

    st.write('### Your Build:')
    st.write(f'- CPU: {cpu_choice} :  Rs {82.5*cpu_options[cpu_choice]} ')
    st.write(f'- GPU: {gpu_choice} : Rs {82.5*gpu_options[gpu_choice]} ')
    st.write(f'- Motherboard: {mb_choice} : Rs {82.5*mb_options[mb_choice]} ')
    st.write(f'- Cooling: {cooling_choice} : Rs {82.5*cooling_options[cooling_choice]} ')
    st.write(f'- Power Supply: {psu_choice} : Rs {82.5*psu_options[psu_choice]} ')

    if st.button('Get Live Estimate'):
        st.write(f'### Estimated Price : Rs {82.5*total_price} ')

    if st.button('Expert Diagnosis'):
        st.write('Your custom PC has been diagonised by our BuildGPT expert. Here is the detailed analysis of the your build:')

    # Add a "Build PC" button
    if st.button('Place Order'):
        st.write('Your custom PC has been ordered! Thank you for shopping with us.')

    st.text('Please note: Because we regularly update Prices and Availability,\nPrice-Point Build-Configurations can vary. VyaparX Titans Forge Station is \nreader-supported. When you buy through our links, at no extra cost to you,\nwe may earn an affiliate commission.')

else :
    st.write("# Custom PC Build Seller")
    st.write("Welcome, seller! Please fill out the following form to list your custom PC build for sale.")




