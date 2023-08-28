import streamlit as st
import random, json
import time

import paho.mqtt.subscribe as subscribe


st.title("Simple MQTT Server")

# Using object notation
vinworthjasaupur = st.sidebar.checkbox("vinworthjasaupur")
upapltest = st.sidebar.checkbox("upapltest")
vinworthtest = st.sidebar.checkbox("vinworthtest")

schemes = [vinworthjasaupur, upapltest, vinworthtest]
names = ["vinworthjasaupur", "upapltest", "vinworthtest"]
schemeids = {"vinworthtest":"Bulandshahar - Alampur nagla", "vinworthjasaupur": "Jaunpur (Jasaupur)", "861190059947132":"Sant Ravidas Nagar - Jethupur", "861190059974243":"Ambedkar Nagar- Rukunpur kasimpur","861198066252826": "Amethi- sogara"}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


counter = 1
while True:
    for i, scheme in enumerate(schemes):
        if scheme:
            msg = subscribe.simple(names[i], qos=0, msg_count=1, retained=True, hostname="20.235.93.174",port=1883, client_id="paho-sub", keepalive=1, will=None, auth={'username':"raiak", 'password':"RAIsw@2023"}, tls=None)
            if msg!=None:
                message = st.chat_message("assistant")
                message.write("Topic name: "+names[i] + "  Message Counter -"+ str(counter))
                if names[i] == "vinworthjasaupur" or names[i]== "vinworthtest":
                    schemename = schemeids[names[i]]
                elif names[i]== "upapltest":
                    # print((json.loads(msg.payload))['trig'])
                    schemename = schemeids[str((json.loads(msg.payload))['trig'])]
                
                schemenametext = "Scheme name: "+schemename
                message.write(schemenametext)
                message.write(json.loads(msg.payload))
                counter+=1
                # print((msg.topic, msg.payload))
                # with st.chat_message("user"):
                #     # st.markdown(prompt)
                #     # Add user message to chat history
                #     st.session_state.messages.append({"role": "user", "content": "data1"})


# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#         assistant_response = random.choice(
#             [
#                 "Hello there! How can I assist you today?",
#                 "Hi, human! Is there anything I can help you with?",
#                 "Do you need help?",
#             ]
#         )
#         # Simulate stream of response with milliseconds delay
#         for chunk in assistant_response.split():
#             full_response += chunk + " "
#             time.sleep(0.05)
#             # Add a blinking cursor to simulate typing
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": full_response})