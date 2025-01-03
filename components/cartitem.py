import streamlit as st
import pandas as pd


class CartItem:
    def show():
        config = {
            "_index": st.column_config.TextColumn("Product Description"),
            "No": st.column_config.NumberColumn("No."),
            "Total": st.column_config.NumberColumn("Total ($)"),
        }
        df = pd.DataFrame(
            {
                "Product": ["Vini Izi Plus 1h", "Sim Card", "Booster 100 mins"],
                "No": [1, 1, 1],
                "Total": [100, 50, 5]
            })
        df.set_index("Product", inplace=True)
        expander = st.sidebar.expander(
            ":iphone: Mobile Prepaid", True, icon=None)
        expander.dataframe(df, column_config=config)
