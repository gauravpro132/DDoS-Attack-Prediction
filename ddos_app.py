import pickle
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
with open('DDOS_stacked_classifier.pickle', 'rb') as f:
    clf = pickle.load(f)


def main():
    st.set_page_config(
        page_title="DDOS Attack Prediction",
        page_icon="🧊", layout="centered",
        initial_sidebar_state="auto",
    )
    st.title('DDOS-Classifier')
    st.write("API Link = [Fast Api](https://ddos-fastapi.herokuapp.com/docs)")

    dp = st.number_input(' Destination Port', key="1")
    fpl = st.number_input('Total Length of Fwd Packets', key="2")
    bpls = st.number_input('Bwd Packet Length Std', key="3")
    fim = st.number_input('Flow IAT Min', key="4")
    fwit = st.number_input('Fwd IAT Total', key="5")
    bp = st.number_input(' Bwd Packets/s', key="6")
    inbf = st.number_input('Init_Win_bytes_forward', key="7")
    inbb = st.number_input(' Init_Win_bytes_backward', key="8")

    if st.button('Predict'):
        result = clf.predict([[dp, fpl, bpls, fim, fwit, bp, inbf, inbb]])

        if result == ['BENIGN']:
            st.success('BENIGN')

        elif result == ['DDoS']:
            st.success('DDOS')


if __name__ == '__main__':
    main()
