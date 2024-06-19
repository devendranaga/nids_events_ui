#!/usr/bin/python3

# implements base code for the event display screen for nIDS events
# coming from the nIDS from the switch.

import streamlit as st
import pandas as pd
import numpy as np
from schedule import every, repeat, run_pending
import json

import time as t
import sys

import udp_srv as server

st.write('#### Firewall Event Dashboard')

class Event_Data:
    def init(self, ip, port):
        self.conn = server.UdpServer()
        self.conn.init(ip, int(port))

    # {
    #   "rule_id": 10,
    #   "event_type": "allow",
    # }
    def recv(self):
        msg=""

        msg = self.conn.get_data().decode()
        cols = json.loads(msg)

        self.rule_id_list = []
        self.event_type_list = []
        self.event_descr_list = []
        self.ethertype_list = []
        self.timestamp_sec_list = []
        self.timestamp_usec_list = []

        self.rule_id_list.append(cols['rule_id'])
        self.event_type_list.append(cols['event_type'])
        self.event_descr_list.append(cols['event_descr'])
        self.ethertype_list.append(cols['ethertype'])
        self.timestamp_sec_list.append(cols['timestamp_sec'])
        self.timestamp_usec_list.append(cols['timestamp_usec'])

    def get_rule_id_list(self):
        return self.rule_id_list
    
    def get_event_type_list(self):
        return self.event_type_list
    
    def get_event_descr_list(self):
        return self.event_descr_list
    
    def get_ethertype_list(self):
        return self.ethertype_list
    
    def get_timestamp_sec_list(self):
        return self.timestamp_sec_list
    
    def get_timestamp_usec_list(self):
        return self.timestamp_usec_list


evt_data = Event_Data()
evt_data.init(sys.argv[1], sys.argv[2])

# Initialize the event data
evt_data.recv()
new_data = pd.DataFrame(
    {
        "Rule_Id": evt_data.get_rule_id_list(),
        "Event Type": evt_data.get_event_type_list(),
        "Event Description": evt_data.get_event_descr_list(),
        "Ethertype": evt_data.get_ethertype_list(),
        "Timestamp_sec": evt_data.get_timestamp_sec_list(),
        "Timestamp_usec": evt_data.get_timestamp_usec_list()
    },
)
# display now on the screen
evt_hdr_tbl = st.dataframe(new_data)

# Display stats periodically
with st.empty():
    @repeat(every(1).second)
    def display_periodically():

        st.columns(1)
        evt_data.recv()
        new_data = pd.DataFrame(
             {
                  "Rule_Id": evt_data.get_rule_id_list(),
                  "Event Type": evt_data.get_event_type_list(),
                  "Event Description": evt_data.get_event_descr_list(),
                  "Ethertype": evt_data.get_ethertype_list(),
                  "Timestamp_sec": evt_data.get_timestamp_sec_list(),
                  "Timestamp_usec": evt_data.get_timestamp_usec_list()
             }
        )
        evt_hdr_tbl.add_rows(new_data)

    while True:
        run_pending()
        t.sleep(1)


