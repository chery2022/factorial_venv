import streamlit as st
from factorial import fact

def main():
    st.title('Factorial Caculator')
    number = st.number_input('Nhap vao so : ',min_value=0,max_value=900)
    if st.button('Tinh'):
        result = fact(number)
        st.write(f'Giai thua cua {number} la : {result}')


if __name__ == '__main__':
    main()

