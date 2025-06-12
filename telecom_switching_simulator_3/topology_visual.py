from pyvis.network import Network
import streamlit as st

def draw_topology():
    net = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')

    # Add PSTN nodes
    net.add_node('PSTN Core', label='PSTN Core Switch', color='red', shape='triangle')
    net.add_node('PSTN User A', label='User A', color='red')
    net.add_node('PSTN User B', label='User B', color='red')

    # Add PSDN nodes
    net.add_node('PSDN Server', label='PSDN Server', color='blue', shape='diamond')
    net.add_node('PSDN Client 1', label='Client 1', color='blue')
    net.add_node('PSDN Client 2', label='Client 2', color='blue')

    # Add PLMN nodes
    net.add_node('PLMN Base Station', label='PLMN Base Station', color='green', shape='star')
    net.add_node('PLMN Mobile 1', label='Mobile 1', color='green')
    net.add_node('PLMN Mobile 2', label='Mobile 2', color='green')

    # Add edges - PSTN
    net.add_edge('PSTN User A', 'PSTN Core')
    net.add_edge('PSTN User B', 'PSTN Core')

    # Add edges - PSDN
    net.add_edge('PSDN Client 1', 'PSDN Server')
    net.add_edge('PSDN Client 2', 'PSDN Server')

    # Add edges - PLMN
    net.add_edge('PLMN Mobile 1', 'PLMN Base Station')
    net.add_edge('PLMN Mobile 2', 'PLMN Base Station')

    # Cross links (example)
    net.add_edge('PSTN Core', 'PSDN Server')
    net.add_edge('PSDN Server', 'PLMN Base Station')

    # Save as html (instead of net.show())
    net.write_html('topology.html')

def display_topology():
    draw_topology()
    HtmlFile = open('topology.html', 'r', encoding='utf-8')
    components = st.components.v1
    components.html(HtmlFile.read(), height=650)

if __name__ == "__main__":
    display_topology()
