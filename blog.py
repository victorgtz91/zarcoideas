import streamlit as st

# Define the page content for the blog
def blog_page():
    st.title("Welcome to the Blog!")
    # Add your blog content here

# Main function to handle different URL paths
def main():
    path = st.experimental_get_query_params().get("path", [""])[0]
    if path == "blog":
        blog_page()
    else:
        # Display the default content or homepage
        st.title("Welcome to My Homepage")
        # Add your homepage content here

# Run the main function
if __name__ == "__main__":
    main()
