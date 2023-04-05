import streamlit as st
from asset import gameslist, softwarelist, faqs
from asset import cpu_options, gpu_options, mb_options, cooling_options, psu_options

# Set up the page layout
st.set_page_config(page_title='Custom PC Builder', page_icon='💻')

#st.sidebar.write("Are you a seller or a buyer?")
user_type = st.sidebar.radio("", ["Welcome", "PC Build Station"])

if user_type == "Welcome":
    html_code = """
    <div style="background-color:#F8F8F8;padding:10px;border-radius:5px">
        <h2 style="color:#3D405B;">PCWorks</h2>
        <p style="color:#4C4C4C;">Welcome to PCWorks, your one stop place for all 
        your custom PC needs. From buying new or old parts to selling, from helping you build 
        your own PC to lifetime support. We provide all the services</p>
    </div>
    """
    # Display the HTML code in your Streamlit app
    st.markdown(html_code, unsafe_allow_html=True)

elif user_type == "PC Build Station":
    html_code = """
    <div style="background-color:#F8F8F8;padding:10px;border-radius:5px">
        <h2 style="color:#3D405B;">PCWorks Build Station</h2>
        <p style="color:#4C4C4C;">At PCWorks PC build station, 
        we believe that building a custom PC should be a seamless and 
        enjoyable experience for everyone. Our platform will help you to
          determine your exact needs and requirements, whether you're a gamer, 
          a machine learning professional, or a crypto miner. 
          We'll help you choose the best components for your build, 
          including the CPU, GPU, RAM, storage, and other peripherals, 
          ensuring that everything is perfectly matched to your needs and budget..</p>
    </div>
    """
    # Display the HTML code in your Streamlit app
    st.markdown(html_code, unsafe_allow_html=True)
    st.write("# PC Build Station")
    st.write("Welcome, buyer! Please fill out the following form to get a quote for a custom PC build.")
    # Get the user's component choices
    
    
    build_type = st.sidebar.radio("Station", ["Requirements", "Build"])

    if build_type == "Requirements":
        purpose_type = st.radio('Main Use Purpose', ['Gaming', 'Machine Learning', 'Crypto Mining', '3D Modeling/Rendering'])
        st.write("Things to Remember for your build")
        if purpose_type == 'Gaming':
            st.write(faqs['Gaming'])
        elif purpose_type == 'Machine Learning':
            st.write(faqs['ML'])
        elif purpose_type == 'Crypto Mining':
            st.write(faqs['Mining'])
        else: st.write(faqs['3D'])
        
        st.slider('Choose your budget', 0, 500000)
        st.multiselect('Select Games you play or want to plan', gameslist)
        st.multiselect('Select Softwares you use or plan to use', softwarelist)
    
    else : 
        cpu_choice = st.sidebar.selectbox('CPU', list(cpu_options.keys()))
        gpu_choice = st.sidebar.selectbox('GPU', list(gpu_options.keys()))
        mb_choice = st.sidebar.selectbox('Motherboard', list(mb_options.keys()))
        cooling_choice = st.sidebar.selectbox('Cooling', list(cooling_options.keys()))
        psu_choice = st.sidebar.selectbox('Power Supply', list(psu_options.keys()))

        # Calculate the total price
        total_price = cpu_options[cpu_choice] + gpu_options[gpu_choice] + mb_options[mb_choice] + cooling_options[cooling_choice] + psu_options[psu_choice]

        # Display the component choices and total price
        st.write('### Your Build:')
        st.write(f'- CPU: {cpu_choice} :  Rs {82.5*cpu_options[cpu_choice]} ')
        st.write(f'- GPU: {gpu_choice} : Rs {82.5*gpu_options[gpu_choice]} ')
        st.write(f'- Motherboard: {mb_choice} : Rs {82.5*mb_options[mb_choice]} ')
        st.write(f'- Cooling: {cooling_choice} : Rs {82.5*cooling_options[cooling_choice]} ')
        st.write(f'- Power Supply: {psu_choice} : Rs {82.5*psu_options[psu_choice]} ')

        if st.button('Get Live Estimate'):
            st.write(f'### Estimated Price : Rs {82.5*total_price} ')

        # if st.button('Expert Diagnosis'):
        #     st.write('Your custom PC has been diagonised by our BuildGPT expert. Here is the detailed analysis of the your build:')

        # Add a "Build PC" button
        if st.button('Place Order'):
            st.write('Your custom PC Order has been created! A google response form will be sent to you shorty!! Thanks for shopping with us :) ')

        st.text('Please note: Because we regularly update Prices and Availability,\nPrice-Point Build-Configurations can vary. PCWorks Build Station is \nreader-supported. When you buy through our links, at no extra cost to you,\nwe may earn an affiliate commission.')

else :
    st.write("# Custom PC Build Seller")
    st.write("Welcome, seller! Please fill out the following form to list your custom PC build for sale.")




