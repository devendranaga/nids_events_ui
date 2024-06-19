# nIDS Event Display GUI

GUI for the nIDS events using streamlit. 

## How to setup streamlint

```bash
sudo apt install python-is-python3 python3-pip
sudo pip3 install streamlit
```

# How to run

```bash
python3 -m streamlit run base.py 127.0.0.1 2125
```

on ip:port -> 127.0.0.1 and 2125 the nIDS will send out the events.

see `testing/udp_client.py` to run the client and the packet format of the event.
