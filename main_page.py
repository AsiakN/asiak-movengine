  # Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Movie Recommender streamlit app",
        page_icon="👋",
    )

    st.header("Movie recommender system built using Content-based filtering based off the KNN algorithm")

    st.write("# Welcome to the Asiak Movie Engine! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This app built with a Jupyyter Notebook and deployed with Streamlit is
        an application of Content-based filtering using K-Nearest Neighbour Algorithm. 

        **👈 Select a page from the sidebar** to get some recommendations or 
        learn more about the data
        ### Want the source code?
        - Check out my github [AsiakN](https://github.com/AsiakN/asiak-movengine)
        - Send me a DM on [Twiter](https://twitter.com/NathanielAsiak)
        - Let's Connect on [Linkedin](https://www.linkedin.com/in/nathanielasiak/)
        - Check out streamlit to learn more about deploying machine learning applications
             [streamlit](https://docs.streamlit.io)
    """
    )

    st.markdown('**_Best_**.')
    st.markdown('**_the_ _Asiak_**. ❤')

if __name__ == "__main__":
    run()